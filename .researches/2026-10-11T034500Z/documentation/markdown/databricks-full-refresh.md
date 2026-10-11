# databricks-full-refresh

Source: https://docs.databricks.com/aws/en/ldp/full-refresh-st
Retrieved: 2026-10-11

Full refresh for streaming tables | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
Support 
Knowledge Base 
Community 
Training English 
English 
日本語 
Português 
Français AWS 
Azure 
GCP 
SAP Try Databricks 

Data engineering 
Lakeflow pipelines 
Build pipelines 
Full refresh for streaming tables On this page Last updated on Sep 11, 2026 
Full refresh for streaming tables 
A full refresh of a streaming table discards all existing data and metadata and restarts the stream from the beginning. Specifically, it truncates the streaming table , removes all checkpoint data, and restarts the streaming process with new checkpoints for every flow writing to the table. The following sections cover when to run a full refresh, its impact on data sources, and best practices. 
For an overview of how refreshes work across pipeline datasets, see How do pipelines refresh? . For guidance on how to trigger a full refresh, see Run a pipeline update . 
Impact on data sources ​ 
A full refresh removes all existing data from the streaming table . If your data source has retention limits (such as Kafka topics with short retention periods), some historical data may become unrecoverable after a full refresh. 
For example, if your source is Kafka with 24-hour retention and you run a full refresh after that window, older messages are no longer available and cannot be reprocessed. note 
Full refreshes are not recommended for high-volume streaming workloads or when upstream retention prevents replaying historical data. 
If the streaming table has dependent downstream tables, the pipeline fails until those tables are also fully refreshed, unless the streaming table has skipChangeCommits enabled. Downstream materialized views must also be fully refreshed. 
When to run a full refresh ​ 
Full refreshes must be triggered explicitly. You can run a full refresh by clicking Full Refresh in the pipeline UI or by enabling auto full refresh in Lakeflow Connect . 
A full refresh is recommended when changes prevent a streaming query from safely resuming from its existing checkpoint, or when previously processed data would become inconsistent with updated logic, schema, or source configuration. The following sections describe common scenarios. 
Schema changes ​ 
The following schema changes in the target table are not backward-compatible and require a full refresh: 
Renaming columns without column mapping mode enabled. 
Changing deduplication columns. 
Modifying column data types, including: 
Type narrowing (for example, BIGINT → INT or DOUBLE → FLOAT ). 
Incompatible type changes (for example, STRING → INT ). 
Hard deletion of columns from the table schema. 
For these types of schema changes, Databricks recommends creating a new column with the desired schema or name, then using a view on top of the streaming table to union the old and new values. 
Physical data layout changes ​ 
The following physical data layout changes require a full refresh: 
Migrating from legacy partitioning to a new clustering scheme. 
Upstream source changes ​ 
The following upstream source changes require a full refresh: 
Modifying the source tables read by the streaming query. 
Switching between source types (for example, Kafka to Delta or Auto Loader to Kafka). 
Changing source locations, such as table paths or Kafka topic subscriptions. 
Dropping and recreating a source Delta table, even when the schema remains unchanged. 
Stateful processing changes ​ 
The following stateful processing changes require a full refresh: 
Modifying aggregation grouping keys or aggregate functions. 
Adding or removing aggregations. 
Changing join keys or join types. 
Adding or removing joins. 
Modifying deduplication columns or deduplication logic. 
Data continuity issues ​ 
A full refresh may be required when data continuity is compromised: 
CDC logs have become unavailable due to retention expiration. 
Corruption or deletion of the streaming checkpoint directory. 
Corruption or loss of schema tracking or schema location files. 
For more information on recovering a pipeline from checkpoint failure, see Recover a pipeline from streaming checkpoint failure . 
Limitations ​ 
The following limitations apply to full refreshes. See Best practices for information to help working within these limitations. 
A full refresh does not reprocess data unless your source retains the full historical dataset. 
Large datasets can make full refreshes costly and time-consuming. 
Downstream consumers that depend on the table may fail or return incomplete results until the refresh completes. 
Best practices ​ 

Situation 
Best practices 

Design for stability 
Plan your schema to avoid changes that require a full refresh. Adding columns is generally safe, while modifying existing columns or partitioning schemes typically requires recomputing the table. 

Stream from sources with short retention periods 
Streaming from sources, such as a Kafka topic, that do not have long retention periods means that a full refresh loses data not still in the source. 
To avoid losing historical data, stream raw data into a streaming table (a bronze table, in the medallion architecture ). Use flexible column types (variant or string, for example), to avoid this table requiring a full refresh if upstream data changes. This table can store historical data and be used by downstream streaming tables (that may have stricter types or other structural changes). If the downstream tables require a full refresh, this table has historical data, while not requiring a full refresh itself. 

Consider alternatives before running a full refresh 
Alternatives include: 
If changing the source of a flow, consider creating a new flow rather than updating the existing flow of a streaming table . This preserves the existing data in the table, but may write duplicate data because the new flow has a new checkpoint. 
Alternatively, you can reset the checkpoint, but this may lead to duplicate data being written to the target table. 
If none of these options is acceptable, consider creating a new streaming table and using a view to union the old and new streaming tables . 

When a full refresh is required 
Follow these best practices when a full refresh is required: 
Test the operation in a development or staging environment. 
Document downstream dependencies that are affected. 
Schedule the refresh during a maintenance window to minimize impact on production workloads. 
Ensure the source system retains enough historical data to replay the stream. ← ✕ 

Situation 
Best practices 

Design for stability 
Plan your schema to avoid changes that require a full refresh. Adding columns is generally safe, while modifying existing columns or partitioning schemes typically requires recomputing the table. 

Stream from sources with short retention periods 
Streaming from sources, such as a Kafka topic, that do not have long retention periods means that a full refresh loses data not still in the source. 
To avoid losing historical data, stream raw data into a streaming table (a bronze table, in the medallion architecture ). Use flexible column types (variant or string, for example), to avoid this table requiring a full refresh if upstream data changes. This table can store historical data and be used by downstream streaming tables (that may have stricter types or other structural changes). If the downstream tables require a full refresh, this table has historical data, while not requiring a full refresh itself. 

Consider alternatives before running a full refresh 
Alternatives include: 
If changing the source of a flow, consider creating a new flow rather than updating the existing flow of a streaming table . This preserves the existing data in the table, but may write duplicate data because the new flow has a new checkpoint. 
Alternatively, you can reset the checkpoint, but this may lead to duplicate data being written to the target table. 
If none of these options is acceptable, consider creating a new streaming table and using a view to union the old and new streaming tables . 

When a full refresh is required 
Follow these best practices when a full refresh is required: 
Test the operation in a development or staging environment. 
Document downstream dependencies that are affected. 
Schedule the refresh during a maintenance window to minimize impact on production workloads. 
Ensure the source system retains enough historical data to replay the stream. 
To backfill data after a full refresh, you can create an append once flow . This performs a one-time backfill without continuing to run after the first backfill. The code remains in your pipeline, and if the pipeline is ever fully refreshed again, the backfill reruns. On this page 
Impact on data sources 
When to run a full refresh 
Schema changes 
Physical data layout changes 
Upstream source changes 
Stateful processing changes 
Data continuity issues 
Limitations 
Best practices Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 