# bq-storage

Source: https://docs.cloud.google.com/bigquery/docs/storage_overview
Retrieved: 2026-10-10

Overview of BigQuery storage  |  Google Cloud Documentation Skip to main content Documentation close 
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
Español 
Español – América Latina 
Français 
Indonesia 
Italiano 
Português 
Português – Brasil 
עברית 
中文 – 简体 
中文 – 繁體 
日本語 
한국어 Sign in 
BigQuery Start free Overview Guides Reference Samples Resources 
Documentation 
More 
Overview 
Guides 
Reference 
Samples 
Resources 
Console 
Discover 
Product overview 
Try BigQuery using the sandbox 
Get started 
Console walkthroughs and videos 
Use the console 
Explore the console 
Load and query data 
Use Notebook gallery 
Create reservations 
Try DataFrames 
Use agents 
Analyze data with the Colab Data Science Agent 
Use the bq CLI tool 
Use the client libraries 
Plan 
Introduction to the resource hierarchy 
API dependencies 
Datasets 
Introduction 
Create datasets 
List datasets 
Cross-region replication 
Managed disaster recovery 
Migrate to managed disaster recovery 
Dataset data retention 
Tables 
BigQuery tables 
Introduction 
Create and use tables 
Specify table schemas 
Specify a schema 
Specify nested and repeated columns 
Specify default column values 
Specify an identity column 
Specify ObjectRef values 
Segment with partitioned tables 
Introduction 
Create partitioned tables 
Manage partitioned tables 
Query partitioned tables 
Optimize with clustered tables 
Introduction 
Create clustered tables 
Manage clustered tables 
Query clustered tables 
Use metadata indexing 
External data sources 
Introduction 
BigLake tables 
Introduction 
Create Amazon S3 BigLake tables 
Create Azure Blob storage BigLake tables 
Create Cloud Storage BigLake tables 
Object tables 
Introduction 
Create Cloud Storage object tables 
External tables 
Introduction 
Create Apache Iceberg external tables 
Create Bigtable external tables 
Create Cloud Storage external tables 
Create Google Drive external tables 
Use metadata caching 
Manage Hive partitioned data 
Create a table definition file for external data 
Federated datasets 
Create and manage AWS Glue federated datasets 
Create Spanner external datasets 
Apache Iceberg managed tables 
Interact with Lakehouse data 
Views 
Overview 
Logical views 
Introduction 
Create logical views 
Materialized views 
Introduction 
Create materialized views 
Load, transform, and export 
Introduction 
Build a data pipeline with Data Engineering Agent 
Migrate data warehouse 
Introduction 
Plan a migration with migration lineage 
Migration assessment 
Migrate data 
Migrate data pipelines 
Use custom organization policies 
Migrate SQL and schema 
Enable SQL translations 
Translate SQL queries and schema interactively 
Translate SQL queries using the API 
Translate SQL queries in batch 
Generate metadata for translation and assessment 
Transform SQL translations with YAML 
Map SQL object names for batch translation 
Load data 
Introduction 
Create data integration workflows using the BigQuery web UI 
Storage overview 
BigQuery Data Transfer Service 
Introduction 
Supported data sources 
Data location and transfers 
Authorize transfers 
Enable transfers 
Set up network connections 
Cloud SQL instance access 
AWS VPN and network attachment 
Azure VPN and network attachment 
Manage transfers 
Transfer run notifications 
Use service accounts 
Use third-party transfers 
Use custom organization policies 
Data source change log 
Event-driven transfers 
Transfer data into Managed Iceberg tables 
Batch load data 
Introduction 
Auto-detect schemas 
Load Avro data 
Load Parquet data 
Load ORC data 
Load CSV data 
Load JSON data 
Load externally partitioned data 
Load data from a Datastore export 
Load data from a Firestore export 
Load data using the Storage Write API 
Load data into partitioned tables 
Write and read data with the Storage API 
Read data with the Storage Read API 
Write data with the Storage Write API 
Introduction 
Use the Storage Write API (gRPC) 
Overview 
Stream data 
Batch load data 
Stream updates with change data capture ingestion 
Best practices 
Supported protocol buffer and Arrow data types 
Use the Storage Write API (REST) 
Load data from other Google services 
Discover and catalog Cloud Storage data 
Load data using third-party apps 
Load data using BigQuery Omni operations 
Optimize load jobs 
Transform data 
Introduction 
Prepare data 
Introduction 
Prepare data with Gemini 
Transform with DML 
Transform data in partitioned tables 
Work with change history 
Transform data with pipelines 
Introduction 
Create pipelines 
Export data 
Introduction 
Export query results 
Export to Cloud Storage 
Export to Bigtable 
Export to Spanner 
Export to AlloyDB 
Export to Pub/Sub 
Export as Protobuf columns 
ELT tutorials 
Build ELT for marketing analytics data 
Analyze 
Introduction 
Explore your data 
Search for resources 
Profile your data 
Data insights 
About data insights 
Generate table insights 
Generate dataset insights 
Analyze with a data canvas 
Analyze data with Gemini 
Analyze data with the Gemini CLI 
Analyze your data 
Run a query 
Write queries with Gemini 
Write query results 
Query data with SQL 
Introduction 
Arrays 
JSON data 
Multi-statement queries 
Parameterized queries 
Pipe syntax 
Analyze data using pipe syntax 
Recursive CTEs 
Sketches 
Table sampling 
Time series 
Transactions 
Wildcard tables 
Use notebooks 
Introduction 
Create notebooks 
Explore query results 
Visualize query results 
Create and share Data Apps 
Use Spark 
Use Colab Data Science Agent 
Use DataFrames 
Introduction 
Install DataFrames 
Manipulate data 
Customize Python functions 
Use ML and AI 
Use the data type system 
Manage sessions and I/O 
Visualize graphs 
Use DataFrames in dbt 
Optimize performance 
Migrate to DataFrames version 2.0 
Use the BigQuery JupyterLab plugin 
Use geospatial analytics 
Introduction 
Work with geospatial analytics 
Work with raster data 
Best practices for spatial analysis 
Visualize geospatial data 
Grid systems for spatial analysis 
Geospatial analytics syntax reference 
Geospatial analytics tutorials 
Get started with geospatial analytics 
Use geospatial analytics to plot a hurricane's path 
Visualize geospatial analytics data in a Colab notebook 
Use raster data to analyze temperature 
Routines 
Introduction 
Manage routines 
User-defined functions 
User-defined functions in Python 
User-defined aggregate functions 
Table functions 
Remote functions 
SQL stored procedures 
Stored procedures for Apache Spark 
Analyze object tables by using remote functions 
Remote functions and Translation API tutorial 
Analyze multimodal data 
Introduction 
Work with ObjectRef values 
Analyze multimodal data with SQL and BigQuery DataFrames 
Search indexes 
Introduction 
Manage search indexes 
Search indexed data 
Work with text analyzers 
Run global queries 
Access historical data 
Use open source Python libraries 
Use BigQuery Graph 
Introduction 
Create and query a graph 
Schema overview 
Query overview 
Query best practices 
Work with measures 
Use the visual graph modeler 
Visualize graphs 
Chat with a graph 
Work with visualization tools and integrations 
Use BigQuery Graph and Spanner Graph 
Search a graph 
Build a cross-cloud property graph over Iceberg lakehouses 
Manage queries 
Save queries 
Introduction 
Create saved queries 
Continuous queries 
Introduction 
Create continuous queries 
Use stream-to-stream joins in continuous queries 
Understand window aggregation in continuous queries 
Use cached results 
Use sessions 
Introduction 
Work with sessions 
Write queries in sessions 
Optimize queries 
Introduction 
Use the query plan explanation 
Get query performance insights 
Optimize query computation 
Use history-based optimizations 
Optimize storage for query performance 
Use materialized views 
Use BI Engine 
Use nested and repeated data 
Optimize functions 
Use primary and foreign keys 
Paginate with the BigQuery API 
Query external data sources 
Establish connections 
Introduction 
Create connections 
Create a Cloud resource connection 
Create a default Cloud resource connection 
AlloyDB connections 
Amazon S3 connections 
Apache Spark connections 
Azure Blob Storage connections 
Cloud SQL connections 
Databricks connections 
SAP Datasphere connections 
Spanner connections 
Create cross-cloud connections 
Manage connections 
Run queries on external data 
Query BigLake tables 
Amazon S3 BigLake tables 
Azure Blob storage BigLake tables 
Cloud Storage BigLake tables 
Analyze data with BigQuery Omni 
Export query results 
Export to Amazon S3 
Export to Azure Blob Storage 
Query external tables 
Apache Iceberg external tables 
Bigtable external tables 
Cloud Storage external tables 
Google Drive external tables 
Run federated queries 
Introduction 
Run AlloyDB federated queries 
Run Cloud SQL federated queries 
Run SAP Datasphere federated queries 
Run Spanner federated queries 
Analyze other external data types 
Query open table formats with manifest files 
Analyze Salesforce Data Cloud data 
Use analysis and BI tools 
Introduction 
Use Connected Sheets 
Use Tableau Desktop 
Use Looker 
Use Data Studio 
Use third-party tools 
Google Cloud Ready - BigQuery 
Overview 
Partners 
BigQuery AI 
Introduction 
Generative AI functions 
Overview 
End-to-end user journeys for generative AI models 
Choose a text generation function 
Set permissions for generative AI functions 
Control costs with token quotas 
Optimize costs with model distillation 
Cloud AI API functions 
Overview 
Choose a natural language processing function 
Choose a document processing function 
Tutorials 
Generate text 
Generate text with Gemini 
Generate text with Gemma 
Generate text with any supported model 
Generate text using AI.GENERATE 
Handle quota errors 
Analyze images 
Perform semantic analysis 
Tune text generation models 
Use tuning and evaluation to improve model performance 
Generate structured data 
Generate structured data 
Natural language processing 
Understand text 
Translate text 
Document processing 
Process documents 
Parse PDFs in a retrieval-augmented generation pipeline 
Speech recognition 
Transcribe audio files 
Computer vision 
Annotate images 
Run inference on image data 
Analyze images with an imported classification model 
Analyze images with an imported feature vector model 
Embeddings and vector search 
Overview 
Vector indexes 
Manage vector indexes 
Automate embedding generation 
Tutorials 
Generate embeddings 
Generate text embeddings using a remote model 
Generate text embeddings using an open model 
Generate image and video embeddings using an LLM 
Handle quota errors by calling ML.GENERATE_EMBEDDING iteratively 
Generate and search multimodal embeddings 
Generate text embeddings using pretrained TensorFlow models 
Generate embeddings with transformer models in ONNX format 
Vector search 
Search embeddings with vector search 
Perform semantic search and retrieval-augmented generation 
Assistive AI 
Gemini in BigQuery overview 
Set up Gemini in BigQuery 
Use Cloud Assist 
Security and privacy 
Gemini in BigQuery locations 
Analyze with conversational analytics agent 
Overview 
Opt out from prompt analytics 
Create data agents 
Analyze data with conversations 
Machine learning 
Introduction 
Understand user journeys 
End-to-end user journeys for ML models 
End-to-end user journeys for forecasting models 
End-to-end user journeys for imported models 
The TimesFM time series forecasting model 
The TabFM regression and classification model 
Reference patterns 
ML models and MLOps 
Model creation 
Feature engineering and management 
Feature preprocessing overview 
Supported input feature types 
Automatic preprocessing 
Manual preprocessing 
Feature serving 
Perform feature engineering with the TRANSFORM clause 
Hyperparameter tuning overview 
Model evaluation overview 
Model inference overview 
Explainable AI overview 
Model weights overview 
ML pipelines overview 
Model monitoring overview 
Manage BigQueryML models in Agent Platform 
Work with models 
List models 
Manage models 
Get model metadata 
Update model metadata 
Export models 
Delete models 
Classification 
Regression 
Dimensionality reduction 
Clustering 
Recommendation 
Forecasting 
Anomaly detection 
Contribution analysis 
Tutorials 
Getting started 
Get started with BigQuery ML using SQL 
Get started with BigQuery ML using the Cloud console 
Regression and classification 
Create a linear regression model 
Create a logistic regression classification model 
Create a boosted trees classification model 
Clustering 
Cluster data with a k-means model 
Recommendation 
Create recommendations based on explicit feedback with a matrix factorization model 
Create recommendations based on implicit feedback with a matrix factorization model 
Imported and remote models 
Make predictions with imported TensorFlow models 
Make predictions with scikit-learn models in ONNX format 
Make predictions with PyTorch models in ONNX format 
Make predictions with remote models on Agent Platform 
Hyperparameter tuning 
Improve model performance with hyperparameter tuning 
Export models 
Export a BigQuery ML model for online prediction 
Augmented analytics 
Forecasting 
Forecast a single time series with an ARIMA_PLUS univariate model 
Forecast multiple time series with an ARIMA_PLUS univariate model 
Forecast time series with a TimesFM univariate model 
Forecast a single time series with a TimesFM multivariate model 
Forecast multiple time series with a TimesFM multivariate model 
Scale an ARIMA_PLUS univariate model to millions of time series 
Forecast a single time series with a multivariate model 
Forecast multiple time series with a multivariate model 
Use custom holidays with an ARIMA_PLUS univariate model 
Limit forecasted values for an ARIMA_PLUS univariate model 
Forecast hierarchical time series with an ARIMA_PLUS univariate model 
Anomaly detection 
Anomaly detection with a TimesFM univariate model 
Anomaly detection with a multivariate time series 
Contribution analysis 
Get data insights from contribution analysis using a summable metric 
Get data insights from contribution analysis using a summable ratio metric 
Administer 
Introduction 
Understand editions 
Manage resources 
Understand reliability 
Manage configuration settings 
Manage code assets 
Manage data preparations 
Manage notebooks 
Manage saved queries 
Manage pipelines 
Organize code assets with folders 
Introduction 
Create and manage folders 
Manage tables 
Manage tables 
Manage table data 
Modify table schemas 
Restore deleted tables 
Manage table clones 
Introduction 
Create table clones 
Manage table snapshots 
Introduction 
Create table snapshots 
Restore table snapshots 
List table snapshots 
View table snapshot metadata 
Update table snapshot metadata 
Delete table snapshots 
Create periodic table snapshots 
Manage datasets 
Manage datasets 
Update dataset properties 
Restore deleted datasets 
Manage views and materialized views 
Get information about views 
Manage views 
Manage materialized views 
Manage materialized view replicas 
Schedule resources 
Introduction 
Schedule code assets 
Schedule data preparations 
Schedule notebooks 
Schedule pipelines 
Schedule DAGs 
Schedule jobs and queries 
Run jobs programmatically 
Schedule queries 
Workload management 
Introduction 
Understand slots 
Understand reservations 
Manage workloads 
Work with slot reservations 
Manage assignments 
Manage commitments 
Manage jobs 
Manage query queues 
Plan workloads 
Estimate capacity requirements 
View slot recommendations 
Legacy reservations 
Introduction to legacy reservations 
Legacy slot commitments 
Purchase and manage legacy slot commitments 
Work with legacy slot reservations 
Manage BI Engine 
Introduction 
Reserve BI Engine capacity 
Monitor workloads 
Introduction 
Monitor resource utilization 
Monitor jobs 
Monitor sharing listings 
Monitor BI Engine 
Monitor Data Transfer Service 
Monitor materialized views 
Monitor reservations 
Monitor continuous queries 
Dashboards, charts, and alerts 
Set up alerts with scheduled queries 
Optimize resources 
Control costs 
Estimate and control costs 
Create custom query quotas 
Optimize with recommendations 
Introduction 
Manage cluster and partition recommendations 
Manage materialized view recommendations 
Organize with labels 
Introduction 
Add labels 
View labels 
Update labels 
Filter using labels 
Delete labels 
Govern 
Introduction 
Manage data quality 
Scan for data quality issues 
Use Knowledge Catalog 
Control access to resources 
Introduction 
IAM roles and permissions 
Changes to dataset-level access controls 
Basic roles and permissions 
Security center overview 
Control access with IAM 
Control access to resources with IAM 
Control access with tags 
Control access with conditions 
Control access with custom constraints 
Control access with authorization 
Authorized datasets 
Authorized routines 
Authorized views 
Tutorials 
Create an authorized view 
Restrict network access 
Control access with VPC service controls 
Regional endpoints 
Control column and row access 
Control access to table columns 
Introduction to column-level access control 
Restrict access with column-level access control 
Impact on writes 
Control access to table rows 
Introduction to row-level security 
Work with row-level security 
Use row-level security with other BigQuery features 
Best practices for row-level security 
Manage policy tags 
Manage policy tags across locations 
Best practices for using policy tags 
Protect sensitive data 
Mask data in table columns 
Introduction to data masking 
Mask column data 
Anonymize data with differential privacy 
Use differential privacy 
Extend differential privacy 
Restrict data access using analysis rules 
Use Sensitive Data Protection 
Manage encryption 
Encryption at rest 
Customer-managed encryption keys 
Column-level encryption with Cloud KMS 
AEAD encryption 
Share data 
Introduction 
Configure user roles 
Manage data exchanges 
Manage listings 
Manage subscriptions 
View and subscribe to listings 
Manage resources with custom constraints 
Data clean rooms 
Introduction 
Use query templates 
Entity resolution 
Introduction 
Use entity resolution 
VPC Service Controls for Sharing 
Stream sharing with Pub/Sub 
Commercialize listings on Cloud Marketplace 
Audit 
Introduction 
Audit policy tags 
View audit logs 
Data Policy audit logs 
Data Transfer Service audit logs 
Sharing audit logs 
BigLake API audit logs 
BigQuery Migration API audit logs 
Migrate audit logs 
BigQuery audit logs reference 
Troubleshoot 
Introduction 
Troubleshoot with information schema views 
Issue types 
Queries 
Materialized views 
Quota and limit 
Access control 
Troubleshoot data transfers 
Overview 
Transfer configurations 
Migrations 
Storage API 
Workload management 
Develop 
Introduction 
Authenticate to BigQuery 
Introduction 
Get started 
Authenticate as an end user 
Authenticate with JSON Web Tokens 
Use the BigQuery MCP server 
Use the Migration Service MCP server 
Use the Data Transfer Service MCP server 
Connect LLMs with MCP toolbox for databases 
Use BigQuery agent analytics 
Use ODBC and JDBC drivers 
Use the Google JDBC driver 
Use the Google ODBC driver 
Use the Simba ODBC and JDBC drivers 
Version control with repositories and workspaces 
Use repositories 
Introduction 
Create and manage repositories 
Manage code with Git repositories 
Use workspaces 
Introduction 
Create and manage workspaces 
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
Storage 
Home 
Documentation 
Data analytics 
BigQuery 
Guides Send feedback Stay organized with collections Save and categorize content based on your preferences. 
Overview of BigQuery storage 
BigQuery storage is optimized for running analytic queries over
large datasets. It also supports high-throughput streaming ingestion and
high-throughput reads. Understanding BigQuery storage can help
you to optimize your workloads. 
Overview 
One of the key features of BigQuery's architecture is the
separation of storage and compute. This allows BigQuery to scale
both storage and compute independently, based on demand. Figure 1. BigQuery architecture. 
When you run a query, the query engine distributes the work in parallel across
multiple workers, which scan the relevant tables in storage, process the query,
and then gather the results. BigQuery executes queries completely
in memory, using a petabit network to ensure that data moves extremely quickly
to the worker nodes. 
Here are some key features of BigQuery storage: 

