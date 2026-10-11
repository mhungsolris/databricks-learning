# jobs

Source: https://docs.databricks.com/aws/en/admin/system-tables/jobs
Retrieved: 2026-10-11

Jobs system table reference | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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
System tables 
Compute & workloads 
Jobs system table reference On this page Last updated on Oct 9, 2026 
Jobs system table reference note 
The lakeflow schema was previously known as workflow . The content of both schemas is identical. 
This article is a reference for the lakeflow system tables, which record job activity in your account. These tables include records from all workspaces in your account deployed in the same cloud region. To see records from another region, you must view the tables from a workspace deployed in that region. 
Requirements ​ 
To access these system tables, users must either: 
Be both a metastore admin and an account admin, or 
Have USE and SELECT permissions on the system schemas. See Grant access to system tables . 
Available jobs tables ​ 
All job-related system tables live in the system.lakeflow schema. Currently, the schema hosts six tables: 

Table 
Description 
Supports streaming 
Free retention period 
Includes global or regional data 

jobs 
Tracks all jobs created in the account 
Yes 
365 days 
Regional 

job_tasks 
Tracks all job tasks that run in the account 
Yes 
365 days 
Regional 

job_run_timeline 
Tracks the job runs and related metadata 
Yes 
365 days 
Regional 

job_task_run_timeline 
Tracks job task runs and related metadata 
Yes 
365 days 
Regional 

pipelines 
Tracks all pipelines created in the account 
Yes 
365 days 
Regional 

pipeline_update_timeline 
Tracks the pipeline updates and related metadata 
Yes 
365 days 
Regional ← ✕ 

Table 
Description 
Supports streaming 
Free retention period 
Includes global or regional data 

jobs 
Tracks all jobs created in the account 
Yes 
365 days 
Regional 

job_tasks 
Tracks all job tasks that run in the account 
Yes 
365 days 
Regional 

job_run_timeline 
Tracks the job runs and related metadata 
Yes 
365 days 
Regional 

job_task_run_timeline 
Tracks job task runs and related metadata 
Yes 
365 days 
Regional 

pipelines 
Tracks all pipelines created in the account 
Yes 
365 days 
Regional 

pipeline_update_timeline 
Tracks the pipeline updates and related metadata 
Yes 
365 days 
Regional note 
In addition to the 365-day retention window, Databricks retains the most recent record for each entity in the slowly changing dimension (SCD2) tables ( jobs , job_tasks , and pipelines ). This means the latest historical entry for each job_id , job_task , or pipeline_id is always available, even if it is older than 365 days. Records beyond the 365-day window other than the latest entry per entity are removed. 
Record availability ​ 
For the jobs , job_tasks , job_run_timeline , and job_task_run_timeline tables, records are typically available within one hour. Data delivery for new workspaces can take longer than this. note 
For the job_run_timeline and job_task_run_timeline tables, availability is measured from the period_end_time column. See timeline slicing logic . 
Detailed schema reference ​ 
The following sections provide schema references for each of the jobs-related system tables. 
Query an SCD2 table ​ 
Several system tables are slowly changing dimension tables (SCD2), including jobs , job_tasks , and pipelines . When a row changes, a new row is emitted with the updated values, so the table holds the full history of every entity. Deletions are recorded as a new row with delete_time populated, not by removing rows. 
To find the current state of an entity in an SCD2 table, take the row with the most recent change_time , then exclude the rows that record a deletion: SQL 
-- Get the current state of every job, excluding deleted jobs with latest AS ( SELECT * , ROW_NUMBER ( ) OVER ( PARTITION BY workspace_id , job_id ORDER BY change_time DESC ) as rn FROM system . lakeflow . jobs QUALIFY rn = 1 ) SELECT * FROM latest WHERE delete_time IS NULL 
Apply the delete_time filter after selecting the most recent row, as in the preceding example. Filtering delete_time in the same query that reads the table returns each deleted entity's last state before deletion instead of omitting the entity. 
To adapt the query to another SCD2 table, replace the table name and partition by that table's entity key. For the tables on this page: 
jobs : workspace_id , job_id 
job_tasks : workspace_id , job_id , task_key 
pipelines : workspace_id , pipeline_id 
The job run timeline, job task run timeline, and pipeline update timeline tables are immutable, so they need no deduplication. 
Jobs table schema ​ 
The jobs table is a slowly changing dimension table (SCD2). When a row changes, a new row is emitted with the updated values, so the table contains the full history of each job. See Query an SCD2 table . 
Table path : system.lakeflow.jobs 

Column name 
Data type 
Description 
Notes 

account_id 
string 
The ID of the account this job belongs to 

workspace_id 
string 
The ID of the workspace this job belongs to 

job_id 
string 
The ID of the job 
Only unique within a single workspace 

name 
string 
The user-supplied name of the job 

description 
string 
The user-supplied description of the job 
This field is empty if you have customer-managed keys configured. 

creator_id 
string 
The ID of the principal who created the job 

tags 
map 
The user-supplied custom tags associated with this job 

change_time 
timestamp 
The time when the job was last modified 
Timezone recorded as +00:00 (UTC) 

delete_time 
timestamp 
The time when the job was deleted by the user 
Timezone recorded as +00:00 (UTC) 

run_as 
string 
The ID of the user or service principal whose permissions are used for the job run 

trigger 
struct 
The trigger configuration for the job 
NULL when a job has more than one trigger. See triggers for the complete set. Not populated for rows emitted before early December 2025. 

trigger_type 
string 
The type of trigger for the job 
MULTIPLE indicates the job has more than one trigger. Not populated for rows emitted before early December 2025. 

triggers 
array 
The full set of all trigger configurations for the job, each with the same structure as trigger . 
Populated for all jobs with triggers. When a job has multiple triggers, this column includes the only complete view of all trigger configurations. 

run_as_user_name 
string 
The email of the user, the ID of the service principal, or group name whose permissions are used for the job run 
Not populated for rows emitted before early December 2025 

creator_user_name 
string 
The email of the user, the ID of the service principal, or group name who created the job 
Not populated for rows emitted before early December 2025 

paused 
boolean 
Indicates whether the job is paused 
Not populated for rows emitted before early December 2025 

timeout_seconds 
long 
The timeout duration for the job in seconds 
Not populated for rows emitted before early December 2025 

health_rules 
array 
Set of health rules defined for this job 
Not populated for rows emitted before early December 2025 

deployment 
struct 
Deployment information for jobs managed by external sources 
Not populated for rows emitted before early December 2025 

create_time 
timestamp 
The time at which this job was created. Timezone recorded as +00:00 (UTC). 
Not populated for rows emitted before early December 2025 ← ✕ 

Column name 
Data type 
Description 
Notes 

account_id 
string 
The ID of the account this job belongs to 

workspace_id 
string 
The ID of the workspace this job belongs to 

job_id 
string 
The ID of the job 
Only unique within a single workspace 

name 
string 
The user-supplied name of the job 

description 
string 
The user-supplied description of the job 
This field is empty if you have customer-managed keys configured. 

creator_id 
string 
The ID of the principal who created the job 

tags 
map 
The user-supplied custom tags associated with this job 

change_time 
timestamp 
The time when the job was last modified 
Timezone recorded as +00:00 (UTC) 

delete_time 
timestamp 
The time when the job was deleted by the user 
Timezone recorded as +00:00 (UTC) 

run_as 
string 
The ID of the user or service principal whose permissions are used for the job run 

trigger 
struct 
The trigger configuration for the job 
NULL when a job has more than one trigger. See triggers for the complete set. Not populated for rows emitted before early December 2025. 

trigger_type 
string 
The type of trigger for the job 
MULTIPLE indicates the job has more than one trigger. Not populated for rows emitted before early December 2025. 

triggers 
array 
The full set of all trigger configurations for the job, each with the same structure as trigger . 
Populated for all jobs with triggers. When a job has multiple triggers, this column includes the only complete view of all trigger configurations. 

run_as_user_name 
string 
The email of the user, the ID of the service principal, or group name whose permissions are used for the job run 
Not populated for rows emitted before early December 2025 

