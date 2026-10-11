# Research Consolidation: Iceberg runtime semantics

**Sources:** 8
**Format:** source-based

---

## Source URLs

- https://iceberg.apache.org/docs/latest/spark-getting-started/
- https://iceberg.apache.org/docs/latest/spark-queries/
- https://iceberg.apache.org/docs/latest/spark-ddl/
- https://iceberg.apache.org/docs/latest/spark-writes/
- https://iceberg.apache.org/docs/latest/evolution/
- https://iceberg.apache.org/docs/latest/partitioning/
- https://iceberg.apache.org/docs/latest/hadoop/
- https://docs.snowflake.com/en/user-guide/tables-iceberg-query

## 2026-10-11-architecture-supplement-search-results

- **spark**: Getting Started - Apache Iceberg™ Skip to content Apache Iceberg™ Apache Iceberg™ Initializing search
Home
Quickstart
Docs
Releases
Project
Community
Blog
Specification Apache Iceberg™
Home
Quickstart Quickstart
Spark
Flink
Hive
Docs Docs
Java Java
Latest (1.12.0) Latest (1.12.0)
Introduction
Concepts Concepts
Tables Tables
Branching and Tagging
Configuration
Encryption
Evolution
Maintenance
Metrics Reporting
Partitioning
Performance
Reliability
Schemas
Views Views
Configuration
Catalogs Catalogs
REST Catalog Protocol
API API
Quickstart
API
File I/O
Javadoc
Integrations Integrations
Apache Spark Apache Spark
Getting Started Getting Started Table of contents
Using Iceberg in Spark
Adding catalogs
Creating a table
Writing
Reading
Type compatibility
Spark type to Iceberg type
Iceberg type to Spark type
Next steps
Configuration
DDL
Procedures
Queries
Structured Streaming
Writes
Apache Flink Apache Flink
Getting Started
Flink Connector
Flink DDL
Flink Queries
Flink Writes
Flink TableMaintenance
Flink Configuration
Kafka Connect
Apache Hive
Migration Migration
Overview
Hive Migration
Delta Lake Migration
Catalogs Catalogs
Catalog properties
REST Compatible Catalog
AWS Glue
AWS DynamoDB
HadoopCatalog
HiveCatalog
JDBC
Java Custom Catalog
Nessie
Storage Storage
AWS S3
Dell ECS
Nightly Nightly
Introduction
Concepts Concepts
Tables Tables
Branching and Tagging
Configuration
Encryption
Evolution
Maintenance
Metrics Reporting
Partitioning
Performance
Reliability
Schemas
Views Views
Configuration
Catalogs Catalogs
REST Catalog Protocol
API API
Quickstart
API
File I/O
Javadoc
Integrations Integrations
Apache Spark Apache Spark
Getting Started
Configuration
DDL
Procedures
Queries
Structured Streaming
Writes
Apache Flink Apache Flink
Getting Started
Flink Connector
Flink DDL
Flink Queries
Flink Writes
Flink TableMaintenance
Flink Configuration
Kafka Connect
Ap
- **queries**: Queries - Apache Iceberg™ Skip to content Apache Iceberg™ Apache Iceberg™ Initializing search
Home
Quickstart
Docs
Releases
Project
Community
Blog
Specification Apache Iceberg™
Home
Quickstart Quickstart
Spark
Flink
Hive
Docs Docs
Java Java
Latest (1.12.0) Latest (1.12.0)
Introduction
Concepts Concepts
Tables Tables
Branching and Tagging
Configuration
Encryption
Evolution
Maintenance
Metrics Reporting
Partitioning
Performance
Reliability
Schemas
Views Views
Configuration
Catalogs Catalogs
REST Catalog Protocol
API API
Quickstart
API
File I/O
Javadoc
Integrations Integrations
Apache Spark Apache Spark
Getting Started
Configuration
DDL
Procedures
Queries Queries Table of contents
Querying with SQL
Spark SQL functions
Time travel Queries with SQL
Schema selection in time travel queries
Querying with DataFrames
Catalogs with DataFrameReader
Time travel Queries with DataFrame
Incremental read
Inspecting tables
History
Metadata Log Entries
Snapshots
Entries
Files
Manifests
Partitions
Positional Delete Files
All Metadata Tables
All Data Files
All Delete Files
All Entries
All Manifests
References
Inspecting with DataFrames
Time Travel with Metadata Tables
Structured Streaming
Writes
Apache Flink Apache Flink
Getting Started
Flink Connector
Flink DDL
Flink Queries
Flink Writes
Flink TableMaintenance
Flink Configuration
Kafka Connect
Apache Hive
Migration Migration
Overview
Hive Migration
Delta Lake Migration
Catalogs Catalogs
Catalog properties
REST Compatible Catalog
AWS Glue
AWS DynamoDB
HadoopCatalog
HiveCatalog
JDBC
Java Custom Catalog
Nessie
Storage Storage
AWS S3
Dell ECS
Nightly Nightly
Introduction
Concepts Concepts
Tables Tables
Branching and Tagging
Configuration
Encryption
Evolution
Maintenance
Metrics Reporting
Partitioning
Performance
Reliability
Schemas
Views Views
Configuration
Catalogs Catalogs
REST Catalog Protocol
API API
Quickstart
API
F
- **ddl**: DDL - Apache Iceberg™ Skip to content Apache Iceberg™ Apache Iceberg™ Initializing search
Home
Quickstart
Docs
Releases
Project
Community
Blog
Specification Apache Iceberg™
Home
Quickstart Quickstart
Spark
Flink
Hive
Docs Docs
Java Java
Latest (1.12.0) Latest (1.12.0)
Introduction
Concepts Concepts
Tables Tables
Branching and Tagging
Configuration
Encryption
Evolution
Maintenance
Metrics Reporting
Partitioning
Performance
Reliability
Schemas
Views Views
Configuration
Catalogs Catalogs
REST Catalog Protocol
API API
Quickstart
API
File I/O
Javadoc
Integrations Integrations
Apache Spark Apache Spark
Getting Started
Configuration
DDL DDL Table of contents
CREATE TABLE
PARTITIONED BY
CREATE TABLE ... AS SELECT
REPLACE TABLE ... AS SELECT
DROP TABLE
DROP TABLE
DROP TABLE PURGE
ALTER TABLE
ALTER TABLE ... RENAME TO
ALTER TABLE ... SET TBLPROPERTIES
ALTER TABLE ... ADD COLUMN
ALTER TABLE ... RENAME COLUMN
ALTER TABLE ... ALTER COLUMN
ALTER TABLE ... DROP COLUMN
ALTER TABLE SQL extensions
ALTER TABLE ... ADD PARTITION FIELD
ALTER TABLE ... DROP PARTITION FIELD
ALTER TABLE ... REPLACE PARTITION FIELD
ALTER TABLE ... WRITE ORDERED BY
ALTER TABLE ... WRITE DISTRIBUTED BY PARTITION
ALTER TABLE ... SET IDENTIFIER FIELDS
ALTER TABLE ... DROP IDENTIFIER FIELDS
Branching and Tagging DDL
ALTER TABLE ... CREATE BRANCH
ALTER TABLE ... CREATE TAG
ALTER TABLE ... REPLACE BRANCH
ALTER TABLE ... REPLACE TAG
ALTER TABLE ... DROP BRANCH
ALTER TABLE ... DROP TAG
Iceberg views in Spark
Creating a view
Creating a view with properties
Creating a view with location
Dropping a view
Replacing a view
Setting and removing view properties
Showing available views
Showing the CREATE statement of a view
Displaying view details
Procedures
Queries
Structured Streaming
Writes
Apache Flink Apache Flink
Getting Started
Flink Connector
Flink DDL
Flink Queries
Flink Writes
Flink TableMaintenance
Flink Configuration
Ka
- **writes**: Writes - Apache Iceberg™ Skip to content Apache Iceberg™ Apache Iceberg™ Initializing search
Home
Quickstart
Docs
Releases
Project
Community
Blog
Specification Apache Iceberg™
Home
Quickstart Quickstart
Spark
Flink
Hive
Docs Docs
Java Java
Latest (1.12.0) Latest (1.12.0)
Introduction
Concepts Concepts
Tables Tables
Branching and Tagging
Configuration
Encryption
Evolution
Maintenance
Metrics Reporting
Partitioning
Performance
Reliability
Schemas
Views Views
Configuration
Catalogs Catalogs
REST Catalog Protocol
API API
Quickstart
API
File I/O
Javadoc
Integrations Integrations
Apache Spark Apache Spark
Getting Started
Configuration
DDL
Procedures
Queries
Structured Streaming
Writes Writes Table of contents
Writing with SQL
INSERT INTO
Snapshot summary
MERGE INTO
MERGE INTO syntax
Snapshot summary
INSERT OVERWRITE
Overwrite behavior
Dynamic overwrite
Static overwrite
DELETE FROM
Snapshot summary
UPDATE
Snapshot summary
Writing to Branches
Via SQL
Via DataFrames
Writing with DataFrames
Appending data
Overwriting data
Creating tables
Merging data
Schema Merge
Writing Distribution Modes
Controlling File Sizes
Apache Flink Apache Flink
Getting Started
Flink Connector
Flink DDL
Flink Queries
Flink Writes
Flink TableMaintenance
Flink Configuration
Kafka Connect
Apache Hive
Migration Migration
Overview
Hive Migration
Delta Lake Migration
Catalogs Catalogs
Catalog properties
REST Compatible Catalog
AWS Glue
AWS DynamoDB
HadoopCatalog
HiveCatalog
JDBC
Java Custom Catalog
Nessie
Storage Storage
AWS S3
Dell ECS
Nightly Nightly
Introduction
Concepts Concepts
Tables Tables
Branching and Tagging
Configuration
Encryption
Evolution
Maintenance
Metrics Reporting
Partitioning
Performance
Reliability
Schemas
Views Views
Configuration
Catalogs Catalogs
REST Catalog Protocol
API API
Quickstart
API
File I/O
Javadoc
Integrations Integrations
Apache Spark Apache Spark
Ge
- **evolution**: Evolution - Apache Iceberg™ Skip to content Apache Iceberg™ Apache Iceberg™ Initializing search
Home
Quickstart
Docs
Releases
Project
Community
Blog
Specification Apache Iceberg™
Home
Quickstart Quickstart
Spark
Flink
Hive
Docs Docs
Java Java
Latest (1.12.0) Latest (1.12.0)
Introduction
Concepts Concepts
Tables Tables
Branching and Tagging
Configuration
Encryption
Evolution Evolution Table of contents
Schema evolution
Correctness
Partition evolution
Sort order evolution
Maintenance
Metrics Reporting
Partitioning
Performance
Reliability
Schemas
Views Views
Configuration
Catalogs Catalogs
REST Catalog Protocol
API API
Quickstart
API
File I/O
Javadoc
Integrations Integrations
Apache Spark Apache Spark
Getting Started
Configuration
DDL
Procedures
Queries
Structured Streaming
Writes
Apache Flink Apache Flink
Getting Started
Flink Connector
Flink DDL
Flink Queries
Flink Writes
Flink TableMaintenance
Flink Configuration
Kafka Connect
Apache Hive
Migration Migration
Overview
Hive Migration
Delta Lake Migration
Catalogs Catalogs
Catalog properties
REST Compatible Catalog
AWS Glue
AWS DynamoDB
HadoopCatalog
HiveCatalog
JDBC
Java Custom Catalog
Nessie
Storage Storage
AWS S3
Dell ECS
Nightly Nightly
Introduction
Concepts Concepts
Tables Tables
Branching and Tagging
Configuration
Encryption
Evolution
Maintenance
Metrics Reporting
Partitioning
Performance
Reliability
Schemas
Views Views
Configuration
Catalogs Catalogs
REST Catalog Protocol
API API
Quickstart
API
File I/O
Javadoc
Integrations Integrations
Apache Spark Apache Spark
Getting Started
Configuration
DDL
Procedures
Queries
Structured Streaming
Writes
Apache Flink Apache Flink
Getting Started
Flink Connector
Flink DDL
Flink Queries
Flink Writes
Flink TableMaintenance
Flink Configuration
Kafka Connect
Apache Hive
Migration Migration
Overview
Hive Migration
Delta Lake Migration
Catalogs Catalogs
Cata
- **partition**: Partitioning - Apache Iceberg™ Skip to content Apache Iceberg™ Apache Iceberg™ Initializing search
Home
Quickstart
Docs
Releases
Project
Community
Blog
Specification Apache Iceberg™
Home
Quickstart Quickstart
Spark
Flink
Hive
Docs Docs
Java Java
Latest (1.12.0) Latest (1.12.0)
Introduction
Concepts Concepts
Tables Tables
Branching and Tagging
Configuration
Encryption
Evolution
Maintenance
Metrics Reporting
Partitioning Partitioning Table of contents
What is partitioning?
What does Iceberg do differently?
Partitioning in Hive
Problems with Hive partitioning
Iceberg's hidden partitioning
Performance
Reliability
Schemas
Views Views
Configuration
Catalogs Catalogs
REST Catalog Protocol
API API
Quickstart
API
File I/O
Javadoc
Integrations Integrations
Apache Spark Apache Spark
Getting Started
Configuration
DDL
Procedures
Queries
Structured Streaming
Writes
Apache Flink Apache Flink
Getting Started
Flink Connector
Flink DDL
Flink Queries
Flink Writes
Flink TableMaintenance
Flink Configuration
Kafka Connect
Apache Hive
Migration Migration
Overview
Hive Migration
Delta Lake Migration
Catalogs Catalogs
Catalog properties
REST Compatible Catalog
AWS Glue
AWS DynamoDB
HadoopCatalog
HiveCatalog
JDBC
Java Custom Catalog
Nessie
Storage Storage
AWS S3
Dell ECS
Nightly Nightly
Introduction
Concepts Concepts
Tables Tables
Branching and Tagging
Configuration
Encryption
Evolution
Maintenance
Metrics Reporting
Partitioning
Performance
Reliability
Schemas
Views Views
Configuration
Catalogs Catalogs
REST Catalog Protocol
API API
Quickstart
API
File I/O
Javadoc
Integrations Integrations
Apache Spark Apache Spark
Getting Started
Configuration
DDL
Procedures
Queries
Structured Streaming
Writes
Apache Flink Apache Flink
Getting Started
Flink Connector
Flink DDL
Flink Queries
Flink Writes
Flink TableMaintenance
Flink Configuration
Kafka Connect
Apache Hive
Migration Migrat
- **hadoop**: 
- **horizon**: 

---

## Summary

- Total items: 8
- Sources: 1
- Content cleaning: 714 chars removed (5.9% reduction)

### Key Findings

No explicit key findings recorded.

