# unifiedAuth

Source: https://docs.databricks.com/aws/en/dev-tools/auth/
Retrieved: 2026-10-11

Authorize access to Databricks resources | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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

Authenticate developer tools On this page Last updated on Oct 9, 2026 
Authorize access to Databricks resources 
This page explains how to authorize access to Databricks resources using the Databricks CLI and REST APIs. It describes different authorization methods, when to use them, and how to configure authentication for your use case. 
To access Databricks resources with the CLI or REST APIs, you must authenticate using a Databricks account with appropriate permissions. Your Databricks administrator or a user with administrator privileges configures the account. 
Account and API types ​ 
There are two types of accounts that you can use for authentication: 
User account: For interactive CLI commands and API calls. 
Service principal: For automated CLI commands and API calls without human interaction. 
Databricks has two types of APIs that require different authentication approaches: 
Account-level APIs: Available to account owners and admins, hosted on the account console URL. See account-level APIs . 
Workspace-level APIs: Available to workspace users and admins, hosted at workspace URLs. See workspace-level APIs . 
Authorization methods ​ 
Choose the authorization method that best fits your use case. Databricks tools and SDKs support multiple authorization methods, so you can select the most appropriate one for your scenario. 

Method 
Description 
Use case 

OAuth token federation (Recommended) 
OAuth tokens from your identity provider for users or service principals. 
Enables you to authenticate to Databricks without managing Databricks secrets. 

OAuth for service principals 
Short-lived OAuth tokens for service principals. 
To reduce the need for long-term credentials, use OAuth OBO to act as the service principal through the interactive (U2M) flow (recommended). See Authenticate as a service principal using OAuth OBO . For unattended, automated, and CI/CD workflows, use the M2M flow with a client ID and secret. 

OAuth for users (OAuth U2M) 
Short-lived OAuth tokens for users. 
Attended authentication scenario, where you use your web browser to authenticate with Databricks in real time, when prompted. ← ✕ 

Method 
Description 
Use case 

OAuth token federation (Recommended) 
OAuth tokens from your identity provider for users or service principals. 
Enables you to authenticate to Databricks without managing Databricks secrets. 

OAuth for service principals 
Short-lived OAuth tokens for service principals. 
To reduce the need for long-term credentials, use OAuth OBO to act as the service principal through the interactive (U2M) flow (recommended). See Authenticate as a service principal using OAuth OBO . For unattended, automated, and CI/CD workflows, use the M2M flow with a client ID and secret. 

OAuth for users (OAuth U2M) 
Short-lived OAuth tokens for users. 
Attended authentication scenario, where you use your web browser to authenticate with Databricks in real time, when prompted. 
Unified authentication ​ 
Databricks unified authentication provides a consistent way to configure authentication across all supported tools and SDKs. This approach uses standard environment variables and configuration profiles to store credential values, so you can run CLI commands or call APIs without repeatedly configuring authentication. 
Unified authentication handles account types differently: 
User authorization: OAuth automatically creates and manages access tokens for tools that support unified authentication. See Authorize user access to Databricks with OAuth . 
Service principal authorization: OAuth requires client credentials (client ID and secret) that Databricks provides after you assign the service principal to workspaces. See Authorize service principal access to Databricks with OAuth . 
To use OAuth access tokens, your Databricks workspace or account administrator must grant your user account or service principal the CAN USE permission for the account and workspace features that your code will access. 
Environment variables ​ 
To configure unified authentication, set the following environment variables. Some variables apply to both user and service principal authorization, while others are required only for service principals. 

Environment variable 
Description 

DATABRICKS_HOST 
The URL of either your Databricks account console ( http://accounts.cloud.databricks.com ) or your Databricks workspace URL ( https://{workspace-id}.cloud.databricks.com ). Choose based on the type of operations your code performs. 

DATABRICKS_ACCOUNT_ID 
Used for Databricks account operations. This is your Databricks account ID. To get it, see Locate your account ID . 

DATABRICKS_CLIENT_ID 
(Service principal OAuth only) The client ID you were assigned when creating your service principal . 

DATABRICKS_CLIENT_SECRET 
(Service principal OAuth only) The client secret you generated when creating your service principal . ← ✕ 

Environment variable 
Description 

DATABRICKS_HOST 
The URL of either your Databricks account console ( http://accounts.cloud.databricks.com ) or your Databricks workspace URL ( https://{workspace-id}.cloud.databricks.com ). Choose based on the type of operations your code performs. 

DATABRICKS_ACCOUNT_ID 
Used for Databricks account operations. This is your Databricks account ID. To get it, see Locate your account ID . 

DATABRICKS_CLIENT_ID 
(Service principal OAuth only) The client ID you were assigned when creating your service principal . 

DATABRICKS_CLIENT_SECRET 
(Service principal OAuth only) The client secret you generated when creating your service principal . 
Rather than setting environment variables manually, consider defining them in a Databricks configuration profile ( .databrickscfg ) on your client machine. 
Configuration profiles ​ 
Databricks configuration profiles contain settings and credentials that Databricks tools and SDKs need to authorize access. These profiles are stored in local client files (typically named .databrickscfg ) for your tools, SDKs, scripts, and apps to use. 
For more information, see Databricks configuration profiles . 
Third-party integrations ​ 
When integrating with third-party services and tools, you must use the authentication mechanisms provided by those services. However, Databricks provides support for common integrations: 
Databricks Terraform Provider: Access Databricks APIs from Terraform using your Databricks user account. See Provision a service principal by using Terraform . 
Git providers: GitHub, GitLab, and Bitbucket can access Databricks APIs using a Databricks service principal. See Service principals for CI/CD . 
Jenkins: Access Databricks APIs using a Databricks service principal. See CI/CD with Jenkins on Databricks . On this page 
Account and API types 
Authorization methods 
Unified authentication 
Environment variables 
Configuration profiles 
Third-party integrations Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 