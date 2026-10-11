# databricks-pipeline-updates

Source: https://docs.databricks.com/aws/en/ldp/updates
Retrieved: 2026-10-11

Run a pipeline update | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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
Pipeline update On this page Last updated on Sep 11, 2026 
Run a pipeline update 
A pipeline update starts a cluster, validates your source code, and refreshes the tables and views defined in the pipeline. You can trigger an update manually, on a schedule, or programmatically. 
What is a pipeline update? ​ 
After you create a pipeline and are ready to run it, you start an update . A pipeline update does the following: 
Starts a cluster with the correct configuration. 
Discovers all the defined tables and views and checks for any analysis errors such as invalid column names, missing dependencies, and syntax errors. 
Creates or updates tables and views with the most recent data available. 
Using a dry run , you can check for problems in a pipeline's source code without waiting for tables to be created or updated. This feature is useful when developing or testing pipelines because it lets you find and fix errors in your pipeline, such as incorrect table or column names. 
How are pipeline updates triggered? ​ 
Use one of the following options to start pipeline updates: 

Update trigger 
Details 

Manual 
You can manually trigger pipeline updates from the Lakeflow Pipelines Editor, or the pipelines list. See Manually trigger a pipeline update . 

Scheduled 
You can schedule updates for pipelines using jobs. See Pipeline task for jobs . 

Programmatic 
You can programmatically trigger updates using third-party tools, APIs, and CLIs. See Run pipelines in a workflow and pipeline REST API . ← ✕ 

Update trigger 
Details 

Manual 
You can manually trigger pipeline updates from the Lakeflow Pipelines Editor, or the pipelines list. See Manually trigger a pipeline update . 

Scheduled 
You can schedule updates for pipelines using jobs. See Pipeline task for jobs . 

Programmatic 
You can programmatically trigger updates using third-party tools, APIs, and CLIs. See Run pipelines in a workflow and pipeline REST API . 
Manually trigger a pipeline update ​ 
Use one of the following options to manually trigger a pipeline update: 
Run the full pipeline, or a subset of the pipeline (a single source file, or a single table), from the Lakeflow Pipelines Editor. For more information, see Run pipeline code . 
Run the full pipeline from the Jobs & Pipelines list. Click in the same row as the pipeline in the list. 
From the pipeline monitoring page, click the button. note 
The default behavior for manually triggered pipeline updates is to refresh all datasets defined in the pipeline. 
Pipeline refresh semantics ​ 
The following table describes the default refresh, full refresh, and reset checkpoints behavior for materialized views and streaming tables : 

Update type 
Materialized view 
Streaming table 

Refresh (default) 
Updates results to reflect the current results of the defining query. Databricks examines the cost and performs an incremental refresh when it is more efficient. See Incremental refresh for materialized views 
Processes new records through the logic defined in streaming tables and flows. 

Full refresh 
Recomputes results to reflect the current results of the defining query. 
Clears data from streaming tables , clears checkpoints from flows, and reprocesses all records from the data source. See Full refresh for streaming tables 

Reset streaming flow checkpoints 
Not applicable to materialized views . 
Clears checkpoints from flows but does not clear data from streaming tables , then reprocesses all records from the data source. ← ✕ 

Update type 
Materialized view 
Streaming table 

Refresh (default) 
Updates results to reflect the current results of the defining query. Databricks examines the cost and performs an incremental refresh when it is more efficient. See Incremental refresh for materialized views 
Processes new records through the logic defined in streaming tables and flows. 

Full refresh 
Recomputes results to reflect the current results of the defining query. 
Clears data from streaming tables , clears checkpoints from flows, and reprocesses all records from the data source. See Full refresh for streaming tables 

