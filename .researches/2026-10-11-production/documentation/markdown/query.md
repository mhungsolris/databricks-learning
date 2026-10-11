# query

Source: https://docs.databricks.com/aws/en/admin/system-tables/query-history
Retrieved: 2026-10-11

Query history system table reference | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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
Query history system table reference On this page Last updated on Oct 6, 2026 
Query history system table reference 
This article includes information on the query history system table, including an outline of the table's schema. 
Table path : This system table is located at system.query.history . 
Record availability ​ 
Records are typically available within one hour . Data delivery for new workspaces can take longer than this. 
When the query history table uses customer-managed keys, this availability does not apply. See Reading encrypted fields . 
Using the query history table ​ 
The query history table includes records for queries run using SQL warehouses, serverless compute for notebooks and jobs , and Lakeflow pipelines that use serverless or classic compute. The table includes records from all workspaces in your account that are in the same region as the workspace you use to access the table. 
By default, only admins have access to the system table. If you would like to share the table's data with a user or group, Databricks recommends creating a dynamic view for each user or group. See Create a dynamic view . 
Query history system table schema ​ 
The query history table uses the following schema: 

Column name 
Data type 
Description 
Example 

account_id 
string 
ID of the account. 
11e22ba4-87b9-4cc2 -9770-d10b894b7118 

workspace_id 
string 
The ID of the workspace where the query was run. 
1234567890123456 

statement_id 
string 
The ID that uniquely identifies the execution of the statement. You can use this ID to find the statement execution in the Query History UI. 
7a99b43c-b46c-432b -b0a7-814217701909 

session_id 
string 
The Spark session ID. 
01234567-cr06-a2mp -t0nd-a14ecfb5a9c2 

execution_status 
string 
The statement termination state. Possible values are: - FINISHED : execution was successful - FAILED : execution failed with the reason for failure described in the accompanying error message - CANCELED : execution was canceled 
FINISHED 

compute 
struct 
A struct that represents the type of compute resource used to run the statement and the ID of the resource where applicable. The type value is one of: - WAREHOUSE : run on a SQL warehouse. - SERVERLESS_COMPUTE : run on serverless compute , such as notebooks, jobs, or serverless Lakeflow pipelines . - CLASSIC_COMPUTE : run on classic compute, such as classic Lakeflow pipelines . The warehouse_id field is only populated when type is WAREHOUSE . The cluster_id field is never populated. 
{ type: WAREHOUSE, cluster_id: NULL, warehouse_id: ec58ee3772e8d305 } 

executed_by_user_id 
string 
The ID of the user who ran the statement. 
2967555311742259 

executed_by 
string 
The email address or username of the user who ran the statement. 
example@databricks.com 

statement_text 
string 
Text of the SQL statement. By default, this field returns <REDACTED> unless you are an account admin or a member of the databricks_pii_access account-level group. See Access masked statement text . If you have configured customer-managed keys, see Reading encrypted fields . Due to storage limitations, longer statement text values are compressed. Even with compression, you may reach a character limit. 
SELECT 1 

statement_type 
string 
The statement type. For example: ALTER , COPY , and INSERT . 
SELECT 

error_message 
string 
Message describing the error condition. If you have configured customer-managed keys, see Reading encrypted fields . 
[INSUFFICIENT_PERMISSIONS] Insufficient privileges: User does not have permission SELECT on table 'default.nyctaxi_trips'. 

client_application 
string 
Client application that ran the statement. For example: Databricks SQL Editor, Tableau, and Power BI. This field is derived from information provided by client applications. While values are expected to remain static over time, this cannot be guaranteed. 
Databricks SQL Editor 

client_driver 
string 
The connector used to connect to Databricks to run the statement. For example: Databricks SQL Driver for Go, Databricks ODBC Driver, Databricks JDBC Driver. 
Databricks JDBC Driver 

cache_origin_statement_id 
string 
For query results fetched from cache, this field contains the statement ID of the query that originally inserted the result into the cache. If the query result is not fetched from cache, this field contains the query's own statement ID. 
01f034de-5e17-162d -a176-1f319b12707b 

total_duration_ms 
bigint 
Total execution time of the statement in milliseconds (excluding result fetch time). 
1 

