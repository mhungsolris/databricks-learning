# pipeline-properties

Source: https://docs.databricks.com/aws/en/ldp/properties
Retrieved: 2026-10-11

Pipeline properties reference | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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

Data engineering 
Lakeflow pipelines 
Configure pipelines 
Pipeline configuration reference On this page Last updated on Sep 11, 2026 
Pipeline properties reference 
Reference for pipeline JSON configuration settings and table properties. For more details on using these properties and configurations, see the following articles: 
Configure pipelines 
Pipelines REST API 
Lakeflow pipelines configuration and Apache Spark™ Declarative Pipelines ​ 
Lakeflow pipelines are built on Apache Spark™ Declarative Pipelines (SDP). The pipeline configuration is largely a superset of the SDP project specification. Differences in the properties usage between SDP and Lakeflow pipelines are noted. For a comparison of the capabilities that Lakeflow pipelines and SDP share, see Apache Spark Declarative Pipelines . 
How to set properties ​ 
You set most pipeline properties in one of the following ways: 
Pipeline JSON or YAML : Add the property to the pipeline specification, either in the pipeline settings UI or in a Declarative Automation Bundles configuration file. Pipeline-level settings such as catalog , channel , and edition are set this way. 
The configuration object : Spark configuration properties (properties prefixed with pipelines. ) can be set for the entire pipeline by adding them to the configuration object in the pipeline specification. See Configure pipelines . 
SQL : In a SQL source file, set a Spark configuration property for the datasets that follow it with SET . 
Python : In a Python source file, set a Spark configuration property on an individual dataset with the spark_conf argument of the dataset decorator. 
Setting a property in SQL or Python applies it at the dataset level, which overrides the pipeline-level value from the configuration object. Not every property supports every method: pipeline-level settings can only be set in the specification, while Spark configuration properties can be set at either the pipeline or dataset level. 
Pipeline configurations ​ 

id 
Type: string 
A globally unique identifier for this pipeline. The identifier is assigned by the system and cannot be changed. 
Lakeflow pipelines only. SDP does not assign a pipeline identifier 

name 
Type: string 
A user-friendly name for this pipeline. The name can be used to identify pipeline jobs in the UI. 
Available in SDP as the required name field 

configuration 
Type: object 
An optional list of settings to add to the Spark configuration of the cluster that runs the pipeline. These settings are read by the pipeline runtime and available to pipeline queries through the Spark configuration. 
Elements must be formatted as key:value pairs. 
Available in SDP as configuration 

parameters 
Type: object Beta 
This feature is in Beta . 
An optional map of key-value pairs that pipeline source code can reference using named parameter syntax (for example, :source_catalog ). Use parameters to reuse the same pipeline source code across environments or datasets without editing the source. 
Keys can contain alphanumeric characters, underscores ( _ ), hyphens ( - ), and periods ( . ). Values are always strings. 
You can override these defaults when starting an update, on a pipeline task in a job, or with pushed-down job parameters. Pipeline parameters can only be referenced from SQL source code. See Use parameters with pipelines . 
Lakeflow pipelines only 

libraries 
Type: array of objects 
An array of code files containing the pipeline code and required artifacts. 
Available in SDP as libraries , specified as a list of source-file glob patterns rather than an array of code file objects 

clusters 
Type: array of objects 
An array of specifications for the clusters to run the pipeline. 
If this is not specified, pipelines automatically select a default cluster configuration for the pipeline. 
Lakeflow pipelines only. SDP does not manage compute 

development 
Type: boolean 
A flag indicating whether to run the pipeline in development or production mode. 
The default value is false . 
Lakeflow pipelines only 

notifications 
Type: array of objects 
An optional array of specifications for email notifications when a pipeline update completes, fails with a retryable error, fails with a non-retryable error, or a flow fails. 
Lakeflow pipelines only 

continuous 
Type: boolean 
A flag indicating whether to run the pipeline continuously. 
The default value is false . 
Lakeflow pipelines only 

catalog 
Type: string 
The name of the default catalog for the pipeline, where all datasets and metadata for pipeline are published. Setting this value enables Unity Catalog for the pipeline. 
If left unset, the pipeline publishes to the legacy Hive metastore using the location specified in storage . 
In legacy publishing mode, specifies the catalog containing the target schema where all datasets from the current pipeline are published. See LIVE schema (legacy) . 
Available in SDP as catalog 