Reset streaming flow checkpoints 
Not applicable to materialized views . 
Clears checkpoints from flows but does not clear data from streaming tables , then reprocesses all records from the data source. 
By default, all materialized views and streaming tables in a pipeline refresh with each update. You can optionally omit tables from updates using the following features: 
Select tables for refresh : Use this UI to add or remove materialized views and streaming tables before running an update. See Start a pipeline update for selected tables . 
Refresh failed tables : Start an update for failed materialized views and streaming tables , including downstream dependencies. See Start a pipeline update for failed tables . 
Both of these features support default refresh semantics or full refresh. You can optionally use the Select tables for refresh dialog to exclude additional tables when running a refresh for failed tables. 
For streaming tables , you can choose to clear the streaming checkpoints for selected flows and not the data from the associated streaming tables . To clear the checkpoints for selected flows, use the Databricks REST API to start a refresh. See Start a pipeline update to clear selective streaming flows' checkpoints . 
When to use a full refresh ​ 
Databricks recommends running full refreshes only when necessary. A full refresh always reprocesses all records from the specified data sources through the logic that defines the dataset. The time and resources to complete a full refresh are correlated to the size of the source data. 
Materialized views return the same results whether default or full refresh is used. Using a full refresh with streaming tables resets all state processing and checkpoint information and can result in dropped records if input data is no longer available. See Full refresh for streaming tables 
Databricks only recommends full refresh when the input data sources contain the data needed to recreate the desired state of the table or view. Consider the following scenarios where input source data is no longer available and the outcome of running a full refresh: 

Data source 
Reason input data is absent 
Outcome of full refresh 

Kafka 
Short retention threshold 
Records no longer present in the Kafka source are dropped from the target table. 

Files in object storage 
Lifecycle policy 
Data files no longer present in the source directory are dropped from the target table. 

Records in a table 
Deleted for compliance 
Only records present in the source table are processed. ← ✕ 

Data source 
Reason input data is absent 
Outcome of full refresh 

Kafka 
Short retention threshold 
Records no longer present in the Kafka source are dropped from the target table. 

Files in object storage 
Lifecycle policy 
Data files no longer present in the source directory are dropped from the target table. 

Records in a table 
Deleted for compliance 
Only records present in the source table are processed. 
To prevent full refreshes from being run on a table or view, set the table property pipelines.reset.allowed to false . See Pipeline table properties . You can also use an append flow to append data to an existing streaming table without requiring a full refresh. 
Start a pipeline update for selected tables ​ 
You can optionally reprocess data for only selected tables in your pipeline. For example, during development, you only change a single table and want to reduce testing time, or a pipeline update fails and you want to refresh only the failed tables . 
The Lakeflow Pipelines Editor has options for reprocessing a source file, selected tables, or a single table. For details, see Run pipeline code . 
Start a pipeline update for failed tables ​ 
If a pipeline update fails because of errors in one or more tables in the pipeline graph, you can start an update of only failed tables and any downstream dependencies. note 
Excluded tables are not refreshed, even if they depend on a failed table. 
To update failed tables, on the pipeline monitoring page, click Refresh failed tables . 
To update only selected failed tables from the pipeline monitoring page: 

Click next to the Refresh failed tables button and click Select tables for refresh . The Select tables for refresh dialog appears. 

To select the tables to refresh, click each table. The selected tables are highlighted and labeled. To remove a table from the update, click the table again. 

