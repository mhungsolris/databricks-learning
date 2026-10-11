# github

Source: https://docs.databricks.com/aws/en/dev-tools/ci-cd/github
Retrieved: 2026-10-11

GitHub Actions | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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
GitHub Actions On this page Last updated on Oct 7, 2026 
GitHub Actions Preview 
This feature is in Public Preview . 
GitHub Actions trigger runs of your CI/CD flows from your GitHub repositories and allow you to automate your build, test, and deployment CI/CD pipeline. 
This page provides information about the GitHub Actions developed by Databricks and examples for common use cases. For information about other CI/CD features and best practices on Databricks, see the following: 
CI/CD on Databricks 
CI/CD workflows on Databricks 
Developer best practices on Databricks 
Databricks GitHub Actions ​ 
Databricks has developed the following GitHub Actions for your CI/CD workflows on GitHub. Add GitHub Actions YAML files to your repo's .github/workflows directory. note 
This article covers GitHub Actions , which is developed by a third party. To contact the provider, see GitHub Actions Support . 

GitHub Action 
Description 

databricks/setup-cli 
A composite action that sets up the Databricks CLI in a GitHub Actions workflow. ← ✕ 

GitHub Action 
Description 

databricks/setup-cli 
A composite action that sets up the Databricks CLI in a GitHub Actions workflow. note 
To deploy a Databricks app through CI/CD, see CI/CD for Databricks Apps with GitHub Actions . App workflows deploy from the app's Git repository ( git_source ) rather than uploading files. To automatically redeploy the app on every push without maintaining a workflow, use automatic Git deployments . 
Run a CI/CD workflow that updates a Git folder ​ 
The following example GitHub Actions YAML file updates a workspace Git folder when a remote branch updates. For information about the Git folder approach for CI/CD, see Other tools for source control . 
Requirements ​ 
This example uses workload identity federation for GitHub Actions for enhanced security, and requires that you have added a service principal in your account with a GitHub Actions federation policy. See Enable workload identity federation for GitHub Actions . important 
The federation policy subject (the identity of the federated token) must exactly match the expected token subject. For this example, the entity type and name is Environment and Prod . The constructed subject should be in the form repo:my-github-org-or-user/my-repo:environment:Prod . 
After you create a service principal with a federation policy, set the DATABRICKS_HOST environment variable to your Databricks host workspace and the DATABRICKS_CLIENT_ID environment variable to the service principal UUID. The DATABRICKS_AUTH_TYPE environment variable is set in the action. For information about Databricks environment variables, see Environment variables and fields for unified authentication . 
Create the Action ​ 
Now add a file .github/workflows/sync_git_folder.yml to your repository with the following YAML: YAML 
name : Sync Git Folder concurrency : prod_environment on : push : branches : # Set your base branch name here - git - folder - cicd - example permissions : # These permissions are required for workload identity federation. id-token : write contents : read jobs : deploy : runs-on : ubuntu - latest name : 'Update git folder' environment : Prod env : DATABRICKS_AUTH_TYPE : github - oidc DATABRICKS_HOST : $ { { vars.DATABRICKS_HOST } } DATABRICKS_CLIENT_ID : $ { { secrets.DATABRICKS_CLIENT_ID } } # This is the service principal UUID. steps : - uses : actions/checkout@v3 - uses : databricks/setup - cli@main - name : Update git folder # Set your workspace path and branch name here run : databricks repos update /Workspace/<git - folder - path > - - branch git - folder - cicd - example 
Run a CI/CD workflow with a bundle that runs a pipeline update ​ 
The following example GitHub Actions YAML file triggers a test deployment that validates, deploys, and runs the specified job in the bundle within a pre-production target named dev as defined within a bundle configuration file. 
Requirements ​ 
This example requires that there is: 

A user-defined environment variable DATABRICKS_BUNDLE_TARGET . 

