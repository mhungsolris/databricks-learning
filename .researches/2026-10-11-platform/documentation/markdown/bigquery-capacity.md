# bigquery-capacity

Source: https://docs.cloud.google.com/bigquery/docs/admin-intro
Retrieved: 2026-10-11

Introduction to BigQuery administration  |  Google Cloud Documentation Skip to main content Documentation close 
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
Introduction to BigQuery administration 
BigQuery administration lets you configure, secure, and monitor
data resources and compute workloads across your organization. You can use
these capabilities to allocate compute capacity, optimize query performance,
control costs, and enforce access policies. 
To take a tour of BigQuery data administration features
directly in the Google Cloud console, click Take the tour . 
Take the tour 
Tools 
BigQuery provides several interfaces you can use for administration tasks.
Often a particular task can be done with
multiple tools, letting you choose the tool that works best for you. For
example, you can create a table by using the Explorer pane in the
Google Cloud console, a bq mk --table command, or a CREATE TABLE SQL
statement. 
Google Cloud console. The Google Cloud console has several pages dedicated
to BigQuery administration. For more information, see Use the Google Cloud console . 

SQL statements. The BigQuery page in the
Google Cloud console has
a query editor where you can do administrative tasks by using DDL and DCL
statements. For more information, see Data definition language (DDL) and Data control language (DCL) . 
You can use stored procedures to automate administration tasks that use
SQL statements. For more information, see Work with stored procedures . 

bq commands. The bq command-line tool lets you do many administrative tasks by using bq commands. You can use the bq command-line tool to do tasks that aren't
supported in the Google Cloud console, to prototype capabilities before
encoding them in queries or API methods, or if you prefer working in a
command-line interface. For more information, see Use the bq command-line tool . 
Manage resources 
BigQuery resources include organizations, folders, projects,
datasets, and tables. This section describes how to manage
your organization's resources. 
For information about organizing BigQuery resources, see Introduction to the resource hierarchy .
In particular, you can create an Organization resource, which lets you do
some tasks, such as setting access controls, at the organization level. 
Manage datasets 
Datasets are containers for tables. You can create tables in a dataset, and then
manage them as a group. For example, you can configure a dataset's default
table expiration time, which applies to all tables in the dataset unless you
override it. You can copy a group of tables by making a copy of their dataset,
and you can control access to tables at the dataset level. 
Refer to the following documents for more information about dataset
administration: 
For more information about creating, copying, moving, and updating datasets,
see Introduction to datasets . 
For more information about dataset-level access control, see Controlling access to datasets and Authorized datasets . 
Manage tables 
In BigQuery, data is stored in tables, where it can be queried.
You can create tables, load data into tables from various types of sources and
in various formats, partition tables based on a specific column or by ingestion
time, cluster tables, update table properties, and export table data. 
Refer to the following documents for more information about table
administration: 
For more information about loading data into BigQuery tables,
see Introduction to loading tables . 
For more information about managing tables and exporting table data, see Introduction to tables . 
For more information about partitioning and clustering tables, see Introduction to partitioned tables and Introduction to clustered tables . 
Label resources 
To help organize your BigQuery resources, you can add labels to
your datasets, tables, and views. Labels are key-value pairs that you can attach
to a resource. After labeling your resources, you can search for them based on
label values. For example, you could use labels to group datasets by department
by adding labels like dept:sales , dept:marketing , or dept:analytics .
Then you could break down your billed charges by department using the labels. 
For more information, see Introduction to labels . 
Get resource information 
You can get information about your BigQuery resources by querying
the INFORMATION_SCHEMA views. BigQuery provides views for each resource type. For example, the INFORMATION_SCHEMA.TABLES view contains
information about your tables. 
The following are a few examples of information you can obtain by querying INFORMATION_SCHEMA views: 
See when a table was created. 
Get the names and data types of each column in a table. 
Find all of the jobs running in a project. 
Get a list of the table snapshots that were created from a base
table. 
For a dataset, table, view, or routine, get the DDL statement that can be
used to create the resource. 
Get the options that were used to create a table (for example, table
expiration). 
Find the partitioning and clustering columns on a table. 
Get a project's assigned reservation and its slot capacity. 
For more information, see Introduction to BigQuery INFORMATION_SCHEMA . 
Copy data 
You might want to create copies of
your data for various reasons, such as protection from human error, or to retain
data for comparison in the future.
BigQuery provides several options for copying a table's data from
a particular point in time. 

Time travel. You might need to access a table's state as it was sometime
within the past
week; for example, if the data became corrupted due to human error.
BigQuery retains historical data for your tables for
seven days. You can access a table's recent historical data by using the
time travel feature. 
For more information, see Access historical data using time travel . 

Table snapshots. If you want to be able to access a table's state from earlier than one week in
the past, consider creating table snapshots periodically.
Table snapshots are lightweight, read-only copies that let you
preserve the state of your tables indefinitely. With table snapshots, for
example, you can compare a table's current data to the data from the beginning
of the year, which isn't possible by using time travel.
You are only charged for storing the data that differs between the base
table and its table snapshot. 
For more information, see Introduction to table snapshots . 

