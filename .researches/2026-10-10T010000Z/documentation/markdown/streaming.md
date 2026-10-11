# streaming

Source: https://docs.databricks.com/aws/en/structured-streaming/concepts
Retrieved: 2026-10-10

Structured Streaming concepts | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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

Apache Spark 
Structured Streaming On this page Last updated on Oct 7, 2026 
Structured Streaming concepts 
Apache Spark Structured Streaming is a near real-time processing engine that offers end-to-end fault tolerance with exactly-once processing guarantees using familiar Spark APIs. Structured Streaming lets you express computation on streaming data in the same way you express a batch computation on static data. The Structured Streaming engine performs the computation incrementally and continuously updates the result as streaming data arrives. 
For a step-by-step tutorial, see Run your first Structured Streaming workload . 
Read from a data stream ​ 
Use Structured Streaming to incrementally ingest data from supported data sources. 

Auto Loader 
Incrementally and efficiently process new data files as they arrive in cloud storage. 

Delta Lake table streaming reads and writes 
Use Delta Lake tables as streaming sources and sinks with exactly-once processing guarantees. 

SQL and Spark APIs 
Connect to message buses, queues, and enterprise applications using SQL and Spark APIs. 

Micro-batch size 
Limit input rates to maintain consistent batch sizes and prevent processing delays. 
Write to a data sink ​ 
Configure how Structured Streaming delivers data to target systems. 

Checkpoints 
Store processing state to enable fault tolerance and exactly-once delivery semantics. 

Output mode 
Choose between append, update, and complete modes for stateful streaming queries. 

Trigger intervals 
Set trigger intervals to balance latency and cost for your processing requirements. 

Real-time mode in Structured Streaming 
Process data for real-time workloads with end-to-end latency as low as five milliseconds. 
Stateful and stateless processing ​ 
Stateless queries process rows without retaining state. Stateful queries maintain intermediate state for aggregations, joins, and deduplication. 

Stateless streaming queries 
Optimize queries that process data without maintaining intermediate state. 

Watermarks 
Control how long Structured Streaming waits for late-arriving data in stateful operations. 

Stateful streaming 
Manage aggregations, stream-stream joins, and deduplication using stateful operators. 
Monitor and manage ​ 
Track query performance, apply optimizations, and govern data access for production Structured Streaming workloads. 

Monitor with StreamingQueryListener 
Track query progress and performance metrics using the Spark UI and listener API. 

Govern with Unity Catalog 
Configure Unity Catalog for streaming workloads with governance and access control. On this page 
Read from a data stream 
Write to a data sink 
Stateful and stateless processing 
Monitor and manage Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 