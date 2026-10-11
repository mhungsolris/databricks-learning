# databricks-realtime

Source: https://docs.databricks.com/aws/en/structured-streaming/real-time/setup
Retrieved: 2026-10-11

Set up real-time mode | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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
Real-time mode 
Setup On this page Last updated on Sep 11, 2026 
Set up real-time mode 
This page describes the prerequisites and configuration needed to run real-time mode queries in Structured Streaming . For a step-by-step tutorial, see Tutorial: Run a real-time streaming workload . For conceptual information about real-time mode, see Real-time mode concepts . 
Prerequisites ​ 
To use real-time mode, you must configure your compute to meet the following requirements: 
Use classic compute. Dedicated and standard access modes are supported. Standard access mode is supported for Python only. Lakeflow pipelines and serverless clusters are not supported. 
Use Databricks Runtime 16.4 LTS and above. 
Turn off autoscaling. 
Turn off Photon. 
Set spark.databricks.streaming.realTimeMode.enabled to true . 
Turn off spot instances to avoid interruptions. 
For latency-sensitive workloads with UDFs, Databricks recommends that you use dedicated access mode. See Table functions . 
For instructions on creating and configuring classic compute, see Compute configuration reference . 
Stream to stream joins ​ 
Stream to stream inner joins require additional configuration for real-time mode. Outer joins aren't supported. See Stream to stream join . important 
To run a stream to stream join in real-time mode with multiple other streams on the same cluster, you must use Databricks Runtime 18 LTS and above. 
In Databricks Runtime 18.2 and below, Structured Streaming doesn't support the following configurations for other processing modes, including processingTime and availableNow . 
To enable stream to stream joins for real-time mode, set the following Spark configurations: 
Python 
Scala 
SQL Python 
spark . conf . set ( "spark.databricks.streaming.realTimeMode.streamStreamJoin.enabled" , "true" ) spark . conf . set ( "spark.sql.streaming.join.stateFormatVersion" , "4" ) spark . conf . set ( "spark.sql.streaming.join.stateFormatV4.enabled" , "true" ) spark . conf . set ( "spark.sql.streaming.stateStore.rocksdb.mergeOperatorVersion" , "2" ) spark . conf . set ( "spark.sql.streaming.realTimeMode.controlMessage.enabled" , "true" ) Scala 
spark . conf . set ( "spark.databricks.streaming.realTimeMode.streamStreamJoin.enabled" , "true" ) spark . conf . set ( "spark.sql.streaming.join.stateFormatVersion" , "4" ) spark . conf . set ( "spark.sql.streaming.join.stateFormatV4.enabled" , "true" ) spark . conf . set ( "spark.sql.streaming.stateStore.rocksdb.mergeOperatorVersion" , "2" ) spark . conf . set ( "spark.sql.streaming.realTimeMode.controlMessage.enabled" , "true" ) SQL 
SET spark . databricks . streaming . realTimeMode . streamStreamJoin . enabled = true ; SET spark . sql . streaming . join . stateFormatVersion = 4 ; SET spark . sql . streaming . join . stateFormatV4 . enabled = true ; SET spark . sql . streaming . stateStore . rocksdb . mergeOperatorVersion = 2 ; SET spark . sql . streaming . realTimeMode . controlMessage . enabled = true ; 
Query configuration ​ 
To run a query in real-time mode, you must enable the real-time trigger. Real-time triggers are supported only in update mode. 
Python 
Scala Python 
query = ( spark . readStream . format ( "kafka" ) . option ( "kafka.bootstrap.servers" , broker_address ) . option ( "subscribe" , input_topic ) . load ( ) . writeStream . format ( "kafka" ) . option ( "kafka.bootstrap.servers" , broker_address ) . option ( "topic" , output_topic ) . option ( "checkpointLocation" , checkpoint_location ) . outputMode ( "update" ) # In PySpark, the realTime trigger requires specifying the interval. . trigger ( realTime = "5 minutes" ) . start ( ) ) Scala 
import org . apache . spark . sql . execution . streaming . RealTimeTrigger val readStream = spark . readStream . format ( "kafka" ) . option ( "kafka.bootstrap.servers" , brokerAddress ) . option ( "subscribe" , inputTopic ) . load ( ) . writeStream . format ( "kafka" ) . option ( "kafka.bootstrap.servers" , brokerAddress ) . option ( "topic" , outputTopic ) . option ( "checkpointLocation" , checkpointLocation ) . outputMode ( "update" ) . trigger ( RealTimeTrigger . apply ( ) ) // RealTimeTrigger can also accept an argument specifying the checkpoint interval. // For example, this code indicates a checkpoint interval of 5 minutes: // .trigger(RealTimeTrigger.apply("5 minutes")) . start ( ) 
Compute sizing ​ 
You can run one real-time job per compute resource if the compute has enough task slots. 
To run in low-latency mode, the total number of available task slots must be greater than or equal to the number of tasks across all query stages. 
Slot calculation examples ​ 

Pipeline type 
Configuration 
Required slots 

Single-stage stateless (Kafka source + sink) 
maxPartitions = 8 
8 slots 

Two-stage stateful (Kafka source + shuffle) 
maxPartitions = 8, shuffle partitions = 20 
28 slots (8 + 20) 

Three-stage (Kafka source + shuffle + repartition) 
maxPartitions = 8, two shuffle stages of 20 each 
48 slots (8 + 20 + 20) ← ✕ 

Pipeline type 
Configuration 
Required slots 

Single-stage stateless (Kafka source + sink) 
maxPartitions = 8 
8 slots 

Two-stage stateful (Kafka source + shuffle) 
maxPartitions = 8, shuffle partitions = 20 
28 slots (8 + 20) 

Three-stage (Kafka source + shuffle + repartition) 
maxPartitions = 8, two shuffle stages of 20 each 
48 slots (8 + 20 + 20) 
If you don't set maxPartitions , use the number of partitions in the Kafka topic. 
Additional resources ​ 
Tutorial: Run a real-time streaming workload 
Real-time mode examples 
Optimize and monitor real-time mode query performance 
Real-time mode reference On this page 
Prerequisites 
Stream to stream joins 
Query configuration 
Compute sizing 
Slot calculation examples 
Additional resources Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 