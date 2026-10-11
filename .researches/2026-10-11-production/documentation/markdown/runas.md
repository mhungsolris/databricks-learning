# runas

Source: https://docs.databricks.com/aws/en/dev-tools/bundles/run-as
Retrieved: 2026-10-11

Specify a run identity for a Declarative Automation Bundles workflow | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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

CI/CD 
Declarative Automation Bundles 
Configure bundles 
Bundle run identity On this page Last updated on Oct 7, 2026 
Specify a run identity for a Declarative Automation Bundles workflow 
This article describes how to use the run_as setting to specify the identity to use when running Declarative Automation Bundles workflows. 
The run_as setting can be configured as a top-level mapping to apply to resources, or within a target deployment mapping in a bundle configuration file . It can be set to a user_name or a service_principal_name . (Non-admins can only set this field to their own email.) 
This setting provides the ability to separate the identity used to deploy a bundle job or pipeline from the one used by the job or pipeline workflow to run. This increases the flexibility of bundle development and management, while also allowing guardrails to be established for deployments and runs. In particular: 
If the identity used to deploy a bundle is the same as the identity configured in the bundle's run_as setting there are no restrictions. All bundle resources are supported. 
If the identity used to deploy a bundle is different from the identity configured in the bundle's run_as setting, only jobs and pipelines are supported. 
A job or pipeline resource's own run_as mapping can also be set to an account group with group_name . The top-level and target run_as mappings do not support groups. See Set Run as to a group and Set the run-as identity to a group . 
Set a bundle run identity ​ 
To set the run identity of bundle resources, specify run_as as a top-level mapping as shown in the following example: YAML 
bundle : name : 'run_as' # This is the identity that will be used when "databricks bundle run my_test_job_1" is executed. run_as : service_principal_name : '5cf3z04b-a73c-4x46-9f3d-52da7999069e' resources : jobs : my_test_job_1 : name : Test job 1 tasks : - task_key : 'task_1' new_cluster : num_workers : 1 spark_version : 13.2.x - snapshot - scala2.12 node_type_id : i3.xlarge runtime_engine : PHOTON notebook_task : notebook_path : './test.py' my_test_job_2 : name : Test job 2 run_as : # This is the identity that will be used when "databricks bundle run my_test_job_2" is executed. service_principal_name : '69511ed2-zb27-444c-9863-4bc8ff497637' tasks : - task_key : 'task_2' notebook_task : notebook_path : './test.py' important 
The run_as setting is not supported for model serving endpoints. An error occurs if these resources are defined in a bundle where run_as is also configured. 
Set target deployment identities ​ 
It is best practice to configure run identities for staging and production target deployments. In addition, setting a run_as identity to a service principal for production targets is the most secure way of running a production workflow as it: 
Ensures that either the workflow was deployed by the same service principal or by someone with CAN_USE permissions on the service principal itself. 
Decouples the permission to run the production workflow from the identity that created or deployed the bundle. 
Allows users to configure and set a service principal for production with fewer permissions than the identity used to deploy the production bundle. 
In the following example databricks.yml configuration file, three target modes have been configured: development, staging, and production. The development mode is configured to run as an individual user, and the staging and production modes are configured to run using two different service principals. Service principals are always in the form of an application ID, which can be retrieved from a Service principal 's page in your workspace admin settings . YAML 
bundle : name : my_targeted_bundle run_as : service_principal_name : '5cf3z04b-a73c-4x46-9f3d-52da7999069e' targets : # Development deployment settings, set as the default development : mode : development default : true workspace : host : https : //my - host.cloud.databricks.com run_as : user_name : someone@example.com # Staging deployment settings staging : workspace : host : https : //my - host.cloud.databricks.com root_path : /Shared/staging - workspace/.bundle/$ { bundle.name } /$ { bundle.target } run_as : service_principal_name : '69511ed2-zb27-444c-9863-4bc8ff497637' # Production deployment settings production : mode : production workspace : host : https : //my - host.cloud.databricks.com root_path : /Shared/production - workspace/.bundle/$ { bundle.name } /$ { bundle.target } run_as : service_principal_name : '68ed9cd5-8923-4851-x0c1-c7536c67ff99' resources : jobs : my_test_job : name : Test job tasks : - task_key : 'task' new_cluster : num_workers : 1 spark_version : 13.3.x - cpu - ml - scala2.12 node_type_id : i3.xlarge runtime_engine : STANDARD notebook_task : notebook_path : './test.py' On this page 
Set a bundle run identity 
Set target deployment identities Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 