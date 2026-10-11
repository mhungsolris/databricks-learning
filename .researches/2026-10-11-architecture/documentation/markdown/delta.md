# delta

Source: https://docs.delta.io/
Retrieved: 2026-10-11

Welcome to the Delta Lake documentation | Delta Lake Skip to content Delta Lake Search Ctrl K Cancel GitHub Select theme Dark Light Auto 
Introduction 
Apache Spark connector 
Quick Start 
Table batch reads and writes 
Table streaming reads and writes 
Table deletes, updates, and merges 
Change data feed 
Table utility commands 
Constraints 
How does Delta Lake manage feature compatibility? 
Delta default column values 
Delta column mapping 
Use liquid clustering for Delta tables 
What are deletion vectors? 
Use catalog-managed tables 
Drop Delta table features 
Use row tracking for Delta tables 
Delta Connect (aka Spark Connect Support in Delta) 
Storage configuration 
Delta type widening 
Universal Format (UniForm) 
Read Delta Sharing Tables 
Concurrency control 
Migration guide 
Best practices 
Frequently asked questions (FAQ) 
Optimizations 
Trino connector 
Starburst connector 
Presto connector 
AWS Redshift Spectrum connector 
Snowflake connector 
Google BigQuery connector 
Apache Flink connector 
Other connectors 
Delta Kernel 
Delta Standalone (deprecated) 
Delta Lake APIs 
Releases 
Delta Lake resources 
Delta Table Properties Reference 
Contribute GitHub Select theme Dark Light Auto On this page 
Overview 
On this page 
Overview 
Welcome to the Delta Lake documentation 
Delta Lake is an open source project that enables building a Lakehouse architecture on top of data lakes . Delta Lake provides ACID transactions , scalable metadata handling, and unifies streaming and batch data processing on top of existing data lakes, such as S3, ADLS, GCS, and HDFS. 
Specifically, Delta Lake offers: 
ACID transactions on Spark: Serializable isolation levels ensure that readers never see inconsistent data. 
Scalable metadata handling: Leverages Spark distributed processing power to handle all the metadata for petabyte-scale tables with billions of files at ease. 
Streaming and batch unification: A table in Delta Lake is a batch table as well as a streaming source and sink. Streaming data ingest, batch historic backfill, interactive queries all just work out of the box. 
Schema enforcement: Automatically handles schema variations to prevent insertion of bad records during ingestion. 
Time travel : Data versioning enables rollbacks, full historical audit trails, and reproducible machine learning experiments. 
Upserts and deletes : Supports merge, update and delete operations to enable complex use cases like change-data-capture, slowly-changing-dimension (SCD) operations, streaming upserts, and so on. 
Vibrant connector ecosystem: Delta Lake has connectors read and write Delta tables from various data processing engines like Apache Spark, Apache Flink, Apache Hive, Apache Trino, AWS Athena, and more. 
To get started follow the quickstart guide to learn how to use Delta Lake with Apache Spark. Edit page Next Quick Start 