Managed . BigQuery storage is a completely managed service.
You don't need to provision storage resources or reserve units of storage.
BigQuery automatically allocates storage for you when you load
data into the system. You only pay for the amount of storage that you use. The
BigQuery pricing model charges for compute and storage
separately. For pricing details, see BigQuery pricing . 

Durable . BigQuery storage is designed for 99.999999999%
(11 9's) annual durability. BigQuery replicates your data
across multiple availability zones to protect from data loss due to machine-level
failures or zonal failures.
For more information, see Reliability: Disaster
planning . 

Encrypted . BigQuery automatically encrypts all data before
it is written to disk. You can provide your own encryption key or let Google
manage the encryption key. For more information, see Encryption at rest . 

Efficient . BigQuery storage uses an efficient encoding
format that is optimized for analytic workloads. 

If you want to learn more
about BigQuery's storage format, see the blog post Inside Capacitor, BigQuery's next-generation columnar storage format . 
Table data 
The majority of the data that you store in BigQuery is table
data. Table data includes standard tables, table clones, table snapshots, and
materialized views. You are billed for the storage that you use for these
resources. For more information, see Storage pricing . 

Standard tables contain structured data. Every
table has a schema, and every column in the schema has a data type.
BigQuery stores data in columnar format. See Storage layout in this document. 

Table clones are lightweight, writable
copies of standard tables. BigQuery only stores the delta
between a table clone and its base table. 

Table snapshots are point-in-time
copies of tables. Table snapshots are read-only, but you can restore a table
from a table snapshot. BigQuery only stores the delta between a
table snapshot and its base table. 

Materialized views are precomputed
views that periodically cache the results of the view query. The cached
results are stored in BigQuery storage. 
In addition, cached query results are stored as
temporary tables. You aren't charged for cached query results stored in
temporary tables. 
External tables are a special type of table,
where the data resides in a data store that is external to
BigQuery, such as Cloud Storage. An external table has a table
schema, just like a standard table, but the table definition points to the
external data store. In this case, only the table metadata is kept in
BigQuery storage. BigQuery does not charge for
external table storage, although the external data store might charge for
storage. 
BigQuery organizes tables and other resources into logical
containers called datasets . How you group your BigQuery
resources affects permissions, quotas, billing, and other aspects of your
BigQuery workloads. For more information and best practices, see Introduction to the resource hierarchy . 
The data retention policy that is used for a table is determined by the
configuration of the dataset that contains the table. For more information,
see Data retention with time travel and fail-safe . 
Metadata 
BigQuery storage also holds metadata about your
BigQuery resources. You aren't charged for metadata storage. 
When you create any persistent entity in BigQuery, such as a
table, view, or user-defined function (UDF), BigQuery stores
metadata about the entity. This is true even for resources that don't contain
any table data, such as UDFs and logical views. 
Metadata includes information such as the table schema, partitioning and
clustering specifications, table expiration times, and other information. This
type of metadata is visible to the user and can be configured when you create
the resource. In addition, BigQuery stores metadata that it uses
internally to optimize queries. This metadata is not directly visible to users. 
Storage layout 
Many traditional database systems store their data in row-oriented format,
meaning rows are stored together, with the fields in each row appearing
sequentially on disk. Row-oriented databases are efficient at looking up
individual records. However, they can be less efficient at performing analytical
functions across many records, because the system has to read every field when
accessing a record. Figure 2. Row-oriented format. 
BigQuery stores table data in columnar format, meaning it
stores each column separately. Column-oriented databases are particularly
efficient at scanning individual columns over an entire dataset. 
Column-oriented databases are optimized for analytic workloads that aggregate
data over a very large number of records. Often, an analytic query only needs to
read a few columns from a table. For example, if you want to compute the sum of
a column over millions of rows, BigQuery can read that column
data without reading every field of every row. 
Another advantage of column-oriented databases is that data within a column
typically has more redundancy than data across a row. This characteristic allows
for greater data compression by using techniques such as run-length encoding,
which can improve read performance. Figure 3. Column-oriented format. 
Storage billing models 
BigQuery offers two storage billing models: logical (uncompressed) and physical (compressed). 
Changing your storage billing model only changes the metering configuration. It
does not involve data migration, file format conversion, or any infrastructure
changes. Your data is always stored in the same compressed physical format.
Changing this setting has no impact on query performance, latency, or
integration with other applications, such as Looker. 
The model you select determines only how your stored bytes are measured and
priced according to storage pricing : 
Logical billing: You are billed based on the uncompressed size of the
data. This is the default model. 
Physical billing: You are billed based on the compressed size of the
data on disk. 
Whichever billing model you choose, your data is stored as physical bytes. 
You set the storage billing model at the dataset level.
If you don't specify a storage billing model when you create a dataset, it
defaults to using logical storage billing. However, you can change a dataset's storage billing model after you create it. If you change a dataset's storage
billing model, you must wait 14 days before you can change the storage billing
model again. 
When you change a dataset's billing model, it takes 24 hours for the
change to take effect. Any tables or table partitions in long-term storage
are not reset to active storage when you change a dataset's billing model.
Query performance and query latency are not affected by changing a dataset's
billing model. 
Datasets use time travel and fail-safe storage for data retention.
Time travel and fail-safe storage are charged separately at active storage rates
when you use physical storage billing, but are included in the base rate you are
charged when you use logical storage billing. You can modify the time travel
window you use for a dataset in order to balance physical storage costs with
data retention. You can't modify the fail-safe window. For more information
about dataset data retention, see Data retention with time travel and fail-safe .
For more information on forecasting your storage costs, see Forecast storage billing . You can't enroll a dataset in physical storage billing if your organization has
any existing legacy flat-rate slot commitments located in the same region as the dataset. This doesn't apply to commitments
purchased with a BigQuery edition . 
Optimize storage 
Optimizing BigQuery storage improves query performance and
controls cost. To view the table storage metadata, query the following INFORMATION_SCHEMA views: 
INFORMATION_SCHEMA.TABLE_STORAGE 
INFORMATION_SCHEMA.TABLE_STORAGE_BY_ORGANIZATION 
For information about optimizing storage, see Optimize storage in BigQuery . 
Load data 
There are several basic patterns for ingesting data into
BigQuery. 

Batch load: Load your source data into a BigQuery table in
a single batch operation. This can be a one-time operation or you can automate
it to occur on a schedule. A batch load operation can create a new table or
append data into an existing table. 

Streaming: Continually stream smaller batches of data, so that the data is
available for querying in near-real-time. 

Generated data: Use SQL statements to insert rows into an existing table
or write the results of a query to a table. 
For more information about when to choose each of these ingestion methods, see Introduction to loading data .
For pricing information, see Data ingestion pricing . 
Read data from BigQuery storage 
Most of the time, you store data in BigQuery in order to run
analytical queries on that data. However,
sometimes you might want to read records directly from a table.
BigQuery provides several ways to read table data: 

BigQuery API : Synchronous paginated access with the tabledata.list method. Data is read in a serial fashion, one page per invocation.
For more information, see Browsing table data . 

BigQuery Storage API : Streaming high-throughput access that also supports server-side column
projection and filtering. Reads can be parallelized across many readers by
segmenting them into multiple disjoint streams. 

Export : Asynchronous high-throughput copying to Google Cloud Storage, either with
extract jobs or the EXPORT DATA statement . If you need to copy data in
Cloud Storage, export the data either with an extract job or an EXPORT DATA statement. 

Copy : Asynchronous copying of datasets within BigQuery. The copy
is done logically when the source and destination location is the same. 
For pricing information, see Data extraction pricing . 
Based on the application requirements, you can read the table data: 
Read and copy: If you need an at-rest copy in
Cloud Storage, export the data either with an extract job or an EXPORT DATA statement. If you only want to read the data, use the
BigQuery Storage API. If you want to make a copy
within BigQuery, then use a copy job. 
Scale: The BigQuery API is the least efficient method and shouldn't
be used for high volume reads. If you need to export more than 50 TB of
data per day, use the EXPORT DATA statement or the BigQuery Storage API. 
Time to return the first row: The BigQuery API is the fastest method to
return the first row, but should only be used to read small amounts of
data. The BigQuery Storage API is slower to return the first
row, but has much higher-throughput. Exports and copies must finish before
any rows can be read, so the time to the first row for these types of jobs
can be on the order of minutes. 
Deletion 
When you delete a table, the data persists for at least the duration of your time travel window .

After this, data is cleaned
up from disk within the Google Cloud deletion timeline .

Some deletion operations, such as the DROP COLUMN statement ,
are metadata-only operations. In this case, storage is freed up the next time
you modify the affected rows. If you do not modify the table, there is no
guaranteed time within which the storage is freed up. 
For more information, see Data deletion on Google Cloud . 
What's next 
Learn about working with tables . 
Learn how to optimize storage . 
Learn how to query data in BigQuery . 
Learn about data security and governance . Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License , and code samples are licensed under the Apache 2.0 License . For details, see the Google Developers Site Policies . Java is a registered trademark of Oracle and/or its affiliates. 
Last updated 2026-10-07 UTC. Need to tell us more? [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 

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
Español 
Español – América Latina 
Français 
Indonesia 
Italiano 
Português 
Português – Brasil 
עברית 
中文 – 简体 
中文 – 繁體 
日本語 
한국어 