creator_user_name 
string 
The email of the user, the ID of the service principal, or group name who created the job 
Not populated for rows emitted before early December 2025 

paused 
boolean 
Indicates whether the job is paused 
Not populated for rows emitted before early December 2025 

timeout_seconds 
long 
The timeout duration for the job in seconds 
Not populated for rows emitted before early December 2025 

health_rules 
array 
Set of health rules defined for this job 
Not populated for rows emitted before early December 2025 

deployment 
struct 
Deployment information for jobs managed by external sources 
Not populated for rows emitted before early December 2025 

create_time 
timestamp 
The time at which this job was created. Timezone recorded as +00:00 (UTC). 
Not populated for rows emitted before early December 2025 Example query ​ SQL 
-- Get the most recent version of a job SELECT * , ROW_NUMBER ( ) OVER ( PARTITION BY workspace_id , job_id ORDER BY change_time DESC ) as rn FROM system . lakeflow . jobs QUALIFY rn = 1 
To return one row per trigger, including jobs with multiple triggers, expand the triggers array: SQL 
SELECT workspace_id , job_id , trigger . * FROM ( SELECT * , ROW_NUMBER ( ) OVER ( PARTITION BY workspace_id , job_id ORDER BY change_time DESC ) as rn FROM system . lakeflow . jobs QUALIFY rn = 1 ) LATERAL VIEW EXPLODE ( triggers ) AS trigger 
Job task table schema ​ 
The job_tasks table is a slowly changing dimension table (SCD2). When a row changes, a new row is emitted with the updated values, so the table contains the full history of each job task. See Query an SCD2 table . 
Table path : system.lakeflow.job_tasks 

Column name 
Data type 
Description 
Notes 

account_id 
string 
The ID of the account this job belongs to 

workspace_id 
string 
The ID of the workspace this job belongs to 

job_id 
string 
The ID of the job 
Only unique within a single workspace 

task_key 
string 
The reference key for a task in a job 
Only unique within a single job 

depends_on_keys 
array 
The task keys of all upstream dependencies of this task 

change_time 
timestamp 
The time when the task was last modified 
Timezone recorded as +00:00 (UTC) 

delete_time 
timestamp 
The time when a task was deleted by the user 
Timezone recorded as +00:00 (UTC) 

timeout_seconds 
long 
The timeout duration for the task in seconds 
Not populated for rows emitted before early December 2025 

health_rules 
array 
Set of health rules defined for this job task 
Not populated for rows emitted before early December 2025 ← ✕ 

Column name 
Data type 
Description 
Notes 

account_id 
string 
The ID of the account this job belongs to 

workspace_id 
string 
The ID of the workspace this job belongs to 

job_id 
string 
The ID of the job 
Only unique within a single workspace 

task_key 
string 
The reference key for a task in a job 
Only unique within a single job 

depends_on_keys 
array 
The task keys of all upstream dependencies of this task 

change_time 
timestamp 
The time when the task was last modified 
Timezone recorded as +00:00 (UTC) 

delete_time 
timestamp 
The time when a task was deleted by the user 
Timezone recorded as +00:00 (UTC) 

timeout_seconds 
long 
The timeout duration for the task in seconds 
Not populated for rows emitted before early December 2025 

health_rules 
array 
Set of health rules defined for this job task 
Not populated for rows emitted before early December 2025 Example query ​ SQL 
-- Get the most recent version of each job task SELECT * , ROW_NUMBER ( ) OVER ( PARTITION BY workspace_id , job_id , task_key ORDER BY change_time DESC ) as rn FROM system . lakeflow . job_tasks QUALIFY rn = 1 
Job run timeline table schema ​ 
The job run timeline table is immutable and complete at the time it is produced. 
Table path : system.lakeflow.job_run_timeline 

Column name 
Data type 
Description 
Notes 

account_id 
string 
The ID of the account this job belongs to 

workspace_id 
string 
The ID of the workspace this job belongs to 

job_id 
string 
The ID of the job 
This key is only unique within a single workspace 

run_id 
string 
The ID of the job run 

period_start_time 
timestamp 
The start time for the run or for the time period 
Timezone information is recorded at the end of the value with +00:00 representing UTC. For details on how Databricks slices long runs into hourly intervals, see timeline slicing logic . 

period_end_time 
timestamp 
The end time for the run or for the time period 
Timezone information is recorded at the end of the value with +00:00 representing UTC. For details on how Databricks slices long runs into hourly intervals, see timeline slicing logic . 

trigger_type 
string 
The type of trigger that can fire a run 
For possible values, see Trigger type values 

run_type 
string 
The type of job run 
For possible values, see Run type values 

run_name 
string 
The user-supplied run name associated with this job run 

compute_ids 
array 
Array containing the job compute IDs for the parent job run 
Use for identifying the job cluster used by WORKFLOW_RUN run types. For other compute information, refer to the job_task_run_timeline table. 

result_state 
string 
The outcome of the job run 
For runs longer than one hour that are split across multiple rows, this column is populated only in the row that represents the end of the run. For possible values, see Result state values . 

termination_code 
string 
The termination code of the job run 
For runs longer than one hour that are split across multiple rows, this column is populated only in the row that represents the end of the run. For possible values, see Termination code values . 

job_parameters 
map 
The job-level parameters used in the job run 
Contains only the values from job_parameters . Deprecated parameter fields ( notebook_params , python_params , python_named_params , spark_submit_params , and sql_params ) are not included. 

source_task_run_id 
string 
The ID of the source task run. Use this column to identify which task run triggered this job run. 
Not populated for rows emitted before early December 2025 

root_task_run_id 
string 
The ID of the root task run. Use this column to identify which task run triggered this job run. 
Not populated for rows emitted before early December 2025 

compute 
array 
Details about the compute resources used in the job run 
Not populated for rows emitted before early December 2025 

termination_type 
string 
The type of termination for the job run 
Not populated for rows emitted before early December 2025 

setup_duration_seconds 
long 
The duration of the setup phase for the job run in seconds 
Not populated for rows emitted before early December 2025 

queue_duration_seconds 
long 
The duration spent in the queue for the job run in seconds 
Not populated for rows emitted before early December 2025 

run_duration_seconds 
long 
The total duration of the job run in seconds 
Not populated for rows emitted before early December 2025 

cleanup_duration_seconds 
long 
The duration of the cleanup phase for the job run in seconds 
Not populated for rows emitted before early December 2025 

execution_duration_seconds 
long 
The duration of the execution phase for the job run in seconds 
Not populated for rows emitted before early December 2025 ← ✕ 

Column name 
Data type 
Description 
Notes 

account_id 
string 
The ID of the account this job belongs to 

workspace_id 
string 
The ID of the workspace this job belongs to 

job_id 
string 
The ID of the job 
This key is only unique within a single workspace 

run_id 
string 
The ID of the job run 

period_start_time 
timestamp 
The start time for the run or for the time period 
Timezone information is recorded at the end of the value with +00:00 representing UTC. For details on how Databricks slices long runs into hourly intervals, see timeline slicing logic . 

period_end_time 
timestamp 
The end time for the run or for the time period 
Timezone information is recorded at the end of the value with +00:00 representing UTC. For details on how Databricks slices long runs into hourly intervals, see timeline slicing logic . 

trigger_type 
string 
The type of trigger that can fire a run 
For possible values, see Trigger type values 

run_type 
string 
The type of job run 
For possible values, see Run type values 

run_name 
string 
The user-supplied run name associated with this job run 

compute_ids 
array 
Array containing the job compute IDs for the parent job run 
Use for identifying the job cluster used by WORKFLOW_RUN run types. For other compute information, refer to the job_task_run_timeline table. 

result_state 
string 
The outcome of the job run 
For runs longer than one hour that are split across multiple rows, this column is populated only in the row that represents the end of the run. For possible values, see Result state values . 

termination_code 
string 
The termination code of the job run 
For runs longer than one hour that are split across multiple rows, this column is populated only in the row that represents the end of the run. For possible values, see Termination code values . 

