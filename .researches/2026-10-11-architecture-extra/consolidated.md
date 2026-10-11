# Research Consolidation: Catalog and streaming boundaries

**Sources:** 3
**Format:** source-based

---

## Source URLs

- https://docs.snowflake.com/en/user-guide/opencatalog/overview
- https://iceberg.apache.org/javadoc/nightly/org/apache/iceberg/hadoop/HadoopCatalog.html
- https://iceberg.apache.org/docs/latest/spark-structured-streaming/

## 2026-10-11-architecture-extra-search-results

- **openCatalog**: Snowflake Open Catalog overview | Snowflake Documentation DOCUMENTATION / EN Language English Français Deutsch 日本語 한국어 Português Get started Guides Developer Reference Release notes Tutorials Status For AI agents: documentation index at /llms.txt — fetch to discover all Snowflake documentation pages. Markdown version of this page: /en/user-guide/opencatalog/overview.md
Overview
Snowflake Horizon Catalog

Applications and tools for connecting to Snowflake

Virtual warehouses
Databases, Tables, & Views
Data types

Data Integration
Snowflake Openflow
Apache Iceberg™
Apache Iceberg™ Tables
Snowflake Open Catalog
Getting started
Tutorial: Get Started
Create an additional Open Catalog account
Sign in
Access control
Securing Snowflake Open Catalog
Enroll in MFA
Use network policies to restrict access to Snowflake Open Catalog
SSO
External OAuth
Key pair authentication
Inbound private connectivity
Outbound private connectivity
Accounts
Manage users
Find the account name
Setting up catalogs
Create external cloud storage for a catalog
Create a catalog
Enable credential vending for an external catalog
Create a catalog role
Create a principal role
Configure and remove a service connection
Register a service connection
Connect with External OAuth
Connect with key pair authentication
Managing catalogs
Organize catalog content
Secure catalogs
View the schema for a table in Snowflake Open Catalog
Querying data in catalogs
Query a table in Snowflake Open Catalog using Snowflake
Sync a Snowflake-managed table with Snowflake Open Catalog
Query a table in Snowflake Open Catalog using a third-party engine
Code examples: Apache Spark
Release notes
Zero-Copy Connectors
About SAP® and Snowflake
About Salesforce Data Cloud and Snowflake
About Workday Live Data Query for Snowflake
About Workday Data Cloud and Snowflake
Data engineering
Data loading
Dynamic tables
Streams and tasks
Row timestamps
DCM Projects
dbt Projects on Snowflake
- **hadoop**: HadoopCatalog JavaScript is disabled on your browser. Skip navigation links
Overview
Package
Class
Tree
Deprecated
Index
Help
Summary:
Nested |
Field |
Constr |
Method
Detail:
Field |
Constr |
Method SEARCH: Package org.apache.iceberg.hadoop
Class HadoopCatalog java.lang.Object org.apache.iceberg.BaseMetastoreCatalog org.apache.iceberg.hadoop.HadoopCatalog All Implemented Interfaces: Closeable , AutoCloseable , org.apache.hadoop.conf.Configurable , Catalog , SupportsNamespaces public class HadoopCatalog extends BaseMetastoreCatalog implements SupportsNamespaces , org.apache.hadoop.conf.Configurable HadoopCatalog provides a way to use table names like db.table to work with path-based tables
 under a common location. It uses a specified directory under a specified filesystem as the
 warehouse directory, and organizes multiple levels directories that mapped to the database,
 namespace and the table respectively. The HadoopCatalog takes a location as the warehouse
 directory. When creating a table such as $db.$tbl, it creates $db/$tbl directory under the
 warehouse directory, and put the table metadata into that directory.
The HadoopCatalog now supports Catalog.createTable(org.apache.iceberg.catalog.TableIdentifier, org.apache.iceberg.Schema, org.apache.iceberg.PartitionSpec, java.lang.String, java.util.Map<java.lang.String, java.lang.String>) , Catalog.dropTable(org.apache.iceberg.catalog.TableIdentifier) , the Catalog.renameTable(org.apache.iceberg.catalog.TableIdentifier, org.apache.iceberg.catalog.TableIdentifier) is not supported yet.
Note: The HadoopCatalog requires that the underlying file system supports atomic rename.

Nested Class Summary
Nested classes/interfaces inherited from class org.apache.iceberg. BaseMetastoreCatalog BaseMetastoreCatalog.BaseMetastoreCatalogTableBuilder
Nested classes/interfaces inherited from interface org.apache.iceberg.catalog. Catalog Catalog.TableBuilder

Constructor Summary Constructors Constructor Descript
- **icebergStreaming**: Structured Streaming - Apache Iceberg™ Skip to content Apache Iceberg™ Apache Iceberg™ Initializing search
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
Structured Streaming Structured Streaming Table of contents
Streaming Reads
Limit input rate
Asynchronous Micro-Batch Planning
Streaming Writes
Partitioned table
Maintenance for streaming tables
Tune the rate of commits
Expire old snapshots
Compacting data files
Rewrite manifests
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

---

## Summary

- Total items: 3
- Sources: 1
- Content cleaning: 205 chars removed (3.4% reduction)

### Key Findings

No explicit key findings recorded.

