# spark-streaming-overview

Source: https://spark.apache.org/docs/4.0.4/streaming/index.html
Retrieved: 2026-10-11

Structured Streaming Programming Guide - Spark 4.0.4 Documentation 4.0.4 
Overview 
Programming Guides Quick Start RDDs, Accumulators, Broadcasts Vars SQL, DataFrames, and Datasets Structured Streaming Spark Streaming (DStreams) MLlib (Machine Learning) GraphX (Graph Processing) SparkR (R on Spark) PySpark (Python on Spark) 
API Docs Python Scala Java R SQL, Built-in Functions 
Deploying Overview Submitting Applications Spark Standalone YARN Kubernetes 
More Configuration Monitoring Tuning Guide Job Scheduling Security Hardware Provisioning Migration Guide Building Spark Contributing to Spark Third Party Projects 

Structured Streaming Programming Guide 
Overview 
Getting Started 
APIs on DataFrames and Datasets 
Performance Tips 
Additional Information 
Structured Streaming Programming Guide 
Overview 
Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine. You can express your streaming computation the same way you would express a batch computation on static data. The Spark SQL engine will take care of running it incrementally and continuously and updating the final result as streaming data continues to arrive. You can use the Dataset/DataFrame API in Scala, Java, Python or R to express streaming aggregations, event-time windows, stream-to-batch joins, etc. The computation is executed on the same optimized Spark SQL engine. Finally, the system ensures end-to-end exactly-once fault-tolerance guarantees through checkpointing and Write-Ahead Logs. In short, Structured Streaming provides fast, scalable, fault-tolerant, end-to-end exactly-once stream processing without the user having to reason about streaming. 
Internally, by default, Structured Streaming queries are processed using a micro-batch processing engine, which processes data streams as a series of small batch jobs thereby achieving end-to-end latencies as low as 100 milliseconds and exactly-once fault-tolerance guarantees. However, since Spark 2.3, we have introduced a new low-latency processing mode called Continuous Processing , which can achieve end-to-end latencies as low as 1 millisecond with at-least-once guarantees. Without changing the Dataset/DataFrame operations in your queries, you will be able to choose the mode based on your application requirements. 
In this guide, we are going to walk you through the programming model and the APIs. We are going to explain the concepts mostly using the default micro-batch processing model, and then later discuss Continuous Processing model. First, let’s start with a simple example of a Structured Streaming query - a streaming word count. 