job_parameters 
map 
The job-level parameters used in the job run 
Contains only the values from job_parameters . Deprecated parameter fields ( notebook_params , python_params , python_named_params , spark_submit_params , and sql_params ) are not included. 

source_task_run_id 
string 
The ID of the source task run. Use this column to identify which task run triggered this job run. 
Not populated for rows emitted before early December 2025 

root_task_run_id 
string 
The ID of the root task run. Use this column to identify which task run triggered this job run. 
Not populated for rows emitted before early December 2025 

compute 
array 
Details about the compute resources used in the job run 
Not populated for rows emitted before early December 2025 

termination_type 
string 
The type of termination for the job run 
Not populated for rows emitted before early December 2025 

setup_duration_seconds 
long 
The duration of the setup phase for the job run in seconds 
Not populated for rows emitted before early December 2025 

queue_duration_seconds 
long 
The duration spent in the queue for the job run in seconds 
Not populated for rows emitted before early December 2025 

run_duration_seconds 
long 
The total duration of the job run in seconds 
Not populated for rows emitted before early December 2025 

cleanup_duration_seconds 
long 
The duration of the cleanup phase for the job run in seconds 
Not populated for rows emitted before early December 2025 

execution_duration_seconds 
long 
The duration of the execution phase for the job run in seconds 
Not populated for rows emitted before early December 2025 note 
The duration columns in the job_run_timeline table ( setup_duration_seconds , queue_duration_seconds , run_duration_seconds , cleanup_duration_seconds , and execution_duration_seconds ) are only populated for single-task jobs that were created using the legacy Jobs APIs (for example, /api/2.0/jobs/create ). For non-legacy or multi-task job runs, these columns log a value of 0 . 
For all non-legacy or multi-task job runs, use the job_task_run_timeline table, which reports durations per task run. Example query ​ SQL 
-- This query gets the daily job count for a workspace for the last 7 days: SELECT workspace_id , COUNT ( DISTINCT run_id ) as job_count , to_date ( period_start_time ) as date FROM system . lakeflow . job_run_timeline WHERE period_start_time > CURRENT_TIMESTAMP ( ) - INTERVAL 7 DAYS GROUP BY ALL -- This query returns the daily job count for a workspace for the last 7 days, distributed by the outcome of the job run. SELECT workspace_id , COUNT ( DISTINCT run_id ) as job_count , result_state , to_date ( period_start_time ) as date FROM system . lakeflow . job_run_timeline WHERE period_start_time > CURRENT_TIMESTAMP ( ) - INTERVAL 7 DAYS AND result_state IS NOT NULL GROUP BY ALL -- This query returns the average time of job runs, measured in seconds. The records are organized by job. A top 90 and a 95 percentile column show the average lengths of the job's longest runs. with job_run_duration as ( SELECT workspace_id , job_id , run_id , CAST ( SUM ( period_end_time - period_start_time ) AS LONG ) as duration FROM system . lakeflow . job_run_timeline WHERE period_start_time > CURRENT_TIMESTAMP ( ) - INTERVAL 7 DAYS GROUP BY ALL ) SELECT t1 . workspace_id , t1 . job_id , COUNT ( DISTINCT t1 . run_id ) as runs , MEAN ( t1 . duration ) as mean_seconds , AVG ( t1 . duration ) as avg_seconds , PERCENTILE ( t1 . duration , 0.9 ) as p90_seconds , PERCENTILE ( t1 . duration , 0.95 ) as p95_seconds FROM job_run_duration t1 GROUP BY ALL ORDER BY mean_seconds DESC LIMIT 100 -- This query provides a historical runtime for a specific job based on the `run_name` parameter. For the query to work, you must set the `run_name`. SELECT workspace_id , run_id , SUM ( period_end_time - period_start_time ) as run_time FROM system . lakeflow . job_run_timeline WHERE run_type = "SUBMIT_RUN" AND run_name = :run_name AND period_start_time > CURRENT_TIMESTAMP ( ) - INTERVAL 60 DAYS GROUP BY ALL -- This query collects a list of retried job runs with the number of retries for each run. with repaired_runs as ( SELECT workspace_id , job_id , run_id , COUNT ( * ) - 1 as retries_count FROM system . lakeflow . job_run_timeline WHERE result_state IS NOT NULL GROUP BY ALL HAVING retries_count > 0 ) SELECT * FROM repaired_runs ORDER BY retries_count DESC LIMIT 10 ; 
Job task run timeline table schema ​ 
The job task run timeline table is immutable and complete at the time it is produced. 
Table path : system.lakeflow.job_task_run_timeline 

Column name 
Data type 
Description 
Notes 

account_id 
string 
The ID of the account this job belongs to 

workspace_id 
string 
The ID of the workspace this job belongs to 

job_id 
string 
The ID of the job 
Only unique within a single workspace 

run_id 
string 
The ID of the task run 

job_run_id 
string 
The ID of the job run 

parent_run_id 
string 
The ID of the parent run 

period_start_time 
timestamp 
The start time for the task or for the time period 
Timezone information is recorded at the end of the value with +00:00 representing UTC. For details on how Databricks slices long runs into hourly intervals, see timeline slicing logic . 

period_end_time 
timestamp 
The end time for the task or for the time period 
Timezone information is recorded at the end of the value with +00:00 representing UTC. For details on how Databricks slices long runs into hourly intervals, see timeline slicing logic . 

task_key 
string 
The reference key for a task in a job 
This key is only unique within a single job 

compute_ids 
array 
The compute_ids array contains IDs of job clusters, interactive clusters, and SQL warehouses used by the job task 

result_state 
string 
The outcome of the job task run 
For task runs longer than one hour that are split across multiple rows, this column is populated only in the row that represents the end of the run. For possible values, see Result state values . 

termination_code 
string 
The termination code of the task run 
For task runs longer than one hour that are split across multiple rows, this column is populated only in the row that represents the end of the run. For possible values, see Termination code values . 

compute 
array 
Details about the compute resources used in the job task run 
Not populated for rows emitted before early December 2025 

termination_type 
string 
The type of termination for the job task run 
Not populated for rows emitted before early December 2025 

task_parameters 
map 
The task-level parameters used in the job task run 
Contains only the values from job_parameters . Deprecated parameter fields ( notebook_params , python_params , python_named_params , spark_submit_params , and sql_params ) are not included. Not populated for rows emitted before early December 2025. 

setup_duration_seconds 
long 
The duration of the setup phase for the task run in seconds 
Not populated for rows emitted before early December 2025 

cleanup_duration_seconds 
long 
The duration of the cleanup phase for the task run in seconds 
Not populated for rows emitted before early December 2025 

execution_duration_seconds 
long 
The duration of the execution phase for the task run in seconds 
Not populated for rows emitted before early December 2025 ← ✕ 

Column name 
Data type 
Description 
Notes 

account_id 
string 
The ID of the account this job belongs to 

workspace_id 
string 
The ID of the workspace this job belongs to 

job_id 
string 
The ID of the job 
Only unique within a single workspace 

run_id 
string 
The ID of the task run 

job_run_id 
string 
The ID of the job run 

parent_run_id 
string 
The ID of the parent run 

period_start_time 
timestamp 
The start time for the task or for the time period 
Timezone information is recorded at the end of the value with +00:00 representing UTC. For details on how Databricks slices long runs into hourly intervals, see timeline slicing logic . 

period_end_time 
timestamp 
The end time for the task or for the time period 
Timezone information is recorded at the end of the value with +00:00 representing UTC. For details on how Databricks slices long runs into hourly intervals, see timeline slicing logic . 

task_key 
string 
The reference key for a task in a job 
This key is only unique within a single job 

compute_ids 
array 
The compute_ids array contains IDs of job clusters, interactive clusters, and SQL warehouses used by the job task 

result_state 
string 
The outcome of the job task run 
For task runs longer than one hour that are split across multiple rows, this column is populated only in the row that represents the end of the run. For possible values, see Result state values . 

