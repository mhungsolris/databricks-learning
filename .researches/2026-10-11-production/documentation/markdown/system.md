# system

Source: https://docs.databricks.com/aws/en/admin/system-tables
Retrieved: 2026-10-11

System tables reference | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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

Administration 
System tables On this page Last updated on Oct 8, 2026 
System tables reference important 
Databricks highly discourages you from moving this data outside the platform because it can expose sensitive data and put your deployment at risk. Due to the nature of system table information, you are reminded that you are responsible to maintain the security, and prevent misuse, of any exported system table information. 
System tables provide a Databricks -hosted analytical store of your account's operational data. Use them to monitor costs, audit security events, track compute and job performance, and observe data and AI workloads. 
What are system tables? ​ 
System tables are a Databricks -hosted analytical store of your account's operational data found in the system catalog. System tables can be used for historical observability across your account. note 
The information schema tables ( system.information_schema ) work differently from other system tables. See Information schema . 
Requirements ​ 
To access system tables, your workspace must be enabled for Unity Catalog . For more information, see Enable system tables . 
Only a subset of system tables are available in Databricks on AWS GovCloud. See Supported system tables . 
Which system tables are available? ​ 
Currently, Databricks hosts the following system tables: 

Table 
Description 
Supports streaming 
Free retention period 
Includes global or regional data 

Alert configuration (Public Preview) 
A slow-changing dimension table that captures the configuration of every alert over time. Table path : system.alert.alerts 
No 
365 days 
Regional 

Alert evaluation history (Public Preview) 
Records one row for each alert evaluation, including the evaluated state and notification delivery status. Table path : system.alert.alert_evaluation_history 
No 
365 days 
Regional 

Audit logs (Public Preview) 
Includes records for all audit events from workspaces in your region. For a list of available audit events, see Audit log reference . Table path : system.access.audit 
Yes 
365 days 
Regional for workspace-level events. Global for account-level events. 

Billable usage 
Includes records for all billable usage across your account. Table path : system.billing.usage 
Yes 
365 days 
Global 

Clean room events (Public Preview) 
Captures events related to clean rooms. Table path : system.access.clean_room_events 
Yes 
365 days 
Regional 

Clusters 
A slow-changing dimension table that contains the full history of compute configurations over time for any cluster. 
Yes 
365 days 
Regional 

Column lineage 
Includes a record for each read or write event on a Unity Catalog column (but does not include events that do not have a source). Table path : system.access.column_lineage 
Yes 
365 days 
Regional 

Data classification results (Public Preview) 
Stores column-level detections of sensitive data classes across enabled catalogs in your metastore. Table path : system.data_classification.results 
No 
13 months 
Regional 

Data quality monitoring results (Public Preview) 
Stores results of data quality monitoring checks (freshness, completeness) and incident information, including downstream impact, across enabled tables in your metastore. Table path : system.data_quality_monitoring.table_results 
No 
13 months 
Regional 

Governed tags (Beta) 
Contains versioned records for all governed tag definitions in your account, including customer-created and system-generated tags. Table path : system.tags.governed_tags 
No 
365 days 
Global 

Genie Code events (Public Preview) 
Tracks user messages sent to the Genie Code . Table path : system.access.assistant_events 
No 
365 days 
Regional 

Unity Gateway usage (Public Preview) 
Captures request and response details for Unity Gateway model services including token usage, latency, performance metrics, and routing information. Table path : system.ai_gateway.usage 
Yes 
365 days 
Regional 

Unity Gateway external model spend (Beta) 
Records estimated USD spend for requests routed to external models through model provider services. 
Table path : system.ai_gateway.external_model_spend 
No 
365 days 
Regional 

Lakebase observability (Beta) 
Captures Lakebase Postgres observability telemetry, such as session history, query plans, wait events, and schema-change history, across the tables in the system.lakebase schema. Table path : system.lakebase.* 
No 
7 days 
Regional 

OpenSharing data materialization events 
Captures data materialization events created from view, materialized view, and streaming table sharing. Table path : system.sharing.materialization_history 
Yes 
365 days 
Regional for workspace-level events. 

Instance events (Public Preview) 
Captures state transitions of classic compute instances. Table path : system.compute.instance_events 
Yes 
365 days 
Regional 

Instance pools (Public Preview) 
A slow-changing dimension table that contains the full history of instance pool configurations over time. Table path : system.compute.instance_pools 
Yes 
365 days 
Regional 

