# databricks-output-mode

Source: https://docs.databricks.com/aws/en/structured-streaming/output-mode
Retrieved: 2026-10-11

Select an output mode for Structured Streaming | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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
Output mode On this page Last updated on Sep 11, 2026 
Select an output mode for Structured Streaming 
Selecting the right output mode determines how a stateful Structured Streaming query emits results and affects your pipeline's latency and cost. Only stateful streams containing aggregations require an output mode configuration. 
Joins only support the append output mode, and output mode doesn't impact deduplication. The arbitrary stateful operators mapGroupsWithState and flatMapGroupsWithState emit records using their own custom logic, so the stream's output mode doesn't affect their behavior. 
For stateless streaming, all output modes behave the same. 
To configure output mode correctly, you must understand stateful streaming, watermarks, and triggers. See the following articles: 
What is stateful streaming? 
Apply watermarks to control data processing thresholds 
Configure Structured Streaming trigger intervals 
What is output mode? ​ 
A Structured Streaming query's output mode determines which records the query's operators emit during each trigger. The three types of records that can be emitted are: 
Records that future processing does not change. 
The records that have changed since the last trigger. 
All records in the state table. 
Knowing which types of records to emit is important for stateful operators because a particular row produced by a stateful operator might change from trigger to trigger. For example, as a streaming aggregation operator receives more rows for a particular window, that window's aggregation values might change across triggers. 
For stateless operators, the distinction between record types does not affect the behavior of the operator. The records a stateless operator emits during a trigger are always the source records processed during that trigger. 
Available output modes ​ 
There are three output modes that tell an operator which records to emit during a particular trigger: 

Output Mode 
Description 

Append mode (default) 
By default, streaming queries run in append mode. In this mode, operators only emit rows that don't change in future triggers. Stateful operators use the watermark to determine when this happens. 

Update mode 
In update mode, operators emit all rows that changed during the trigger, even if the emitted record might change in a subsequent trigger. 

Complete mode 
Complete mode only works with streaming aggregations. In complete mode, all resulting rows ever produced by the operator are emitted downstream. ← ✕ 

Output Mode 
Description 

Append mode (default) 
By default, streaming queries run in append mode. In this mode, operators only emit rows that don't change in future triggers. Stateful operators use the watermark to determine when this happens. 

Update mode 
In update mode, operators emit all rows that changed during the trigger, even if the emitted record might change in a subsequent trigger. 

