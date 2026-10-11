# jobs-values

Source: https://docs.databricks.com/aws/en/jobs/task-values
Retrieved: 2026-10-11

Use task values to pass information between tasks | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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
Task values On this page Last updated on Oct 8, 2026 
Use task values to pass information between tasks 
Task values refer to the Databricks Utilities taskValues subutility, which lets you pass arbitrary values between tasks in a Databricks job. See taskValues subutility (dbutils.jobs.taskValues) . 
You specify a key-value pair using dbutils.jobs.taskValues.set() in one task and then can use the task name and key to reference the value in subsequent tasks. note 
Because dbutils.jobs.taskValues.set() and dbutils.jobs.taskValues.get() in the dbutils.jobs.taskValues subutility are Python functions, they can be used only in notebooks with Python selected as the language. However, you can reference task values using dynamic value references for all tasks that support parameters. See Reference task values . 
Set task values ​ 
Set task values in Python notebooks using dbutils.jobs.taskValues.set() . 
Task value keys must be strings. Each key must be unique if you have multiple task values defined in a notebook. 
You can manually or programmatically assign task values to keys. Only values that can be expressed as valid JSON are permitted. The size of the JSON representation of the value cannot exceed 48 KiB. 
For example, the following example sets a static string for the key fave_food : Python 
dbutils . jobs . taskValues . set ( key = "fave_food" , value = "beans" ) 
The following example uses a notebook task parameter to query all update records for a particular booking and return the current booking status and total count of records: Python 
from pyspark . sql . functions import col dbutils . widgets . text ( "booking_id" , "51567" , "Booking ID" ) booking_id = dbutils . widgets . get ( "booking_id" ) query = ( spark . read . table ( "samples.wanderbricks.booking_updates" ) . orderBy ( col ( "updated_at" ) , ascending = False ) . where ( col ( "booking_id" ) == booking_id ) . select ( col ( "status" ) ) ) dbutils . jobs . taskValues . set ( key = "record_count" , value = query . count ( ) ) dbutils . jobs . taskValues . set ( key = "booking_status" , value = query . take ( 1 ) [ 0 ] [ 0 ] ) 
You can pass lists of values using this pattern and then use them to coordinate downstream logic, such as For each tasks. See Use a For each task to run another task in a loop . 
The following example extracts the distinct values for destination ID to a Python list and sets this as a task value: Python 
dest_list = list ( spark . read . table ( "samples.wanderbricks.properties" ) . select ( "destination_id" ) . distinct ( ) . toPandas ( ) [ "destination_id" ] ) dbutils . jobs . taskValues . set ( key = "dest_list" , value = dest_list ) 
Reference task values ​ 
Databricks recommends referencing task values as task parameters configured using the dynamic value reference pattern {{tasks.<task_name>.values.<value_name>}} . 
For example, to reference the task value with the key dest_list from a task named destination_lookup , use the syntax {{tasks.destination_lookup.values.dest_list}} . 
See Configure task parameters and Dynamic value references . 
Use dbutils.jobs.taskValues.get ​ 
The syntax dbutils.jobs.taskValues.get() requires specifying the upstream task name. This syntax is not recommended, as you can use task values in multiple downstream tasks, meaning numerous updates are necessary if a task name changes. 
Using this syntax, you can optionally specify a default value and a debugValue . The default value is used if the key cannot be found. The debugValue allows you to set a static value to use during manual code development and testing in notebooks before you schedule the notebook as a task. 
The following example gets the value for the key booking_status set in a task name booking_lookup . The value confirmed is returned only when running the notebook interactively. Python 
booking_status = dbutils . jobs . taskValues . get ( taskKey = "booking_lookup" , key = "booking_status" , debugValue = "confirmed" ) note 
Databricks does not recommend setting default values, as they can be challenging to troubleshoot and prevent expected error messages due to missing keys or incorrectly named tasks. 
Read values from a For each task's iterations ​ 
A task that runs inside a For each task runs one time per iteration, and each iteration can set a task value with dbutils.jobs.taskValues.set() as in any task. A downstream task can read each iteration's value from a single returned list, ordered by iteration index. Beta 
Reading a For each task's aggregated iteration outputs is in Beta. It is enabled by default and requires Databricks Runtime 15.4 LTS or above on classic compute. 
On serverless compute , dbutils.jobs.taskValues.get requires environment version 5 or above. On environment versions 1 through 4, it returns only the first iteration's value instead of the list, and can raise a TypeError . Dynamic value references return the full list on any compute. 
On either read surface, use the key of the nested task that runs inside the For each task, not the For each task itself. Its key returns the values from every iteration as a single list ordered by iteration index. For example, if three iterations of a nested task named process each set result : Python 
results = dbutils . jobs . taskValues . get ( taskKey = "process" , key = "result" ) # results == [1, 2, 3] 
The dynamic value reference {{tasks.process.values.result}} resolves to the same array. 
An iteration that did not set the key keeps its position in the result: it appears as None (JSON null ) from dbutils.jobs.taskValues.get , and as a null in a dynamic value reference. For example, if the second of three iterations did not set result , results is [1, None, 3] . 
Aggregated references have two limits: an assembled array cannot exceed approximately 48 KB (49,344 characters) for a single parameter value, and a single parameter value can contain at most three aggregated task-value references. 
View task values ​ 
The returned value of a task value for each run is displayed in the Output pane of the Task run details . See View task run history . On this page 
Set task values 
Reference task values 
Use dbutils.jobs.taskValues.get 
Read values from a For each task's iterations 
View task values Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 