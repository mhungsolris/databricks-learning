# sdp

Source: https://docs.databricks.com/aws/en/ldp/concepts/spark-declarative-pipelines
Retrieved: 2026-10-11

Apache Spark Declarative Pipelines | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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
Concepts 
Apache Spark Declarative Pipelines On this page Last updated on Oct 9, 2026 
Apache Spark Declarative Pipelines 
Lakeflow pipelines are built on Apache Spark™ Declarative Pipelines (SDP). Lakeflow pipelines run on the performance-optimized Databricks Runtime , and are interoperable with SDP. Because pipelines build on SDP rather than proprietary APIs, the transformation code you write stays portable to other SDP runtimes. 
What is Spark Declarative Pipelines? ​ 
Apache Spark Declarative Pipelines is a declarative framework for developing and running batch and streaming data pipelines in SQL and Python. SDP automates the orchestration and organizes the dependencies between the flows in your pipeline. SDP simplifies ingestion and transformation development, so that you do not have to focus on the mechanics of the orchestration of your data workflows. 
Common use cases for SDP include: 
Batch data ingestion from sources such as cloud storage (Amazon S3, Azure ADLS Gen2, and Google Cloud Storage). 
Incremental data ingestion from message buses (such as Apache Kafka, Amazon Kinesis, Google Pub/Sub, Azure EventHub, and Apache Pulsar). 
Incremental batch and streaming transformations with stateless and stateful operators. 
For more details on declarative data processing, see Procedural vs. declarative data processing in Databricks . 
How do Lakeflow pipelines extend SDP? ​ 
Lakeflow pipelines share the same declarative authoring model as SDP and add production features such as AUTO CDC, data quality expectations, and a queryable event log. This table compares the capabilities that Lakeflow pipelines share with SDP and the production features that Databricks adds on top. For a property-by-property mapping between the SDP project specification and pipeline configuration, see Pipeline properties reference . 

Capability 
SDP 
Lakeflow pipelines 

Declarative pipelines in SQL and Python 
✓ 
✓ 

Streaming tables 
✓ 
✓ 

Materialized views 
✓ 
✓ 

Temporary views 
✓ 
✓ 

Append flows 
✓ 
✓ 

Sinks (Delta, Apache Kafka, and Azure Event Hubs ) 
✓ 
✓ 

Automatic orchestration and dependency resolution 
✓ 
✓ 

Pipeline code that is portable across SDP runtimes 
✓ 
✓ 

AUTO CDC (SCD Type 1 and SCD Type 2) and AUTO CDC from snapshot 
— 
✓ 

Data quality expectations 
— 
✓ 

Queryable event log 
— 
✓ 

Update flows and foreachBatch sinks 
— 
✓ 

Continuous mode 
— 
✓ ← ✕ 

Capability 
SDP 
Lakeflow pipelines 

Declarative pipelines in SQL and Python 
✓ 
✓ 

Streaming tables 
✓ 
✓ 

Materialized views 
✓ 
✓ 

Temporary views 
✓ 
✓ 

Append flows 
✓ 
✓ 

Sinks (Delta, Apache Kafka, and Azure Event Hubs ) 
✓ 
✓ 

Automatic orchestration and dependency resolution 
✓ 
✓ 

Pipeline code that is portable across SDP runtimes 
✓ 
✓ 

AUTO CDC (SCD Type 1 and SCD Type 2) and AUTO CDC from snapshot 
— 
✓ 

Data quality expectations 
— 
✓ 

Queryable event log 
— 
✓ 

Update flows and foreachBatch sinks 
— 
✓ 

Continuous mode 
— 
✓ 
Additional resources ​ 
What are Lakeflow pipelines ? 
Lakeflow pipelines Python language reference 
Pipeline properties reference 
Procedural vs. declarative data processing in Databricks On this page 
What is Spark Declarative Pipelines? 
How do Lakeflow pipelines extend SDP? 
Additional resources Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 