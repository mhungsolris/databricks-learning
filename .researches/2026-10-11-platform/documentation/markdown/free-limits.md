# free-limits

Source: https://docs.databricks.com/aws/en/getting-started/free-edition-limitations
Retrieved: 2026-10-11

Databricks Free Edition limitations | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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

Sign up for Databricks 
Free Edition 
Free Edition limitations On this page Last updated on Sep 29, 2026 
Databricks Free Edition limitations note 
Databricks Free Edition is a no-cost offering and does not include guaranteed reliability, support, or service-level agreements. Free Edition accounts include many of the latest Databricks releases, but some features may be limited or unavailable. If you would like access to the full Databricks platform, you must create a new Databricks account by starting a free trial . 
Databricks Free Edition is available at no cost to all qualified users. To keep it accessible to all, each account is subject to the Databricks fair usage policy. 
If you exceed your quota, your workspace's compute resources will be shut down and unavailable for the rest of the day (and in extreme cases, the rest of the month). While your compute will be unavailable, your data and settings will not be deleted. You’ll be able to resume your work when the limit resets. 
Compute limitations ​ 
Free Edition users only have access to serverless compute resources . Custom compute configurations are not supported. Additionally, outbound internet access is restricted to a limited set of trusted domains. 

Resource 
Limits 

Serverless compute for notebooks 
Limited compute size and usage. 

SQL warehouses 
One SQL warehouse, limited to a 2X-Small cluster size. 

Jobs 
Max of 5 concurrent job tasks per account. 

Lakeflow pipelines 
One active pipeline per pipeline type. 

Model serving endpoints 

Limits on the number of active endpoints 

No GPU serving endpoints 

No provisioned throughput 

No custom models on GPU or batch inference 

Certain models not available 

AI Search endpoints 
One AI Search endpoint, limited to one search unit. Additionally, Direct Vector Access in AI Search is not supported. 

Apps 
Up to 3 Databricks Apps per account. Apps run for up to 24 hours after being started, updated, or redeployed. After that, the app is automatically stopped to help manage resource usage. You can restart the app at any time. 

Lakebase 
One Lakebase project per account, with scale-to-zero compute. ← ✕ 

Resource 
Limits 

Serverless compute for notebooks 
Limited compute size and usage. 

SQL warehouses 
One SQL warehouse, limited to a 2X-Small cluster size. 

Jobs 
Max of 5 concurrent job tasks per account. 

Lakeflow pipelines 
One active pipeline per pipeline type. 

Model serving endpoints 

Limits on the number of active endpoints 

No GPU serving endpoints 

No provisioned throughput 

No custom models on GPU or batch inference 

Certain models not available 

AI Search endpoints 
One AI Search endpoint, limited to one search unit. Additionally, Direct Vector Access in AI Search is not supported. 

Apps 
Up to 3 Databricks Apps per account. Apps run for up to 24 hours after being started, updated, or redeployed. After that, the app is automatically stopped to help manage resource usage. You can restart the app at any time. 

Lakebase 
One Lakebase project per account, with scale-to-zero compute. 
For a full list of serverless compute limitations, see Serverless compute limitations . 
Unlock more with LinkedIn verification ​ 
Some Free Edition feature limits can be increased after you verify your identity using LinkedIn . LinkedIn verification helps Databricks confirm that your account belongs to a real individual, so that Databricks can safely provide higher usage limits while continuing to protect the platform from abuse. 
If your account is eligible, a Verify identity button appears in the top bar of your workspace, and remains there until your account is verified. 
To verify your identity: 
In the top bar of your workspace, click Verify identity . 
In the Verify you're a real person dialog, click Verify on LinkedIn . A new window opens for LinkedIn. If your browser blocks it, allow pop-up windows for the site, then try again. 
In the LinkedIn window, sign in and approve sharing your name, email, and verification status with Databricks. Databricks does not post on your behalf or access your connections. 
When verification succeeds, a notification confirms that you're verified and the Verify identity button no longer appears. 
If LinkedIn needs more information, it prompts you to finish verifying. Complete the steps on LinkedIn, then return to your workspace and try again. If LinkedIn verification isn't offered in your region or for your account type, you can continue to use Free Edition. For more information, see LinkedIn's verification help . 
After you verify, you get access to limited serverless GPU compute . note 
LinkedIn verification does not remove all Free Edition limitations. Enterprise-only features and administrative restrictions continue to apply. 
Unsupported features ​ 
The following features are not supported in Databricks Free Edition: 
R and Scala 
Custom workspace storage locations 
Online tables 
Clean rooms 
All legacy Databricks features 
Knowledge Assistant 
Administrative limitations ​ 
Free Edition accounts are meant for non-commercial use. Because of this, they have the following enterprise admin-related limits: 
One workspace and one metastore per account. 
No access to the account console or account-level APIs. 
No compliance enforcement, security customization, or private networking configurations. 
Authentication is limited to email OTP, Sign in with Google, and Sign in with Microsoft. No SSO or SCIM support. 
Additional limitations ​ 
Databricks may delete Free Edition accounts that are inactive for a prolonged period. 
Free Edition accounts are not covered by the Databricks support policy or Service Level Agreement (SLA). 
Free Edition accounts may not be used for commercial purposes. 
Free Edition accounts cannot become Databricks Marketplace providers. On this page 
Compute limitations 
Unlock more with LinkedIn verification 
Unsupported features 
Administrative limitations 
Additional limitations Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 