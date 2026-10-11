# partitioning

Source: https://docs.databricks.com/aws/en/tables/partitions
Retrieved: 2026-10-11

When to partition tables on Databricks | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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

Tables 
Table functionality 
Data layout 
Partitioning tables On this page Last updated on Sep 11, 2026 
When to partition tables on Databricks note 
Databricks recommends liquid clustering for all managed tables. For managed tables using Apache Iceberg , Unity Catalog supports only liquid clustering and interprets PARTITION BY columns as clustering keys. See Convert a partitioned table to liquid clustering . 
Most tables on Databricks with less than 100 TB of data don't need partitioning. Databricks uses Delta Lake for all tables by default and automatically clusters data in unpartitioned tables by ingestion time, so you get partitioning-like performance without manual tuning. Consider a custom partitioning strategy only when it outperforms these defaults. See Use ingestion time clustering . 
Custom partitioning strategies ​ 
Advanced users of Apache Spark and Delta Lake might identify a partitioning strategy that outperforms the default ingestion time clustering . warning 
An ineffective partitioning strategy might negatively affect query performance and require a full rewrite of data to fix. A full rewrite might be very expensive and slow for large tables. 
Before using custom partitioning strategies, Databricks recommends liquid clustering for all tables and predictive optimization for Unity Catalog managed tables. See Use liquid clustering for tables and Predictive optimization for Unity Catalog managed tables . 
To convert an existing partitioned Delta Lake table to liquid clustering, use ALTER TABLE ... REPLACE PARTITIONED BY WITH CLUSTER BY . Liquid clustering works for both low and high cardinality columns and avoids the fixed partition boundaries and small-file issues common with static partitioning. See Convert a partitioned table to liquid clustering . 
Supported data types for partition columns ​ 
Partitioning supports these data types for partition columns: 
Date 
Timestamp 
TimestampNTZ 
Interval 
String 
Binary 
Boolean 
Integer, Long, Short, Byte 
Float, Double, Decimal 
Partition columns must be top-level columns. You can't partition by any of the following: 
Complex types, such as StructType , MapType , ArrayType , or VariantType 
Struct fields, such as struct_col.field . Delta Lake treats a struct field in PARTITIONED BY as an expression rather than a column reference. 
To organize a table by a struct field, use liquid clustering instead, which recognizes a struct field as a clustering key. Liquid clustering is the only way to data-skip on a struct field without first extracting it into a top-level column. See Use liquid clustering for tables . 
Minimum size recommendations ​ 
Partitioning below these minimum sizes is likely to negatively affect query performance rather than improve it. Consider the following when you decide whether to partition a table: 
For tables: 
With less than 1 TB of data, don't partition. 
With more than 1 TB to 100 TB of data, use liquid clustering instead of partitioning. Partitioning likely negatively affects performance more often than it helps. 
With 100 TB or more of data, partitioning might improve performance, but Databricks recommends using liquid clustering first and verifying performance improvements. 
For partitions, verify that each partition contains at least 1 GB of data. Tables with fewer, larger partitions tend to outperform tables with many smaller partitions. 
Use ingestion time clustering ​ 
By using Delta Lake , unpartitioned tables automatically use ingestion time clustering . Ingestion time has query performance improvements similar to partitioning strategies with datetime fields, without any need to manually optimize or tune your data. note 
To maintain ingestion time clustering when performing a large number of modifications using UPDATE or MERGE statements on a table, Databricks recommends using liquid clustering on a column that matches the ingestion order, such as an event timestamp or a creation date. See Use liquid clustering for tables . 
Delta Lake and Parquet partitioning compatibility ​ 
Delta Lake uses Parquet for storing data, and some partitioned Delta Lake tables have data layouts similar to Parquet tables stored with Apache Spark . Apache Spark uses Hive-style partitioning when saving data in Parquet format. Hive-style partitioning is not part of the Delta Lake protocol, and workloads should not rely on this partitioning strategy to interact with Delta Lake tables. 
Databricks recommends that you interact with data stored in Delta Lake using officially supported clients and APIs. Many Delta Lake features break assumptions about data layout that might have been used with Parquet, Hive, or even earlier Delta Lake protocol versions. note 
When you enable column mapping for a Delta Lake table, random prefixes replace column names in partition directories for Hive-style partitioning. See Rename and drop columns with Delta Lake column mapping . 
Delta Lake partitioning compared to other data lakes ​ 
Partitioning techniques useful in other open source technologies (such as Apache Spark , Parquet, Hive, and Hadoop) do not always hold true for Databricks . If you do choose to partition your table, consider the following: 
Transactions are not defined by partition boundaries. Because Delta Lake ensures ACID through transaction logs, you do not need to separate a batch of data by a partition to guarantee atomicity. 
Databricks compute clusters do not have data locality tied to physical media. Data ingested into the lakehouse is stored in cloud object storage. While data is cached to local disk storage during data processing, Databricks uses file-based statistics to identify the minimal amount of data for parallel loading. 
Z-order and partitions ​ note 
Databricks recommends liquid clustering over Z-ordering for all new tables. See Use liquid clustering for tables . 
You can use Z-order indexes alongside partitions to speed up queries on large datasets. Most tables use ingestion time clustering to avoid needing to tune Z-order and partitions. 
Keep the following rules in mind when you plan a query optimization strategy based on partition boundaries and Z-order: 
Z-order requires the OPTIMIZE command. You cannot combine files across partition boundaries, and so Z-order clustering can only occur within a partition. For unpartitioned tables, files can be combined across the entire table. 
Partitioning works well only for low or known cardinality fields (for example, date fields or physical locations), but not for fields with high cardinality such as timestamps. Z-order works for all fields, including high cardinality fields and fields that may grow infinitely (for example, timestamps or the customer ID in a transactions or orders table). 
You cannot Z-order on fields used for partitioning. 
How Databricks optimizes around existing partitions ​ 
Many customers migrate to Delta Lake from Parquet-based data lakes, such as using the CONVERT TO DELTA statement to convert an existing Parquet-based table to a Delta Lake table without rewriting existing data. Because conversion doesn't rewrite existing data, large tables might inherit previous partitioning strategies. 
Some Databricks optimizations use these partitions when possible, mitigating negative performance effects for partitioning strategies that aren't optimized for Delta Lake . 
Delta Lake and Apache Spark are open-source technologies. While Databricks has features that reduce reliance on partitioning, the open source community might build new features that add complexity. On this page 
Custom partitioning strategies 
Supported data types for partition columns 
Minimum size recommendations 
Use ingestion time clustering 
Delta Lake and Parquet partitioning compatibility 
Delta Lake partitioning compared to other data lakes 
Z-order and partitions 
How Databricks optimizes around existing partitions Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 