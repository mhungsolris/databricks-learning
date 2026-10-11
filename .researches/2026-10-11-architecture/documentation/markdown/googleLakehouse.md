# googleLakehouse

Source: https://docs.cloud.google.com/lakehouse/docs/manage-tables
Retrieved: 2026-10-11

Overview of Apache Iceberg tables  |  Lakehouse  |  Google Cloud Documentation Skip to main content Documentation close 
Get Started 
Get Started with Google Cloud 
Product List 
Cloud Customer Care 
Featured Products 
Agent Platform 
Apigee API Management 
BigQuery 
Compute Engine 
Cloud CDN 
Cloud Run 
Cloud Storage 
Cloud SQL 
Gemini Enterprise 
Google Kubernetes Engine 
Looker 
Cross-product Tools 
Access and resources management 
Costs and usage management 
Infrastructure as code 
SDK, languages, frameworks, and tools 
Technology Areas 
AI and ML 
Application development 
Application hosting 
Compute 
Data analytics and pipelines 
Databases 
Distributed, hybrid, and multicloud 
Industry solutions 
Migration 
Networking 
Observability and monitoring 
Security 
Storage / Console 
English 
Deutsch 
Español – América Latina 
Français 
Indonesia 
Italiano 
Português – Brasil 
עברית 
中文 – 简体 
中文 – 繁體 
日本語 
한국어 Sign in 
Lakehouse Start free Overview Guides Reference Resources 
Documentation 
More 
Overview 
Guides 
Reference 
Resources 
Console 
Discover 
What is borderless Lakehouse? 
How borderless Lakehouse works 
Key concepts 
Get started 
Create and query an Iceberg table using the Google Cloud console 
Create and query an Iceberg table using the gcloud CLI 
Set up cross-cloud data access 
Use cases 
Forecast demand from customer feedback 
Configure the Lakehouse runtime catalog 
About the Lakehouse runtime catalog 
Set up catalog endpoints 
Apache Iceberg REST catalog endpoint 
About the Iceberg REST catalog endpoint 
Set up the Iceberg REST catalog endpoint 
Use open-source engines and tools 
Apache Spark 
Apache Flink 
Trino 
Terraform 
Custom Apache Iceberg catalog for BigQuery endpoint 
Overview 
Configure for Apache Spark 
Use Apache Iceberg 1.10 and higher 
Use Apache Iceberg 1.9 and lower 
Create and manage resources 
Use with BigQuery tables 
Use with stored procedures 
Customize features 
Apache Hive catalog endpoint 
Overview 
Set up Apache Spark and Hive 
Supported storage formats and types 
Limitations and considerations 
Manage catalog endpoints 
Overview 
Create catalog 
Update catalog 
Create namespace 
Enable credential vending 
Get catalog details 
Delete catalog 
Delete namespace 
View audit logs 
Manage tables 
Compare table types 
Manage Apache Iceberg tables 
Overview 
Create table 
Register table 
List tables 
Get table details 
Insert data 
Modify data with DML 
Alter table 
Configure table options 
Upgrade Iceberg V1 tables to V2 
Use Binary Deletion Vectors in Iceberg V3 tables 
Delete table 
Query tables 
Query tables using SQL 
Query tables with conversational analytics 
Generate data insights for Iceberg tables 
Import tables 
Import Iceberg tables using Dataflow 
Migrate Apache Iceberg CDC data using Dataflow 
Import Parquet files using Dataflow 
Import Delta Lake tables using Dataflow 
Migrate Delta Lake CDC data using Dataflow 
Access cross-cloud data 
About cross-cloud data access 
Set up cross-cloud connections 
AWS Glue 
Databricks Unity Catalog 
Snowflake Horizon Catalog 
Workday Data Lake 
SAP Business Data Cloud 
About SAP BDC integration 
Set up cross-cloud connection for SAP BDC 
Query SAP BDC data 
Publish data products to SAP BDC 
VPC SC config for SAP BDC 
Query remote data 
Supported regions and capabilities 
Back up and restore 
Cross-region replication and disaster recovery 
Overview 
Use cross-region replication and disaster recovery 
Load and ingest 
Migrate external metadata to Apache Iceberg tables 
Migrate metadata from Dataproc Metastore 
Stream data with the Storage Write API 
Change data capture ingestion 
Secure and control access 
Authentication 
Access control with IAM 
Overview 
Roles and permissions 
Manage catalog, namespace, and table ACLs 
Credential vending 
Regional endpoints 
Troubleshoot 
Common issues 
Table management and security rules 
Cross-cloud data access 
Troubleshoot common issues 
Databricks Unity Catalog 
SAP Business Data Cloud 
Get Started 
Get Started with Google Cloud 
Product List 
Cloud Customer Care 
Featured Products 
Agent Platform 
Apigee API Management 
BigQuery 
Compute Engine 
Cloud CDN 
Cloud Run 
Cloud Storage 
Cloud SQL 
Gemini Enterprise 
Google Kubernetes Engine 
Looker 
Cross-product Tools 
Access and resources management 
Costs and usage management 
Infrastructure as code 
SDK, languages, frameworks, and tools 
Technology Areas 
AI and ML 
Application development 
Application hosting 
Compute 
Data analytics and pipelines 
Databases 
Distributed, hybrid, and multicloud 
Industry solutions 
Migration 
Networking 
Observability and monitoring 
Security 
Storage As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 
Home 
Documentation 
Data analytics 
Lakehouse 
Guides Send feedback 
Overview of Apache Iceberg tables Stay organized with collections Save and categorize content based on your preferences. 
Apache Iceberg tables, managed by the Lakehouse runtime catalog and the Iceberg REST catalog
endpoint , are open and
interoperable Iceberg tables adhering to the open source Apache Iceberg Table
specification , which can be read and written by using any
Iceberg-compatible processing engine or BigQuery. 
In this document, these tables are referred to as "managed Apache Iceberg tables" or
"Iceberg tables". 
Table options 
You can opt in and enable the following capabilities by configuring table options : 
Read/write interoperability (Preview) : Seamless read and write support for
multiple engines, including BigQuery, Managed service for Apache Spark,
Iceberg-compatible engines such as open source engines (Apache Spark, Apache
Flink, and Trino), and third-party engines (such as Snowflake). 
Automatic table management (Preview) : Automatic table management (storage
optimization) such as compaction and garbage collection. 
In addition to the preceding capabilities, the following capabilities are also
supported by default for Apache Iceberg tables managed by Lakehouse (Preview). 
BigQuery Data definition language (Preview) : You can also create or update
Iceberg tables by using BigQuery DDL statements (for example, CREATE
TABLE , ALTER TABLE , and DROP TABLE ), in addition to creating or
updating tables by using Iceberg-compatible engines such as Spark, Flink,
and Trino. After the tables are created, they are available for reads and
writes in those engines and in BigQuery, and are part of the same catalog
and namespace construct, managed by the Lakehouse runtime catalog. 
Credential vending support for BigQuery (Preview) : BigQuery supports using credential vending for
authentication when reading or writing Iceberg tables in the Lakehouse runtime catalog. You can set credential vending at the catalog level. 
Management actions 
You can perform the following management actions on your Apache Iceberg tables: 
Create a table : Create an Apache
Iceberg table within a catalog namespace using the Google Cloud console,
Spark, Trino, gcloud, BigQuery (Preview), or the Iceberg REST Catalog API ( CreateIcebergTable ). 
Register a table : Register an existing Apache Iceberg table within a catalog namespace using gcloud or the Iceberg REST Catalog API ( RegisterIcebergTable ). 
List tables : View table identifiers
within a namespace using the Google Cloud console, Spark, Trino, gcloud, BigQuery (Preview), or the
Iceberg REST Catalog API ( ListIcebergTableIdentifiers ). 
Get table details : Inspect table
schema, properties, and credentials using the Google Cloud console,
Spark, Trino, gcloud, BigQuery (Preview), or the Iceberg REST Catalog API ( GetIcebergTable , LoadIcebergTableCredentials ). 
Insert data : Append data rows to your
Iceberg tables using Spark, Trino, or BigQuery (Preview). 
Query a table : Execute queries against your Iceberg tables from Spark, Trino, or BigQuery (Preview) using four-part table naming. 
Modify data with DML : Update,
delete, or merge data rows in your Iceberg tables using DML statements from
BigQuery (Preview), Spark, or Trino. 
Alter a table : Evolve table schema and
update metadata properties using the Google Cloud console, Spark,
Trino, gcloud, BigQuery (Preview), or the Iceberg REST Catalog API ( UpdateIcebergTable ). 
Configure table options : Configure properties to enable BigQuery (Preview) DML and automatic table management. 
Manage table ACLs : View and update IAM policies on your Iceberg tables to control access for specific principals ( get-iam-policy , set-iam-policy ). 
Upgrade Iceberg V1 tables to V2 : Upgrade your existing Iceberg V1 tables to the supported V2 format. 
Use Binary Deletion Vectors in Iceberg V3 tables : Enable binary deletion vectors for optimized deletion performance in
Iceberg V3 tables. 
Delete a table : Drop a table
registration from the catalog without purging underlying storage files
using the Google Cloud console, Spark, Trino, gcloud, BigQuery (Preview), or the Iceberg REST
Catalog API ( DeleteIcebergTable ). 
What's next 
See the Apache Iceberg REST
catalog . 
Learn how to query a table . 
Learn how to manage table ACLs . Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License , and code samples are licensed under the Apache 2.0 License . For details, see the Google Developers Site Policies . Java is a registered trademark of Oracle and/or its affiliates. 
Last updated 2026-10-09 UTC. Need to tell us more? [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

Products and pricing 
See all products 
Google Cloud pricing 
Google Cloud Marketplace 
Contact sales 

Support 
Community forums 
Support 
Release Notes 
System status 

Resources 
GitHub 
Getting Started with Google Cloud 
Code samples 
Cloud Architecture Center 
Training and Certification 

Engage 
Blog 
Events 
X (Twitter) 
Google Cloud on YouTube 
Google Cloud Tech on YouTube 
Android 
Chrome 
Firebase 
Google AI 
About Google 
Privacy 
Site terms 
Google Cloud terms 
Manage cookies 
Our third decade of climate action: join us 
Sign up for the Google Cloud newsletter Subscribe 
English 
Deutsch 
Español – América Latina 
Français 
Indonesia 
Italiano 
Português – Brasil 
עברית 
中文 – 简体 
中文 – 繁體 
日本語 
한국어 