waiting_for_compute_duration_ms 
bigint 
Time spent waiting for compute resources to be provisioned in milliseconds. 
1 

waiting_at_capacity_duration_ms 
bigint 
Time spent waiting in queue for available compute capacity in milliseconds. 
1 

execution_duration_ms 
bigint 
Time spent executing the statement in milliseconds. 
1 

compilation_duration_ms 
bigint 
Time spent loading metadata and optimizing the statement in milliseconds. 
1 

total_task_duration_ms 
bigint 
The sum of all task durations in milliseconds. This time represents the combined time it took to run the query across all cores of all nodes. It can be significantly longer than the wall-clock duration if multiple tasks are executed in parallel. It can be shorter than the wall-clock duration if tasks wait for available nodes. 
1 

result_fetch_duration_ms 
bigint 
Time spent, in milliseconds, fetching the statement results after the execution finished. 
1 

start_time 
timestamp 
The time when Databricks received the request. Timezone information is recorded at the end of the value with +00:00 representing UTC. 
2022-12-05T00:00:00.000+0000 

end_time 
timestamp 
The time the statement execution ended, excluding result fetch time. Timezone information is recorded at the end of the value with +00:00 representing UTC. 
2022-12-05T00:00:00.000+00:00 

update_time 
timestamp 
The time the statement last received a progress update. Timezone information is recorded at the end of the value with +00:00 representing UTC. 
2022-12-05T00:00:00.000+00:00 

read_partitions 
bigint 
The number of partitions read after pruning. 
1 

pruned_files 
bigint 
The number of pruned files. 
1 

read_files 
bigint 
The number of files read after pruning. 
1 

read_rows 
bigint 
Total number of rows read by the statement. 
1 

produced_rows 
bigint 
Total number of rows returned by the statement. 
1 

read_bytes 
bigint 
Total size of data read by the statement in bytes. 
1 

pruned_files_bytes 
bigint 
The number of bytes of files pruned after table partition and file pruning. 
1 

read_files_bytes 
bigint 
The number of bytes of files read after table partition and file pruning. 
1 

read_io_cache_percent 
int 
The percentage of bytes of persistent data read from the IO cache. 
50 

from_result_cache 
boolean 
TRUE indicates that the statement result was fetched from the cache. 
TRUE 

spilled_local_bytes 
bigint 
Size of data, in bytes, temporarily written to disk while executing the statement. 
1 

written_bytes 
bigint 
The size in bytes of persistent data written to cloud object storage. 
1 

written_rows 
bigint 
The number of rows of persistent data written to cloud object storage. 
1 

written_files 
bigint 
Number of files of persistent data written to cloud object storage. 
1 

shuffle_read_bytes 
bigint 
The total amount of data in bytes sent over the network. 
1 

query_source 
struct 
A struct that contains key-value pairs representing Databricks entities that were involved in the execution of this statement, such as jobs, notebooks, or dashboards. This field only records Databricks entities. 
{ alert_id: 81191d77-184f-4c4e-9998-b6a4b5f4cef1, sql_query_id: null, dashboard_id: null, notebook_id: null, job_info: { job_id: 12781233243479, job_run_id: null, job_task_run_id: 110373910199121 }, legacy_dashboard_id: null, genie_space_id: null } 

query_parameters 
struct 
A struct containing named and positional parameters used in parameterized queries. Named parameters are represented as key-value pairs mapping parameter names to values. Positional parameters are represented as a list where the index indicates the parameter position. Only one type (named or positional) can be present at a time. 
{ named_parameters: { "param-1": 1, "param-2": "hello" }, pos_parameters: null, is_truncated: false } 

executed_as 
string 
The name of the user or Databricks service principal whose privilege was used to run the statement. 
example@databricks.com 

executed_as_user_id 
string 
The ID of the user or Databricks service principal whose privilege was used to run the statement. 
2967555311742259 

query_tags 
map<string, string> 
Custom key-value tags applied to the query for grouping, filtering, and cost attribution. Tags can be set using session configuration parameters or the SET QUERY_TAGS SQL statement. Key-only tags have a null value. This column is only populated for queries run on SQL warehouses. See Query tags . 
{ "team": "engineering", "cost_center": "701", "env": "prod" } ← ✕ 

Column name 
Data type 
Description 
Example 

