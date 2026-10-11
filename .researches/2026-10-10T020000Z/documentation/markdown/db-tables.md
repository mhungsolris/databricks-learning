# db-tables

Source: https://docs.databricks.com/aws/en/tables/
Retrieved: 2026-10-10

Databricks tables | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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

Tables On this page Last updated on Sep 11, 2026 
Databricks tables 
Databricks supports multiple table types and storage formats to meet different data management needs. For an overview of table types, storage formats, and Unity Catalog integration, see Databricks tables concepts . 
Table types ​ 
Explore different table types and their capabilities for various data management scenarios. 

Unity Catalog managed tables for Delta Lake and Apache Iceberg 
Databricks manages metadata and data files for new tables that require optimized performance. 

Temporary tables in Databricks SQL and Databricks Runtime 
Session-scoped Unity Catalog managed tables for intermediate data. SQL warehouses only. 

Work with external tables 
Data stored in external systems. Unity Catalog manages metadata only. 

Work with foreign tables 
Read-only access to data in external systems connected through Lakehouse Federation . 
Storage formats ​ 
Work with open table formats that support advanced data management capabilities. 

Delta Lake 
Default storage format with ACID transactions, time travel, and schema enforcement for managed and external tables. 

Apache Iceberg 
Open table format for integration with the Iceberg ecosystem, supporting advanced metadata management. 
Table management ​ 
Configure and optimize table behavior, structure, and performance. 

Table constraints 
Define and enforce data quality rules with check constraints and not null constraints. 

Schema enforcement 
Control how Databricks handles schema changes and data type enforcement during writes. 

Table partitioning 
Organize data by partition keys to improve query performance and data management. 

Table size monitoring 
Monitor and analyze table storage usage and growth patterns. 

Convert external to managed 
Migrate external tables to managed tables for improved performance and management. 

External partition discovery 
Automatically discover and register partitions in external tables stored in cloud storage. On this page 
Table types 
Storage formats 
Table management Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 