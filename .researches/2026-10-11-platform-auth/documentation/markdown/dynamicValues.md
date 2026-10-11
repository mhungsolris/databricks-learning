# dynamicValues

Source: https://docs.databricks.com/aws/en/jobs/dynamic-value-references
Retrieved: 2026-10-11

Dynamic value references | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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
Lakeflow Jobs 
Parameterization 
Dynamic value references On this page Last updated on Sep 22, 2026 
Dynamic value references 
Dynamic value references describe a collection of variables available when configuring jobs and tasks. Use dynamic value references to configure conditional statements for tasks or to pass information as parameters or arguments. 
Dynamic value references include information such as: 
Configured values for the job, including the job name, task names, and trigger type. 
Generated metadata about the job, including the job ID, the run ID, and the job run start time. 
Information about how many repair attempts a job has made or retries a task has run. 
The result state for a specified task. 
Values configured using job parameters, task parameters, or set using task values. 
To learn how each task type retrieves parameter values, see Access parameter values from a task . 
Use dynamic value references ​ 
Use dynamic value references when configuring jobs or tasks. You cannot directly reference dynamic value references from assets configured using tasks like notebooks, queries, or JARs. Dynamic value references must be defined using parameters or fields that pass context into tasks. 
Dynamic value references use double curly braces ( {{ }} ). When a job or task runs, a string literal replaces the dynamic value reference. For example, if you configure the following key-value pair as a task parameter: 
{"job_run_id": "job_{{job.run_id}}"} 
If your run ID is 550315892394120 , the value for job_run_id evaluates to job_550315892394120 . note 
Contents of the double curly braces are not evaluated as expressions. You cannot run operations or functions in double-curly braces. 
User-provided value identifiers support alphanumeric and underscore characters. Escape keys that contain special characters by surrounding the identifier with backticks ( ` ` ). 
Syntax errors, including non-existent dynamic reference values and missing braces, are silently ignored and treated as literal strings. However, if you provide a reference that belongs to a known namespace but is not valid, for example, {{job.notebook_url}} , an error message is displayed. 
Use dynamic value references in the jobs UI ​ 
Fields that accept dynamic value references provide a shortcut to insert available dynamic value references. Click { } to see this list and insert it into the provided field. note 
The UI does not auto-complete the keys to reference task values. 
Many fields that accept dynamic value references require additional formatting to use them correctly. See Configure task parameters . 
Use dynamic value references in a job JSON ​ 
Use {{ }} syntax to use dynamic values in job JSON definitions used by the Databricks CLI and REST API. 
Job and task parameters have different syntax, and task parameter syntax varies by task type. 
The following example shows the partial JSON syntax to configure job parameters using dynamic value references: JSON 
{ "parameters" : [ { "name" : "my_job_id" , "default" : "{{job.id}}" } , { "name" : "run_date" , "default" : "{{job.start_time.iso_date}}" } ] } 
The following example shows the partial JSON syntax to configure notebook task parameters using a dynamic value reference: JSON 
{ "notebook_task" : { "base_parameters" : { "workspace_id" : "workspace_{{workspace.id}}" , "file_arrival_location" : "{{job.trigger.file_arrival.location}}" } } } 
Review parameters for a job run ​ 
After a task completes, you can see resolved parameter values under Parameters on the run details page. See View job run details . 
Supported value references ​ 
The following dynamic value references are supported: 

Reference 
Description 

{{job.id}} 
The unique identifier assigned to the job. 

{{job.name}} 
The name of the job at the time of the job run. 

{{job.run_id}} 
The unique identifier assigned to the job run. 

{{job.repair_count}} 
The number of repair attempts on the current job run. 

{{job.start_time.<argument>}} 
A value based on the time (in UTC timezone) that the job run started. The return value is based on the argument option. See Options for date and time values . 

{{job.parameters.<name>}} 
The value of the job-level parameter with the key <name> . 

{{job.trigger.type}} 
The trigger type of the job run. The possible values are periodic , one_time , run_job_task , file_arrival , continuous , table , and model . 

{{job.trigger.file_arrival.location}} 
If a file arrival trigger is configured for this job, the value of the storage location. 

{{job.trigger.table_update.updated_tables}} 
If a table update trigger is configured for this job, a JSON list of tables updated since the last job run in <catalog>.<schema>.<table> format. 

{{job.trigger.table_update.`<catalog.schema.table>`.commit_timestamp.iso_datetime}} 
If a table update trigger is configured for this job, the most recent commit timestamp that triggered the job run. If only one table is monitored, you can omit the table name: {{job.trigger.table_update.commit_timestamp.iso_datetime}} . 

{{job.trigger.table_update.`<catalog.schema.table>`.version}} 
If a table update trigger is configured for this job, the most recent commit version that triggered the job run. If only one table is monitored, you can omit the table name: {{job.trigger.table_update.version}} . 

