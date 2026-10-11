# databricks-production

Source: https://docs.databricks.com/aws/en/structured-streaming/production
Retrieved: 2026-10-11

Production considerations for Structured Streaming | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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
Best practices 
Structured streaming production 
General production best practices On this page Last updated on Oct 8, 2026 
Production considerations for Structured Streaming 
Run production Structured Streaming workloads as scheduled Lakeflow Jobs on Databricks . See Lakeflow Jobs . 
Databricks recommends that you always configure the following: 
Remove unnecessary code from notebooks that would return results, such as display and count . 
Don't run Structured Streaming workloads using all-purpose compute. Always schedule streams as Lakeflow Jobs using jobs compute. 
Schedule Lakeflow Jobs using Continuous mode . This refers to the Databricks Jobs scheduling feature, not the Structured Streaming trigger interval . 
Don't enable autoscaling for compute for Structured Streaming jobs. 
Some workloads benefit from the following: 
Configure RocksDB state store on Databricks 
Asynchronous state checkpointing for stateful queries 
Asynchronous progress tracking 
Databricks introduced Lakeflow pipelines to reduce the complexities of managing production infrastructure for Structured Streaming workloads. Databricks recommends using Lakeflow pipelines for new Structured Streaming pipelines. See Spark Declarative Pipelines . note 
Compute auto-scaling has limitations scaling down cluster size for Structured Streaming workloads. Databricks recommends using Spark Declarative Pipelines on Lakeflow with enhanced autoscaling for streaming workloads. See Optimize Lakeflow pipeline cluster utilization with autoscaling . note 
On serverless compute , only Trigger.AvailableNow() and Trigger.Once() are supported. Databricks recommends Trigger.AvailableNow() . 
For continuous streaming on serverless compute , use Triggered vs. continuous pipeline mode in continuous mode. 
See Streaming limitations . 
Reduce latency for operational streaming ​ 
Operational streaming workloads ingest, transform, and act on data in near real time. Common examples include fraud detection, anomaly detection, personalization, and real-time monitoring and alerting, where delayed processing directly affects business outcomes. Low latency for these workloads typically means tens to hundreds of milliseconds, though many teams set service level agreements (SLAs) in the seconds range to account for variability at higher percentiles. 
For the lowest end-to-end latency, use real-time mode, which achieves end-to-end latency under one second at the tail and around 300 milliseconds in common cases. See Real-time mode concepts . 
When real-time mode doesn't fit your workload, the following best practices reduce latency for micro-batch Structured Streaming : 
Output mode : Use update mode where your query operators and sink support it. Update mode emits updated rows after each trigger and keeps updating them until the watermark expires, so make your downstream sink idempotent to handle updated results. Use append mode for workloads that update mode doesn't support, such as stream-stream joins, or when you can drop late-arriving data. Don't use complete mode for low latency. See Select an output mode for Structured Streaming . 
Trigger : Use a processingTime trigger with a 0 interval, which starts the next micro-batch as soon as the previous one finishes and new data is available. This delivers the lowest micro-batch latency, but it increases cloud storage API costs. Don't use AvailableNow , Once , or Continuous for operational workloads. See Configure Structured Streaming trigger intervals . 
Watermark : Set the watermark long enough to include the late-arriving data that your workload must not drop. The watermark controls how long the query accepts out-of-order event-time data before dropping it and evicting state, so a watermark that is too short silently discards valid late records. Within that constraint, a shorter watermark lowers latency and retains less state, and a longer watermark tolerates more late data at the cost of latency and state. A small multiple of your latency SLA, such as 2x, is a reasonable starting point for tuning. See Apply watermarks to control data processing thresholds . 
Sources and sinks : Read from low-latency sources such as message buses (Apache Kafka, Amazon Kinesis, Apache Pulsar, or Google Cloud Pub/Sub) or change data feeds from Delta Lake and Apache Iceberg tables. Write to low-latency, high-throughput sinks such as message buses, operational databases, or foreach sinks. Design sink operations to be idempotent so that downstream consumers handle duplicates and late-arriving data. 
State and checkpointing : For stateful queries, use the RocksDB state store, which is required for both changelog checkpointing and asynchronous state checkpointing. Enable changelog checkpointing to persist only incremental state changes. When state checkpointing is the bottleneck in your batch duration, enable asynchronous state checkpointing to overlap checkpoint writes with the next micro-batch, after reviewing its failure-recovery and cluster-resizing caveats. Give each query its own checkpoint directory in durable cloud storage. See Configure RocksDB state store on Databricks , Asynchronous state checkpointing for stateful queries , and Structured Streaming checkpoints . 
Offset management : To reduce latency from offset checkpointing in continuous streams, enable asynchronous progress tracking, which updates the offset and commit logs without blocking data processing. It isn't compatible with the AvailableNow or Once triggers. See Asynchronous progress tracking . 
Storage hops : Keep computation within a single streaming pipeline where possible. Splitting logic across multiple jobs or pipelines adds storage hops that increase latency. 
Design streaming workloads to expect failure ​ 
Databricks recommends that you always configure streaming jobs to automatically restart on failure. Some capabilities, including schema evolution, require that Structured Streaming workloads retry automatically. See Configure Structured Streaming jobs to restart streaming queries on failure . 
Some operations like foreachBatch provide at-least-once rather than exactly-once guarantees. For these operations, make sure that your processing pipeline is idempotent. See Use foreachBatch to write to arbitrary data sinks . note 
When a query restarts, the micro-batch planned during the previous run processes. If your job failed due to an out-of-memory error or you manually canceled a job due to an oversized micro-batch, you might need to scale up the compute to successfully process the micro-batch. 
If you change configurations between runs, these configurations apply to the first new batch planned. See Recover after changes in a Structured Streaming query . 
When a job retries ​ 
You can schedule multiple tasks as part of a Databricks job. When you configure a job using the continuous trigger, you cannot set dependencies between tasks. 
You might choose to schedule multiple streams in a single job using one of the following approaches: 
Multiple tasks : Define a job with multiple tasks that run streaming workloads using the continuous trigger. 
Multiple queries : Define multiple streaming queries in the source code for a single task. 
You can also combine these strategies. The following table compares these approaches. 