schema 
Type: string 
The name of the default schema for the pipeline, where all datasets and metadata for the pipeline are published by default. See Set the target catalog and schema . 
Available in SDP as database , which also accepts the alias schema 

target (legacy) 
Type: string 
The name of the default schema for the pipeline, where all datasets and metadata for the pipeline are published by default. Using schema instead of target is preferred. 
Lakeflow pipelines only 

storage (legacy) 
Type: string 
A location on DBFS or cloud storage where output data and metadata required for pipeline execution are stored. Tables and metadata are stored in subdirectories of this location. 
When the storage setting is not specified, the system defaults to a location in dbfs:/pipelines/ . 
The storage setting cannot be changed after a pipeline is created. 
Available in SDP as the required storage field. In Lakeflow pipelines , storage is a legacy setting 

channel 
Type: string 
The version of the pipeline runtime to use. The supported values are: 
preview to test your pipeline with upcoming changes to the runtime version. 
current to use the current runtime version. 
The channel field is optional. The default value is current . Databricks recommends using the current runtime version for production workloads. 
Lakeflow pipelines only 

edition 
Type string 
The product edition to run the pipeline. This setting allows you to choose the best product edition based on the requirements of your pipeline: 
CORE to run streaming ingest workloads. 
PRO to run streaming ingest and change data capture (CDC) workloads. 
ADVANCED to run streaming ingest workloads, CDC workloads, and workloads that require expectations to enforce data quality constraints. 
The edition field is optional. The default value is ADVANCED . 
Lakeflow pipelines only 

photon 
Type: boolean 
A flag indicating whether to use What is Photon? to run the pipeline. Photon is the Databricks high performance Spark engine. Photon-enabled pipelines are billed at a different rate than non-Photon pipelines. 
The photon field is optional. The default value is false . 
Lakeflow pipelines only 

serverless 
Type: boolean 
A flag indicating whether the pipeline uses serverless compute. See Configure a serverless pipeline . 
Lakeflow pipelines only 

event_log 
Type: object 
Configuration for the pipeline's event log destination, as an object with name , catalog , and schema fields that publish the event log to a Unity Catalog table. See Pipeline event log . 
Lakeflow pipelines only 

tags 
Type: object 
An optional map of user-defined tags for the pipeline. A maximum of 25 tags can be added. 
Lakeflow pipelines only 

budget_policy_id 
Type: string 
The ID of the serverless budget policy to apply to this pipeline, used to attribute serverless usage for cost tracking. This field appears in the JSON or YAML configuration only when you explicitly set a policy. If it is unset, Databricks resolves a default policy automatically. The resolved policy is shown in the pipeline settings UI, but it is not written to the JSON or YAML configuration. 
Lakeflow pipelines only 

root_path 
Type: string 
The root path for the pipeline. When set, this directory is added to sys.path when executing Python source files, so modules can be imported relative to it. 
Lakeflow pipelines only 

environment 
Type: object 
An environment specification used to install Python dependencies for the pipeline. 
Lakeflow pipelines only 

pipelines.maxFlowRetryAttempts 
Type: int 
If a retryable failure occurs during a pipeline update, this is the maximum number of times to retry a flow before failing the pipeline update. 
Use this to bound retries on a single flow that's prone to retryable failures so it can't stall an entire update. 
Default: Two retry attempts. When a retryable failure occurs, the pipeline runtime attempts to run the flow three times, including the original attempt. 
Lakeflow pipelines only 

pipelines.numUpdateRetryAttempts 
Type: int 
If a retryable failure occurs during an update, this is the maximum number of times to retry the update before permanently failing the update. The retry is run as a full update. 
Use this to bound retries on an entire update, so a stuck update fails permanently rather than retrying indefinitely. 
This parameter applies only to pipelines using automatic retry and restart behavior . Retries are not attempted for ad-hoc updates run from the editor or when you run a Validate update. 
Default: 
Five for triggered pipelines. 
Unlimited for continuous pipelines. 
Lakeflow pipelines only 
Pipeline table properties ​ 
In addition to the table properties supported by Delta Lake , you can set the following table properties. 

