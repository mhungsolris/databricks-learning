# databricks-stateful

Source: https://docs.databricks.com/aws/en/structured-streaming/stateful-streaming
Retrieved: 2026-10-11

What is stateful streaming? | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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
Structured Streaming 
Stateful processing 
Joins and aggregations On this page Last updated on Oct 9, 2026 
What is stateful streaming? 
This page explains stateful Structured Streaming queries, including stateful operations, optimization recommendations, chaining multiple stateful operators, and state rebalancing. 
A stateful Structured Streaming query requires incremental updates to intermediate state information, whereas a stateless Structured Streaming query only tracks information about which rows have been processed from the source to the sink. For optimization features available for stateless queries, see Optimize stateless streaming queries . 
Stateful operations ​ 
Stateful operations include streaming aggregation, distinct , dropDuplicates , stream-stream joins, and custom stateful applications. 
The intermediate state information required for stateful Structured Streaming queries can lead to unexpected latency and production problems if misconfigured. 
In Databricks Runtime 13.3 LTS or later, you can enable changelog checkpointing with RocksDB to lower checkpoint duration and end-to-end latency for Structured Streaming workloads. Databricks recommends enabling changelog checkpointing for all Structured Streaming stateful queries. See Enable changelog checkpointing . 
Optimize stateful Structured Streaming queries ​ 
Databricks recommends the following for stateful Structured Streaming queries: 
Use compute-optimized instances as workers. 
Set the number of shuffle partitions to 1-2 times the number of cores in the cluster. important 
The number of shuffle partitions is fixed at the time the checkpoint is created. Changing spark.sql.shuffle.partitions has no effect on a streaming query that already has a checkpoint — the query continues using the original partition count. To apply a new partition count, you must start the query with a new checkpoint location. 
In Databricks Runtime 18.0 and above, stateless streaming queries support dynamic shuffle partition changes without requiring a new checkpoint. 
In Databricks Runtime 18 LTS and above, you can change the partition count for stateful queries without losing checkpoint state. See On-demand state repartitioning for stateful streaming queries . 
Set the spark.sql.streaming.noDataMicroBatches.enabled configuration to false in the SparkSession. This prevents the streaming micro-batch engine from processing micro-batches that don't contain data. Setting this configuration to false might also result in stateful operations that use watermarks or processing time timeouts not getting data output until new data arrives instead of immediately. 
Databricks recommends using RocksDB with changelog checkpointing to manage the state for stateful streams. See Configure RocksDB state store on Databricks . note 
The state management scheme can't be changed between query restarts. If a query has been started with the default management, you must restart it from scratch with a new checkpoint location to change the state store. 
Work with multiple stateful operators in Structured Streaming ​ 
In Databricks Runtime 13.3 LTS or later, Databricks offers advanced support for stateful operators in Structured Streaming workloads. You can chain multiple stateful operators together, meaning you can feed the output of an operation, such as a windowed aggregation, to another stateful operation, such as a join. 
In Databricks Runtime 16.2 or later, you can use transformWithState in workloads with multiple stateful operators. See Build a custom stateful application with transformWithState . 
The following examples demonstrate several patterns you can use. important 
The following limitations exist when working with multiple stateful operators: 
Legacy custom stateful operators ( FlatMapGroupWithState and applyInPandasWithState ) are not supported. 
Only the append output mode is supported. 
Chained time window aggregation ​ 
Python 
Scala Python 
words = . . . # streaming DataFrame of schema { timestamp: Timestamp, word: String } # Group the data by window and word and compute the count of each group windowedCounts = words . groupBy ( window ( words . timestamp , "10 minutes" , "5 minutes" ) , words . word ) . count ( ) # Group the windowed data by another window and word and compute the count of each group anotherWindowedCounts = windowedCounts . groupBy ( window ( window_time ( windowedCounts . window ) , "1 hour" ) , windowedCounts . word ) . count ( ) Scala 
import spark . implicits . _ val words = . . . // streaming DataFrame of schema { timestamp: Timestamp, word: String } // Group the data by window and word and compute the count of each group val windowedCounts = words . groupBy ( window ( $ "timestamp" , "10 minutes" , "5 minutes" ) , $ "word" ) . count ( ) // Group the windowed data by another window and word and compute the count of each group val anotherWindowedCounts = windowedCounts . groupBy ( window ( $ "window" , "1 hour" ) , $ "word" ) . count ( ) 
Time window aggregation in two different streams followed by stream-stream window join ​ 
Python 
Scala Python 
clicksWindow = clicksWithWatermark . groupBy ( clicksWithWatermark . clickAdId , window ( clicksWithWatermark . clickTime , "1 hour" ) ) . count ( ) impressionsWindow = impressionsWithWatermark . groupBy ( impressionsWithWatermark . impressionAdId , window ( impressionsWithWatermark . impressionTime , "1 hour" ) ) . count ( ) clicksWindow . join ( impressionsWindow , "window" , "inner" ) Scala 
val clicksWindow = clicksWithWatermark . groupBy ( window ( "clickTime" , "1 hour" ) ) . count ( ) val impressionsWindow = impressionsWithWatermark . groupBy ( window ( "impressionTime" , "1 hour" ) ) . count ( ) clicksWindow . join ( impressionsWindow , "window" , "inner" ) 
Stream-stream time interval join followed by time window aggregation ​ 
Python 
Scala Python 
joined = impressionsWithWatermark . join ( clicksWithWatermark , expr ( """ clickAdId = impressionAdId AND clickTime >= impressionTime AND clickTime <= impressionTime + interval 1 hour """ ) , "leftOuter" # can be "inner", "leftOuter", "rightOuter", "fullOuter", "leftSemi" ) joined . groupBy ( joined . clickAdId , window ( joined . clickTime , "1 hour" ) ) . count ( ) Scala 
val joined = impressionsWithWatermark . join ( clicksWithWatermark , expr ( """ clickAdId = impressionAdId AND clickTime >= impressionTime AND clickTime <= impressionTime + interval 1 hour """ ) , joinType = "leftOuter" // can be "inner", "leftOuter", "rightOuter", "fullOuter", "leftSemi" ) joined . groupBy ( $ "clickAdId" , window ( $ "clickTime" , "1 hour" ) ) . count ( ) 
State rebalancing for Structured Streaming ​ 
State rebalancing is enabled by default for all streaming workloads in Lakeflow pipelines . In Databricks Runtime 11.3 LTS or later, you can set the following configuration option in the Spark cluster configuration to enable state rebalancing: ini 
spark.sql.streaming.statefulOperator.stateRebalancing.enabled true 
State rebalancing benefits stateful Structured Streaming pipelines that undergo cluster resizing events. Stateless streaming operations don't benefit, regardless of changing cluster sizes. note 
Compute auto-scaling has limitations scaling down cluster size for Structured Streaming workloads. Databricks recommends using Spark Declarative Pipelines on Lakeflow with enhanced autoscaling for streaming workloads. See Optimize Lakeflow pipeline cluster utilization with autoscaling . 
Cluster resizing events trigger state rebalancing. Micro-batches might have higher latency during rebalancing events as the state loads from cloud storage to the new executors. On this page 
Stateful operations 
Optimize stateful Structured Streaming queries 
Work with multiple stateful operators in Structured Streaming 
Chained time window aggregation 
Time window aggregation in two different streams followed by stream-stream window join 
Stream-stream time interval join followed by time window aggregation 
State rebalancing for Structured Streaming Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 