termination_code 
string 
The termination code of the task run 
For task runs longer than one hour that are split across multiple rows, this column is populated only in the row that represents the end of the run. For possible values, see Termination code values . 

compute 
array 
Details about the compute resources used in the job task run 
Not populated for rows emitted before early December 2025 

termination_type 
string 
The type of termination for the job task run 
Not populated for rows emitted before early December 2025 

task_parameters 
map 
The task-level parameters used in the job task run 
Contains only the values from job_parameters . Deprecated parameter fields ( notebook_params , python_params , python_named_params , spark_submit_params , and sql_params ) are not included. Not populated for rows emitted before early December 2025. 

setup_duration_seconds 
long 
The duration of the setup phase for the task run in seconds 
Not populated for rows emitted before early December 2025 

cleanup_duration_seconds 
long 
The duration of the cleanup phase for the task run in seconds 
Not populated for rows emitted before early December 2025 

execution_duration_seconds 
long 
The duration of the execution phase for the task run in seconds 
Not populated for rows emitted before early December 2025 
Pipelines table schema ​ 
The pipelines table is a slowly changing dimension table (SCD2). When a row changes, a new row is emitted with the updated values, so the table contains the full history of each pipeline, including its creation, updates, and deletion. See Query an SCD2 table . 
Table path : system.lakeflow.pipelines 

Column name 
Data type 
Description 
Notes 

account_id 
string 
The ID of the account this pipeline belongs to 

workspace_id 
string 
The ID of the workspace this pipeline belongs to 

pipeline_id 
string 
The ID of the pipeline 
Only unique within a single workspace 

pipeline_type 
string 
The type of the pipeline 
For possible values, see Pipeline type values 

name 
string 
The user-supplied name of the pipeline 

created_by 
string 
The email of the user, the ID of the service principal, or group name that created the pipeline 

run_as 
string 
The email of the user, ID of the service principal, or group name whose permissions are used for the pipeline run 

tags 
map 
The user-supplied custom tags associated with this job 

settings 
struct 
The settings of the pipeline 
See Pipeline settings 

configuration 
map 
The user-supplied configuration of the pipeline 

change_time 
timestamp 
The time when the pipeline was last modified 
Timezone recorded as +00:00 (UTC) 

delete_time 
timestamp 
The time when the pipeline was deleted by the user 
Timezone recorded as +00:00 (UTC) 

create_time 
timestamp 
The time when a pipeline was created by the user. Timezone recorded as +00:00 (UTC). 
Not populated for rows emitted before early December 2025 ← ✕ 

Column name 
Data type 
Description 
Notes 

account_id 
string 
The ID of the account this pipeline belongs to 

workspace_id 
string 
The ID of the workspace this pipeline belongs to 

pipeline_id 
string 
The ID of the pipeline 
Only unique within a single workspace 

pipeline_type 
string 
The type of the pipeline 
For possible values, see Pipeline type values 

name 
string 
The user-supplied name of the pipeline 

created_by 
string 
The email of the user, the ID of the service principal, or group name that created the pipeline 

run_as 
string 
The email of the user, ID of the service principal, or group name whose permissions are used for the pipeline run 

tags 
map 
The user-supplied custom tags associated with this job 

settings 
struct 
The settings of the pipeline 
See Pipeline settings 

configuration 
map 
The user-supplied configuration of the pipeline 

change_time 
timestamp 
The time when the pipeline was last modified 
Timezone recorded as +00:00 (UTC) 

delete_time 
timestamp 
The time when the pipeline was deleted by the user 
Timezone recorded as +00:00 (UTC) 

create_time 
timestamp 
The time when a pipeline was created by the user. Timezone recorded as +00:00 (UTC). 
Not populated for rows emitted before early December 2025 Example query ​ SQL 
-- Get the most recent version of a pipeline SELECT * , ROW_NUMBER ( ) OVER ( PARTITION BY workspace_id , pipeline_id ORDER BY change_time DESC ) as rn FROM system . lakeflow . pipelines QUALIFY rn = 1 -- Enrich billing logs with pipeline metadata with latest_pipelines AS ( SELECT * , ROW_NUMBER ( ) OVER ( PARTITION BY workspace_id , pipeline_id ORDER BY change_time DESC ) as rn FROM system . lakeflow . pipelines QUALIFY rn = 1 ) SELECT usage . * , pipelines . * FROM system . billing . usage LEFT JOIN latest_pipelines ON ( usage . workspace_id = pipelines . workspace_id AND usage . usage_metadata . dlt_pipeline_id = pipelines . pipeline_id ) WHERE usage . usage_metadata . dlt_pipeline_id IS NOT NULL 
Pipeline update timeline table schema ​ 
The pipeline update timeline table is immutable and complete at the time it is produced. 
Table path : system.lakeflow.pipeline_update_timeline 

Column name 
Data type 
Description 
Notes 

account_id 
string 
The ID of the account this pipeline belongs to 

workspace_id 
string 
The ID of the workspace this pipeline belongs to 

pipeline_id 
string 
The ID of the pipeline 
Only unique within a single workspace 

update_id 
string 
The ID of the pipeline update 
Only unique within a single workspace 

update_type 
string 
The type of the pipeline update 
For possible values, see Pipeline update type values 

request_id 
string 
The ID of the request. Helps to understand how many times an update had to be retried/restarted 

run_as_user_name 
string 
The email of the user, the ID of the service principal, or group name whose permissions are used for the pipeline update 

trigger_type 
string 
What triggered this update 
For possible values, see Pipeline trigger type values 

trigger_details 
struct 
The details of the pipeline's trigger 
For possible values, see Pipeline trigger type details 

result_state 
string 
The outcome of the pipeline update 
For updates running across more than 1 hour hours that are split across multiple rows, this column is populated only in the row that represents the end of the update. For possible values, see Pipeline result reference . 

compute 
struct 
Details about the compute resource used in the pipeline update 

period_start_time 
timestamp 
The start time for the pipeline update or for the hour. The value is stored as a UTC timestamp. 
Timezone information is recorded at the end of the value with +00:00 representing UTC. For details on how Databricks slices long runs into hourly intervals, see timeline slicing logic . 

period_end_time 
timestamp 
The end time for the pipeline update or for the hour. The value is stored as a UTC timestamp. 
Timezone information is recorded at the end of the value with +00:00 representing UTC. For details on how Databricks slices long runs into hourly intervals, see timeline slicing logic . 

refresh_selection 
array 
A list of tables to update without fullRefresh 

full_refresh_selection 
array 
A list of tables to update with fullRefresh 

reset_checkpoint_selection 
array 
A list of streaming flows to clear the checkpoints for ← ✕ 

Column name 
Data type 
Description 
Notes 

account_id 
string 
The ID of the account this pipeline belongs to 

workspace_id 
string 
The ID of the workspace this pipeline belongs to 

pipeline_id 
string 
The ID of the pipeline 
Only unique within a single workspace 

update_id 
string 
The ID of the pipeline update 
Only unique within a single workspace 

update_type 
string 
The type of the pipeline update 
For possible values, see Pipeline update type values 

request_id 
string 
The ID of the request. Helps to understand how many times an update had to be retried/restarted 

run_as_user_name 
string 
The email of the user, the ID of the service principal, or group name whose permissions are used for the pipeline update 

trigger_type 
string 
What triggered this update 
For possible values, see Pipeline trigger type values 

trigger_details 
struct 
The details of the pipeline's trigger 
For possible values, see Pipeline trigger type details 

result_state 
string 
The outcome of the pipeline update 
For updates running across more than 1 hour hours that are split across multiple rows, this column is populated only in the row that represents the end of the update. For possible values, see Pipeline result reference . 

compute 
struct 
Details about the compute resource used in the pipeline update 

period_start_time 
timestamp 
The start time for the pipeline update or for the hour. The value is stored as a UTC timestamp. 
Timezone information is recorded at the end of the value with +00:00 representing UTC. For details on how Databricks slices long runs into hourly intervals, see timeline slicing logic . 

