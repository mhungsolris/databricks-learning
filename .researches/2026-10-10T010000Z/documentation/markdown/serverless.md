# serverless

Source: https://docs.databricks.com/aws/en/compute/serverless/
Retrieved: 2026-10-10

Connect to serverless compute | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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

Compute 
Serverless compute On this page Last updated on Sep 11, 2026 
Connect to serverless compute 
This page explains how to connect to and use serverless compute for notebooks, workflows, and Lakeflow pipelines in Databricks . 
What is serverless compute? ​ 
Serverless compute is a Databricks -managed service that allows users to quickly connect to on-demand computing resources for notebooks, workflows, and Lakeflow pipelines . 
When you choose to use serverless compute, you can run workloads without provisioning any compute resources in your cloud account. Instead, Databricks automatically allocates and manages the necessary compute resources. This speeds up start-up and scaling times, minimizes idle time, and reduces the need to manage compute resources. 
Serverless workloads are protected by multiple layers of security and are designed to be enterprise-ready. For more information, see Databricks serverless security . note 
Serverless compute is available by default in most workspaces and does not require enablement. Workspaces that have Unity Catalog enabled automatically have access to serverless compute. 
Other Databricks features, such as serverless SQL warehouses, model serving, and AI features, use serverless infrastructure independently and have their own configuration paths. This page covers serverless compute for notebooks, workflows, and Lakeflow pipelines only. 
Use serverless compute for your workloads ​ 
Use the following pages to learn how to configure workloads to use serverless compute: 
Serverless notebooks 
Git Folder Serverless (Beta) 
Serverless jobs 
Serverless Lakeflow pipelines 
Streaming on serverless compute 
AI Runtime (Preview) 
Guides for AI Runtime 
Other features that use serverless infrastructure ​ 
Many Databricks features run on serverless infrastructure but are configured and managed separately from serverless compute for notebooks, jobs, and Lakeflow pipelines . For example: 
Serverless SQL warehouses 
Databricks Model Training - forecasting 
Data quality monitoring 
Predictive optimization 
Serverless compute requirements ​ 
Serverless compute is available by default in most workspaces. No manual enablement steps are required. 
Legacy workspaces that are not enabled for Unity Catalog do not have access to serverless compute. To access serverless compute, you must upgrade to Unity Catalog . See Upgrade a Databricks workspace to Unity Catalog . 
Serverless compute limitations ​ 
For a list of limitations, see Serverless compute limitations . 
Frequently asked questions (FAQ) ​ 
How are releases rolled out? 
How do I determine which serverless version I am running? 
How do I estimate costs for serverless? 
How do I analyze DBU usage for a specific workload? 
Is there a delay between when you run a job or query and the appearance of charges on the billable usage system table? 
Why do I see billing records for serverless jobs even though I haven't run serverless workloads? 
Does serverless compute support private repos? 
How do I install libraries for my job tasks? 
Can I connect to custom data sources? 
How does the serverless compute plane networking work? 
Can I configure serverless compute for jobs with Declarative Automation Bundles ? 
How do I run my serverless workload from my local development machine or from my data application? 
How are releases rolled out? ​ 
Serverless compute is a versionless product, which means that Databricks automatically upgrades the serverless compute runtime to support enhancements and upgrades to the platform. All users get the same updates, rolled out over a short period of time. 
How do I determine which serverless version I am running? ​ 
Serverless workloads always run on the latest runtime version. See Release notes for the most recent version. 
How do I estimate costs for serverless? ​ 
Databricks recommends running and benchmarking a representative or specific workload and then analyzing the billing system table. See Billable usage system table reference . 
How do I analyze DBU usage for a specific workload? ​ 
To see the cost for a specific workload, query the system.billing.usage system table. See Monitor the cost of serverless compute for sample queries and to download our cost observability dashboard. 
Is there a delay between when you run a job or query and the appearance of charges on the billable usage system table? ​ 
Yes, there could be up to a 24-hour delay between when you run a workload and its usage being reflected in the billable usage system table. 
Why do I see billing records for serverless jobs even though I haven't run serverless workloads? ​ 
Data quality monitoring and predictive optimization run on serverless infrastructure and are billed under the serverless jobs SKU. These features are managed separately from serverless compute for notebooks, workflows, and Lakeflow pipelines . 
Does serverless compute support private repos? ​ 
Repositories can be private or require authentication. For security reasons, a pre-signed URL is required when accessing authenticated repositories. 
How do I install libraries for my job tasks? ​ 
Databricks recommends using environments to install and manage libraries for your jobs. See Configure environment for job tasks . 
Can I connect to custom data sources? ​ 
No, only sources that use Lakehouse Federation are supported. See Supported data sources . 
How does the serverless compute plane networking work? ​ 
Serverless compute resources run in the serverless compute plane, which is managed by Databricks . For more details on the network and architecture, see Serverless compute plane networking . 
Can I configure serverless compute for jobs with Declarative Automation Bundles ? ​ 
Yes, Declarative Automation Bundles can be used to configure jobs that use serverless compute. See Job that uses serverless compute . 
How do I run my serverless workload from my local development machine or from my data application? ​ 
Databricks Connect allows you to connect to Databricks from your local machine and run workloads on serverless. See Databricks Connect . On this page 
What is serverless compute? 
Use serverless compute for your workloads 
Other features that use serverless infrastructure 
Serverless compute requirements 
Serverless compute limitations 
Frequently asked questions (FAQ) 
How are releases rolled out? 
How do I determine which serverless version I am running? 
How do I estimate costs for serverless? 
How do I analyze DBU usage for a specific workload? 
Is there a delay between when you run a job or query and the appearance of charges on the billable usage system table? 
Why do I see billing records for serverless jobs even though I haven't run serverless workloads? 
Does serverless compute support private repos? 
How do I install libraries for my job tasks? 
Can I connect to custom data sources? 
How does the serverless compute plane networking work? 
Can I configure serverless compute for jobs with Declarative Automation Bundles? 
How do I run my serverless workload from my local development machine or from my data application? Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 