A bundle configuration file at the root of the repository, which is explicitly declared through the GitHub Actions YAML file's setting working-directory: . This bundle configuration file should define a Databricks workflow named sample_job and a target named dev . For example: YAML 
# This is a bundle definition for pipeline_update. bundle : name : pipeline_update include : - resources/ *.yml variables : catalog : description : The catalog to use schema : description : The schema to use resources : jobs : sample_job : name : sample_job parameters : - name : catalog default : $ { var.catalog } - name : schema default : $ { var.schema } tasks : - task_key : refresh_pipeline pipeline_task : pipeline_id : $ { resources.pipelines.sample_pipeline.id } environments : - environment_key : default spec : environment_version : '4' pipelines : sample_pipeline : name : sample_pipeline catalog : $ { var.catalog } schema : $ { var.schema } serverless : true root_path : '../src/sample_pipeline' libraries : - glob : include : ../src/sample_pipeline/transformations/ ** environment : dependencies : - - - editable $ { workspace.file_path } targets : dev : mode : development default : true workspace : host : <dev - workspace - url > variables : catalog : my_catalog schema : $ { workspace.current_user.short_name } prod : mode : production workspace : host : <production - workspace - url > root_path : /Workspace/Users/someone@example.com/.bundle/$ { bundle.name } /$ { bundle.target } variables : catalog : my_catalog schema : prod permissions : - user_name : someone@example.com level : CAN_MANAGE 
For more information about bundle configuration, see Declarative Automation Bundles configuration . 