period_end_time 
timestamp 
The end time for the pipeline update or for the hour. The value is stored as a UTC timestamp. 
Timezone information is recorded at the end of the value with +00:00 representing UTC. For details on how Databricks slices long runs into hourly intervals, see timeline slicing logic . 

refresh_selection 
array 
A list of tables to update without fullRefresh 

full_refresh_selection 
array 
A list of tables to update with fullRefresh 

reset_checkpoint_selection 
array 
A list of streaming flows to clear the checkpoints for Example query ​ SQL 
-- This query gets the daily pipeline update count for a workspace for the last 7 days: SELECT workspace_id , COUNT ( DISTINCT update_id ) as update_count , to_date ( period_start_time ) as date FROM system . lakeflow . pipeline_update_timeline WHERE period_start_time > CURRENT_TIMESTAMP ( ) - INTERVAL 7 DAYS GROUP BY ALL -- This query returns the daily pipeline update count for a workspace for the last 7 days, distributed by the outcome of the pipeline update. SELECT workspace_id , COUNT ( DISTINCT update_id ) as update_count , result_state , to_date ( period_start_time ) as date FROM system . lakeflow . pipeline_update_timeline WHERE period_start_time > CURRENT_TIMESTAMP ( ) - INTERVAL 7 DAYS AND result_state IS NOT NULL GROUP BY ALL -- This query returns the average time of pipeline updates, measured in seconds. The records are organized by pipeline. A top 90 and a 95 percentile column show the average lengths of the pipeline's longest updates. with pipeline_update_duration as ( SELECT workspace_id , pipeline_id , update_id , CAST ( SUM ( period_end_time - period_start_time ) AS LONG ) as duration FROM system . lakeflow . pipeline_update_timeline WHERE period_start_time > CURRENT_TIMESTAMP ( ) - INTERVAL 7 DAYS GROUP BY ALL ) SELECT t1 . workspace_id , t1 . pipeline_id , COUNT ( DISTINCT t1 . update_id ) as update_count , MEAN ( t1 . duration ) as mean_seconds , AVG ( t1 . duration ) as avg_seconds , PERCENTILE ( t1 . duration , 0.9 ) as p90_seconds , PERCENTILE ( t1 . duration , 0.95 ) as p95_seconds FROM pipeline_update_duration t1 GROUP BY ALL ORDER BY mean_seconds DESC LIMIT 100 
Common join patterns ​ 
The following sections provide sample queries that highlight commonly used join patterns for jobs system tables. 
Join the jobs and job run timeline tables ​ Enrich job run with a job name ​ SQL 
with jobs as ( SELECT * , ROW_NUMBER ( ) OVER ( PARTITION BY workspace_id , job_id ORDER BY change_time DESC ) as rn FROM system . lakeflow . jobs QUALIFY rn = 1 ) SELECT job_run_timeline . * , jobs . name FROM system . lakeflow . job_run_timeline LEFT JOIN jobs USING ( workspace_id , job_id ) 
Join the job run timeline and usage tables ​ Enrich each billing log with job run metadata ​ 
The following query enriches billing logs with job run metadata from both classic and serverless jobs: SQL 
with aggregated_job_runs AS ( SELECT j . workspace_id , COALESCE ( t . job_id , j . job_id ) as origin_job_id , COALESCE ( t . job_run_id , j . run_id ) AS origin_job_run_id , j . job_id as billing_job_id , j . run_id as billing_run_id , CASE WHEN j . root_task_run_id IS NOT NULL THEN true ELSE false END AS is_workflow_run FROM system . lakeflow . job_run_timeline j LEFT JOIN system . lakeflow . job_task_run_timeline t ON j . workspace_id = t . workspace_id AND j . root_task_run_id = t . run_id WHERE j . period_start_time >= CURRENT_DATE ( ) - INTERVAL 7 DAYS GROUP BY ALL ) , billing_logs_enriched AS ( SELECT t2 . origin_job_id , t2 . origin_job_run_id , t1 . * FROM system . billing . usage t1 INNER JOIN aggregated_job_runs t2 ON t1 . workspace_id = t2 . workspace_id AND t1 . usage_metadata . job_id = t2 . billing_job_id AND t1 . usage_metadata . job_run_id = t2 . billing_run_id WHERE billing_origin_product = "JOBS" AND usage_date >= CURRENT_DATE ( ) - INTERVAL 7 DAYS ) SELECT workspace_id , origin_job_id AS job_id , origin_job_run_id AS run_id , sku_name , SUM ( usage_quantity ) as total_usage_quantity , SUM ( CASE WHEN usage_metadata . job_run_id != origin_job_run_id THEN usage_quantity ELSE 0 END ) AS workflow_run_usage_quantity , COUNT ( DISTINCT usage_metadata . job_run_id ) - 1 AS workflow_runs FROM billing_logs_enriched GROUP BY ALL Calculate cost per job run ​ 
This query joins with the billing.usage system table to calculate a cost per job run. SQL 
with jobs_usage AS ( SELECT * , usage_metadata . job_id , usage_metadata . job_run_id as run_id , identity_metadata . run_as as run_as FROM system . billing . usage WHERE billing_origin_product = "JOBS" ) , jobs_usage_with_usd AS ( SELECT jobs_usage . * , usage_quantity * pricing . default as usage_usd FROM jobs_usage LEFT JOIN system . billing . list_prices pricing ON jobs_usage . sku_name = pricing . sku_name AND pricing . price_start_time <= jobs_usage . usage_start_time AND ( pricing . price_end_time >= jobs_usage . usage_start_time OR pricing . price_end_time IS NULL ) AND pricing . currency_code = "USD" ) , jobs_usage_aggregated AS ( SELECT workspace_id , job_id , run_id , FIRST ( run_as , TRUE ) as run_as , sku_name , SUM ( usage_usd ) as usage_usd , SUM ( usage_quantity ) as usage_quantity FROM jobs_usage_with_usd GROUP BY ALL ) SELECT t1 . * , MIN ( period_start_time ) as run_start_time , MAX ( period_end_time ) as run_end_time , FIRST ( result_state , TRUE ) as result_state FROM jobs_usage_aggregated t1 LEFT JOIN system . lakeflow . job_run_timeline t2 USING ( workspace_id , job_id , run_id ) GROUP BY ALL ORDER BY usage_usd DESC LIMIT 100 Get usage logs for an SUBMIT_RUN jobs ​ SQL 
SELECT * FROM system . billing . usage WHERE EXISTS ( SELECT 1 FROM system . lakeflow . job_run_timeline WHERE job_run_timeline . job_id = usage_metadata . job_id AND run_name = :run_name AND workspace_id = :workspace_id ) 
Join the job task run timeline and clusters tables ​ Enrich job task runs with clusters metadata ​ SQL 
with clusters as ( SELECT * , ROW_NUMBER ( ) OVER ( PARTITION BY workspace_id , cluster_id ORDER BY change_time DESC ) as rn FROM system . compute . clusters QUALIFY rn = 1 ) , exploded_task_runs AS ( SELECT * , EXPLODE ( compute_ids ) as cluster_id FROM system . lakeflow . job_task_run_timeline WHERE array_size ( compute_ids ) > 0 ) SELECT * FROM exploded_task_runs t1 LEFT JOIN clusters t2 USING ( workspace_id , cluster_id ) Find jobs running on all-purpose compute ​ 
This query joins with the compute.clusters system table to return recent jobs that are running on all-purpose compute instead of jobs compute. SQL 
with clusters AS ( SELECT * , ROW_NUMBER ( ) OVER ( PARTITION BY workspace_id , cluster_id ORDER BY change_time DESC ) as rn FROM system . compute . clusters WHERE cluster_source = "UI" OR cluster_source = "API" QUALIFY rn = 1 ) , job_tasks_exploded AS ( SELECT workspace_id , job_id , EXPLODE ( compute_ids ) as cluster_id FROM system . lakeflow . job_task_run_timeline WHERE period_start_time >= CURRENT_DATE ( ) - INTERVAL 30 DAY GROUP BY ALL ) , all_purpose_cluster_jobs AS ( SELECT t1 . * , t2 . cluster_name , t2 . owned_by , t2 . dbr_version FROM job_tasks_exploded t1 INNER JOIN clusters t2 USING ( workspace_id , cluster_id ) ) SELECT * FROM all_purpose_cluster_jobs LIMIT 10 ; Find jobs that haven’t run in the last 30 days ​ 
This query joins the lakeflow.jobs and lakeflow.job_run_timeline system tables to return jobs that haven't run in the last 30 days. SQL 
with latest_jobs AS ( SELECT * , ROW_NUMBER ( ) OVER ( PARTITION BY workspace_id , job_id ORDER BY change_time DESC ) as rn FROM system . lakeflow . jobs QUALIFY rn = 1 ) , latest_not_deleted_jobs AS ( SELECT workspace_id , job_id , name , change_time , tags FROM latest_jobs WHERE delete_time IS NULL ) , last_seen_job_timestamp AS ( SELECT workspace_id , job_id , MAX ( period_start_time ) as last_executed_at FROM system . lakeflow . job_run_timeline WHERE run_type = "JOB_RUN" GROUP BY ALL ) SELECT t1 . workspace_id , t1 . job_id , t1 . name , t1 . change_time as last_modified_at , t2 . last_executed_at , t1 . tags FROM latest_not_deleted_jobs t1 LEFT JOIN last_seen_job_timestamp t2 USING ( workspace_id , job_id ) WHERE ( t2 . last_executed_at <= CURRENT_DATE ( ) - INTERVAL 30 DAYS ) OR ( t2 . last_executed_at IS NULL ) ORDER BY last_executed_at ASC 
Jobs monitoring dashboard ​ 
The following dashboard uses system tables to help you get started monitoring your jobs and operational health. It includes common use cases such as job performance tracking, failure monitoring, and resource utilization. 


