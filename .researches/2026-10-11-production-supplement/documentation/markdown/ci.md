# ci

Source: https://docs.databricks.com/aws/en/dev-tools/ci-cd
Retrieved: 2026-10-11

CI/CD on Databricks | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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

CI/CD On this page Last updated on Oct 7, 2026 
CI/CD on Databricks 
Continuous integration and continuous delivery (CI/CD) refers to the process of developing and delivering software in short, frequent cycles through the use of automation pipelines. CI/CD is common in software development, and is becoming increasingly necessary in data engineering and data science. By automating the building, testing, and deployment of code, development teams deliver releases more reliably than with manual processes. 
Databricks provides tools for developing CI/CD pipelines that support approaches that may differ between organizations due to unique aspects of their software development lifecycles. This page provides information about available tools for CI/CD pipelines on Databricks. 
For details about developer and CI/CD recommendations and best practices, see the following: 
CI/CD workflows on Databricks 
Developer best practices on Databricks 
How does Databricks support CI/CD for machine learning? 
High-level flow ​ 
A common flow for a Databricks CI/CD pipeline is: 
Version : Store your Databricks code and notebooks in a version control system like Git. This allows you to track changes over time and collaborate with other team members. 
Individual users use a Git folder to author and test changes before committing them to a Git repository. See CI/CD with Databricks Git folders . 
Optionally configure bundle Git settings . 
Code : Develop code and unit tests in a Databricks notebook in the workspace or locally using an IDE. 
Use the Lakeflow Pipelines Editor to develop pipelines in the workspace. 
Use the Databricks Visual Studio Code extension to develop and deploy local changes to Databricks workspaces. 
Build : Use Declarative Automation Bundles settings to automatically build certain artifacts during deployments. 
Configure the bundle configuration artifacts mapping. 
Pylint extended with the Databricks Labs pylint plugin helps enforce coding standards and detect bugs in your Databricks notebooks and application code. 
Deploy : Deploy changes to the Databricks workspace using Declarative Automation Bundles with tools like Azure DevOps , GitHub Actions , or Jenkins . 
Configure deployments using bundle deployment modes . 
For details about using Azure DevOps and Databricks, see Continuous integration and delivery on Databricks using Azure DevOps . 
For Databricks GitHub Actions examples, see GitHub Actions . 
To use Jenkins Pipeline with Databricks, see CI/CD with Jenkins on Databricks . 
Test : Develop and run automated tests to validate your code changes. 
Use tools like pytest to test your integrations. 
Run : Use the Databricks CLI with Declarative Automation Bundles to automate runs in your Databricks workspaces. 
Run bundle resources using databricks bundle run . 
Monitor : Monitor the performance of your code and production workloads in Databricks using tools such as jobs monitoring . This helps you identify and resolve any issues that arise in your production environment. 
Available tools ​ 
The following tools support CI/CD core principles: version all files and unify asset management, define infrastructure as code, isolate environments, automate testing, and monitor and automate rollbacks. 

Area 
Use these tools when you want to… 

Declarative Automation Bundles 
Programmatically define, deploy, and run Databricks resources, including Lakeflow Jobs, Lakeflow pipelines , and MLOps Stacks using CI/CD best practices and flows. 

Databricks Terraform provider 
Provision and manage Databricks workspaces and infrastructure using Terraform . For details on when to use the Databricks Terraform provider instead of Declarative Automation Bundles , see Developer tools use cases . 

Continuous integration and delivery on Databricks using Azure DevOps 
Develop a CI/CD pipeline for Databricks that uses Azure DevOps. 

GitHub Actions 
Include a GitHub Action developed for Databricks in your CI/CD flow. 

Git webhooks for app auto-deploy 
Automatically redeploy a Databricks app when you push to its configured Git branch. Databricks registers a webhook (a service hook on Azure DevOps) on the repository, so pushes deploy without a CI/CD workflow. 

CI/CD with Jenkins on Databricks 
Develop a CI/CD pipeline for Databricks that uses Jenkins. 

Orchestrate Lakeflow Jobs with Apache Airflow 
Manage and schedule a data pipeline that uses Apache Airflow. 

