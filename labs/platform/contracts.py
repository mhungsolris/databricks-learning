"""Portable artifact contracts, never a Databricks API integration substitute."""
from pathlib import Path
import ast
import json

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "labs/platform"

def load(relative):
    return json.loads((BASE / relative).read_text(encoding="utf-8"))

def validate_dag(job):
    tasks = job["tasks"]
    names = [task["task_key"] for task in tasks]
    if len(names) != len(set(names)):
        raise ValueError("Duplicate task key")
    edges = {task["task_key"]: [d["task_key"] for d in task.get("depends_on", [])] for task in tasks}
    seen, active = set(), set()
    def visit(name):
        if name not in edges:
            raise ValueError("Unknown dependency")
        if name in active:
            raise ValueError("Cycle")
        if name in seen:
            return
        active.add(name)
        for parent in edges[name]:
            visit(parent)
        active.remove(name)
        seen.add(name)
    for name in names:
        visit(name)
    return edges

def sql_constants(relative):
    tree = ast.parse((BASE / relative).read_text(encoding="utf-8"))
    return [call.args[0].value for call in ast.walk(tree)
            if isinstance(call, ast.Call) and isinstance(call.func, ast.Attribute)
            and call.func.attr == "sql" and call.args and isinstance(call.args[0], ast.Constant)
            and isinstance(call.args[0].value, str)]

def pipeline_datasets():
    tree = ast.parse((BASE / "src/medallion.py").read_text(encoding="utf-8"))
    result = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            decorators = [d for d in node.decorator_list if isinstance(d, ast.Call)]
            dataset = next(d for d in decorators if getattr(d.func, "attr", None) == "materialized_view")
            name = next(k.value.value for k in dataset.keywords if k.arg == "name")
            result[name] = node
    return result

def permits_fixture(policy, principal, catalog, schema, action):
    """Explicit rows only: excludes actual UC inheritance, ownership/admin and memberships."""
    return any(row["principal"] == principal and catalog in row["catalogs"]
               and schema in row["schemas"] and action in row["actions"]
               for row in policy["access"])
