---
title: 'Lab 28 · Governance design'
prev:
  text: 'Chapter 28'
  link: /platform/28-unity-catalog
next:
  text: 'Chapter 29'
  link: /platform/29-databricks-sql
---

# Lab 28 · Governance design

LOCAL LAB design plus an optional DATABRICKS FREE EDITION LAB metadata subset. Workspace evidence PENDING USER WORKSPACE.

Design the ROAS system for Data Engineer, Marketing Analyst, Finance and Service Principal, using Bronze callbacks, Silver events, Gold ROAS and donor/customer PII. Submit environment hierarchy, stable ownership groups, run identity, action/traversal grants, inherited access review and lineage path. Justify either environment catalogs or domain catalogs with explicit environment isolation.

Review labs/platform/governance-policy.json and sql/governance.sql as a design example. Write positive/negative access expectations: Marketing may read Gold but not PII; Finance sees approved aggregates; production writer has only required output/source privileges; dev writer cannot write prod. Explain how group/parent grants could defeat a narrow revoke.

Optional safe subset, only with owned objects from Lab26:

```sql
SELECT current_catalog(), current_schema();
SHOW TABLES;
DESCRIBE TABLE gold_roas;
SHOW GRANTS ON TABLE gold_roas;
```

Inspect Catalog Explorer hierarchy/lineage where available. Record availability and read-only metadata, redacted. These statements are proposed workspace actions, not local UC proof. SHOW GRANTS needs appropriate visibility and does not on its own prove effective access for every principal.

Do not create account groups, service principals, cloud storage credentials or external locations in Free Edition. Enterprise group/IAM/private-network/multi-workspace tests require an authorized supported environment. Do not apply roas_prod example grants to real existing objects. PASS: role/action matrix and ownership/isolation reasoning; NOT YET: namespace hierarchy presented as enough.