Job run timeline 
Tracks the start and end times of job runs. Table path : system.lakeflow.job_run_timeline 
Yes 
365 days 
Regional 

Job task timeline 
Tracks the start and end times and compute resources used for job task runs. Table path : system.lakeflow.job_task_run_timeline 
Yes 
365 days 
Regional 

Job tasks 
Tracks all job tasks that run in the account. Table path : system.lakeflow.job_tasks 
Yes 
365 days 
Regional 

Jobs 
Tracks all jobs created in the account. Table path : system.lakeflow.jobs 
Yes 
365 days 
Regional 

Marketplace funnel events (Public Preview) 
Includes consumer impression and funnel data for your listings. Table path : system.marketplace.listing_funnel_events 
Yes 
365 days 
Regional 

Marketplace listing access (Public Preview) 
Includes consumer info for completed request data or get data events on your listings. Table path : system.marketplace.listing_access_events 
Yes 
365 days 
Regional 

MLflow tracking experiment metadata (Public Preview) 
Each row represents an experiment created in the Databricks-managed MLflow system. Table path : system.mlflow.experiments_latest 
Yes 
180 days 
Regional 

MLflow tracking run metadata (Public Preview) 
Each row represents a run created in the Databricks-managed MLflow system. Table path : system.mlflow.runs_latest 
Yes 
180 days 
Regional 

MLflow tracking run metrics (Public Preview) 
Holds the timeseries metrics logged to MLflow associated with a given model training, evaluation, or agent development. Table path : system.mlflow.run_metrics_history 
Yes 
180 days 
Regional 

Model serving endpoint data (Public Preview) 
A slow-changing dimension table that stores metadata for each served foundation model in a model serving endpoint. Table path : system.serving.served_entities 
Yes 
365 days 
Regional 

Model serving endpoint usage (Public Preview) 
Captures token counts for each request to a model serving endpoint and its responses. To capture the endpoint usage in this table, you must enable usage tracking on your serving endpoint . Table path : system.serving.endpoint_usage 
Yes 
90 days 
Regional 

Network access events (Inbound) (Public Preview) 
A table that records an event for every time inbound access to a workspace is denied by an ingress policy. Table path : system.access.inbound_network 
Yes 
30 days 
Regional 

Network access events (Outbound) (Public Preview) 
A table that records an event every time outbound internet access is denied from your account. Table path : system.access.outbound_network 
Yes 
365 days 
Regional 

Node timeline 
Captures the utilization metrics of your all-purpose and jobs compute resources. Table path : system.compute.node_timeline 
Yes 
90 days 
Regional 

Node types 
Captures the currently available node types with their basic hardware information. Table path : system.compute.node_types 
No 
Indefinite 
Regional 

Pipeline events (Beta) 
Records event log entries for Lakeflow pipelines in your region: lifecycle transitions, flow progress, data quality metrics, and errors. Table path : system.lakeflow_pipeline_events_preview.pipeline_events 
Yes 
365 days 
Regional 

Pipeline update timeline 
Tracks the start and end times and compute resources used for pipeline updates. Table path : system.lakeflow.pipeline_update_timeline 
Yes 
365 days 
Regional 

Pipelines 
Tracks all pipelines created in the account. Table path : system.lakeflow.pipelines 
Yes 
365 days 
Regional 

Automatic upgrades (Public Preview) 
Tracks the history of feature enablement operations performed by automatic upgrades on Unity Catalog managed tables. Table path : system.storage.table_auto_upgrade_operations_history 
No 
180 days 
Regional 

Predictive optimization (Public Preview) 
Tracks the operation history of the predictive optimization feature. Table path : system.storage.predictive_optimization_operations_history 
No 
180 days 
Regional 

Pricing 
A historical log of SKU pricing. A record gets added each time there is a change to a SKU price. Table path : system.billing.list_prices 
No 
Indefinite 
Global 

Query history 
Captures records for all queries run on SQL warehouses and serverless compute for notebooks and jobs . Table path : system.query.history 
No 
365 days 
Regional 

Replication 
Tracks replication status for Databricks managed disaster recovery (DR). Table path : system.replication.states 
Yes 
365 days 
Global 

SQL warehouse events 
Captures events related to SQL warehouses. For example, starting, stopping, running, scaling up and down. Table path : system.compute.warehouse_events 
Yes 
365 days 
Regional 