Service principals for CI/CD 
Use service principals, instead of users, with CI/CD. 

Authenticate access to Databricks using OAuth token federation 
Use workload identity federation for CI/CD authentication, which eliminates the need for Databricks secrets, making it the most secure way to authenticate to Databricks. ← ✕ 

Area 
Use these tools when you want to… 

Declarative Automation Bundles 
Programmatically define, deploy, and run Databricks resources, including Lakeflow Jobs, Lakeflow pipelines , and MLOps Stacks using CI/CD best practices and flows. 

Databricks Terraform provider 
Provision and manage Databricks workspaces and infrastructure using Terraform . For details on when to use the Databricks Terraform provider instead of Declarative Automation Bundles , see Developer tools use cases . 

Continuous integration and delivery on Databricks using Azure DevOps 
Develop a CI/CD pipeline for Databricks that uses Azure DevOps. 

GitHub Actions 
Include a GitHub Action developed for Databricks in your CI/CD flow. 

Git webhooks for app auto-deploy 
Automatically redeploy a Databricks app when you push to its configured Git branch. Databricks registers a webhook (a service hook on Azure DevOps) on the repository, so pushes deploy without a CI/CD workflow. 

CI/CD with Jenkins on Databricks 
Develop a CI/CD pipeline for Databricks that uses Jenkins. 

Orchestrate Lakeflow Jobs with Apache Airflow 
Manage and schedule a data pipeline that uses Apache Airflow. 

Service principals for CI/CD 
Use service principals, instead of users, with CI/CD. 

Authenticate access to Databricks using OAuth token federation 
Use workload identity federation for CI/CD authentication, which eliminates the need for Databricks secrets, making it the most secure way to authenticate to Databricks. 
Declarative Automation Bundles ​ 
Declarative Automation Bundles are the recommended approach to CI/CD on Databricks. Use Declarative Automation Bundles to describe Databricks resources such as jobs and pipelines as source files, and bundle them together with other assets to provide an end-to-end definition of a deployable project. These bundles of files can be source controlled, and you can use external CI/CD automation such as Github Actions to trigger deployments. 
Bundles includes many features such as custom templates for enforcing consistency and best practices across your organization, and comprehensive support for deploying the code files and configuration for many Databricks resources. Authoring a bundle requires some knowledge of bundle configuration syntax . 
For recommendations on how to use bundles in CI/CD, see CI/CD workflows on Databricks and Developer best practices on Databricks . 
Other tools for source control ​ 
As an alternative to applying full CI/CD with Declarative Automation Bundles , Databricks offers options to only source-control and deploy code files and notebooks. 

Git folder : Git folders can be used to reflect the state of a remote Git repository. You can create a git folder for production to manage source-controlled source files and notebooks. Then manually pull the Git folder to the latest state, or use external CI/CD tools such as GitHub Actions to pull the Git folder on merge. Use this approach when you don't have access to external CI/CD pipelines. 
This approach works for external orchestrators such as Airflow, but note that only the code files, such as notebooks and dashboard drafts, are in source control. Configurations for jobs or pipelines that run assets in the Git folder and configurations for publishing dashboards are not in source control. 

Git with jobs : Git with jobs enables you to configure some job types to use a remote Git repository as the source for code files. When a job run begins, Databricks takes a snapshot of the repository and runs all tasks against that version. This approach only supports limited job tasks, and only code files (notebooks and other files) are source-controlled. Job configurations such as task sequences, compute settings, and schedules are not source controlled, making this approach less suitable for multi-environment, cross-workspace deployments. 

Git with apps : Databricks Apps can deploy directly from a remote Git repository instead of uploading files to the workspace. You configure the repository on the app and deploy a branch, tag, or commit, so the running app is pinned to a specific commit. Pushes to the configured branch can automatically redeploy the app. This works with the databricks apps CLI or with Declarative Automation Bundles ( git_repository and git_source ). For a GitHub Actions example, see CI/CD for Databricks Apps with GitHub Actions . On this page 
High-level flow 
Available tools 
Declarative Automation Bundles 
Other tools for source control Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 