account_id 
string 
ID of the account. 
11e22ba4-87b9-4cc2 -9770-d10b894b7118 

workspace_id 
string 
The ID of the workspace where the query was run. 
1234567890123456 

statement_id 
string 
The ID that uniquely identifies the execution of the statement. You can use this ID to find the statement execution in the Query History UI. 
7a99b43c-b46c-432b -b0a7-814217701909 

session_id 
string 
The Spark session ID. 
01234567-cr06-a2mp -t0nd-a14ecfb5a9c2 

execution_status 
string 
The statement termination state. Possible values are: - FINISHED : execution was successful - FAILED : execution failed with the reason for failure described in the accompanying error message - CANCELED : execution was canceled 
FINISHED 

compute 
struct 
A struct that represents the type of compute resource used to run the statement and the ID of the resource where applicable. The type value is one of: - WAREHOUSE : run on a SQL warehouse. - SERVERLESS_COMPUTE : run on serverless compute , such as notebooks, jobs, or serverless Lakeflow pipelines . - CLASSIC_COMPUTE : run on classic compute, such as classic Lakeflow pipelines . The warehouse_id field is only populated when type is WAREHOUSE . The cluster_id field is never populated. 
{ type: WAREHOUSE, cluster_id: NULL, warehouse_id: ec58ee3772e8d305 } 

executed_by_user_id 
string 
The ID of the user who ran the statement. 
2967555311742259 

executed_by 
string 
The email address or username of the user who ran the statement. 
example@databricks.com 

statement_text 
string 
Text of the SQL statement. By default, this field returns <REDACTED> unless you are an account admin or a member of the databricks_pii_access account-level group. See Access masked statement text . If you have configured customer-managed keys, see Reading encrypted fields . Due to storage limitations, longer statement text values are compressed. Even with compression, you may reach a character limit. 
SELECT 1 

statement_type 
string 
The statement type. For example: ALTER , COPY , and INSERT . 
SELECT 

error_message 
string 
Message describing the error condition. If you have configured customer-managed keys, see Reading encrypted fields . 
[INSUFFICIENT_PERMISSIONS] Insufficient privileges: User does not have permission SELECT on table 'default.nyctaxi_trips'. 

client_application 
string 
Client application that ran the statement. For example: Databricks SQL Editor, Tableau, and Power BI. This field is derived from information provided by client applications. While values are expected to remain static over time, this cannot be guaranteed. 
Databricks SQL Editor 

client_driver 
string 
The connector used to connect to Databricks to run the statement. For example: Databricks SQL Driver for Go, Databricks ODBC Driver, Databricks JDBC Driver. 
Databricks JDBC Driver 

cache_origin_statement_id 
string 
For query results fetched from cache, this field contains the statement ID of the query that originally inserted the result into the cache. If the query result is not fetched from cache, this field contains the query's own statement ID. 
01f034de-5e17-162d -a176-1f319b12707b 

total_duration_ms 
bigint 
Total execution time of the statement in milliseconds (excluding result fetch time). 
1 

waiting_for_compute_duration_ms 
bigint 
Time spent waiting for compute resources to be provisioned in milliseconds. 
1 

waiting_at_capacity_duration_ms 
bigint 
Time spent waiting in queue for available compute capacity in milliseconds. 
1 

execution_duration_ms 
bigint 
Time spent executing the statement in milliseconds. 
1 

compilation_duration_ms 
bigint 
Time spent loading metadata and optimizing the statement in milliseconds. 
1 

total_task_duration_ms 
bigint 
The sum of all task durations in milliseconds. This time represents the combined time it took to run the query across all cores of all nodes. It can be significantly longer than the wall-clock duration if multiple tasks are executed in parallel. It can be shorter than the wall-clock duration if tasks wait for available nodes. 
1 

result_fetch_duration_ms 
bigint 
Time spent, in milliseconds, fetching the statement results after the execution finished. 
1 

start_time 
timestamp 
The time when Databricks received the request. Timezone information is recorded at the end of the value with +00:00 representing UTC. 
2022-12-05T00:00:00.000+0000 

end_time 
timestamp 
The time the statement execution ended, excluding result fetch time. Timezone information is recorded at the end of the value with +00:00 representing UTC. 
2022-12-05T00:00:00.000+00:00 

