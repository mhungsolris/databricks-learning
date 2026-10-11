# Production hardening research plan

Kind: descriptive | Audience: data engineers moving from BigQuery/Airflow to Databricks | Purpose: diagnose, test and release a bounded ROAS pipeline | Non-goals: production deployment or a cloud performance benchmark without a user workspace.

Research question: What are current AWS Databricks layout, execution, observability, expectations and bundle/OIDC release semantics and their availability boundaries?

Known baseline: Spark 4.0.4 and Delta 4.0.1 local evidence, Chapters 00-30; no selected workspace, CLI authentication or cloud execution.

Enough evidence: authoritative current product/CLI pages for each feature, with runtime/cloud requirements and explicit unsupported local claims; actual local plans, file layout, transformation and failure tests.

Course document checkpoint: Kind: descriptive | Audience: experienced SQL/Airflow learners | Purpose: investigate and safely operate ROAS workflows | Non-goals: implementation trivia, invented production timings, a FinOps course.

Lab checkpoint: Kind: runbook | Audience: the same learners | Purpose: reproduce bounded local experiments and prepare workspace acceptance | Non-goals: treating static checks as deployment proof.

Gate checkpoint: Kind: normative | Audience: learners and reviewers | Purpose: assess evidence-ranked diagnosis and release readiness | Non-goals: product trivia or public reviewer answers.
