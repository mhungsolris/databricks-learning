"""PORTABLE TEST: real artifact contracts, no workspace API mocks."""
import ast
from copy import deepcopy
import unittest
from labs.platform.contracts import BASE, load, validate_dag, pipeline_datasets, permits_fixture

class PlatformArtifacts(unittest.TestCase):
    def setUp(self):
        self.job = load("resources/roas.job.yml")["resources"]["jobs"]["roas"]

    def test_dag_validation_barrier_and_failure_branch(self):
        edges = validate_dag(self.job)
        self.assertEqual(set(edges["validate"]), {"ingest_cost", "ingest_revenue"})
        self.assertEqual(edges["silver"], ["validate"])
        self.assertEqual(edges["gold"], ["silver"])
        self.assertEqual(edges["reconcile"], ["gold"])
        tasks = {t["task_key"]: t for t in self.job["tasks"]}
        self.assertEqual(tasks["failure_report"]["run_if"], "AT_LEAST_ONE_FAILED")
        self.assertEqual(tasks["validate"]["max_retries"], 0)
        self.assertEqual(self.job["max_concurrent_runs"], 1)

    def test_bad_dependency_and_cycle_rejected(self):
        for parent in ("missing", "reconcile"):
            bad = deepcopy(self.job)
            bad["tasks"][0]["depends_on"] = [{"task_key": parent}]
            with self.assertRaises(ValueError):
                validate_dag(bad)

    def test_duplicate_task_rejected(self):
        bad = deepcopy(self.job)
        bad["tasks"].append(deepcopy(bad["tasks"][0]))
        with self.assertRaises(ValueError):
            validate_dag(bad)

    def test_task_sources_and_parameter_contract(self):
        for task in self.job["tasks"]:
            source = (BASE / "resources" / task["notebook_task"]["notebook_path"]).resolve()
            self.assertTrue(source.is_relative_to(BASE))
            tree = ast.parse(source.read_text(encoding="utf-8"))
            self.assertTrue(tree.body)
            self.assertEqual(task["notebook_task"]["base_parameters"]["stage"], task["task_key"])
            self.assertEqual(task["timeout_seconds"], 600)
            self.assertFalse(any(k in task for k in ("new_cluster", "existing_cluster_id", "job_cluster_key")))
        self.assertEqual({p["name"] for p in self.job["parameters"]},
                         {"catalog", "schema", "force_validation_failure"})
        main = load("databricks.yml")
        self.assertFalse(any("default" in var for var in main["variables"].values()))

    def test_pipeline_source_graph_and_no_side_effect_actions(self):
        datasets = pipeline_datasets()
        self.assertEqual(set(datasets), {"bronze_events", "silver_events_pipeline", "gold_campaign_pipeline"})
        source = (BASE / "src/medallion.py").read_text(encoding="utf-8")
        self.assertIn("FROM bronze_events", source)
        self.assertIn("FROM silver_events_pipeline", source)
        for node in datasets.values():
            for call in (x for x in ast.walk(node) if isinstance(x, ast.Call)):
                self.assertNotIn(getattr(call.func, "attr", ""), ("collect", "save", "start", "write", "count"))
        config = load("resources/medallion.pipeline.yml")["resources"]["pipelines"]["medallion"]
        self.assertTrue(config["serverless"])
        self.assertFalse(config["continuous"])
        self.assertEqual(config["schema"], "${var.schema}")
        self.assertNotIn("target", config)

    def test_policy_fixture_environment_and_pii_separation(self):
        policy = load("governance-policy.json")
        for principal in ("marketing_analysts", "finance"):
            self.assertTrue(permits_fixture(policy, principal, "roas_prod", "gold", "SELECT"))
            self.assertFalse(permits_fixture(policy, principal, "roas_prod", "restricted", "SELECT"))
            self.assertFalse(permits_fixture(policy, principal, "roas_prod", "gold", "MODIFY"))
        self.assertFalse(permits_fixture(policy, "data_engineers", "roas_prod", "silver", "MODIFY"))
        self.assertTrue(permits_fixture(policy, "roas_service_principal", "roas_prod", "silver", "MODIFY"))
        sql = (BASE / "sql/governance.sql").read_text(encoding="utf-8")
        for privilege in ("USE CATALOG", "USE SCHEMA", "SELECT ON TABLE"):
            self.assertIn("GRANT " + privilege, sql)

    def test_fixture_key_collision_retry_and_revision(self):
        events = load("fixtures.json")["events"]
        self.assertEqual(len(events), 6)
        self.assertEqual(len({tuple(e[1:4]) for e in events}), 4)
        self.assertEqual({e[2] for e in events if e[3] == "E1"}, {"a", "b"})
        self.assertEqual({e[4] for e in events if e[3] == "E2"}, {1, 2})
        self.assertEqual(events[0][1:], events[1][1:])

    def test_equal_revision_conflict_and_namespace_in_sources(self):
        source = (BASE / "src/roas_task.py").read_text(encoding="utf-8")
        self.assertIn("Conflicting equal revision", source)
        self.assertIn("Duplicate cost grain", source)
        self.assertIn('schema.startswith("course_roas_")', source)
        self.assertIn("PARTITION BY source_system,app_id,event_id", source)
