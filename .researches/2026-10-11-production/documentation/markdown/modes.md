# modes

Source: https://docs.databricks.com/aws/en/dev-tools/bundles/deployment-modes
Retrieved: 2026-10-11

Declarative Automation Bundles deployment modes | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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
Deployment modes On this page Last updated on Sep 11, 2026 
Declarative Automation Bundles deployment modes 
This page describes the syntax for Declarative Automation Bundles deployment modes. Bundles enable programmatic management of Databricks workflows. See What are Declarative Automation Bundles ? 
In CI/CD workflows, developers typically code, test, deploy, and run solutions in various phases, or modes . For example, the simplest set of modes includes a development mode for pre-production validation, followed by a production mode for validated deliverables. Declarative Automation Bundles provides an optional collection of default behaviors that correspond to each of these modes. 
Deployment modes are optional. You can deploy bundles without setting a mode or configuring presets . Deployment modes are a convenience for applying a group of commonly used settings at once. 
Development mode ​ 
To deploy your bundle in development mode, add the mode mapping, set to development , to the intended target. See bundle configuration targets mapping . For example, this target named dev is treated as a development target: YAML 
targets : dev : mode : development 
Deploying a target in development mode by running the databricks bundle deploy -t <target-name> command implements the following behaviors, which can be customized using presets : 
Prepends all resources that are not deployed as files or notebooks with the prefix [dev ${workspace.current_user.short_name}] and tags each deployed job and pipeline with a dev Databricks tag. 
Marks all related deployed Lakeflow pipelines as development: true . 
Enables the use of --cluster-id <cluster-id> in related calls to the bundle deploy command, which overrides any and all existing cluster definitions that are already specified in the related bundle configuration file. Instead of using --cluster-id <cluster-id> in related calls to the bundle deploy command, you can set the cluster_id mapping here, or as a child mapping of the bundle mapping, to the ID of the cluster to use. 
Pauses all schedules and triggers on deployed resources such as jobs or quality monitors. To unpause an individual job, set the pause_status to UNPAUSED for the mapping that defines how it runs. For example, schedule.pause_status for a scheduled job or continuous.pause_status for a continuous job. See job . 
Enables concurrent runs on all deployed jobs for faster iteration. Disable concurrent runs for an individual job by setting max_concurrent_runs to 1 . 
Disables the deployment lock for faster iteration. This lock prevents deployment conflicts which are unlikely to occur in dev mode. Re-enable the lock by setting bundle.deployment.lock.enabled to true . 
Production mode ​ 
To deploy your bundle in production mode, add the mode mapping, set to production , to the intended target. See bundle configuration targets mapping . For example, this target named prod is treated as a production target: YAML 
targets : prod : mode : production 
Deploying a target in production mode by running the databricks bundle deploy -t <target-name> command implements the following behaviors: 

Validates that all related deployed Lakeflow pipelines are marked as development: false . 

Validates that the current Git branch is equal to the Git branch that is specified in the target. Specifying a Git branch in the target is optional and can be done with an additional git property as follows: YAML 
git : branch : main 
This validation can be overridden by specifying --force while deploying. 

Databricks recommends that you use service principals for production deployments. You can enforce this by setting run_as to a service principal. See Service principals and Specify a run identity for a Declarative Automation Bundles workflow . If you do not use service principals, then note the following additional behaviors: 
Validates that artifact_path , file_path , root_path , or state_path mappings are not overridden to a specific user. 
Validates that the run_as and permissions mappings are specified to clarify which identities have specific permissions for deployments. 

Unlike the preceding behavior for setting the mode mapping to development , setting the mode mapping to production does not allow overriding any existing cluster definitions that are specified in the related bundle configuration file, for instance by using the --compute-id <cluster-id> option or the compute_id mapping. tip 
To guarantee that deployed assets can't be modified by non-admin users and that running jobs aren't affected by in-progress deployments, deploy your bundle to an immutable, read-only folder. See immutable_folder . 
Custom presets ​ 
Declarative Automation Bundles supports configurable presets for targets , which allows you to customize the behaviors for targets. For available presets, see the configuration reference . note 
Unless an exception is specified for a preset, if both mode and presets are set, presets override the default mode behavior, and settings of individual resources override the presets. For example: 
If the max_concurrent_runs for a job is 10, but the jobs_max_concurrent_runs preset is set to 20, the job's maximum concurrent runs is 10. 
If a schedule is set to UNPAUSED , but the trigger_pause_status preset is set to PAUSED , the schedule will be unpaused. 
The following example shows a custom presets configuration for the target named dev : YAML 
targets : dev : presets : name_prefix : 'testing_' # prefix all resource names with testing_ pipelines_development : true # set development to true for pipelines trigger_pause_status : PAUSED # set pause_status to PAUSED for all triggers and schedules jobs_max_concurrent_runs : 10 # set max_concurrent runs to 10 for all jobs tags : department : finance On this page 
Development mode 
Production mode 
Custom presets Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 