SQL warehouses 
Contains the full history of configurations over time for any SQL warehouse. Table path : system.compute.warehouses 
Yes 
365 days 
Regional 

Table lineage 
Includes a record for each read or write event on a Unity Catalog table or path. Table path : system.access.table_lineage 
Yes 
365 days 
Regional 

Workspaces (Public Preview) 
The workspaces_latest table is a slow-changing dimension table of metadata for all the workspaces in the account. Table path : system.access.workspaces_latest 
No 
Indefinite 
Global 

Zerobus Ingest (Streams) (Beta) 
A table that stores all data related to stream events incurred by Zerobus Ingest usage. Table path : system.lakeflow.zerobus_stream 
Yes 
365 days 
Regional 

Zerobus Ingest (Ingestion) (Beta) 
A table that stores all data related to records ingested using Zerobus Ingest. Table path : system.lakeflow.zerobus_ingest 
Yes 
365 days 
Regional ← ✕ 

Table 
Description 
Supports streaming 
Free retention period 
Includes global or regional data 

Alert configuration (Public Preview) 
A slow-changing dimension table that captures the configuration of every alert over time. Table path : system.alert.alerts 
No 
365 days 
Regional 

Alert evaluation history (Public Preview) 
Records one row for each alert evaluation, including the evaluated state and notification delivery status. Table path : system.alert.alert_evaluation_history 
No 
365 days 
Regional 

Audit logs (Public Preview) 
Includes records for all audit events from workspaces in your region. For a list of available audit events, see Audit log reference . Table path : system.access.audit 
Yes 
365 days 
Regional for workspace-level events. Global for account-level events. 

Billable usage 
Includes records for all billable usage across your account. Table path : system.billing.usage 
Yes 
365 days 
Global 

Clean room events (Public Preview) 
Captures events related to clean rooms. Table path : system.access.clean_room_events 
Yes 
365 days 
Regional 

Clusters 
A slow-changing dimension table that contains the full history of compute configurations over time for any cluster. 
Yes 
365 days 
Regional 

Column lineage 
Includes a record for each read or write event on a Unity Catalog column (but does not include events that do not have a source). Table path : system.access.column_lineage 
Yes 
365 days 
Regional 

Data classification results (Public Preview) 
Stores column-level detections of sensitive data classes across enabled catalogs in your metastore. Table path : system.data_classification.results 
No 
13 months 
Regional 

Data quality monitoring results (Public Preview) 
Stores results of data quality monitoring checks (freshness, completeness) and incident information, including downstream impact, across enabled tables in your metastore. Table path : system.data_quality_monitoring.table_results 
No 
13 months 
Regional 

Governed tags (Beta) 
Contains versioned records for all governed tag definitions in your account, including customer-created and system-generated tags. Table path : system.tags.governed_tags 
No 
365 days 
Global 

Genie Code events (Public Preview) 
Tracks user messages sent to the Genie Code . Table path : system.access.assistant_events 
No 
365 days 
Regional 

Unity Gateway usage (Public Preview) 
Captures request and response details for Unity Gateway model services including token usage, latency, performance metrics, and routing information. Table path : system.ai_gateway.usage 
Yes 
365 days 
Regional 

Unity Gateway external model spend (Beta) 
Records estimated USD spend for requests routed to external models through model provider services. 
Table path : system.ai_gateway.external_model_spend 
No 
365 days 
Regional 

Lakebase observability (Beta) 
Captures Lakebase Postgres observability telemetry, such as session history, query plans, wait events, and schema-change history, across the tables in the system.lakebase schema. Table path : system.lakebase.* 
No 
7 days 
Regional 

OpenSharing data materialization events 
Captures data materialization events created from view, materialized view, and streaming table sharing. Table path : system.sharing.materialization_history 
Yes 
365 days 
Regional for workspace-level events. 

Instance events (Public Preview) 
Captures state transitions of classic compute instances. Table path : system.compute.instance_events 
Yes 
365 days 
Regional 

Instance pools (Public Preview) 
A slow-changing dimension table that contains the full history of instance pool configurations over time. Table path : system.compute.instance_pools 
Yes 
365 days 
Regional 

Job run timeline 
Tracks the start and end times of job runs. Table path : system.lakeflow.job_run_timeline 
Yes 
365 days 
Regional 