update_time 
timestamp 
The time the statement last received a progress update. Timezone information is recorded at the end of the value with +00:00 representing UTC. 
2022-12-05T00:00:00.000+00:00 

read_partitions 
bigint 
The number of partitions read after pruning. 
1 

pruned_files 
bigint 
The number of pruned files. 
1 

read_files 
bigint 
The number of files read after pruning. 
1 

read_rows 
bigint 
Total number of rows read by the statement. 
1 

produced_rows 
bigint 
Total number of rows returned by the statement. 
1 

read_bytes 
bigint 
Total size of data read by the statement in bytes. 
1 

pruned_files_bytes 
bigint 
The number of bytes of files pruned after table partition and file pruning. 
1 

read_files_bytes 
bigint 
The number of bytes of files read after table partition and file pruning. 
1 

read_io_cache_percent 
int 
The percentage of bytes of persistent data read from the IO cache. 
50 

from_result_cache 
boolean 
TRUE indicates that the statement result was fetched from the cache. 
TRUE 

spilled_local_bytes 
bigint 
Size of data, in bytes, temporarily written to disk while executing the statement. 
1 

written_bytes 
bigint 
The size in bytes of persistent data written to cloud object storage. 
1 

written_rows 
bigint 
The number of rows of persistent data written to cloud object storage. 
1 

written_files 
bigint 
Number of files of persistent data written to cloud object storage. 
1 

shuffle_read_bytes 
bigint 
The total amount of data in bytes sent over the network. 
1 

query_source 
struct 
A struct that contains key-value pairs representing Databricks entities that were involved in the execution of this statement, such as jobs, notebooks, or dashboards. This field only records Databricks entities. 
{ alert_id: 81191d77-184f-4c4e-9998-b6a4b5f4cef1, sql_query_id: null, dashboard_id: null, notebook_id: null, job_info: { job_id: 12781233243479, job_run_id: null, job_task_run_id: 110373910199121 }, legacy_dashboard_id: null, genie_space_id: null } 

query_parameters 
struct 
A struct containing named and positional parameters used in parameterized queries. Named parameters are represented as key-value pairs mapping parameter names to values. Positional parameters are represented as a list where the index indicates the parameter position. Only one type (named or positional) can be present at a time. 
{ named_parameters: { "param-1": 1, "param-2": "hello" }, pos_parameters: null, is_truncated: false } 

executed_as 
string 
The name of the user or Databricks service principal whose privilege was used to run the statement. 
example@databricks.com 

executed_as_user_id 
string 
The ID of the user or Databricks service principal whose privilege was used to run the statement. 
2967555311742259 

