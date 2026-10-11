# iceberg-support

Source: https://docs.databricks.com/aws/en/iceberg/
Retrieved: 2026-10-10

What is Apache Iceberg in Databricks? | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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
Table formats 
Iceberg On this page Last updated on Sep 22, 2026 
What is Apache Iceberg in Databricks ? 
Apache Iceberg is an open-source table format for analytics workloads that supports features like schema evolution, time travel, and hidden partitioning. Like Delta Lake , Iceberg creates an abstraction layer that allows ACID transactions on your data in object storage. 
Databricks supports Iceberg tables that use the Apache Parquet file format and versions 1, 2, and 3 of the Iceberg specification. Iceberg maintains atomicity and consistency by writing new metadata files for each table change. All Iceberg tables in Databricks follow the open Iceberg table format specification. See the Iceberg table specification . 
An Iceberg catalog is the top-level layer of the Iceberg table architecture that returns the current metadata when loading a table. The Iceberg catalog handles operations like creating, dropping, and renaming tables. 
Databricks supports Iceberg tables managed by: 
Unity Catalog 
Foreign catalogs , such as AWS Glue, Hive metastore , or Snowflake Horizon Catalog 
Requirements ​ 
To use Apache Iceberg managed or foreign tables, you must meet the following requirements: 
Use a workspace with Unity Catalog enabled. 
Use Databricks Runtime 16.4 LTS or above. 
For managed tables, you must also meet the following requirement: 
A workspace with serverless compute enabled 
Databricks uses serverless compute to maintain Iceberg table metadata for managed tables. Serverless compute must have network connectivity to the cloud storage account that backs the table. If a firewall protects the storage account, configure serverless network connectivity so that serverless compute can reach it. The required setup depends on your cloud. For more information, see Serverless compute plane networking . 
Create Iceberg tables in Unity Catalog ​ 
Iceberg tables that you create in Unity Catalog are managed Iceberg tables . You can create these tables using: 
Databricks Runtime or Databricks SQL 
External Iceberg-compatible engines that support the Iceberg REST Catalog API, such as Apache Spark, Flink, Trino, or Kafka. See Access Databricks tables from Apache Iceberg clients . 
Managed Iceberg tables are fully integrated with Databricks platform features: 
Unity Catalog manages lifecycle tasks like snapshot expiration and file compaction on these tables. 
Liquid clustering improves query performance. 
Predictive optimization automates operations to reduce storage costs and improve query speed. 
materialized views support incremental refresh to keep results up to date as source data changes. 
streaming tables support incremental data loading from Kafka and cloud object storage using Databricks SQL . 
Databricks recommends using Iceberg client version 1.9.2 and above to read and write to Unity Catalog . 
Read Iceberg tables managed by other catalogs ​ 
A foreign Iceberg table is an Iceberg table managed by a catalog outside Unity Catalog . The external catalog stores the table's current metadata. Databricks uses Lakehouse Federation to retrieve metadata and read the table from object storage. 
Foreign Iceberg tables are read-only in Databricks and have limited platform support. 
Access Iceberg tables using external systems ​ 
You can access all Iceberg tables in Unity Catalog using the Iceberg REST Catalog API . This open API supports read and write operations from external Iceberg engines across different languages and platforms. See Access Databricks tables from Apache Iceberg clients . note 
External Iceberg engines can't read views defined in Unity Catalog . See Limitations . 
The REST Catalog supports credential vending, which delivers temporary credentials to external engines for accessing the underlying storage. For more information, see Unity Catalog credential vending for external system access . warning 
Credential vending is not supported on workspaces that use default storage. See Limitations . 
Clone managed tables using Iceberg ​ 
You can create a full, independent copy of a managed table that uses Iceberg with DEEP CLONE . A deep clone copies the table's data files and metadata to a new managed table using Iceberg in Unity Catalog . See Clone a managed table that uses Iceberg . 
Create a materialized view compatible with external Iceberg readers ​ Preview 
Managed Iceberg materialized views are in Public Preview . To enable this feature, reach out to your Databricks account team. 
You can create a materialized view that is compatible with external Iceberg readers. To create one, use USING ICEBERG in the CREATE MATERIALIZED VIEW statement. For the complete syntax, see CREATE MATERIALIZED VIEW (pipelines) . For full requirements, see Enable external data access to streaming tables and materialized views . SQL 
CREATE MATERIALIZED VIEW < mv_name > USING ICEBERG AS SELECT * FROM samples . nyctaxi . trips ; 
After you create the materialized view , run REPAIR TABLE with SYNC METADATA . See REPAIR TABLE . SQL 
REPAIR TABLE < mv_name > SYNC METADATA ; 
External Iceberg readers can read the materialized view but can't write to it. To read the materialized view from an external Iceberg reader, see Enable external data access to streaming tables and materialized views . 
Partition evolution ​ 
With partition evolution, you can change the partitioning scheme of an existing Apache Iceberg table without rewriting data. New data is written with the updated partition layout and existing data retains its original partition layout. Apache Iceberg tracks the partition specs and applies the correct filter at query time. See partition evolution for Apache Iceberg . note 
Partition evolution is supported on managed Iceberg tables through external Iceberg engines using the Iceberg REST Catalog, but not through Databricks SQL . Expression-based partition transforms such as years() and bucket() are not supported for managed Iceberg tables. See Limitations . 
To configure external access, see Access Databricks tables from Apache Iceberg clients . 
The following examples show how to use partition evolution with Spark SQL and the Iceberg extension. For Apache Iceberg partition evolution syntax and supported transforms, see Apache Iceberg Spark DDL . 
Add a partition field ​ 
To add a new partition field to an existing table: SQL 
ALTER TABLE catalog . schema . table ADD PARTITION FIELD column_name ; 
Drop a partition field ​ 
To remove an existing partition field from a table: SQL 
ALTER TABLE catalog . schema . table DROP PARTITION FIELD column_name ; 
Replace a partition field ​ 
To swap one partition field for another without an intermediate repartition: SQL 
ALTER TABLE catalog . schema . table REPLACE PARTITION FIELD old_column WITH new_column ; 
Limitations ​ 
The following limitations apply to Iceberg tables in Databricks and are subject to change: 
Iceberg tables support only the Apache Parquet file format. 
For Iceberg v2, position deletes and equality-based deletes aren't supported. Instead, Databricks supports Iceberg v3 deletion vectors for row-level deletions. 
Branching and tagging aren't supported. Only the main branch is accessible when reading foreign Iceberg tables. 
Partitioning: 
Partition evolution is supported on managed Iceberg tables only when interacting from external Iceberg engines. 
Foreign Iceberg tables don't support partition evolution. 
Partitioning by BINARY type isn't supported. 
External Iceberg engines can't read views . With Unity Catalog , the Iceberg REST Catalog API makes tables available but not views. 
The following data types aren't supported: 
UUID 
Fixed(L) 
TIME 
Nested STRUCT with required fields 
For limitations specific to Iceberg v3, see Limitations . 
Managed Iceberg table limitations ​ 
The following limitations apply specifically to managed Iceberg tables: 
AI Search is supported only for managed tables using Iceberg v3 or above. See Databricks AI Search and Use Apache Iceberg v3 features . 
If you use managed Iceberg tables as a source for synced tables for Lakebase , incremental processing with automatic change data feed isn't supported. 
Managed Iceberg tables can only be created if predictive optimization is enabled for table maintenance. 
The following table properties are managed by Unity Catalog and can't be manually set: 
write.location-provider.impl 
write.data.path 
write.metadata.path 
write.format.default 
write.delete.format.default 
The compression codec to change table compression isn't supported. All tables use Zstd by default. 
Partitioning by expressions (for example, years() , months() , days() , hours() , bucket() ) isn't supported. 
Features not supported in Apache Iceberg also aren't available for managed Iceberg tables. This includes Delta Lake generated columns , Constraints on Databricks , and Collation support for Delta Lake . 
Foreign Iceberg table limitations ​ 
The following limitations apply specifically to foreign Iceberg tables: 
Time travel is supported only for Iceberg snapshots that have been previously read in Databricks (that is, snapshots where a SELECT statement was executed). 
Using bucket transform functions for Iceberg partitioning can degrade query performance when conditional filters are used. 
Cloud storage tiering products such as Amazon S3 are not integrated with foreign Iceberg tables. Accessing foreign Iceberg tables in Databricks can restore data archived in lower-cost storage tiers. 
On dedicated access mode clusters, reads and REFRESH FOREIGN TABLE operations on Iceberg tables require ALL PRIVILEGES . On this page 
Requirements 
Create Iceberg tables in Unity Catalog 
Read Iceberg tables managed by other catalogs 
Access Iceberg tables using external systems 
Clone managed tables using Iceberg 
Create a materialized view compatible with external Iceberg readers 
Partition evolution 
Add a partition field 
Drop a partition field 
Replace a partition field 
Limitations 
Managed Iceberg table limitations 
Foreign Iceberg table limitations Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 