For information on downloading the dashboard, see Monitor job costs & performance with system tables 
Troubleshooting ​ 
Job is not logged in the lakeflow.jobs table ​ 
If a job is not visible in the system tables: 
The job was created in a different region 
Recent job creation (table lag) 
While the latest record for each job_id is always retained, older historical records beyond the 365-day retention window are removed. If you need a fresh record, modify any of the job's fields present in the schema to emit a new row. 
Can't find a job seen in the job_run_timeline table ​ 
Not all job runs are visible everywhere. While JOB_RUN entries appear in all job-related tables, WORKFLOW_RUN (notebook workflow runs) are recorded only in job_run_timeline and SUBMIT_RUN (one-time submitted runs) are only recorded in both timeline tables. These runs are not populated to other job system tables like jobs or job_tasks . 
See the Run types table below for a detailed breakdown of where each type of run is visible and accessible. 
Job run not visible in billing.usage table ​ 
In system.billing.usage , the usage_metadata.job_id is only populated for jobs that run on job compute or serverless compute. 
Additionally, WORKFLOW_RUN jobs do not have their own usage_metadata.job_id or usage_metadata.job_run_id attribution in system.billing.usage .
Instead, their compute usage is attributed to the parent notebook that triggered them.
This means when a notebook launches a workflow run, all compute costs appear under the parent notebook's usage, not as a separate workflow job. 
See Usage metadata reference for more information. 
Calculate the cost of a job running on an all-purpose compute ​ 
Precise cost calculation for jobs running on purpose compute is not possible with 100% accuracy. When a job runs on an interactive (all-purpose) compute, multiple workloads like notebooks, SQL queries, or other jobs often run simultaneously on that same compute resource. Because the cluster resources are shared, there's no direct 1:1 mapping between computing costs and individual job runs. 
For accurate job cost tracking, Databricks recommends running jobs on dedicated job compute or serverless compute, where the usage_metadata.job_id and usage_metadata.job_run_id allow for precise cost attribution. 
If you must use all-purpose compute, you can: 
Monitor overall cluster usage and costs in system.billing.usage based on usage_metadata.cluster_id . 
Track job runtime metrics separately. 
Consider that any cost estimate will be approximate due to shared resources. 
See Usage metadata reference for more information on cost attribution. 
Reference values ​ 
The following section includes references for select columns in jobs-related tables. 
Slicing logic in the timeline tables ​ 
The period_start_time and period_end_time columns in the job_run_timeline and job_task_run_timeline tables record the active period of a job run or task run. warning 
Starting on January 19, 2026, new rows emitted to the timeline tables will use a clock-hour-aligned slicing logic . Existing rows will remain unchanged. 
Slices are created at one-hour intervals based on the run's start time. For example, a job starting at 4:47 PM creates slices from 4:47-5:47 PM, 5:47-6:47 PM, and so on. 
Slices will align to clock hour boundaries. For example, a job starting at 4:47 PM will create slices from 4:47-5:00 PM, 5:00-6:00 PM, 6:00-7:00 PM, and so on. See clock-hour-aligned slicing logic for details. 
Each row records up to an hour of runtime. Runs that last longer than 1 hour are recorded over multiple rows. This slicing ensures hourly granularity for monitoring long-running jobs. note 
If a run never began execution, it is represented by a row where period_start_time equals period_end_time . This indicates no active runtime. To understand why the run didn't start, check the termination_code column. Short-running jobs ​ 
For runs shorter than 1 hour, a single row is emitted, with period_start_time set to the run’s start time and period_end_time set to the run’s end time. 
For example, a job started at 12:13 PM UTC and ended at 12:45 PM UTC is represented by a single row: 

workspace_id 
job_id 
run_id 
period_start_time 
period_end_time 

6051921418418893 
280090038844882 
174832649710507 
2025-06-08T12:13:01.605 
2025-06-08T12:45:06.009 ← ✕ 

workspace_id 
job_id 
run_id 
period_start_time 
period_end_time 

6051921418418893 
280090038844882 
174832649710507 
2025-06-08T12:13:01.605 
2025-06-08T12:45:06.009 Long-running jobs ​ 
For runs that last longer than 1 hour, multiple rows are emitted with the same run_id , each representing up to one hour of the run's duration: 
The first row starts at the run's actual start time and ends at the end of the first run hour. 
Intermediate rows (if any) span full hourly windows, aligned to the previous slice period_end_time . 
The last row starts at the beginning of the previous slice and ends at the run's actual end time. 
For example, a job that ran from 4:47 PM UTC to 8:28 PM UTC is sliced into multiple rows. Each row represents an hour of activity, except for the last row, which may be shorter: 

workspace_id 
job_id 
run_id 
period_start_time 
period_end_time 

6051921418418893 
280090038844882 
55408597258956 
2025-07-01T16:47:55.992 
2025-07-01T17:47:56.434 

6051921418418893 
280090038844882 
55408597258956 
2025-07-01T17:47:56.434 
2025-07-01T18:47:58.876 

6051921418418893 
280090038844882 
55408597258956 
2025-07-01T18:47:58.876 
2025-07-01T19:47:59.682 

6051921418418893 
280090038844882 
55408597258956 
2025-07-01T19:47:59.682 
2025-07-01T20:28:29.743 ← ✕ 

workspace_id 
job_id 
run_id 
period_start_time 
period_end_time 

6051921418418893 
280090038844882 
55408597258956 
2025-07-01T16:47:55.992 
2025-07-01T17:47:56.434 

6051921418418893 
280090038844882 
55408597258956 
2025-07-01T17:47:56.434 
2025-07-01T18:47:58.876 

6051921418418893 
280090038844882 
55408597258956 
2025-07-01T18:47:58.876 
2025-07-01T19:47:59.682 

6051921418418893 
280090038844882 
55408597258956 
2025-07-01T19:47:59.682 
2025-07-01T20:28:29.743 Clock-hour-aligned slicing logic ​ note 
This slicing logic applies to new rows in the jobs timeline tables starting January 19, 2026 . 
Starting January 19, 2026, the timeline tables use clock-hour-aligned slicing. All time slices align to standard clock hour boundaries. 
For job runs shorter than 1 hour that start and end within the same clock hour, a single row is emitted: 

workspace_id 
job_id 
run_id 
period_start_time 
period_end_time 