pipelines.autoOptimize.zOrderCols 
Default: None 
An optional string containing a comma-separated list of column names to z-order this table by. For example, pipelines.autoOptimize.zOrderCols = "year,month" 
Databricks recommends liquid clustering instead of Z-ordering for optimizing data layout in pipeline tables. To let Databricks select and maintain the clustering columns automatically, use CLUSTER BY AUTO ( cluster_by_auto=True in Python). See Use liquid clustering for tables . 
Lakeflow pipelines only 

pipelines.reset.allowed 
Default: true 
Controls whether a full refresh is allowed for this table. 
Available in SDP as pipelines.reset.allowed 

pipelines.autoOptimize.managed 
Default: true 
Enables or disables automatically scheduled optimization of this table. 
For pipelines managed by predictive optimization , this property is not used. 
Lakeflow pipelines only 
Pipelines trigger interval ​ 
You can specify a pipeline trigger interval for the entire pipeline or as part of a dataset declaration. See Set trigger interval for continuous pipelines . 

pipelines.trigger.interval 
The default is based on flow type: 
Five seconds for streaming queries. 
One minute for complete queries when all input data is from Delta sources. 
Ten minutes for complete queries when some data sources may be non-Delta. 
The value is a number plus the time unit. The following are the valid time units: 
second , seconds 
minute , minutes 
hour , hours 
day , days 
You can use the singular or plural unit when defining the value, for example: 
{"pipelines.trigger.interval" : "1 hour"} 
{"pipelines.trigger.interval" : "10 seconds"} 
{"pipelines.trigger.interval" : "30 second"} 
{"pipelines.trigger.interval" : "1 minute"} 
{"pipelines.trigger.interval" : "10 minutes"} 
{"pipelines.trigger.interval" : "10 minute"} 
Lakeflow pipelines only 
Databricks recommends setting pipelines.trigger.interval on individual tables because streaming and batch queries have different defaults. Set the value on the pipeline only when processing requires controlling updates for the entire pipeline graph. 
To set the interval on a table in Python, use the spark_conf argument: Python 
@dp . table ( spark_conf = { "pipelines.trigger.interval" : "10 seconds" } ) def < function - name > ( ) : return ( < query > ) 
To set the interval on the datasets that follow it in SQL, use SET : SQL 
SET pipelines . trigger . interval = 10 seconds ; CREATE OR REFRESH MATERIALIZED VIEW TABLE_NAME AS SELECT . . . 
To set the interval on the entire pipeline, add it to the configuration object in the pipeline specification: JSON 
{ "configuration" : { "pipelines.trigger.interval" : "10 seconds" } } 
Cluster attributes that are not user-settable ​ 
Because pipelines manage cluster lifecycles, many cluster settings are set by the system and cannot be manually configured by users, either in a pipeline configuration or in a cluster policy used by a pipeline. The following table lists these settings and why they cannot be manually set. 
Lakeflow pipelines only. SDP does not manage compute, so these cluster attributes do not apply 

cluster_name 
SDP sets the names of the clusters used to run pipeline updates. These names cannot be overridden. 

data_security_mode 
access_mode 
These values are automatically set by the system. 

spark_version 
SDP clusters run on a custom version of Databricks Runtime that is continually updated to include the latest features. The version of Spark is bundled with the Databricks Runtime version and cannot be overridden. 

autotermination_minutes 
Because SDP manages cluster auto-termination and reuse logic, the cluster auto-termination time cannot be overridden. 

runtime_engine 
Although you can control this field by enabling Photon for your pipeline, you cannot set this value directly. 

effective_spark_version 
This value is automatically set by the system. 

cluster_source 
This field is set by the system and is read-only. 

docker_image 
Because SDP manages the cluster lifecycle, you cannot use a custom container with pipeline clusters. 

workload_type 
This value is set by the system and cannot be overridden. 
Source and query options ​ 
Some data ingestion and processing behaviors are configured on the data source or query rather than as pipeline properties. These include schema evolution, schema hints and inference, ingestion rate limits, and file filtering. To configure them, use the options for read_files and Auto Loader . For schema evolution with from_json , see Infer and evolve the schema using from_json in pipelines . On this page 
Lakeflow pipelines configuration and Apache Spark™ Declarative Pipelines 
How to set properties 
Pipeline configurations 
Pipeline table properties 
Pipelines trigger interval 
Cluster attributes that are not user-settable 
Source and query options Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 