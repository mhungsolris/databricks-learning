# Architecture research plan

Kind: descriptive | Audience: Python/SQL data engineer moving toward architecture judgment | Purpose: choose formats and platforms from requirements and defend trade-offs | Non-goals: cloud deployment, marketing rankings, toy performance comparisons.

Runtime guide: Kind: runbook | Audience: Windows learner with Docker | Purpose: reproduce Iceberg semantics with Spark 4.0.4 | Non-goals: production Hadoop catalog or authenticated catalog setup.

ADRs and gates: Kind: descriptive | Audience: learner and reviewer | Purpose: defend decisions, alternatives and measurable reversal conditions | Non-goals: a universal platform winner or published assessment solutions.

Research questions:
1. Which official Iceberg artifact supports Spark 4.0/Scala 2.13, and which local schema, partition and mutation semantics can be reproduced?
2. Known baseline: Spark 4.0.4 and Delta 4.0.1 are locally verified; platform execution is pending. Platform format support must be reverified.
3. Enough evidence: version-qualified official integration/spec sources plus official platform pages for each managed/external/read/write boundary. Record date, cloud, status and gaps. Archive through repository scripts with publication disabled.