6051921418418893 
280090038844882 
174832649710507 
2025-12-08T12:13:01.605 
2025-12-08T12:45:06.009 ← ✕ 

workspace_id 
job_id 
run_id 
period_start_time 
period_end_time 

6051921418418893 
280090038844882 
174832649710507 
2025-12-08T12:13:01.605 
2025-12-08T12:45:06.009 
For job runs that cross clock-hour boundaries, multiple rows are emitted with slices aligned to clock hours: 
The first row starts at the run's actual start time and ends at the next clock hour boundary. 
Intermediate rows (if any) span complete clock hours. For example: 2:00-3:00 PM and 3:00-4:00 PM. 
The last row starts at a clock hour boundary and ends at the run's actual end time. 
For example, a job run that ran from 1:25 AM UTC to 3:40 AM UTC is sliced into three rows: 

workspace_id 
job_id 
run_id 
period_start_time 
period_end_time 

6051921418418893 
280090038844882 
55408597258956 
2025-12-01T01:25:00.000 
2025-12-01T02:00:00.000 

6051921418418893 
280090038844882 
55408597258956 
2025-12-01T02:00:00.000 
2025-12-01T03:00:00.000 

6051921418418893 
280090038844882 
55408597258956 
2025-12-01T03:00:00.000 
2025-12-01T03:40:00.000 ← ✕ 

workspace_id 
job_id 
run_id 
period_start_time 
period_end_time 

6051921418418893 
280090038844882 
55408597258956 
2025-12-01T01:25:00.000 
2025-12-01T02:00:00.000 

6051921418418893 
280090038844882 
55408597258956 
2025-12-01T02:00:00.000 
2025-12-01T03:00:00.000 

6051921418418893 
280090038844882 
55408597258956 
2025-12-01T03:00:00.000 
2025-12-01T03:40:00.000 
Trigger type values ​ 
For more information on the types of job triggers, see Automate jobs with schedules and triggers . 
In the job_run_timeline and jobs tables, the possible values for the trigger_type column are: 

Trigger type 
Description 
Applicable tables 

CONTINUOUS 
The job or run is triggered by a continuous trigger that keeps the job running. 
job_run_timeline , jobs 

CRON 
The job or run is triggered on a recurring schedule using cron syntax. 
job_run_timeline , jobs 

FILE_ARRIVAL 
The job or run is triggered when new files arrive in a configured storage location. 
job_run_timeline , jobs 

MODEL 
The job or run is triggered by a model version serving event. 
job_run_timeline , jobs 

MULTIPLE 
The job has two or more triggers. The trigger column is NULL . Read the triggers array instead. 
jobs 

ONETIME 
The job run was triggered by a one-time manual or API trigger. 
job_run_timeline 

ONETIME_RETRY 
The job or run was triggered as a retry of a previous failed run. 
job_run_timeline , jobs 

PERIODIC 
The job or run is triggered by a periodic schedule based on a time interval (for example, every hour). 
job_run_timeline , jobs 

RUN_JOB_TASK 
The job run was triggered as part of a run job task from another job. 
job_run_timeline 

TABLE 
The job or run is triggered by a table update using a table trigger configuration. 
job_run_timeline , jobs 

NULL 
The trigger type is not set. This can occur for older job records or jobs where the trigger type was not configured. 
jobs ← ✕ 

Trigger type 
Description 
Applicable tables 

CONTINUOUS 
The job or run is triggered by a continuous trigger that keeps the job running. 
job_run_timeline , jobs 

CRON 
The job or run is triggered on a recurring schedule using cron syntax. 
job_run_timeline , jobs 

FILE_ARRIVAL 
The job or run is triggered when new files arrive in a configured storage location. 
job_run_timeline , jobs 

MODEL 
The job or run is triggered by a model version serving event. 
job_run_timeline , jobs 

MULTIPLE 
The job has two or more triggers. The trigger column is NULL . Read the triggers array instead. 
jobs 

ONETIME 
The job run was triggered by a one-time manual or API trigger. 
job_run_timeline 

ONETIME_RETRY 
The job or run was triggered as a retry of a previous failed run. 
job_run_timeline , jobs 

PERIODIC 
The job or run is triggered by a periodic schedule based on a time interval (for example, every hour). 
job_run_timeline , jobs 

RUN_JOB_TASK 
The job run was triggered as part of a run job task from another job. 
job_run_timeline 

TABLE 
The job or run is triggered by a table update using a table trigger configuration. 
job_run_timeline , jobs 

NULL 
The trigger type is not set. This can occur for older job records or jobs where the trigger type was not configured. 
jobs 
Run type values ​ 
In the job_run_timeline table, the possible values for the run_type column are: 

Type 
Description 
UI Location 
API Endpoint 
System Tables 

JOB_RUN 
Standard job execution 
Jobs & Job Runs UI 
/jobs and /jobs/runs endpoints 
jobs, job_tasks, job_run_timeline, job_task_run_timeline 

SUBMIT_RUN 
One-time run via POST /jobs/runs/submit 
Job Runs UI only 
/jobs/runs endpoints only 
job_run_timeline, job_task_run_timeline 

WORKFLOW_RUN 
Run initiated from notebook workflow 
Not visible 
Not accessible 
job_run_timeline ← ✕ 

Type 
Description 
UI Location 
API Endpoint 
System Tables 

JOB_RUN 
Standard job execution 
Jobs & Job Runs UI 
/jobs and /jobs/runs endpoints 
jobs, job_tasks, job_run_timeline, job_task_run_timeline 

SUBMIT_RUN 
One-time run via POST /jobs/runs/submit 
Job Runs UI only 
/jobs/runs endpoints only 
job_run_timeline, job_task_run_timeline 

WORKFLOW_RUN 
Run initiated from notebook workflow 
Not visible 
Not accessible 
job_run_timeline 
Result state values ​ 
In the job_task_run_timeline and job_run_timeline tables, the possible values for the result_state column are: 

State 
Description 

SUCCEEDED 
The run completed successfully. 

FAILED 
The run completed with an error. 

SKIPPED 
Run was never executed because a condition was not met. 

CANCELLED 
The run was canceled at the user's request. 

TIMED_OUT 
The run was stopped after reaching the timeout. 

ERROR 
The run completed with an error. 

BLOCKED 
The run was blocked on an upstream dependency. 

NULL 
The row represents an intermediate slice of a long-running job. The result_state is only available in the row that represents the end of the run. ← ✕ 

State 
Description 

SUCCEEDED 
The run completed successfully. 

FAILED 
The run completed with an error. 

SKIPPED 
Run was never executed because a condition was not met. 

CANCELLED 
The run was canceled at the user's request. 

TIMED_OUT 
The run was stopped after reaching the timeout. 

ERROR 
The run completed with an error. 

BLOCKED 
The run was blocked on an upstream dependency. 

NULL 
The row represents an intermediate slice of a long-running job. The result_state is only available in the row that represents the end of the run. 
Termination code values ​ 
In the job_task_run_timeline and job_run_timeline tables, the possible values for the termination_code column are: 

Termination code 
Description 

SUCCESS 
The run was completed successfully. 

CANCELLED 
The run was canceled during execution by the Databricks platform; for example, if the maximum run duration was exceeded. 

SKIPPED 
Run was never executed, for example, if the upstream task run failed, the dependency type condition was not met, or there were no material tasks to execute. 

DRIVER_ERROR 
The run encountered an error while communicating with the Spark Driver. 

CLUSTER_ERROR 
The run failed due to a cluster error. 

REPOSITORY_CHECKOUT_FAILED 
Failed to complete the checkout due to an error when communicating with the third party service. 

INVALID_CLUSTER_REQUEST 
The run failed because it issued an invalid request to start the cluster. 

WORKSPACE_RUN_LIMIT_EXCEEDED 
The workspace has reached the quota for the maximum number of concurrent active runs. Consider scheduling the runs over a larger time frame. 

FEATURE_DISABLED 
The run failed because it tried to access a feature unavailable for the workspace. 

