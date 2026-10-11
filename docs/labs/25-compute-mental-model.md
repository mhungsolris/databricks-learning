---
title: 'Lab 25 · Compute classification'
prev:
  text: 'Chapter 25'
  link: /platform/25-compute-mental-model
next:
  text: 'Chapter 26'
  link: /platform/26-lakeflow-jobs
---

# Lab 25 · Compute classification

LOCAL LAB: select serverless notebook, serverless jobs, classic jobs, SQL warehouse, pipeline compute or insufficient information. Require WHY and one fact that would change the answer.

| # | Workload | Known facts |
|---|---|---|
| 1 | Exploratory notebook | Python DataFrame/SQL over UC tables; no custom extensions |
| 2 | Hourly ETL | Supported Python notebook task and pinned pure-Python dependencies |
| 3 | Marketing dashboard | SQL queries over Gold, BI concurrency unknown |
| 4 | Scala JAR | Uses RDD API and native JNI dependency |
| 5 | Declarative medallion | Lakeflow dataset graph, managed triggered update |
| 6 | “A JAR job” | API/dependency/environment requirements unknown |
| 7 | External API extractor | Requires endpoint not allowed by current Free Edition outbound policy |
| 8 | SQL reconciliation | SQL task on an accessible supported warehouse |
| 9 | Legacy Spark Submit | Requires unsupported serverless task/runtime customization |
| 10 | Bounded callback processing | Notebook job using AvailableNow, supported APIs and UC source/target |

Do not create resources. Card7 may require an external adapter rather than any available compute. Cards3/6 need additional information for capacity or compatibility. Submit execution surface, assumptions, compatibility/source check, cost owner and production limitations. PASS when reasoning is complete; NOT YET when the choice follows file extension only.

