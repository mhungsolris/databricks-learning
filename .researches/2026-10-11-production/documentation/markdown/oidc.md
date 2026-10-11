# oidc

Source: https://docs.databricks.com/aws/en/dev-tools/auth/provider-github
Retrieved: 2026-10-11

Enable workload identity federation for GitHub Actions | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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

Authenticate developer tools 
Authenticate using OAuth token federation 
Enable token federation for CI/CD 
GitHub Actions On this page Last updated on Oct 2, 2026 
Enable workload identity federation for GitHub Actions 
Databricks OAuth token federation, also known as OpenID Connect (OIDC), allows your automated workloads running outside of Databricks to securely access Databricks without Databricks secrets. See Authenticate access to Databricks using OAuth token federation . 
To enable workload identity federation for GitHub Actions: 
Create a federation policy 
Configure the GitHub Actions YAML file 
After you enable workload identity federation, the Databricks SDKs and the Databricks CLI automatically fetch workload identity tokens from GitHub and exchange them for Databricks OAuth tokens. 
Create a federation policy ​ 
First, create a workload identity federation policy. For instructions, see Configure a service principal federation policy . For GitHub, set the following values for the policy: 
Organization: The name of your GitHub organization. For example, if your repository URL is https://github.com/databricks-inc/data-platform , then the organization is databricks-inc . 
Repository: The name of the single repository to allow, such as data-platform . 
Entity type: The kind of GitHub entity represented in the sub (subject) claim of your token. The default is Branch . Databricks recommends using Environment , which you can enable by setting the environment attribute in your GitHub Actions YAML file. See Deploying to a specific environment . 
Issuer URL: https://token.actions.githubusercontent.com 
Subject: A string formed by concatenating values from the GitHub Actions job context. The required format depends on your repository's GitHub sub claim. See the following note. 
Audiences: Databricks recommends setting this to your Databricks account ID. If omitted, the account ID is used by default. 
Subject claim: (Optional) The JWT claim that contains the workload identity ( sub ) value from the OIDC token. For GitHub, leave the field as sub , which encodes the repository, branch, tag, pull/merge request, or environment that triggered the workflow. To authenticate as a reusable workflow rather than the calling repository, see Authenticate using a reusable workflow . note 
Databricks matches the Subject against the token's sub claim exactly, and GitHub's sub format depends on when the repository was created. Repositories created, renamed, or transferred on or after July 15, 2026 include numeric organization and repository IDs, such as repo:octo-org@123456/octo-repo@456789:environment:prod . Earlier repositories use repo:<org>/<repo>:environment:prod , unless they opt in to the immutable format. 
To find your repository's exact sub , see About security hardening with OpenID Connect . The immutable format isn't available on GitHub Enterprise Server. 
For example, the following Databricks CLI command creates a federation policy for an organization named my-org and a Databricks service principal numeric ID of 5581763342009999 . The example subject uses the name-only format for a repository created before July 15, 2026: Bash 
databricks account service-principal-federation-policy create 5581763342009999 --json '{ "oidc_policy": { "issuer": "https://token.actions.githubusercontent.com", "audiences": [ "a2222dd9-33f6-455z-8888-999fbbd77900" ], "subject": "repo:my-github-org/my-repo:environment:prod" } }' 
Configure the GitHub Actions YAML file ​ 
Next, configure the GitHub Actions YAML file. Set the following environment variables: 
DATABRICKS_AUTH_TYPE : github-oidc 
DATABRICKS_HOST : Your Databricks workspace URL 
DATABRICKS_CLIENT_ID : The service principal (application) ID YAML 
name : GitHub Actions Demo run-name : $ { { github.actor } } is testing out GitHub Actions 🚀 on : workflow_dispatch permissions : id-token : write contents : read jobs : my_script_using_wif : runs-on : ubuntu - latest environment : prod env : DATABRICKS_AUTH_TYPE : github - oidc DATABRICKS_HOST : https : //my - workspace.cloud.databricks.com/ DATABRICKS_CLIENT_ID : a1b2c3d4 - ee42 - 1eet - 1337 - f00b44r steps : - name : Checkout repository uses : actions/checkout@v4 - name : Install Databricks CLI uses : databricks/setup - cli@main - name : Run Databricks CLI commands run : databricks current - user me 
Authenticate using a reusable workflow ​ 
By default, the sub claim identifies the calling repository. To authenticate as a reusable workflow rather than the calling repository, set subject_claim to job_workflow_ref in the federation policy. Any team can invoke the reusable workflow, but only the reusable workflow itself authenticates with Databricks. 
Create a federation policy ​ 
Create a federation policy using job_workflow_ref as the subject claim. Set subject to the ref of your reusable workflow file: Bash 
databricks account service-principal-federation-policy create 5581763342009999 --json '{ "oidc_policy": { "issuer": "https://token.actions.githubusercontent.com", "audiences": [ "a2222dd9-33f6-455z-8888-999fbbd77900" ], "subject": "my-github-org/shared-workflows/.github/workflows/deploy.yml@refs/heads/main", "subject_claim": "job_workflow_ref" } }' 
Configure the GitHub Actions YAML files ​ 
Create a reusable workflow that authenticates with Databricks , and a calling workflow in any repository that invokes it. 
The following example shows a reusable workflow file ( .github/workflows/deploy.yml in the shared workflows repository): YAML 
on : workflow_call : jobs : deploy : runs-on : ubuntu - latest env : DATABRICKS_AUTH_TYPE : github - oidc DATABRICKS_HOST : https : //my - workspace.cloud.databricks.com/ DATABRICKS_CLIENT_ID : a1b2c3d4 - ee42 - 1eet - 1337 - f00b44r steps : - name : Checkout repository uses : actions/checkout@v4 - name : Install Databricks CLI uses : databricks/setup - cli@main - name : Run Databricks CLI commands run : databricks current - user me 
The following example shows a calling workflow in any repository that uses the reusable workflow: YAML 
on : workflow_dispatch permissions : id-token : write contents : read jobs : call-deploy : uses : my - github - org/shared - workflows/.github/workflows/deploy.yml@main note 
Set permissions: id-token: write on the calling workflow, not the reusable workflow. GitHub only includes the job_workflow_ref claim in the OIDC token when id-token: write is granted on the calling workflow. On this page 
Create a federation policy 
Configure the GitHub Actions YAML file 
Authenticate using a reusable workflow 
Create a federation policy 
Configure the GitHub Actions YAML files Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 