Table clones. If you want to make a lightweight, writable copy of a table, you can use
table clones. You only pay for storage of
the data that differs between a base table and its table clone. For example, you
could create table clones in a test environment so that you can experiment with
copies of production data without impacting the production data and without
having to pay for storage of full copies of the tables. 
For more information, see Introduction to table clones . 
Track data lineage 
Data lineage is a Knowledge Catalog feature that
lets you track how data moves through your systems: where it comes from,
where it is passed to, and what transformations are applied to it.
For more information about how data lineage can help you track data movement in your
project, see About data lineage in Knowledge Catalog. 
Secure resources 
BigQuery security is based on Google Cloud Identity and Access Management .
BigQuery lets you control access to your resources at many
levels, including access to the organization, folders, projects, datasets,
tables, table columns, and table rows. 
For information about controlling access to your BigQuery
resources, see Overview of data security and governance . 
Manage workloads 
BigQuery does many tasks on behalf of your users,
including ingesting, querying, and exporting data. Each task is done by
a BigQuery job . This section describes how you can monitor
and manage your organization's jobs. 
Manage jobs 
Jobs are actions that BigQuery runs on a user's behalf to load,
export, query, or copy data. When a user initiates one of these tasks by using
the Google Cloud console , the bq command-line tool , a SQL statement , or an API call , BigQuery automatically
creates a job to execute the task. 
As a BigQuery administrator, you can monitor, manage, and
troubleshoot your organization's jobs to ensure they are running smoothly. 
For more information, see Manage jobs . 
Manage reservations 
When BigQuery executes queries, it uses units of computing called slots . BigQuery calculates how many
slots are needed to run each query, depending on the size and complexity of the
query. 
BigQuery has two pricing models for charging for the slots that
run your queries: 
On-demand billing. Your queries use a shared pool of slots, and you are
charged for the number of bytes your queries process. For more information on
on-demand billing limits, see Query jobs . 
Capacity-based billing. You assign a reservation or capacity commitment to an
edition, each of which comes with their own feature set and price point to
provide the best working environment for you. 
These pricing models apply per project, so you can have some projects that use
on-demand billing and some projects that use capacity-based billing. 
With on-demand billing, after your monthly allocation of free usage is consumed, you are charged for the
number of bytes that each query processes. Throughput is limited to a predefined
slot quota, which is shared among the queries that run in a project. 
With BigQuery editions billing, you allocate slots for your organization through
autoscaling reservations and optional, but cheaper, capacity commitments. Slots
for each edition come at their own price point, and offer their own set of
features. For more information about BigQuery editions and the features that are
associated with them, see Introduction to
BigQuery editions . 
Refer to the following documents for more information about managing compute
capacity for processing your queries: 

For slots, and the trade-offs between on-demand billing
and capacity-based billing, see Introduction to reservations . 

For the different options for capacity-based billing (monthly or annual commitments), see Slot commitments . 

For creating pools of capacity-based slots, called slot
reservations , see Work with slot reservations . 

For allocating slot reservations to specific projects,
see Work with reservation assignments . 

For estimating the right number of slots to allocate to your
workloads, see Estimate slot capacity requirements . 
Monitor resources 
Google Cloud provides the capability to monitor and audit your
resources,
including BigQuery resources. This section describes the
Google Cloud monitoring and auditing capabilities that apply
to BigQuery. 
For more information, see Introduction to BigQuery
monitoring . 
The Cloud Monitoring dashboard 
Cloud Monitoring provides a dashboard for monitoring BigQuery.
Use this dashboard to view information about BigQuery incidents,
datasets, tables, projects, query times, and slot utilization. 
For more information, see View the Monitoring dashboard . 
Administration charts and alerts 
You can use Cloud Monitoring to create custom charts based on the
resources, metrics, and any aggregation that you specify. 
For more information, see Dashboards and charts . 
You can also create alert policies that notify you if the configured alert is
triggered. For example, you could create an alert that sends an email to a
specified email address if the execution time of a query exceeds a specified
limit. 
For more information, see Creating an alert . 
Monitor reservations 
You can monitor your slot usage on the Workload management page of the
Google Cloud console. You can view your capacity commitments and see where your
slot reservations have been assigned. You can also use the Slot estimator ( Preview ) to help you estimate your organization's
capacity requirements based on historical performance metrics. 
For more information, see Monitoring BigQuery reservations . 
Quotas 
Google Cloud sets limits on the use of resources, including
BigQuery resources, both to
ensure fair usage of shared resources, and to protect you from runaway costs.
You can view your usage of BigQuery resources that have quotas , and request a higher quota , if
needed, by using the Google Cloud console. 
For more information, see BigQuery quotas and limits . 
Audit logs 
Cloud Audit Logs maintain a record of Google Cloud events, including BigQuery
events. You can use the Logs Explorer to query the logs about events related
to BigQuery jobs, datasets, transfers, and more. The Logs
Dashboard displays information about recent errors, and you can use Logs-based metrics to count the log entries that match a given filter. 
For more information, see the Google Cloud logging documentation . 
Optimize workloads 
You can optimize your BigQuery configuration to control both
storage and query processing costs. 

For assistance managing your BigQuery storage costs, see Optimize storage in BigQuery . 

For assistance managing your BigQuery processing costs, see Control costs in BigQuery . 

For assistance optimizing your BigQuery
queries, see Introduction to optimizing query performance . 

For general information about BigQuery costs, see BigQuery pricing and BigQuery billing questions . 
Reliability guidance 
This document provides an understanding of BigQuery reliability,
including insight into availability, durability, data consistency,
consistency of performance, and data recovery in BigQuery, as
well as a review of error handling considerations. To learn more about
reliability and disaster planning, see Understand reliability . 
Troubleshoot 
In addition to the features described in this document for monitoring and
managing your organization's BigQuery system, the following
resources are available for troubleshooting problems that might arise: 
BigQuery error messages 
BigQuery billing questions 
Troubleshoot quota errors 
If you need additional assistance, see Get support . 
What's next 
BigQuery Admin reference guide: recap Send feedback 
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