{{job.trigger.model.updates}} 
If a model update trigger is configured for this job, a JSON list of the model updates since the last job run. Each entry includes the model name. Depending on the trigger condition, entries might also include the version and alias name. 

{{job.trigger.time.<argument>}} 
A value based on the time (in UTC timezone) that the job run was triggered, rounded down to the closest minute for jobs with a cron schedule. The return value is based on the argument option. See Options for date and time values . 

{{task.name}} 
The name of the current task. 

{{task.run_id}} 
The unique identifier of the current task run. 

{{task.execution_count}} 
The number of times the current task was run (including retries and repairs). 

{{task.notebook_path}} 
The notebook path of the current notebook task. 

{{tasks.<task_name>.run_id}} 
The unique identifier assigned to the task run for <task_name> . 

{{tasks.<task_name>.output.catalog_name}} 
The output catalog name for an upstream clean room task. 

{{tasks.<task_name>.output.schema_name}} 
The output schema name for an upstream clean room task. This schema stores all output from the clean room task run. 

{{tasks.<task_name>.result_state}} 
The result state of task <task_name> . The possible values are success , failed , excluded , canceled , evicted , timedout , upstream_canceled , upstream_evicted , and upstream_failed . 

{{tasks.<task_name>.error_code}} 
The error code for task <task_name> if an error occurred running the task. Examples of possible values are RunExecutionError , ResourceNotFound , and UnauthorizedError . For successful tasks, this evaluates to an empty string. 

{{tasks.<task_name>.execution_count}} 
The number of times the task <task_name> was run (including retries and repairs). 

{{tasks.<task_name>.notebook_path}} 
The path to the notebook for the notebook task <task_name> . 

{{tasks.<task_name>.values.<value_name>}} 
The task value with the key <value_name> that was set by task <task_name> . When <task_name> ran inside a For each task, this resolves to a JSON array of the value that each iteration set, ordered by iteration index. See Read values from a For each task's iterations . 

{{tasks.<task_name>.output.rows}} 
The output rows of an upstream SQL task <task_name> . If passed as the Inputs for a For each task, each row is sent iteratively to the nested task. SQL output is limited to 1,000 rows, and 48 KB in size. See SQL output options . 

{{tasks.<task_name>.output.first_row}} 
The first row of the output of an upstream SQL task <task_name> . SQL output is limited to 1,000 rows and 48 KB in size. 

{{tasks.<task_name>.output.first_row.<column_alias>}} 
The value of the column <column_alias> in the first row of the output of an upstream SQL task <task_name> . SQL output is limited to 1,000 rows and 48 KB in size. 

{{tasks.<task_name>.output.alert_state}} 
The state of an upstream SQL alert task. The value is one of UNKNOWN , OK , or TRIGGERED . 

{{workspace.id}} 
The unique identifier assigned to the workspace. 

{{workspace.url}} 
The URL of the workspace. 

{{backfill.day}} 
The day part of the start of the time range for the specific backfill job run. See Backfill jobs . 

{{backfill.is_weekday}} 
Returns true if the start of the time range for the specific backfill job run is a weekday. 

{{backfill.iso_date}} 
The iso date of the start of the time range for the specific backfill job run. 

{{backfill.iso_datetime}} 
The iso datetime of the start of the time range for the specific backfill job run. 

{{backfill.iso_weekday}} 
Returns a digit from 1 to 7, representing the day of the week of the start of the time range for the specific backfill job run. 

{{backfill.month}} 
The month part of the start of the time range for the specific backfill job run. 

{{backfill.timestamp_ms}} 
The timestamp of the start of the time range for the specific backfill job run. 

{{backfill.year}} 
The year part of the start of the time range for the specific backfill job run. ← ✕ 

Reference 
Description 

{{job.id}} 
The unique identifier assigned to the job. 

{{job.name}} 
The name of the job at the time of the job run. 

{{job.run_id}} 
The unique identifier assigned to the job run. 

{{job.repair_count}} 
The number of repair attempts on the current job run. 

{{job.start_time.<argument>}} 
A value based on the time (in UTC timezone) that the job run started. The return value is based on the argument option. See Options for date and time values . 

{{job.parameters.<name>}} 
The value of the job-level parameter with the key <name> . 

{{job.trigger.type}} 
The trigger type of the job run. The possible values are periodic , one_time , run_job_task , file_arrival , continuous , table , and model . 

{{job.trigger.file_arrival.location}} 
If a file arrival trigger is configured for this job, the value of the storage location. 

{{job.trigger.table_update.updated_tables}} 
If a table update trigger is configured for this job, a JSON list of tables updated since the last job run in <catalog>.<schema>.<table> format. 