Complete mode 
Complete mode only works with streaming aggregations. In complete mode, all resulting rows ever produced by the operator are emitted downstream. 
Production considerations ​ 
For many stateful streaming operations, you must choose between append and update modes. The following sections outline considerations that might inform your decision. note 
Complete mode has some applications, but can perform poorly as data scales. Databricks recommends using materialized views to get semantic guarantees associated with complete mode with incremental processing for many stateful operations. See Materialized views . 
Application semantics ​ 
Application semantics describe how downstream applications use the streaming data. 
If downstream services need to take a single action for every downstream write, use append mode in most cases. For example, if you have a downstream notification service sending notifications for every new record written to the sink, append mode ensures each record is only written once. Update mode writes the record every time the state information changes, which would result in numerous updates. 
If downstream services need fresh results, update mode ensures your sink stays as up-to-date as possible. Examples include a machine learning model that reads features in real-time or an analytics dashboard tracking real-time aggregates. 
Operator and sink compatibility ​ 
Structured Streaming does not support all operations available in Apache Spark , and some streaming operations are not supported in all output modes. For more on operator limitations, see the OSS streaming docs . 
Not all sinks support all output modes. Kafka supports all output modes. Delta Lake , which backs all Unity Catalog managed tables, supports append and complete modes but not update mode. For behavior similar to update mode with Delta Lake sinks, see Merge in streaming . 
For more on sink compatibility, see the OSS streaming docs . 
Latency and cost ​ 
Output mode impacts how much time must elapse before writing a record, and the frequency and amount of data written can impact costs associated with streaming pipelines. 
Append mode forces stateful operators to emit results only after stateful results are finalized, which is at least as long as your watermark delay. A watermark delay of 1 hour in the append output mode means that your records have at least a 1-hour delay before being emitted downstream. 
Update mode results in one write per trigger per aggregate value. If your sink charges per write per record, this can be expensive if records update many times before the watermark delay passes. 
Configuration examples ​ 
The following code examples show configuring output mode for streaming updates to Unity Catalog tables: 
Python 
Scala Python 
# Append output mode (default) ( df . writeStream . toTable ( "target_table" ) ) # Append output mode (same as default behavior) ( df . writeStream . outputMode ( "append" ) . toTable ( "target_table" ) ) # Update output mode ( df . writeStream . outputMode ( "update" ) . toTable ( "target_table" ) ) # Complete output mode ( df . writeStream . outputMode ( "complete" ) . toTable ( "target_table" ) ) Scala 
// Append output mode (default) df . writeStream . toTable ( "target_table" ) // Append output mode (same as default behavior) df . writeStream . outputMode ( "append" ) . toTable ( "target_table" ) // Update output mode df . writeStream . outputMode ( "update" ) . toTable ( "target_table" ) // Complete output mode df . writeStream . outputMode ( "complete" ) . toTable ( "target_table" ) note 
The preceding examples write to Unity Catalog managed tables, which use Delta Lake format by default. Delta Lake sinks support only append and complete modes, so the update output mode example fails against a managed table. For behavior similar to update mode with Delta Lake sinks, see Merge in streaming . 
See OSS docs for PySpark DataStreamWriter.outputMode or Scala DataStreamWriter.outputMode . 
Stateful streaming and output modes example ​ 
The following example is meant to help you reason through how output mode interacts with watermarks for stateful streaming. 
Consider a streaming aggregation that calculates the total revenue generated each hour at a store with a watermark delay of 15 minutes. The first microbatch processes the following records: 
$15 at 2:40pm 
$10 at 2:30pm 
$30 at 3:10pm 
At this point, the engine's watermark is 2:55pm because it subtracts 15 minutes (the delay) from the maximum time seen (3:10pm). The streaming aggregation operator has the following in its state: 
[2pm, 3pm] : $25 
[3pm, 4pm] : $30 
The following table outlines what would happen in each output mode: 

Output mode 
Result and reason 

Append 
The streaming aggregation operator does not emit anything downstream. This is because both of these windows might change as new values appear with a subsequent trigger: the watermark of 2:55pm indicates that records after 2:55pm might still arrive, and those records might fall into either the [2pm, 3pm] window or the [3pm, 4pm] window. 

Update 
The operator emits both records, because both records received updates. 

Complete 
The operator emits all records. ← ✕ 

Output mode 
Result and reason 

Append 
The streaming aggregation operator does not emit anything downstream. This is because both of these windows might change as new values appear with a subsequent trigger: the watermark of 2:55pm indicates that records after 2:55pm might still arrive, and those records might fall into either the [2pm, 3pm] window or the [3pm, 4pm] window. 

Update 
The operator emits both records, because both records received updates. 

Complete 
The operator emits all records. 
Now, suppose that the stream receives one more record: 
$20 at 3:20pm 
The watermark updates to 3:05pm because the engine subtracts 15 minutes from 3:20pm. At this point, the streaming aggregation operator has the following in its state: 
[2pm, 3pm] : $25 
[3pm, 4pm] : $50 
The following table outlines what would happen in each output mode: 

Output mode 
Result and reason 

Append 
The streaming aggregation operator observes the watermark of 3:05pm is greater than the end of the [2pm, 3pm] window. By the definition of the watermark, that window can no longer change, so it emits the [2pm, 3pm] window. 

Update 
The streaming aggregation operator emits the [3pm, 4pm] window because the state value has changed from $30 to $50. 

Complete 
The operator emits all records. ← ✕ 

Output mode 
Result and reason 

Append 
The streaming aggregation operator observes the watermark of 3:05pm is greater than the end of the [2pm, 3pm] window. By the definition of the watermark, that window can no longer change, so it emits the [2pm, 3pm] window. 

Update 
The streaming aggregation operator emits the [3pm, 4pm] window because the state value has changed from $30 to $50. 

Complete 
The operator emits all records. 
The following summarizes how stateful operators behave in each append mode: 
In append mode, write records once after the watermark delay. 
In update mode, write records that have changed since the previous trigger. 
In complete mode, write all records ever produced by the stateful operator. On this page 
What is output mode? 
Available output modes 
Production considerations 
Application semantics 
Operator and sink compatibility 
Latency and cost 
Configuration examples 
Stateful streaming and output modes example Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 