A GitHub secret named SP_TOKEN , representing the Databricks access token for a Databricks service principal that is associated with the Databricks workspace to which this bundle is being deployed and run. To create a token: 
Create a Databricks service principal. See Add service principals to your account . 
Generate a secret for the service principal. See Step 1: Create an OAuth secret . Copy the secret and client ID values. 
Manually generate a Databricks access token (account or workspace) using the copied secret and client ID values. See Generate an account-level access token . 
Copy the access_token value from the JSON response. Add a GitHub secret named SP_TOKEN to Actions in your repository and use the Databricks access token as the secret value. See Encrypted secrets . 
The DATABRICKS_TOKEN unified authentication environment variable is set in the action to the SP_TOKEN you configured. 
Create the Action ​ 
Now add a file .github/workflows/pipeline_update.yml to your repository with the following YAML: YAML 
# This workflow validates, deploys, and runs the specified bundle # within a pre-production target named "dev". name : 'Dev deployment' # Ensure that only a single job or workflow using the same concurrency group # runs at a time. concurrency : 1 # Trigger this workflow whenever a pull request is opened against the repo's # main branch or an existing pull request's head branch is updated. on : pull_request : types : - opened - synchronize branches : - main jobs : # Used by the "pipeline_update" job to deploy the bundle. # Bundle validation is automatically performed as part of this deployment. # If validation fails, this workflow fails. deploy : name : 'Deploy bundle' runs-on : ubuntu - latest steps : # Check out this repo, so that this workflow can access it. - uses : actions/checkout@v3 # Download the Databricks CLI. # See https://github.com/databricks/setup-cli - uses : databricks/setup - cli@main # Deploy the bundle to the "dev" target as defined # in the bundle's settings file. - run : databricks bundle deploy working-directory : . env : DATABRICKS_TOKEN : $ { { secrets.SP_TOKEN } } DATABRICKS_BUNDLE_TARGET : dev # Validate, deploy, and then run the bundle. pipeline_update : name : 'Run pipeline update' runs-on : ubuntu - latest # Run the "deploy" job first. needs : - deploy steps : # Check out this repo, so that this workflow can access it. - uses : actions/checkout@v3 # Use the downloaded Databricks CLI. - uses : databricks/setup - cli@main # Run the Databricks workflow named "sample_job" as defined in the # bundle that was just deployed. - run : databricks bundle run sample_job - - refresh - all working-directory : . env : DATABRICKS_TOKEN : $ { { secrets.SP_TOKEN } } DATABRICKS_BUNDLE_TARGET : dev 
You may also want to trigger production deployments. The following GitHub Actions YAML file can exist in the same repo as the preceding file. This file validates, deploys, and runs the specified bundle within a production target named “prod” as defined within a bundle configuration file. YAML 
# This workflow validates, deploys, and runs the specified bundle # within a production target named "prod". name : 'Production deployment' # Ensure that only a single job or workflow using the same concurrency group # runs at a time. concurrency : 1 # Trigger this workflow whenever a pull request is pushed to the repo's # main branch. on : push : branches : - main jobs : deploy : name : 'Deploy bundle' runs-on : ubuntu - latest steps : # Check out this repo, so that this workflow can access it. - uses : actions/checkout@v3 # Download the Databricks CLI. # See https://github.com/databricks/setup-cli - uses : databricks/setup - cli@main # Deploy the bundle to the "prod" target as defined # in the bundle's settings file. - run : databricks bundle deploy working-directory : . env : DATABRICKS_TOKEN : $ { { secrets.SP_TOKEN } } DATABRICKS_BUNDLE_TARGET : prod # Validate, deploy, and then run the bundle. pipeline_update : name : 'Run pipeline update' runs-on : ubuntu - latest # Run the "deploy" job first. needs : - deploy steps : # Check out this repo, so that this workflow can access it. - uses : actions/checkout@v3 # Use the downloaded Databricks CLI. - uses : databricks/setup - cli@main # Run the Databricks workflow named "sample_job" as defined in the # bundle that was just deployed. - run : databricks bundle run sample_job - - refresh - all working-directory : . env : DATABRICKS_TOKEN : $ { { secrets.SP_TOKEN } } DATABRICKS_BUNDLE_TARGET : prod 
Run a CI/CD workflow that builds a JAR and deploys a bundle ​ 
If you have a Java-based ecosystem, your GitHub Action needs to build and upload a JAR before deploying the bundle. The following example GitHub Actions YAML file triggers a deployment that builds and uploads a JAR to a volume, then validates and deploys the bundle to a production target named "prod" as defined within the bundle configuration file. It compiles a Java-based JAR, but the compilation steps for a Scala-based project are similar. 
Requirements ​ 
This example requires that there is: 
A bundle configuration file at the root of the repository, which is explicitly declared through the GitHub Actions YAML file's setting working-directory: . 
A DATABRICKS_TOKEN environment variable that represents the Databricks access token that is associated with the Databricks workspace to which this bundle is being deployed and run. 
A DATABRICKS_HOST environment variable that represents the Databricks host workspace. 
Create the Action ​ 
Now add a file .github/workflows/build_jar.yml to your repository with the following YAML: YAML 
name : Build JAR and deploy with bundles on : pull_request : branches : - main push : branches : - main jobs : build-test-upload : runs-on : ubuntu - latest steps : - name : Checkout code uses : actions/checkout@v4 - name : Set up Java uses : actions/setup - java@v4 with : java-version : '17' # Specify the Java version used by your project distribution : 'temurin' # Use a reliable JDK distribution - name : Cache Maven dependencies uses : actions/cache@v4 with : path : ~/.m2/repository key : $ { { runner.os } } - maven - $ { { hashFiles(' **/pom.xml') } } restore-keys : | ${{ runner.os }}-maven- - name : Build and test JAR with Maven run : mvn clean verify # Use verify to ensure tests are run - name : Databricks CLI Setup uses : databricks/setup - cli@v0.9.0 # Pin to a specific version - name : Upload JAR to a volume env : DATABRICKS_TOKEN : $ { { secrets.DATABRICKS_TOKEN } } DATABRICKS_HOST : $ { { secrets.DATABRICKS_HOST } } # Add host for clarity run : | databricks fs cp target/my-app-1.0.jar dbfs:/Volumes/artifacts/my-app-${{ github.sha }}.jar --overwrite validate : needs : build - test - upload runs-on : ubuntu - latest steps : - name : Checkout code uses : actions/checkout@v4 - name : Databricks CLI Setup uses : databricks/setup - cli@v0.9.0 - name : Validate bundle env : DATABRICKS_TOKEN : $ { { secrets.DATABRICKS_TOKEN } } DATABRICKS_HOST : $ { { secrets.DATABRICKS_HOST } } run : databricks bundle validate deploy : needs : validate if : github.event_name == 'push' && github.ref == 'refs/heads/main' # Only deploy on push to main runs-on : ubuntu - latest steps : - name : Checkout code uses : actions/checkout@v4 - name : Databricks CLI Setup uses : databricks/setup - cli@v0.9.0 - name : Deploy bundle env : DATABRICKS_TOKEN : $ { { secrets.DATABRICKS_TOKEN } } DATABRICKS_HOST : $ { { secrets.DATABRICKS_HOST } } run : databricks bundle deploy - - target prod 
Additional resources ​ 
QuickStart for GitHub Actions 
Understanding GitHub Actions 
Workflow syntax for GitHub Actions On this page 
Databricks GitHub Actions 
Run a CI/CD workflow that updates a Git folder 
Requirements 
Create the Action 
Run a CI/CD workflow with a bundle that runs a pipeline update 
Requirements 
Create the Action 
Run a CI/CD workflow that builds a JAR and deploys a bundle 
Requirements 
Create the Action 
Additional resources Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 