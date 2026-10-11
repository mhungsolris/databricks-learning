# direct

Source: https://docs.databricks.com/aws/en/dev-tools/bundles/direct
Retrieved: 2026-10-11

Migrate to the direct deployment engine | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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
Develop bundles 
Direct deployment engine On this page Last updated on Oct 7, 2026 
Migrate to the direct deployment engine 
Declarative Automation Bundles was originally built on top of the Databricks Terraform provider to manage deployments. However, Databricks CLI versions 0.279.0 and above support two different deployment engines: terraform and direct . The direct deployment engine provides significant advantages and does not depend on Terraform. 
New bundles created using Databricks CLI version 1.3.0 and above use the direct deployment engine by default. Bundles still using the Terraform deployment engine are automatically migrated to the direct engine, so no configuration is required. See Start using direct deployment . 
To prevent auto-migration, set bundle.engine: terraform or DATABRICKS_BUNDLE_ENGINE=terraform . This prevents auto-migration on all Databricks CLI versions. On Databricks CLI versions up to 1.19, the Terraform engine continues to be used. On Databricks CLI version 1.20.0 and above, it results in an error. See Direct deploy a new bundle . important 
In Databricks CLI version 1.20.0, the Terraform deployment engine was removed. The Databricks CLI can still auto-migrate bundles with Terraform state to the direct engine, but if the auto-migration fails, the deploy is aborted. To continue using the Terraform deployment engine, pin to Databricks CLI version 1.19 . See Declarative Automation Bundles will soon default to use the direct deployment engine . 
Direct deployment advantages ​ 
The new direct deployment engine uses the Databricks Go SDK and has the following benefits: 
Faster deployments : Bundle deployments are up to 40% faster. 
More powerful and detailed validation and planning : Detailed diffs of changes using bundle plan -o json reports per-field details explaining what triggered a given action. 
Replayable plans : bundle deploy --plan plan.json executes a previously created plan, ensuring that only approved actions reach production and faster deployments because plan calculation is skipped. 
Simple setup : Issues with firewalls, proxies, and custom provider registries are avoided. 
More resources : Additional resources such as catalogs, external locations, AI Search endpoints, and Genie spaces are supported. 
Immutable folders : Assets can optionally be deployed to an immutable, read-only folder for tamper protection and deployment consistency. See immutable_folder . 
Start using direct deployment ​ 
The direct deployment engine is the default for new bundles created with Databricks CLI version 1.3.0 and above. In Databricks CLI version 1.14 and above, bundles using the Terraform engine are automatically migrated to the direct engine on deploy. 
In Databricks CLI versions 1.8 and above, you can migrate a bundle to the direct engine by setting engine: direct . See Direct deploy a new bundle . 
Direct deploy a new bundle ​ 
To set the direct deployment engine explicitly, do either of the following: 

Set bundle.engine in your databricks.yml: YAML 
bundle : engine : direct 

Set the DATABRICKS_BUNDLE_ENGINE environment variable and deploy: Bash 
DATABRICKS_BUNDLE_ENGINE = direct databricks bundle deploy -t my_target 
If both the configuration and the environment variable are set, the configuration takes precedence. 
Deployment engine comparison ​ 
The new direct deployment engine mostly behaves the same as the Terrform deployment engine, but there are some differences. 
Resource state diff calculation ​ 
Unlike Terraform which maintains a single resource state (a mix of local configuration and remote state), the new engine keeps these separate and only records local configuration in its state file. 
The resources state diff calculation is done in two steps: 
The local bundle configuration is compared to the snapshot configuration used for the most recent deployment. The remote state plays no role. 
The remote state is compared to the snapshot configuration used for the most recent deployment. 
The result is that: 
databricks.yml resource changes are never ignored and will always trigger an update. 
Resource fields not handled by the implementation do not trigger an inconsistent result error. These resources are deployed successfully by the direct engine, but this can result in a drift. The deployed resources are updated during the next plan or deploy. 
Removed configuration settings ​ 
The two engines handle settings that you remove from your bundle configuration differently: 
With the Terraform engine, removing a set field from your databricks.yml leaves the corresponding value unchanged in the platform. Terraform only manages fields that are explicitly present in the configuration, so a removed field retains whatever value it had at the time of the last deployment. 
With the direct engine, removing a set field from your databricks.yml reverts the value to the resource's default. Because the direct engine compares your local configuration to the previous snapshot, a field that is no longer present is treated as a change, and the resource is updated to its default value on the next deployment. 
To persist a value, set it explicitly in your configuration rather than relying on the previously deployed value. 
Resource substitution lookup ​ 
Resource substitutions are available for resolving resource IDs, for example, ${resources.jobs.my_job.id} . See Substitutions . The resolution of resource substitutions in the direct deployment engine is performed in two steps: 
References pointing to fields that are present in the local config are resolved to the value provided in the local config. 
References that are not present in the local config are resolved from the remote state. This is the state fetched using the appropriate GET request for a given resource. 
The schema that is used to resolve a ${resource.*} substitution is in the file out.fields.txt . The fields marked as ALL and STATE can be used for local resolution. The fields marked as ALL or REMOTE can be used for remote resolution. 
Resource compatibility ​ 
The following resources require the direct deployment engine and are not supported with the Terraform deployment engine: 
Cluster policies 
Unity Catalog catalogs 
Unity Catalog external locations 
Unity Catalog secrets 
Genie spaces 
Instance pools 
Job runs 
AI Search endpoints 
MCP services 
Model provider services 
Model services 
Postgres snapshot schedules 
In addition, the lifecycle.started field is available only in the direct deployment engine, and only for apps , clusters , and sql_warehouses . When set to true , it deploys the resource in started mode. See lifecycle . On this page 
Direct deployment advantages 
Start using direct deployment 
Direct deploy a new bundle 
Deployment engine comparison 
Resource state diff calculation 
Removed configuration settings 
Resource substitution lookup 
Resource compatibility Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 