# Platform research plan

Question: Which current Databricks abstractions, Free Edition limits and supported Jobs/pipeline/SQL/Unity Catalog interfaces let a learner design an operable ROAS platform?

Known baseline: local Spark 4.0.4 and Delta 4.0.1 execution, Chapters 00-24 and two correctness gates accepted. No authorized workspace/profile or cloud execution evidence.

Stopping rule: official current AWS documentation for each product and its relevant limits, Apache Spark documentation for SDP, official Airflow/dbt/BigQuery sources for comparisons. Check terminology and executable schema claims separately. Archive retrieved documents and discovery results; publication disabled.

Kind: descriptive | Audience: Data Engineer moving from Airflow/BigQuery/dbt to Databricks | Purpose: choose platform responsibilities and justify boundaries | Non-goals: cloud VM provisioning, production benchmarking, enterprise setup, credential configuration.

Kind: runbook | Audience: same learner with optional self-owned workspace | Purpose: execute bounded sample labs and collect redacted evidence | Non-goals: signup automation or claiming unexecuted workspace steps as verified.

Kind: reference | Audience: reviewer | Purpose: distinguish portable/config evidence from workspace evidence | Non-goals: substitute local simulations for Databricks integration tests.