query_tags 
map<string, string> 
Custom key-value tags applied to the query for grouping, filtering, and cost attribution. Tags can be set using session configuration parameters or the SET QUERY_TAGS SQL statement. Key-only tags have a null value. This column is only populated for queries run on SQL warehouses. See Query tags . 
{ "team": "engineering", "cost_center": "701", "env": "prod" } 
Access masked statement text ​ 
SQL statements can contain sensitive information such as customer names, email addresses, or other personally identifiable information (PII). The statement_text field returns <REDACTED> by default. Account admins and members of the databricks_pii_access group can read the full query text. 
To create the group and manage its membership and permissions, see Create and manage the databricks_pii_access group . 
Troubleshoot overlapping column masks ​ 
If you already applied a column mask to statement_text , for example with an attribute-based access control (ABAC) policy, queries against system.query.history can fail with COLUMN_MASKS_FEATURE_NOT_SUPPORTED.MULTIPLE_MASKS . Only one column mask can apply to a column for a given user. 
To resolve the conflict, you must be a metastore admin or have MANAGE on the table. Use Conflicting filters and masks to identify overlapping policies, then narrow or remove your mask on statement_text . 
Reading encrypted fields ​ 
When workspaces use customer-managed keys for managed services , the statement_text and error_message fields in the system table are encrypted by default. This is because system tables store data from and can be accessed by all workspaces in the region. To decrypt and display encrypted system table fields, account admins must add a key configuration to the system catalog itself. You must have MANAGE permission on the system catalog to perform this operation. 
When the query history table uses customer-managed keys, the typical record availability in Record availability does not apply. warning 
Adding a key configuration to the system catalog removes any Unity Catalog grants you previously applied to the system.query schema and the system.query.history table, resetting them to the default grants. Because grants are metastore-level, this affects all workspaces attached to the metastore, including workspaces where you did not run the command. After you enable customer-managed keys, reapply any custom grants on system.query and system.query.history . 
You can either create a key configuration or reuse an existing one. To add the key to the system catalog, run the following command. You can retrieve the encryption key ID in the account console by clicking Security then Encryption keys then opening the key configuration you want to use. Bash 
curl -v -X PATCH https://my-workspace-url/api/2.1/unity-catalog/catalogs/system -H 'Authorization: Bearer <pat token>' --data '{ "managed_encryption_settings": { "customer_managed_key_id": "<cmk id from account console>" } }' 
Allow up to 24 hours for enablement to complete. After enablement is complete, system.query.history starts displaying the encrypted fields for all new records. Records created before enablement cannot be decrypted. note 
The system catalog is different for each metastore, so the customer-managed key must be configured separately for each metastore. However, metastores in the same region can be configured to use the same key. 
View the query profile for a record ​ 
To navigate to a query's query profile based on a record in the query history table, do the following: 
Identify the record of interest, then copy the record's statement_id . 
Reference the record's workspace_id to ensure you are logged in to the same workspace as the record. 
Click Query History in the workspace sidebar. 
In the Statement ID field, paste the statement_id on the record. 
Click the name of a query. An overview of query metrics appears. 
Click See query profile . 
Understanding scan metrics ​ 
The query history table contains multiple metrics gathered during the scan. You can compute the following additional metrics from the table's columns: 
table_bytes : The total compressed size, in bytes, of the files in the scanned tables. Computed as pruned_files_bytes + read_files_bytes . 
table_files : The total number of files in the scanned tables. Computed as read_files + pruned_files . note 
read_bytes is not directly comparable to table_bytes . table_bytes , read_files_bytes , and pruned_files_bytes are compressed, on-disk file sizes. Unlike those file sizes, read_bytes measures the data actually read after column and row-group pruning. It combines compressed data read from cloud storage with uncompressed data served from the disk cache, and it can increase further when reads are retried. As a result, read_bytes can exceed table_bytes . 
Understanding query_source column ​ 
The query_source column contains a set of unique identifiers of Databricks entities involved in the statement execution. 
If the query_source column contains multiple IDs, it means the statement execution was triggered by multiple entities. For example, a job result may trigger an alert that calls a SQL query. In this example, all three IDs will be populated within query_source . The values of this column are not sorted by execution order. 
Possible query sources are: 
alert_id : Statement triggered from an alert 
sql_query_id : Statement executed from within this SQL editor session 
dashboard_id : Statement executed from a dashboard 
genie_space_id : Statement executed from a Genie Agent 
notebook_id : Statement executed from a notebook 
job_info.job_id : Statement executed within a job 
job_info.job_run_id : Statement executed from a job run 
job_info.job_task_run_id : Statement executed within a job task run Valid combinations of query_source ​ 
The following examples show how the query_source column is populated depending on how the query is run: 

Queries executed during a job run include a populated job_info struct: 
{ alert_id: null, sql_query_id: null, dashboard_id: null, notebook_id: null, job_info: { job_id: 64361233243479, job_run_id: null, job_task_run_id: 110378410199121 }, legacy_dashboard_id: null, genie_space_id: null } 

Queries from alerts include a sql_query_id and alert_id : 
{ alert_id: e906c0c6-2bcc-473a-a5d7-f18b2aee6e34, sql_query_id: 7336ab80-1a3d-46d4-9c79-e27c45ce9a15, dashboard_id: null, notebook_id: null, job_info: null, legacy_dashboard_id: null, genie_space_id: null } 

Queries from dashboards include a dashboard_id , but no job_info : 
{ alert_id: null, sql_query_id: null, dashboard_id: 887406461287882, notebook_id: null, job_info: null, legacy_dashboard_id: null, genie_space_id: null } On this page 
Record availability 
Using the query history table 
Query history system table schema 
Access masked statement text 
Troubleshoot overlapping column masks 
Reading encrypted fields 
View the query profile for a record 
Understanding scan metrics 
Understanding query_source column Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 