Job task timeline 
Tracks the start and end times and compute resources used for job task runs. Table path : system.lakeflow.job_task_run_timeline 
Yes 
365 days 
Regional 

Job tasks 
Tracks all job tasks that run in the account. Table path : system.lakeflow.job_tasks 
Yes 
365 days 
Regional 

Jobs 
Tracks all jobs created in the account. Table path : system.lakeflow.jobs 
Yes 
365 days 
Regional 

Marketplace funnel events (Public Preview) 
Includes consumer impression and funnel data for your listings. Table path : system.marketplace.listing_funnel_events 
Yes 
365 days 
Regional 

Marketplace listing access (Public Preview) 
Includes consumer info for completed request data or get data events on your listings. Table path : system.marketplace.listing_access_events 
Yes 
365 days 
Regional 

MLflow tracking experiment metadata (Public Preview) 
Each row represents an experiment created in the Databricks-managed MLflow system. Table path : system.mlflow.experiments_latest 
Yes 
180 days 
Regional 

MLflow tracking run metadata (Public Preview) 
Each row represents a run created in the Databricks-managed MLflow system. Table path : system.mlflow.runs_latest 
Yes 
180 days 
Regional 

MLflow tracking run metrics (Public Preview) 
Holds the timeseries metrics logged to MLflow associated with a given model training, evaluation, or agent development. Table path : system.mlflow.run_metrics_history 
Yes 
180 days 
Regional 

Model serving endpoint data (Public Preview) 
A slow-changing dimension table that stores metadata for each served foundation model in a model serving endpoint. Table path : system.serving.served_entities 
Yes 
365 days 
Regional 

Model serving endpoint usage (Public Preview) 
Captures token counts for each request to a model serving endpoint and its responses. To capture the endpoint usage in this table, you must enable usage tracking on your serving endpoint . Table path : system.serving.endpoint_usage 
Yes 
90 days 
Regional 

Network access events (Inbound) (Public Preview) 
A table that records an event for every time inbound access to a workspace is denied by an ingress policy. Table path : system.access.inbound_network 
Yes 
30 days 
Regional 

Network access events (Outbound) (Public Preview) 
A table that records an event every time outbound internet access is denied from your account. Table path : system.access.outbound_network 
Yes 
365 days 
Regional 

Node timeline 
Captures the utilization metrics of your all-purpose and jobs compute resources. Table path : system.compute.node_timeline 
Yes 
90 days 
Regional 

Node types 
Captures the currently available node types with their basic hardware information. Table path : system.compute.node_types 
No 
Indefinite 
Regional 

Pipeline events (Beta) 
Records event log entries for Lakeflow pipelines in your region: lifecycle transitions, flow progress, data quality metrics, and errors. Table path : system.lakeflow_pipeline_events_preview.pipeline_events 
Yes 
365 days 
Regional 

Pipeline update timeline 
Tracks the start and end times and compute resources used for pipeline updates. Table path : system.lakeflow.pipeline_update_timeline 
Yes 
365 days 
Regional 

Pipelines 
Tracks all pipelines created in the account. Table path : system.lakeflow.pipelines 
Yes 
365 days 
Regional 

Automatic upgrades (Public Preview) 
Tracks the history of feature enablement operations performed by automatic upgrades on Unity Catalog managed tables. Table path : system.storage.table_auto_upgrade_operations_history 
No 
180 days 
Regional 

Predictive optimization (Public Preview) 
Tracks the operation history of the predictive optimization feature. Table path : system.storage.predictive_optimization_operations_history 
No 
180 days 
Regional 

Pricing 
A historical log of SKU pricing. A record gets added each time there is a change to a SKU price. Table path : system.billing.list_prices 
No 
Indefinite 
Global 

Query history 
Captures records for all queries run on SQL warehouses and serverless compute for notebooks and jobs . Table path : system.query.history 
No 
365 days 
Regional 

Replication 
Tracks replication status for Databricks managed disaster recovery (DR). Table path : system.replication.states 
Yes 
365 days 
Global 

SQL warehouse events 
Captures events related to SQL warehouses. For example, starting, stopping, running, scaling up and down. Table path : system.compute.warehouse_events 
Yes 
365 days 
Regional 

SQL warehouses 
Contains the full history of configurations over time for any SQL warehouse. Table path : system.compute.warehouses 
Yes 
365 days 
Regional 

