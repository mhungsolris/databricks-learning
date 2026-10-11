# Streaming correctness audit

Kind: review record. Scope: Chapters16-24, executable local labs and Mid Gate. Commands and measured results belong to PROGRESS.md and the published streaming evidence manifest; this table records the conceptual checks and their owners.

| Check | Course contract / evidence owner |
|---|---|
| Watermark vs batch high-water mark | Chapter19 has the four-mechanism table; cursor, lookback, reconciliation and streaming watermark answer different questions |
| Checkpoint more than offsets | Chapter18 lists source progress, commits, state and metadata; Labs17/18 inventory real files |
| Checkpoint vs business correctness | Chapters18/24 require source/sink/reconciliation assumptions; cp reset does not reset target |
| Micro-batch vs record-by-record | Chapter16 teaches repeated incremental execution, variable input size and trigger vs processing duration; awareness modes are scoped separately |
| Exactly-once vs physical delivery | Chapter23 permits repeat attempts and checks one logical sink effect |
| Sink semantics | Chapters22/23 map output modes to keyed replacement, snapshots and append; Lab23 compares unsafe and transactional retry |
| State growth | Chapter17 demonstrates retained aggregate state and infinite seen-key growth; Chapters19-21 define eligibility/expiry |
| Checkpoint incompatibility | Chapter18 compatibility table uses pinned official restrictions; Lab24 changes actual grouping keys on diagnostic cp copy |
| When to choose batch | Chapter16 explicitly covers daily sources, hourly SLA, bounded cost and hybrid ROAS architecture |
| Actual restart/recovery | Labs17/18 restart same cp, Lab18 starts new cp, Lab23 retries an incomplete batch and Lab24 rebuilds isolated staging |

## Execution limitations

Local execution uses Spark4.0.4/Delta4.0.1, not Databricks Runtime. Controlled stops are not process crashes. Lab23 injects a callback exception after one durable Delta sink write; no remote API or distributed crash is claimed. Lab24 reproduces incompatible state schema; cloud storage corruption, permission repair and production cutover remain outside this exercise.

Checkpoint new-generation behavior is source-specific. File discovery evidence must not be generalized to Kafka offsets or other source defaults. State provider configuration is observed, not generalized to DBR defaults. Short-policy late-drop evidence depends on controlled event-time advancement; older-than-delay input is not universally guaranteed to drop.

Recovery decisions are pedagogical fact patterns, not an automated production remediation system. A readable compatible cp still needs available source positions; a missing-truth case cannot prove Gold correctness. Cost API and Gold reconciliation may stay scheduled batch while callbacks stream into Bronze. A two-hour event-time state horizon does not replace 72-hour mutation detection and historical repair.