{{job.trigger.table_update.`<catalog.schema.table>`.commit_timestamp.iso_datetime}} 
If a table update trigger is configured for this job, the most recent commit timestamp that triggered the job run. If only one table is monitored, you can omit the table name: {{job.trigger.table_update.commit_timestamp.iso_datetime}} . 

{{job.trigger.table_update.`<catalog.schema.table>`.version}} 
If a table update trigger is configured for this job, the most recent commit version that triggered the job run. If only one table is monitored, you can omit the table name: {{job.trigger.table_update.version}} . 

{{job.trigger.model.updates}} 
If a model update trigger is configured for this job, a JSON list of the model updates since the last job run. Each entry includes the model name. Depending on the trigger condition, entries might also include the version and alias name. 

{{job.trigger.time.<argument>}} 
A value based on the time (in UTC timezone) that the job run was triggered, rounded down to the closest minute for jobs with a cron schedule. The return value is based on the argument option. See Options for date and time values . 

{{task.name}} 
The name of the current task. 

{{task.run_id}} 
The unique identifier of the current task run. 

{{task.execution_count}} 
The number of times the current task was run (including retries and repairs). 

{{task.notebook_path}} 
The notebook path of the current notebook task. 

{{tasks.<task_name>.run_id}} 
The unique identifier assigned to the task run for <task_name> . 

{{tasks.<task_name>.output.catalog_name}} 
The output catalog name for an upstream clean room task. 

{{tasks.<task_name>.output.schema_name}} 
The output schema name for an upstream clean room task. This schema stores all output from the clean room task run. 

{{tasks.<task_name>.result_state}} 
The result state of task <task_name> . The possible values are success , failed , excluded , canceled , evicted , timedout , upstream_canceled , upstream_evicted , and upstream_failed . 

{{tasks.<task_name>.error_code}} 
The error code for task <task_name> if an error occurred running the task. Examples of possible values are RunExecutionError , ResourceNotFound , and UnauthorizedError . For successful tasks, this evaluates to an empty string. 

{{tasks.<task_name>.execution_count}} 
The number of times the task <task_name> was run (including retries and repairs). 

{{tasks.<task_name>.notebook_path}} 
The path to the notebook for the notebook task <task_name> . 

{{tasks.<task_name>.values.<value_name>}} 
The task value with the key <value_name> that was set by task <task_name> . When <task_name> ran inside a For each task, this resolves to a JSON array of the value that each iteration set, ordered by iteration index. See Read values from a For each task's iterations . 

{{tasks.<task_name>.output.rows}} 
The output rows of an upstream SQL task <task_name> . If passed as the Inputs for a For each task, each row is sent iteratively to the nested task. SQL output is limited to 1,000 rows, and 48 KB in size. See SQL output options . 

{{tasks.<task_name>.output.first_row}} 
The first row of the output of an upstream SQL task <task_name> . SQL output is limited to 1,000 rows and 48 KB in size. 

{{tasks.<task_name>.output.first_row.<column_alias>}} 
The value of the column <column_alias> in the first row of the output of an upstream SQL task <task_name> . SQL output is limited to 1,000 rows and 48 KB in size. 

{{tasks.<task_name>.output.alert_state}} 
The state of an upstream SQL alert task. The value is one of UNKNOWN , OK , or TRIGGERED . 

{{workspace.id}} 
The unique identifier assigned to the workspace. 

{{workspace.url}} 
The URL of the workspace. 

{{backfill.day}} 
The day part of the start of the time range for the specific backfill job run. See Backfill jobs . 

{{backfill.is_weekday}} 
Returns true if the start of the time range for the specific backfill job run is a weekday. 

{{backfill.iso_date}} 
The iso date of the start of the time range for the specific backfill job run. 

{{backfill.iso_datetime}} 
The iso datetime of the start of the time range for the specific backfill job run. 

{{backfill.iso_weekday}} 
Returns a digit from 1 to 7, representing the day of the week of the start of the time range for the specific backfill job run. 

{{backfill.month}} 
The month part of the start of the time range for the specific backfill job run. 

{{backfill.timestamp_ms}} 
The timestamp of the start of the time range for the specific backfill job run. 

{{backfill.year}} 
The year part of the start of the time range for the specific backfill job run. 
You can set these references with any task. See Configure task parameters . Backfill parameters are only available when creating a backfill job . 
You can also pass parameters between tasks in a job with task values . See Use task values to pass information between tasks . 
Options for date and time values ​ 
Use the following arguments to specify the return value from time-based parameter variables. All return values are based on a timestamp in the UTC timezone. 

Argument 
Description 

iso_weekday 
Returns a digit from 1 to 7, representing the day of the week of the timestamp. 

is_weekday 
Returns true if the timestamp is on a weekday. 

iso_date 
Returns the date in ISO format. 

iso_datetime 
Returns the date and time in ISO format. 