Table lineage 
Includes a record for each read or write event on a Unity Catalog table or path. Table path : system.access.table_lineage 
Yes 
365 days 
Regional 

Workspaces (Public Preview) 
The workspaces_latest table is a slow-changing dimension table of metadata for all the workspaces in the account. Table path : system.access.workspaces_latest 
No 
Indefinite 
Global 

Zerobus Ingest (Streams) (Beta) 
A table that stores all data related to stream events incurred by Zerobus Ingest usage. Table path : system.lakeflow.zerobus_stream 
Yes 
365 days 
Regional 

Zerobus Ingest (Ingestion) (Beta) 
A table that stores all data related to records ingested using Zerobus Ingest. Table path : system.lakeflow.zerobus_ingest 
Yes 
365 days 
Regional 
System tables are free to use. You are only charged for the compute used to query them. note 
You may see other system tables in your account, in addition to the ones listed above. Those tables are currently in Private Preview and are empty by default. If you are interested in using any of these tables, please reach out to your Databricks account team. 
System tables relationships ​ 
The following entity-relationship diagram outlines how the currently available system tables relate to one another. This diagram highlights the primary and foreign keys of each table. 

Enable system tables ​ 
Because system tables are governed by Unity Catalog , you need to have at least one Unity Catalog -enabled workspace in your account to enable your account's system tables. System tables include data from all workspaces in your account, but they can only be accessed from a Unity Catalog -enabled workspace. 
The metastore needs to be on Unity Catalog Privilege Model Version 1.0 to access system tables. See Upgrade to privilege inheritance . 
Grant access to system tables ​ 
Access to system tables is governed by Unity Catalog . Users with both the account admin and metastore admin roles have access to system tables by default. To allow other users to query system tables, the admin must grant users the following permissions: USE CATALOG on the system catalog, USE SCHEMA on the system schemas, and SELECT on the system schemas. See Manage privileges in Unity Catalog . 
System tables are read-only and cannot be modified. note 
If your account was created after November 8, 2023 , you might not have a metastore admin by default. For more information, see Get started with Unity Catalog . 
Do system tables contain data for all workspaces in your account? ​ 
System tables contain operational data for all workspaces in your account deployed within the same cloud region. Some tables include global data. For details, see the list of available tables . 
Although system tables can only be accessed through a Unity Catalog workspace, they include operational data from non- Unity Catalog workspaces in your account. 
Where is system table data stored? ​ 
Your account's system table data is stored in a Databricks -hosted storage account located in the same region as your metastore. The data is securely shared with you using OpenSharing . 
Configure system table data retention ​ Beta 
Configurable retention for system tables is in Beta . Account admins can control access to this feature from the account-level Previews page by opting into the System Tables Configurable Retention preview. It can take up to 24 hours for the preview to be enabled on your account. 
Configurable retention lets an account admin set a single retention period that applies to all supported system tables in their account. 
When this Beta feature is enabled in an account, the free retention period automatically becomes 395 days for all supported system tables, replacing the table-specific periods. Account admins can then set a custom retention period from 30 to 3,650 days. 
The configured retention period is free during Beta. Data retained for more than 395 days will incur storage charges when configurable retention becomes generally available. 
Supported tables ​ 
The configured retention period for your account applies to all system tables except for those in the system.data_classification , system.data_quality_monitoring , and system.lakebase schemas. 
Configure retention in the account console ​ 
You must be an account admin to configure system table retention. To configure the retention period: 
In the account console sidebar, click Settings . 
Click the Account settings tab. 
In the System Tables data retention (days) setting, enter the retention period in days. 
Click Save . 
Configure retention using the Account Settings API ​ 
You can manage system table retention with the Databricks Account Settings API. You need your Databricks account ID and an account admin personal access token or OAuth token. The setting name is st_retention . 
To retrieve the current retention period, send a GET request to /api/2.1/accounts/{account_id}/settings/st_retention : Bash 
curl --request GET \ --header "Content-Type: application/json" \ --header "Authorization: Bearer $token " \ "<account-console-url>/api/2.1/accounts/<account-id>/settings/st_retention" 
The response contains the value set for the account. If an account admin hasn't configured a value, the response contains the default value of 395 days. 
To change the retention period, send a PATCH request to /api/2.1/accounts/{account_id}/settings/st_retention . The following example sets the retention period to 400 days: Bash 
curl --request PATCH \ --header "Content-Type: application/json" \ --header "Authorization: Bearer $token " \ --data '{ "integer_val": { "value": 400 }, "name": "st_retention" }' \ "<account-console-url>/api/2.1/accounts/<account-id>/settings/st_retention" 
Retention behavior ​ 
If you increase the retention period, the change applies immediately to the tables. 
If you decrease the retention period, Databricks waits seven days before applying the change. During this grace period, an account admin can correct an unintended change before historical data is permanently deleted. 
When a record exceeds the configured retention period, Databricks typically deletes the record within one week. 
Limitations ​ 
Configurable retention doesn't apply to the system.data_classification , system.data_quality_monitoring , and system.lakebase schemas. These system tables retain data according to their table-specific retention policies. 
Increasing the retention period does not backfill any historical data. 
In the event of a disaster or total data loss, Databricks doesn't guarantee recovery of all system table data for the configured retention period. 
Configurable retention is limited to the HIPAA, HITRUST, PCI, C5, and TISAX compliance standards. All other compliance standards are not supported. 
Where are system tables located in Catalog Explorer? ​ 
The system tables in your account are located in a catalog called system , which is included in every Unity Catalog metastore. In the system catalog, you'll see schemas such as access and billing that contain the system tables. 
Considerations for streaming system tables ​ 
Databricks uses OpenSharing to share system table data with customers. Be aware of the following considerations when streaming with OpenSharing : 
To stream from system tables, you must use Databricks Runtime 16.4 and above. To stream the change data feed (CDF) using the readChangeFeed option, you must use Databricks Runtime 17.3 and above. 
If you are using streaming with system tables, set the skipChangeCommits option to true . This ensures the streaming job is not disrupted by deletes in the system tables. See Handle changes to source Delta Lake tables . 
Trigger.AvailableNow is supported on Databricks Runtime 18.0 and above. The query captures the system table's current version when it starts, processes all available data in one or more micro-batches, and then stops. On Databricks Runtime 17.3 and below, Trigger.AvailableNow is converted to Trigger.Once , which processes a single micro-batch per run. 
System tables use the default 7 days retention for VACUUM (see Configure data retention for time travel queries ), meaning your streaming query might break if it lags behind by more than 7 days. Monitor your streams to make sure they catch up with the latest system table version. 
If your streaming job isn't catching up to the latest system table version, use Trigger.AvailableNow (supported on Databricks Runtime 18.0 and above) so that each run processes the full available backlog, or increase the scheduled frequency of the job. 
Read incremental changes from streaming system tables ​ Python 
spark . readStream . option ( "skipChangeCommits" , "true" ) . table ( "system.billing.usage" ) 
Known issues ​ 
New columns may be added to existing system tables at any time. Queries that rely on a fixed schema may break if new columns are introduced. Existing columns will not change or be removed. If you are writing system table data to another target table, consider enabling schema evolution . 
New fields may be added to struct-typed columns at any time. If you are writing system table data to another target table, consider enabling schema evolution . 
No support for real-time monitoring. Data is updated throughout the day. If you don't see a log for a recent event, check back later. 
The __internal_logging system table schema supports payload logging using AI Gateway-enabled inference tables for external models and provisioned throughput workloads. This schema is visible to account admins, but it cannot be enabled and should not be used for customer workflows. 
To prevent performance issues, system table queries that are not sufficiently selective return the following error: System Table query returned too much data. Please repeat query with more selective predicates. 
If your workspace uses a customer-managed VPC , you might be denied access to the S3 bucket where the logs are stored. If so, you need to update your VPC endpoint policy to allow access to the S3 bucket where your region's system tables data is stored. For a list of regional bucket names, see the System tables bucket column in Storage bucket addresses table . 
The system schemas system.operational_data and system.lineage are deprecated and will contain empty tables. On this page 
What are system tables? 
Requirements 
Which system tables are available? 
System tables relationships 
Enable system tables 
Grant access to system tables 
Do system tables contain data for all workspaces in your account? 
Where is system table data stored? 
Configure system table data retention 
Supported tables 
Configure retention in the account console 
Configure retention using the Account Settings API 
Retention behavior 
Limitations 
Where are system tables located in Catalog Explorer? 
Considerations for streaming system tables 
Read incremental changes from streaming system tables 
Known issues Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 