Click Refresh selection . note 
The Refresh selection button displays the number of selected tables in parentheses. 
To reprocess data already ingested for the selected tables, click next to the Refresh selection button and click Full Refresh selection . 
Start a pipeline update to clear selective streaming flows' checkpoints ​ 
You can optionally reprocess data for selected streaming flows in your pipeline without clearing any already ingested data. note 
Flows that are not selected are run using a REFRESH update. You can also specify full_refresh_selection or refresh_selection to selectively refresh other tables. 
To start an update to refresh the selected streaming checkpoints, use the updates request in the Lakeflow pipelines REST API. 
The reset_checkpoint_selection parameter accepts a list of flow names. You must pass each flow name in a fully qualified catalog.schema.flow_name format. Using only the simple name (for example, my_flow instead of my_catalog.my_schema.my_flow ) causes the pipeline update to fail with an IllegalArgumentException . 
If you defined a flow with an explicit name (for example, using the flow_name parameter in create_auto_cdc_flow ), the fully qualified flow name is <catalog>.<schema>.<flow_name> . 
If you did not set an explicit flow name, the default flow name is the fully qualified target table name, in catalog.schema.table format. 
You can find flow names in the pipeline UI or in the pipeline event logs. 
The following example uses the curl command to call the updates request to start a pipeline update: Bash 
curl -X POST \ -H "Authorization: Bearer <your-token>" \ -H "Content-Type: application/json" \ -d '{ "reset_checkpoint_selection": ["my_catalog.my_schema.my_streaming_table"] }' \ https:// < your-databricks-instance > /api/2.0/pipelines/ < your-pipeline-id > /updates 
The following example resets the checkpoint for a flow defined with a custom name: Bash 
curl -X POST \ -H "Authorization: Bearer <your-token>" \ -H "Content-Type: application/json" \ -d '{ "reset_checkpoint_selection": ["my_catalog.my_schema.my_custom_flow_name"] }' \ https:// < your-databricks-instance > /api/2.0/pipelines/ < your-pipeline-id > /updates 
Check a pipeline for errors without waiting for tables to update ​ Preview 
The pipeline Dry run feature is in Public Preview . 
To check whether a pipeline's source code is valid without running a full update, use a dry run . A dry run resolves the definitions of datasets and flows defined in the pipeline but does not materialize or publish any datasets. Errors found during the dry run, such as incorrect table or column names, are reported in the UI. 
To start a dry run, click on the pipeline details page next to Start and click Dry run . 
After the dry run is complete, any errors and incrementalization insights are shown in the event tray in the bottom panel. Clicking the event tray displays any issues found in the bottom panel. Additionally, the event log shows events related only to the dry run, and no metrics are displayed in the pipeline graph. If errors or insights are found, details are available in the event log. 
You can view dry run results in the UI only while the dry run is your pipeline's most recent update. Select it in the update history to view the results. For how long each update type remains available in the UI, see update result availability . 
Update result availability ​ 
Whether an update's results appear in the UI depends on the update type and two conditions: 
Retention window : How long finished updates are kept. Pipelines retain 60 days of past updates. 
Most recent update : Whether the update is the latest one started for the pipeline. 
The following table shows when each update type is available: 

Update type 
Available in the UI while 
Removed from the UI when 

Regular update 
It is within the retention window, or it is still active (has not finished). An active update stays available even if it started before the retention window. 
It has finished and is older than the retention window. 

Dry run 
It is the pipeline's most recent update. 
Any later update starts, whether another dry run or a regular update. ← ✕ 

Update type 
Available in the UI while 
Removed from the UI when 

Regular update 
It is within the retention window, or it is still active (has not finished). An active update stays available even if it started before the retention window. 
It has finished and is older than the retention window. 

Dry run 
It is the pipeline's most recent update. 
Any later update starts, whether another dry run or a regular update. 
In all cases, an update's events remain in the event log after its results are no longer shown in the UI. 
Update run behavior ​ 
The behavior of a pipeline update is determined by how you trigger it: 
Updates for non-continuous pipelines started from the pipeline monitoring UI or the pipeline editor use fast-start, debugging-focused behavior. 
Updates started from Jobs or the Pipelines API, and all updates for continuous pipelines , use automatic retry and restart behavior. This includes continuous pipeline updates started from the pipeline editor. 
For triggered pipelines, you can override the default behavior for a specific run by choosing Run now with different settings from the drop-down in the Lakeflow Pipelines Editor or the pipeline monitoring page. 
Fast-start, debugging-focused behavior ​ 
Used for UI Run now and ad-hoc updates for non-continuous pipelines. These runs optimize for rapid iteration: 
Reuses a cluster to avoid the overhead of restarts. By default, clusters run for two hours. You can change this with the pipelines.clusterShutdown.delay setting in the Configure classic compute for pipelines . 
Disables pipeline retries so you can immediately detect and fix errors. 
Automatic retry and restart behavior ​ 
Used for Jobs, API-triggered updates, and all continuous pipeline updates, including updates started from the pipeline editor. These runs prioritize reliability and cost efficiency: 
Restarts the cluster for specific recoverable errors, including memory leaks and stale credentials. 
Retries execution in the event of specific errors, such as a failure to start a cluster. 
The cluster shuts down immediately after the run completes. note 
Run behavior only controls cluster and pipeline execution. Storage locations and target schemas in the catalog for publishing tables must be configured as part of pipeline settings and are not affected by run behavior. On this page 
What is a pipeline update? 
How are pipeline updates triggered? 
Manually trigger a pipeline update 
Pipeline refresh semantics 
When to use a full refresh 
Start a pipeline update for selected tables 
Start a pipeline update for failed tables 
Start a pipeline update to clear selective streaming flows' checkpoints 
Check a pipeline for errors without waiting for tables to update 
Update result availability 
Update run behavior 
Fast-start, debugging-focused behavior 
Automatic retry and restart behavior Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 