year 
Returns the year part of the timestamp. 

month 
Returns the month part of the timestamp. 

day 
Returns the day part of the timestamp. 

hour 
Returns the hour part of the timestamp. 

minute 
Returns the minute part of the timestamp. 

second 
Returns the second part of the timestamp. 

timestamp_ms 
Returns the timestamp in milliseconds. ← ✕ 

Argument 
Description 

iso_weekday 
Returns a digit from 1 to 7, representing the day of the week of the timestamp. 

is_weekday 
Returns true if the timestamp is on a weekday. 

iso_date 
Returns the date in ISO format. 

iso_datetime 
Returns the date and time in ISO format. 

year 
Returns the year part of the timestamp. 

month 
Returns the month part of the timestamp. 

day 
Returns the day part of the timestamp. 

hour 
Returns the hour part of the timestamp. 

minute 
Returns the minute part of the timestamp. 

second 
Returns the second part of the timestamp. 

timestamp_ms 
Returns the timestamp in milliseconds. 
SQL output options ​ 
You can access the output of an upstream SQL task using dynamic values. 
For example, if you have a SQL task called sales_by_year with the following SQL, it creates output based on the final SELECT statement. SQL 
-- Generate example data CREATE OR REPLACE TEMP VIEW example_sales AS SELECT * FROM VALUES ( 2020 , 12 ) , ( 2021 , 23 ) , ( 2022 , 47 ) , ( 2023 , 15 ) , ( 2024 , 22 ) AS example_sales ( sales_year , num_sales ) ; -- Query example data SELECT sales_year , num_sales FROM example_sales ; 
You can reference the output in a downstream task by creating task configuration using a {{tasks.<task_name>.output.<argument>}} dynamic value. 
In For each tasks, the rows are sent iteratively to the nested task. In this example, if you were to set the Inputs of a For each task to {{tasks.sales_by_year.output.rows}} , then in the nested task, you can use the syntax {{input.<column_alias>}} to iteratively send the row values as parameters. In the nested task configuration, you could create two parameters with the key-value pairs year : {{input.sales_year}} , and sales : {{input.num_sales}} . Assuming the nested task is a SQL task, you could reference the values in your code with a query such as the following. SQL 
-- Example: access data from previous query: SELECT concat ( 'In ' , : year , ' we had ' , :sales , ' sales.' ) 
For more information about For each tasks and their nested tasks, see Use a For each task to run another task in a loop . note 
The SQL query output is retained for 7 days. If the job is paused (for example, on failure), then resumed more than 7 days later, the SQL query output is not available. 
Deprecated dynamic value references ​ 
The following dynamic value references are deprecated. The recommended replacement reference is included in the description of each variable. 

Variable 
Description 

{{job_id}} 
The unique identifier assigned to a job. Use job.id instead. 

{{run_id}} 
The unique identifier assigned to a task run. Use task.run_id instead. 

{{start_date}} 
The date a task run started. The format is YYYY-MM-DD in the UTC timezone. Use job.start_time.<argument> instead. 

{{start_time}} 
The timestamp of the run's start of execution after the cluster is created and ready. The format is milliseconds since UNIX epoch in the UTC timezone, as returned by System.currentTimeMillis() . Use job.start_time.<format> instead. 

{{task_retry_count}} 
The number of retries attempted to run a task if the first attempt fails. The value is 0 for the first attempt and increments with each retry. Use task.execution_count instead. 

{{parent_run_id}} 
The unique identifier assigned to the run of a job with multiple tasks. Use job.run_id instead. 

{{task_key}} 
The unique name assigned to a task that's part of a job with multiple tasks. Use task.name instead. ← ✕ 

Variable 
Description 

{{job_id}} 
The unique identifier assigned to a job. Use job.id instead. 

{{run_id}} 
The unique identifier assigned to a task run. Use task.run_id instead. 

{{start_date}} 
The date a task run started. The format is YYYY-MM-DD in the UTC timezone. Use job.start_time.<argument> instead. 

{{start_time}} 
The timestamp of the run's start of execution after the cluster is created and ready. The format is milliseconds since UNIX epoch in the UTC timezone, as returned by System.currentTimeMillis() . Use job.start_time.<format> instead. 

{{task_retry_count}} 
The number of retries attempted to run a task if the first attempt fails. The value is 0 for the first attempt and increments with each retry. Use task.execution_count instead. 

{{parent_run_id}} 
The unique identifier assigned to the run of a job with multiple tasks. Use job.run_id instead. 

{{task_key}} 
The unique name assigned to a task that's part of a job with multiple tasks. Use task.name instead. On this page 
Use dynamic value references 
Use dynamic value references in the jobs UI 
Use dynamic value references in a job JSON 
Review parameters for a job run 
Supported value references 
Options for date and time values 
SQL output options 
Deprecated dynamic value references Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 