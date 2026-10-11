# jar-task

Source: https://docs.databricks.com/aws/en/jobs/tasks/jar
Retrieved: 2026-10-11

JAR task for jobs | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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
JAR On this page Last updated on Sep 11, 2026 
JAR task for jobs 
Use the JAR task to deploy Scala or Java code compiled into a JAR (Java ARchive). Before you create a JAR task, see Create a Databricks compatible JAR for build requirements and limitations. 
Requirements ​ 
Choose a compute configuration that supports your workload. 
Upload your JAR file to a location or Maven repository compatible with your compute. See JAR library support . 
For standard access mode: An admin must add Maven coordinates and JAR paths to an allowlist . See standard access limitations . 
Configure a JAR task ​ 
Add a JAR task from the Tasks tab in the Jobs UI by doing the following: 

Click Add task . 

Enter a name into the Task name field. 

In the Type drop-down menu, select JAR . 

Specify the Main class . 
This is the full name of the class containing the main method to be executed. This class must be included in a JAR configured as a Dependent library . 

Click Compute to select or configure compute. Choose a classic or serverless compute. 

Configure your environment and add dependencies: 

For classic compute, click Add under Dependent libraries . The Add dependent library dialog appears. 
You can select an existing JAR file or upload a new JAR file. 
Not all locations support JAR files. 
Not all compute configurations support JAR files in all supported locations. 
Each Library Source has a different flow for selecting or uploading a JAR file. See Install libraries . 

For serverless compute, choose an environment then click edit to configure it. 
You must select 4 or higher for the Environment version . 
Add your JAR file. 
Add any other dependencies that you have. Don't include Spark dependencies, because these are already provided in the environment by Databricks Connect . For more information on dependencies in JARs, see Create a Databricks compatible JAR . 

(Optional) Configure Parameters as a list of strings passed as arguments to the main class. See Configure task parameters . 

(Optional) To configure retries, run-duration or streaming-backlog thresholds, or notifications, see Advanced task settings . 

Click Save task . 
To edit, clone, disable, or delete this task, see Configure and edit tasks in Lakeflow Jobs . 
Additional resources ​ 
JAR task : Define a JAR task as code with Declarative Automation Bundles . 
Create a Databricks compatible JAR : Create a Databricks compatible JAR. 
Install libraries : Manage dependent libraries. On this page 
Requirements 
Configure a JAR task 
Additional resources Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 