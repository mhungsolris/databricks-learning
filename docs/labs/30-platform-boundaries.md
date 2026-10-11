---
title: 'Lab 30 · Platform boundaries'
prev:
  text: 'Chapter 30'
  link: /platform/30-platform-boundaries
next:
  text: 'Mid Gate · Platform Design'
  link: /assessments/mid-gate-platform-design
---

# Lab 30 · Platform boundaries

LOCAL LAB architecture exercise, no resource deployment.

Design Architecture A with most internal transformations/orchestration in Databricks and Architecture B with Airflow coordinating APIs, Databricks jobs and other services. Use the company scenario in Chapter30: Meta, Google Ads, GCS, Salesforce and Looker.

For each design submit a diagram, source adapter owner, retained-truth/cutoff contract, task vs dataset graph, per-task compute, UC hierarchy/run identity, SQL serving audience and scheduler/write ownership. Compare simplicity, vendor coupling, operability, skills, observability, cost and portability. State a condition under which you would switch designs.

Trace four failures: validation rejects an input; uncertain job-submission acknowledgement; a72h attribution revision; source retention gap during repair. Add denied PII access as a governance test. Mark proofs PORTABLE TEST, LOCAL SPARK TEST or DATABRICKS WORKSPACE TEST. Require separate production acceptance evidence.

Then submit [Mid Gate · Databricks Platform Design](/assessments/mid-gate-platform-design). PASS: two consistent architectures with explicit trade-offs; NOT YET: maximum platform feature use is the only objective.

