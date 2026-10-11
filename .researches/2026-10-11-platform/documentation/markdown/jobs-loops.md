# jobs-loops

Source: https://docs.databricks.com/aws/en/jobs/tasks/for-each
Retrieved: 2026-10-11

Use a For each task to run another task in a loop | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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
Configure tasks 
For each On this page Last updated on Sep 22, 2026 
Use a For each task to run another task in a loop 
Use the For each task to run a nested task in a loop, passing a different set of parameters to each iteration of the task. 
Adding the For each task to a job requires defining two tasks: The For each task and a nested task . The nested task is the task to run for each iteration of the For each task and is one of the standard Lakeflow Jobs task types. You cannot add another For each task as the nested task. 
For example, you could use the For each task to perform a common set of transformations on multiple tables, passing a table name from a list of table names to each iteration of the task. 
Nested tasks that do not have dependencies on each other can be run concurrently. 
Add the For each task to a job ​ 
You can add a For each task when you create a job or edit a task in an existing job. To configure a For each task: 

Click Add task . 

Enter a name into the Task name field. 

In the Type drop-down menu, select For each . 

Enter a name for the task in the Task name field. 

In the Inputs text box, define the values for the For each task to iterate on as a JSON formatted array of values. To learn more about passing parameters to the nested task, see Parameter types for the For each task . 

To optionally set the number of iterations that can run in parallel, enter a Concurrency value for the task. The default value is 1. 

To optionally receive notifications for task start, success, or failure, click Add . See Add notifications on a job . 

To complete the configuration of the For each task and add a nested task to run for each iteration, click Add a task to loop over . 

Select a task type and configuration options for the nested task. Nested tasks are standard task types and have the same configuration options. See Configure and edit tasks in Lakeflow Jobs . 

To reference parameters passed from the For each task, click Parameters . Use the {{input}} reference to set the value to the array value of each iteration or {{input.<key>}} to reference individual object fields when you iterate over a list of objects. 


(Optional) To configure retries, run-duration or streaming-backlog thresholds, or notifications, see Advanced task settings . 

Click Save task . 
To edit, clone, disable, or delete this task, see Configure and edit tasks in Lakeflow Jobs . 
Switch between the For each task and the nested task ​ 
The For each task appears in the Jobs UI as a node with the nested task node inside the For each node. To switch between the For each task and the nested task, click the respective nodes. 


Parameter types for the For each task ​ 
The For each task passes parameters to each iteration of the nested task. The input is an array of objects, and each object is passed to an iteration of the nested task. There are multiple ways to create the inputs that the task uses: JSON formatted arrays, task values, or job parameters. note 
Parameters are limited to 5,000 characters in the UI directly, or 48 KB if you use task value references (where the value can be much larger than the size of the string that describes it), or 10,000 characters for the value of job parameters. If your parameters require more than 48 KB, you can pass a lookup to a larger config file. See Use a lookup table for large parameter arrays . 
A JSON formatted array of values ​ 
When you create or edit a task, you can directly define an array of values for the nested task, using the Inputs text box. This can be an array of the following data types: 
Key-value pairs 
Strings, numbers, or Boolean types 
Arbitrarily complex JSON objects 
For example, if you pass [{"table": "sales"}, {"table": "orders"}] , reference the field in the nested task with {{input.table}} . 
The Inputs text box, and therefore JSON passed directly in this box, is limited to 5,000 characters. 
Task value references ​ 
You can pass task values from a preceding task. To reference passed task values, use the {{tasks.<task_name>.values.<task_value_name>}} syntax to set the value in the Inputs text box. For example, if a task named generate_countries_list that precedes the For each task sets the following task value: 
dbutils.jobs.taskValues.set(key = "countries", value = countries_array) 
Then the For each task references the task value in the Inputs text box using the following syntax: 
{{tasks.generate_countries_list.values.countries}} . 
You can put up to 5,000 characters in the Inputs text box, but the values that the references represent are able to be up to 48 KB. To learn more about task values, see Use task values to pass information between tasks . 
Job parameters ​ 
You can also use job parameters as input. To reference a job parameter, use the following syntax in the Inputs text box: {{job.parameters.<name>}} . For example, {{job.parameters.countries}} . 
You can put up to 5,000 characters in the Inputs text box to reference job parameters. The job parameter values are limited to 10,000 characters. To learn more about job parameters, see Configure job parameters . 
Reference a For each task in downstream tasks ​ 
The For each task is the top-level task, and downstream tasks can specify it as a dependency. A downstream task cannot set the nested task as a dependency directly, but it can reference the task values that the nested task set on each iteration, read as a single list ordered by iteration index. See Read values from a For each task's iterations . note 
A For each task fails if the upstream task that provides its input values is disabled. See Limitations . 
Run and monitor a job with a For each task ​ 
Running a job with a For each task is identical to running any other job. 
Viewing and managing job runs is also identical to any other job, except the task run history for a For each task, which is presented as a table of task iterations. See View task run history for a For each task . 
Tutorial ​ 
To build a metadata-driven job using a SQL task and a For each task, see Use a control table to drive a For each job . 
Additional resources ​ 
For each task : Define a For each task as code with Declarative Automation Bundles . 
Use a lookup table for large parameter arrays in a For each task : See a For each task example. 
Use a control table to drive a For each job : Follow the metadata-driven job tutorial. On this page 
Add the For each task to a job 
Switch between the For each task and the nested task 
Parameter types for the For each task 
A JSON formatted array of values 
Task value references 
Job parameters 
Reference a For each task in downstream tasks 
Run and monitor a job with a For each task 
Tutorial 
Additional resources Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 