Strategy 
Multiple tasks 
Multiple queries 

How is compute shared? 
Databricks recommends deploying jobs compute appropriately sized to each streaming task. You can optionally share compute across tasks. 
All queries share the same compute. You can optionally assign queries to scheduler pools . 

How are retries handled? 
All tasks must fail before the job retries. 
The task retries if any query fails. ← ✕ 

Strategy 
Multiple tasks 
Multiple queries 

How is compute shared? 
Databricks recommends deploying jobs compute appropriately sized to each streaming task. You can optionally share compute across tasks. 
All queries share the same compute. You can optionally assign queries to scheduler pools . 

How are retries handled? 
All tasks must fail before the job retries. 
The task retries if any query fails. 
For more details on working with multiple tasks or queries, see Run multiple Structured Streaming queries on the same cluster . 
Configure Structured Streaming jobs to restart streaming queries on failure ​ 
Databricks recommends that you configure all streaming workloads using the continuous trigger. See Run jobs continuously . 
The continuous trigger has the following behavior by default: 
Prevents more than one concurrent run of the job. 
Starts a new run when a previous run fails. 
Uses exponential backoff for retries. 
Databricks recommends always using jobs compute instead of all-purpose compute when scheduling workflows. On job failure and retry, new compute resources deploy. note 
Databricks recommends that you do not use streamingQuery.awaitTermination() or spark.streams.awaitAnyTermination() . See When to use awaitTermination() . 
When to use awaitTermination() ​ 
streamingQuery.awaitTermination() and spark.streams.awaitAnyTermination() block the current thread until a streaming query terminates. Whether to use these functions depends on your execution environment. 
For Lakeflow Jobs, do not use streamingQuery.awaitTermination() or spark.streams.awaitAnyTermination() . These functions are not necessary because the Jobs service automatically prevents a run from completing when a streaming query is active. Both functions block notebook cells from completing and prevent the Jobs service from tracking the streaming query, which disrupts backlog metrics and job notifications. 
Use awaitTermination() in the following cases: 

Use case 
Behavior 

Interactive notebooks on all-purpose compute 
awaitTermination() keeps the cell running, allows you to observe query state, and ensures that failures surface in the notebook output. 

Local and development environments 
When running a Spark program locally, the process exits when the main thread completes. Call awaitTermination() to keep the program alive until the streaming query finishes or fails. 

Failure propagation to the driver 
Without awaitTermination() , a streaming query failure in a non-job context may not propagate to the calling thread. The query can fail silently, making failures harder to detect and diagnose. Calling awaitTermination() raises the query exception on the driver again. ← ✕ 

Use case 
Behavior 

Interactive notebooks on all-purpose compute 
awaitTermination() keeps the cell running, allows you to observe query state, and ensures that failures surface in the notebook output. 

Local and development environments 
When running a Spark program locally, the process exits when the main thread completes. Call awaitTermination() to keep the program alive until the streaming query finishes or fails. 

Failure propagation to the driver 
Without awaitTermination() , a streaming query failure in a non-job context may not propagate to the calling thread. The query can fail silently, making failures harder to detect and diagnose. Calling awaitTermination() raises the query exception on the driver again. On this page 
Reduce latency for operational streaming 
Design streaming workloads to expect failure 
When a job retries 
Configure Structured Streaming jobs to restart streaming queries on failure 
When to use awaitTermination() Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 