CLUSTER_REQUEST_LIMIT_EXCEEDED 
The number of cluster creation, start, and upsize requests has exceeded the allotted rate limit. Consider spreading the run execution over a larger time frame. 

STORAGE_ACCESS_ERROR 
The run failed due to an error when accessing the customer blob storage. 

RUN_EXECUTION_ERROR 
The run was completed with task failures. 

UNAUTHORIZED_ERROR 
The run failed due to a permission issue while accessing a resource. 

LIBRARY_INSTALLATION_ERROR 
The run failed while installing the user-requested library. The causes might include, but are not limited to: the provided library is invalid, or insufficient permissions to install the library. 

MAX_CONCURRENT_RUNS_EXCEEDED 
The scheduled run exceeds the limit of maximum concurrent runs set for the job. 

MAX_SPARK_CONTEXTS_EXCEEDED 
The run is scheduled on a cluster that has already reached the maximum number of contexts it is configured to create. 

RESOURCE_NOT_FOUND 
A resource necessary for running the execution does not exist. 

INVALID_RUN_CONFIGURATION 
The run failed due to an invalid configuration. 

CLOUD_FAILURE 
The run failed due to a cloud provider issue. 

MAX_JOB_QUEUE_SIZE_EXCEEDED 
The run was skipped due to reaching the job-level queue size limit. ← ✕ 

Termination code 
Description 

SUCCESS 
The run was completed successfully. 

CANCELLED 
The run was canceled during execution by the Databricks platform; for example, if the maximum run duration was exceeded. 

SKIPPED 
Run was never executed, for example, if the upstream task run failed, the dependency type condition was not met, or there were no material tasks to execute. 

DRIVER_ERROR 
The run encountered an error while communicating with the Spark Driver. 

CLUSTER_ERROR 
The run failed due to a cluster error. 

REPOSITORY_CHECKOUT_FAILED 
Failed to complete the checkout due to an error when communicating with the third party service. 

INVALID_CLUSTER_REQUEST 
The run failed because it issued an invalid request to start the cluster. 

WORKSPACE_RUN_LIMIT_EXCEEDED 
The workspace has reached the quota for the maximum number of concurrent active runs. Consider scheduling the runs over a larger time frame. 

FEATURE_DISABLED 
The run failed because it tried to access a feature unavailable for the workspace. 

CLUSTER_REQUEST_LIMIT_EXCEEDED 
The number of cluster creation, start, and upsize requests has exceeded the allotted rate limit. Consider spreading the run execution over a larger time frame. 

STORAGE_ACCESS_ERROR 
The run failed due to an error when accessing the customer blob storage. 

RUN_EXECUTION_ERROR 
The run was completed with task failures. 

UNAUTHORIZED_ERROR 
The run failed due to a permission issue while accessing a resource. 

LIBRARY_INSTALLATION_ERROR 
The run failed while installing the user-requested library. The causes might include, but are not limited to: the provided library is invalid, or insufficient permissions to install the library. 

MAX_CONCURRENT_RUNS_EXCEEDED 
The scheduled run exceeds the limit of maximum concurrent runs set for the job. 

MAX_SPARK_CONTEXTS_EXCEEDED 
The run is scheduled on a cluster that has already reached the maximum number of contexts it is configured to create. 

RESOURCE_NOT_FOUND 
A resource necessary for running the execution does not exist. 

INVALID_RUN_CONFIGURATION 
The run failed due to an invalid configuration. 

CLOUD_FAILURE 
The run failed due to a cloud provider issue. 

MAX_JOB_QUEUE_SIZE_EXCEEDED 
The run was skipped due to reaching the job-level queue size limit. 
Pipeline type values ​ 
In the pipelines table, the possible values for the pipeline_type column are: 

Pipeline type 
Description 

ETL_PIPELINE 
Standard pipeline 

MATERIALIZED_VIEW 
Materialized views in Databricks SQL 

STREAMING_TABLE 
Streaming tables in Databricks SQL 

INGESTION_PIPELINE 
Lakeflow Connect ingestor 

INGESTION_GATEWAY 
Lakeflow Connect gateway ingestor ← ✕ 

Pipeline type 
Description 

ETL_PIPELINE 
Standard pipeline 

MATERIALIZED_VIEW 
Materialized views in Databricks SQL 

STREAMING_TABLE 
Streaming tables in Databricks SQL 

INGESTION_PIPELINE 
Lakeflow Connect ingestor 

INGESTION_GATEWAY 
Lakeflow Connect gateway ingestor 
Pipeline result reference ​ 
In the pipeline_update_timeline table, the possible values for the result_state column are: 
COMPLETED 
FAILED 
CANCELED 
Pipeline settings reference ​ 
In the pipelines table, the possible values for the settings column are: 

Value 
Description 

photon 
A flag indicating whether to use Photon to run the pipeline 

development 
A flag indicating whether to run the pipeline in development or production mode 

continuous 
A flag indicating whether to run the pipeline continuously 

serverless 
A flag indicating whether to run the pipeline on a serverless cluster 

edition 
The product edition to run the pipeline 

channel 
The version of the pipeline runtime to use ← ✕ 

Value 
Description 

photon 
A flag indicating whether to use Photon to run the pipeline 

development 
A flag indicating whether to run the pipeline in development or production mode 

continuous 
A flag indicating whether to run the pipeline continuously 

serverless 
A flag indicating whether to run the pipeline on a serverless cluster 

edition 
The product edition to run the pipeline 

channel 
The version of the pipeline runtime to use 
Pipeline update type values ​ 
In the pipeline_update_timeline table, the possible values for the update_type column are: 
FULL_REFRESH 
REFRESH 
VALIDATE 
Pipeline trigger type values ​ 
In the pipeline_update_timeline table, the possible values for the trigger_type column are: 
API_CALL 
RETRY_ON_FAILURE 
SERVICE_UPGRADE 
SCHEMA_CHANGE 
JOB_TASK 
USER_ACTION 
DBSQL_REQUEST 
SETTINGS_CHANGE 
SCHEMA_EXPLORATION 
INFRASTRUCTURE_MAINTENANCE 
START_RESOURCES 
DEBUG_INGESTION 
NOTEBOOK_TASK 
DATABRICKS_CONNECT_QUERY 
PREDICTED_EXHAUSTION_RESTART 
Pipeline trigger type details ​ 
When the pipeline trigger type is JOB_TASK , then the trigger_details column is filled in with the following values: 

Value 
Description 
Notes 

job_task.job_id 
The ID of the job that triggered the pipeline update 

job_task.job_task_run_id 
The ID of the job task run that triggered the pipeline update 

job_task.performance_target 
The performance target used for the pipeline update 
Populated only for serverless pipeline updates. Either PERFORMANCE_OPTIMIZED or STANDARD . ← ✕ 

Value 
Description 
Notes 

job_task.job_id 
The ID of the job that triggered the pipeline update 

job_task.job_task_run_id 
The ID of the job task run that triggered the pipeline update 

job_task.performance_target 
The performance target used for the pipeline update 
Populated only for serverless pipeline updates. Either PERFORMANCE_OPTIMIZED or STANDARD . On this page 
Requirements 
Available jobs tables 
Record availability 
Detailed schema reference 
Query an SCD2 table 
Jobs table schema 
Job task table schema 
Job run timeline table schema 
Job task run timeline table schema 
Pipelines table schema 
Pipeline update timeline table schema 
Common join patterns 
Join the jobs and job run timeline tables 
Join the job run timeline and usage tables 
Join the job task run timeline and clusters tables 
Jobs monitoring dashboard 
Troubleshooting 
Job is not logged in the lakeflow.jobs table 
Can't find a job seen in the job_run_timeline table 
Job run not visible in billing.usage table 
Calculate the cost of a job running on an all-purpose compute 
Reference values 
Slicing logic in the timeline tables 
Trigger type values 
Run type values 
Result state values 
Termination code values 
Pipeline type values 
Pipeline result reference 
Pipeline settings reference 
Pipeline update type values 
Pipeline trigger type values 
Pipeline trigger type details Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 