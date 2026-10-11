# oauthM2M

Source: https://docs.databricks.com/aws/en/dev-tools/auth/oauth-m2m
Retrieved: 2026-10-11

Authorize service principal access to Databricks with OAuth | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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
Authenticate as a service principal On this page Last updated on Oct 9, 2026 
Authorize service principal access to Databricks with OAuth 
This page explains how to authorize access to Databricks resources from unattended processes, such as automated CLI commands or REST API calls made from scripts or applications. 
Databricks uses OAuth 2.0 as the preferred protocol for service principal authorization and authentication outside of the UI. Unified client authentication automates token generation and refresh. When a service principal signs in and is granted consent, OAuth issues an access token for the CLI, SDK, or other tool to use on its behalf. Each access token is valid for one hour, after which a new token is automatically requested. 
In this page, authorization refers to using OAuth to grant a service principal access to Databricks resources, while authentication refers to validating credentials through access tokens. 
For more high-level details, see Authorize access to Databricks resources . 
Ways to authorize a service principal ​ 
Databricks supports the following ways to authorize a service principal: 

Automatic (recommended): Use unified authentication with supported tools and SDKs, such as the Databricks Terraform SDK. This approach handles token generation and refresh automatically, and is ideal for automation or other unattended workloads. 

Manual: Generate a code verifier and challenge, then exchange them for an OAuth token. Use this method if your tool or API doesn’t support unified authentication. You may need to build your own token refresh mechanism for your application. For details, see Manually generate OAuth M2M access tokens . 

OAuth OBO: Act as a service principal you manage through the standard user (U2M) OAuth flow, without an OAuth secret. Use this for interactive access when a person drives the session. See Authenticate as a service principal using OAuth OBO . 
Prerequisites ​ 
Before you configure OAuth, perform the following steps: 
Create a Databricks service principal. See Add service principals to your account . 
Go to the Configuration tab for the service principal and select the entitlements it should have for this workspace. 
Go to the Permissions tab and grant access to any Databricks users, service principals, and groups that you want to manage and use this service principal. See Who can manage and use service principals? . 
Authenticate as a service principal using OAuth OBO ​ Beta 
This feature is in Beta . 
OAuth on-behalf-of (OBO) lets you obtain a token that acts with a service principal's identity instead of your own user account, using the standard U2M OAuth flow. 
You must have the Service Principal Manager role on the service principal that you want to authenticate as. If you created the service principal, you have this role automatically. See Roles for managing service principals . 

Initiate the standard U2M flow. The following example uses the Databricks CLI : 
databricks auth login --host <workspace-url> 

A browser window opens for authorization. From the dropdown, select the service principal to authenticate as, then authorize the application. 

The OAuth token is issued with the service principal's identity. The sub claim in the token corresponds to the selected service principal. To view the token, run: 
databricks auth token --host <workspace-url> 
This flow works with any application that supports standard U2M authentication. For the complete steps, see Automatic authorization with unified authentication or Manually generate OAuth U2M access tokens . 
Authorize with OAuth M2M using a client ID and secret ​ 
For unattended workloads such as automation, scripts, and CI/CD, create an OAuth secret for the service principal and exchange it for short-lived access tokens using the client credentials (M2M) flow. 
Step 1: Create an OAuth secret ​ 
To authorize access to your Databricks resources with OAuth, you must create an OAuth secret. The secret is used to generate OAuth access tokens for authentication. A service principal can have up to five OAuth secrets, and each secret can be valid for up to two years. 
Account admins and workspace admins can create an OAuth secret for a service principal. 
Click your username in the top bar and select Settings . 
Click the Identity and access tab. 
Next to Service principals , click Manage . 
Select the service principal. 
Click the Secrets tab. 
Click Generate secret . 
Set the secret’s lifetime in days (maximum 730 days). 
Under Scopes , select the API scopes the secret can use. To restrict the secret, search for and select one or more scopes, such as sql or jobs . To let the secret access every API the service principal is authorized for, select all APIs (not recommended). See Scoped OAuth secrets . 
Click Generate . 
Copy the displayed secret and client ID, then click Done . The secret is shown only once. The client ID is the same as the service principal’s application ID. 
Account admins can also create an OAuth secret from the account console. From the User management tab, select the service principal, then go to the Credentials & secrets tab. note 
To enable the service principal to use clusters or SQL warehouses, you must give the service principal access to them. See Compute permissions or Manage a SQL warehouse . Scoped OAuth secrets ​ 
By default, an OAuth secret can access every API the service principal is authorized for ( all-apis ). A scoped secret restricts access to a specific set of API scopes, such as sql , jobs , or unity-catalog . An OAuth access token minted from a scoped secret can't exceed the secret’s scopes, which limits the impact if the secret is leaked or misused. Databricks recommends binding each secret to only the scopes its integration needs. 
A secret created without scopes, including every existing secret, keeps all-apis access and behaves as before. 
Scopes are set when you generate the secret and can’t be changed afterward. To use different scopes, generate a new secret. In the Secrets table, click Clone on an existing secret to create a new one with the same scopes and lifetime. warning 
A secret with the authentication scope can create new tokens with any scope. Bind this scope only to secrets that manage other credentials. 
For the full list of scopes and the API operations each one covers, see API scopes . 
Step 2: Use OAuth authorization ​ 
To use OAuth authorization with the unified authentication tool, you must set the following associated environment variables, .databrickscfg fields, Terraform fields, or Config fields: 
The Databricks host, specified as https://accounts.cloud.databricks.com for account operations or the target workspace URL , for example https://dbc-a1b2345c-d6e7.cloud.databricks.com for workspace operations. 
The Databricks account ID, for Databricks account operations. 
The service principal client ID. 
The service principal secret. 
To perform OAuth service principal authentication, integrate the following within your code, based on the participating tool or SDK: 
Environment 
Profile 
CLI 
Connect 
VS Code 
Terraform 
Python 
Java 
Go 
To use environment variables for a specific Databricks authentication type with a tool or SDK, see Authorize access to Databricks resources or the tool's or SDK's documentation. See also Environment variables and fields for unified authentication and the Authentication method priority . 
For account-level operations , set the following environment variables: 
DATABRICKS_HOST , set to the value of your Databricks account console URL, https://accounts.cloud.databricks.com . 
DATABRICKS_ACCOUNT_ID 
DATABRICKS_CLIENT_ID 
DATABRICKS_CLIENT_SECRET 
For workspace-level operations , set the following environment variables: 
DATABRICKS_HOST , set to the value of your Databricks workspace URL , for example https://dbc-a1b2345c-d6e7.cloud.databricks.com . 
DATABRICKS_CLIENT_ID 
DATABRICKS_CLIENT_SECRET 
Create or identify a Databricks configuration profile with the following fields in your .databrickscfg file. If you create the profile, replace the placeholders with the appropriate values. To use the profile with a tool or SDK, see Authorize access to Databricks resources or the tool's or SDK's documentation. See also Environment variables and fields for unified authentication and the Authentication method priority . 
For account-level operations , set the following values in your .databrickscfg file. In this case, the Databricks account console URL is https://accounts.cloud.databricks.com : 
[<some-unique-configuration-profile-name>] host          = <account-console-url> account_id    = <account-id> client_id     = <service-principal-client-id> client_secret = <service-principal-secret> 
For workspace-level operations , set the following values in your .databrickscfg file. In this case, the host is the Databricks workspace URL , for example https://dbc-a1b2345c-d6e7.cloud.databricks.com : 
[<some-unique-configuration-profile-name>] host          = <workspace-url> client_id     = <service-principal-client-id> client_secret = <service-principal-secret> 
For the Databricks CLI, do one of the following: 
Set the environment variables as specified on the Environment tab. 
Set the values in your .databrickscfg file as specified on the Profile tab. 
Environment variables always take precedence over values in your .databrickscfg file. 
See also OAuth machine-to-machine (M2M) authentication . note 
OAuth service principal authentication is supported on the following Databricks Connect versions: 
For Python, Databricks Connect for Databricks Runtime 13.1 and above. 
For Scala, Databricks Connect for Databricks Runtime 13.3 LTS and above. 
For Databricks Connect , you can either: 
Use a config profile: Set workspace-level values in your .databrickscfg file as described on the Profile tab. Also set the cluster_id to your workspace instance URL. 
Use environment variables: Set the same values as shown on the Environment tab. Also set the DATABRICKS_CLUSTER_ID to your workspace instance URL. 
Values in .databrickscfg take precedence over environment variables. 
To initialize Databricks Connect with these settings, see Compute configuration for Databricks Connect . 
For the Databricks IDE extension , do the following: 
Set the values in your .databrickscfg file for Databricks workspace-level operations as specified on the Profile tab. 
In the Configuration pane of the Databricks IDE extension , click Configure Databricks . 
In the Command Palette , for Databricks Host , enter your workspace URL , for example https://dbc-a1b2345c-d6e7.cloud.databricks.com , and then press Enter . 
In the Command Palette , select your target profile's name in the list for your URL. 
For more details, see Set up authorization for the Databricks IDE extension . Account-level operations ​ 
For default authentication: 
provider "databricks" { alias = "accounts" } 
For direct configuration: 
provider "databricks" { alias         = "accounts" host          = <retrieve-account-console-url> account_id    = <retrieve-account-id> client_id     = <retrieve-client-id> client_secret = <retrieve-client-secret> } 
Replace the retrieve placeholders with your own implementation to retrieve the values from the console or some other configuration store, such as HashiCorp Vault . See also Vault Provider . In this case, the Databricks account console URL is https://accounts.cloud.databricks.com . Workspace-level operations ​ 
For default configuration: 
provider "databricks" { alias = "workspace" } 
For direct configuration: 
provider "databricks" { alias         = "workspace" host          = <retrieve-workspace-url> client_id     = <retrieve-client-id> client_secret = <retrieve-client-secret> } 
Replace the retrieve placeholders with your own implementation to retrieve the values from the console or some other configuration store, such as HashiCorp Vault . See also Vault Provider . In this case, the host is the Databricks workspace URL , for example https://dbc-a1b2345c-d6e7.cloud.databricks.com . 
For more information about authenticating with the Databricks Terraform provider, see Authentication . Account-level operations ​ 
For default configuration: Python 
from databricks . sdk import AccountClient a = AccountClient ( ) # ... 
For direct configuration: Python 
from databricks . sdk import AccountClient a = AccountClient ( host = retrieve_account_console_url ( ) , account_id = retrieve_account_id ( ) , client_id = retrieve_client_id ( ) , client_secret = retrieve_client_secret ( ) ) # ... 
Replace the retrieve placeholders with your own implementation, to retrieve the values from the console or other configuration store, such as AWS Systems Manager Parameter Store . In this case, the Databricks account console URL is https://accounts.cloud.databricks.com . Workspace-level operations ​ 
For default configuration: Python 
from databricks . sdk import WorkspaceClient w = WorkspaceClient ( ) # ... 
For direct configuration: Python 
from databricks . sdk import WorkspaceClient w = WorkspaceClient ( host = retrieve_workspace_url ( ) , client_id = retrieve_client_id ( ) , client_secret = retrieve_client_secret ( ) ) # ... 
Replace the retrieve placeholders with your own implementation to retrieve the values from the console, or other configuration store, such as AWS Systems Manager Parameter Store . In this case, the host is the Databricks workspace URL , for example https://dbc-a1b2345c-d6e7.cloud.databricks.com . 
For more information about authenticating with Databricks tools and SDKs that use Python and implement unified authentication, see: 
Set up the Databricks Connect client for Python 
Set up authorization for the Databricks IDE extension 
Authenticate the Databricks SDK for Python with your Databricks account or workspace Account-level operations ​ 
For default configuration: Java 
import com . databricks . sdk . AccountClient ; // ... AccountClient a = new AccountClient ( ) ; // ... 
For direct configuration: Java 
import com . databricks . sdk . AccountClient ; import com . databricks . sdk . core . DatabricksConfig ; // ... DatabricksConfig cfg = new DatabricksConfig ( ) . setHost ( retrieveAccountConsoleUrl ( ) ) . setAccountId ( retrieveAccountId ( ) ) . setClientId ( retrieveClientId ( ) ) . setClientSecret ( retrieveClientSecret ( ) ) ; AccountClient a = new AccountClient ( cfg ) ; // ... 
Replace the retrieve placeholders with your own implementation to retrieve the values from the console, or other configuration store, such as AWS Systems Manager Parameter Store . In this case, the Databricks account console URL is https://accounts.cloud.databricks.com . Workspace-level operations ​ 
For default configuration: Java 
import com . databricks . sdk . WorkspaceClient ; // ... WorkspaceClient w = new WorkspaceClient ( ) ; // ... 
For direct configuration: Java 
import com . databricks . sdk . WorkspaceClient ; import com . databricks . sdk . core . DatabricksConfig ; // ... DatabricksConfig cfg = new DatabricksConfig ( ) . setHost ( retrieveWorkspaceUrl ( ) ) . setClientId ( retrieveClientId ( ) ) . setClientSecret ( retrieveClientSecret ( ) ) ; WorkspaceClient w = new WorkspaceClient ( cfg ) ; // ... 
Replace the retrieve placeholders with your own implementation to retrieve the values from the console, or other configuration store, such as AWS Systems Manager Parameter Store . In this case, the host is the Databricks workspace URL , for example https://dbc-a1b2345c-d6e7.cloud.databricks.com . 
For more information about authenticating with Databricks tools and SDKs that use Java and implement unified authentication, see: 
Set up the Databricks Connect client for Scala (the Databricks Connect client for Scala uses the included Databricks SDK for Java for authentication) 
Authenticate the Databricks SDK for Java with your Databricks account or workspace Account-level operations ​ 
Default configuration: Go 
import "github.com/databricks/databricks-sdk-go" // Uses environment configuration automatically a := databricks . Must ( databricks . NewAccountClient ( ) ) 
For direct configuration: Go 
import ( "github.com/databricks/databricks-sdk-go" ) // ... a := databricks . Must ( databricks . NewAccountClient ( & databricks . Config { Host : retrieveWorkspaceUrl ( ) , ClientId : retrieveClientId ( ) , ClientSecret : retrieveClientSecret ( ) , } ) ) // ... 
Replace the retrieve placeholders with your own implementation to retrieve the values from the console, or other configuration store, such as AWS Systems Manager Parameter Store . In this case, the Databricks account console URL is https://accounts.cloud.databricks.com . Workspace-level operations ​ 
For default configuration: Go 
import "github.com/databricks/databricks-sdk-go" // Uses environment configuration automatically w := databricks . Must ( databricks . NewWorkspaceClient ( ) ) 
For direct configuration: Go 
import "github.com/databricks/databricks-sdk-go" // ... w := databricks . Must ( databricks . NewWorkspaceClient ( & databricks . Config { Host : retrieveAccountConsoleUrl ( ) , ClientId : retrieveClientId ( ) , ClientSecret : retrieveClientSecret ( ) , } ) ) // ... 
Replace the retrieve placeholders with your own implementation to retrieve the values from the console, or other configuration store, such as AWS Systems Manager Parameter Store . In this case, the host is the Databricks workspace URL , for example https://dbc-a1b2345c-d6e7.cloud.databricks.com . 
For more information about authenticating with Databricks tools and SDKs that use Go and that implement Databricks client unified authentication , see Authenticate the Databricks SDK for Go with your Databricks account or workspace . 
Manually generate OAuth M2M access tokens ​ 
This section is for tools or services that don't support Databricks unified authentication . If you need to manually generate, refresh, or use Databricks OAuth tokens for M2M authentication, follow these steps. 
To generate an OAuth M2M access token, use the service principal’s client ID and OAuth secret. Each access token is valid for one hour. After it expires, request a new token. You can generate tokens at either the account or workspace level: 
Account level: Use to call both account-level and workspace-level REST APIs in accounts and workspaces the service principal can access. See Generate an account-level access token . 
Workspace level: Use to call REST APIs within a single workspace. See Generate a workspace-level access token . 
Generate an account-level access token ​ 
Use an account-level token to call REST APIs for the account and any workspaces the service principal can access. 

Locate your account ID . 

Construct the token endpoint URL by replacing <account-id> in the following URL with your account ID. 
https://accounts.cloud.databricks.com/oidc/accounts/<my-account-id>/v1/token 

Use curl to request an OAuth access token. Replace: 
<token-endpoint-URL> with the URL above. 
<client-id> with the service principal’s client ID (application ID). 
<client-secret> with the service principal’s OAuth secret. Bash 
export CLIENT_ID = < client-id > export CLIENT_SECRET = < client-secret > curl --request POST \ --url < token-endpoint-URL > \ --user " $CLIENT_ID : $CLIENT_SECRET " \ --data 'grant_type=client_credentials&scope=all-apis' 
This generates a response similar to: JSON 
{ "access_token" : "eyJraWQiOiJkYTA4ZTVjZ…" , "token_type" : "Bearer" , "expires_in" : 3600 } 
The all-apis scope requests an OAuth access token that allows the service principal to call any Databricks REST API it has permission to access. 

Copy the access_token value from the response. 
Generate a workspace-level access token ​ 
Use a workspace-level token only with REST APIs in that workspace. 

Construct the token endpoint URL by replacing <databricks-instance> with your <databricks-instance> with the Databricks workspace instance name , for example dbc-a1b2345c-d6e7.cloud.databricks.com : 
https://<databricks-instance>/oidc/v1/token 

Use curl to request an OAuth access token. Replace: 
<token-endpoint-URL> with the URL above. 
<client-id> with the service principal’s client ID (application ID). 
<client-secret> with the service principal’s OAuth secret. Bash 
export CLIENT_ID = < client-id > export CLIENT_SECRET = < client-secret > curl --request POST \ --url < token-endpoint-URL > \ --user " $CLIENT_ID : $CLIENT_SECRET " \ --data 'grant_type=client_credentials&scope=all-apis' 
This generates a response similar to: JSON 
{ "access_token" : "eyJraWQiOiJkYTA4ZTVjZ…" , "token_type" : "Bearer" , "expires_in" : 3600 } 

Copy the access_token value from the response. note 
To generate a token for a serving endpoint, include the endpoint ID and action in your request. See Fetch an OAuth token manually . 
Assume a role ​ 
A service principal can assume a role when it requests a workspace-level access token. When a service principal assumes a role, the role's permissions replace the service principal's own. In Databricks , a role is implemented as a group, and the service principal must have Assume permission on that group. For more information, see Role-based access control (RBAC) . 
To assume a role, add the assume_group parameter to the token request: Bash 
export CLIENT_ID = < client-id > export CLIENT_SECRET = < client-secret > curl --request POST \ --url < token-endpoint-URL > \ --user " $CLIENT_ID : $CLIENT_SECRET " \ --data 'grant_type=client_credentials&scope=all-apis&assume_group=<group-id>' 
Replace <group-id> with the numeric ID of the role's backing group. 
Assuming a role has the following requirements and limitations: 
Supported only for workspace-level tokens. If you include assume_group in an account-level token request, the request fails. 
The service principal must have Assume permission on the group. If it does not, the request fails. To grant Assume, see Manage permissions on a group . 
For more information about switching roles, see Switch roles . 
Call a Databricks REST API ​ 
Use the OAuth access token to call account-level or workspace-level REST APIs. To call account-level APIs, the service principal must be an account admin. 
Include the token in the authorization header with Bearer authentication. Example account-level REST API request ​ 
This example lists all workspaces for an account. Replace: 
<oauth-access-token> with the service principal’s OAuth access token. 
<account-id> with your account ID. Bash 
export OAUTH_TOKEN = < oauth-access-token > curl --request GET --header "Authorization: Bearer $OAUTH_TOKEN " \ 'https://accounts.cloud.databricks.com/api/2.0/accounts/<account-id>/workspaces' Example workspace-level REST API request ​ 
This example lists all available clusters in a workspace. Replace: 
<oauth-access-token> with the service principal’s OAuth access token. 
<databricks-instance> with the Databricks workspace instance name , for example dbc-a1b2345c-d6e7.cloud.databricks.com . Bash 
export OAUTH_TOKEN = < oauth-access-token > curl --request GET --header "Authorization: Bearer $OAUTH_TOKEN " \ 'https://<workspace-URL>/api/2.0/clusters/list' 
Troubleshoot OAuth M2M authentication ​ 
Use these steps to fix the most common issues with Databricks OAuth M2M authentication for service principals. 
Quick checks ​ 
Start by verifying these common configuration issues that cause OAuth M2M authentication failures: 
Credentials: DATABRICKS_CLIENT_ID is set to the service principal's application ID (client ID), and DATABRICKS_CLIENT_SECRET is set to the OAuth secret value, both with no extra spaces. 
Host: DATABRICKS_HOST points to https://accounts.cloud.databricks.com for account operations or the target workspace URL , for example https://dbc-a1b2345c-d6e7.cloud.databricks.com for workspace operations. Do not include /api . 
Assignment: The service principal is assigned to the target workspace. 
Permissions: The service principal has the required permissions on the target resource. 
Conflicts: No conflicting variables set such as DATABRICKS_TOKEN , DATABRICKS_USERNAME . Run env | grep DATABRICKS and unset conflicts. 
Tools: Use unified authentication and current CLI or SDK versions. 
401 Unauthorized ​ 
Likely causes and fixes: 
Bad client ID or secret: Re-copy DATABRICKS_CLIENT_ID and DATABRICKS_CLIENT_SECRET . Regenerate the secret if unsure. 
Expired secret: Create a new secret if the current one is expired. 
Wrong token issuer: For M2M, use the Databricks OAuth token endpoint, not your IdP or cloud token endpoint. 
Host mismatch: If you authenticate for workspace APIs, DATABRICKS_HOST must be the workspace URL you call. 
403 Forbidden ​ 
Likely causes and fixes: 
Missing resource permissions: Grant the service principal CAN USE or CAN MANAGE on clusters or SQL warehouses, and the required object-level permissions for notebooks, jobs, or data objects. 
No workspace assignment: Assign the service principal to the workspace in the account console. 
Admin API access: For admin-only APIs, assign the service principal to the workspace admin group or grant account admin permissions. 
Configuration problems ​ 
Symptoms include timeouts, “host not found,” “account not found,” or “workspace not found.” 
Fixes: 
Host rules: Use the account console URL for account APIs. Use the workspace URL for workspace APIs. Don't include the /api suffix. 
Account ID: Supply DATABRICKS_ACCOUNT_ID only for account-level operations. Use the UUID from the account console. 
Profile selection: If you use multiple profiles, pass --profile <name> or set DATABRICKS_CONFIG_PROFILE . 
Connectivity ​ 
If OAuth M2M authentication fails due to network issues, use these tests to verify that your environment can reach Databricks endpoints: 
DNS: nslookup <your-host> (should return IP addresses for the hostname) 
TLS and reachability: curl -I https://<your-host> (should return HTTP status 200, 401, or 403) 
Corporate network: Confirm that proxy or firewall rules allow HTTPS to Databricks endpoints 
Additional resources ​ 
Service principals 
Overview of the Databricks identity model 
Additional information about authentication and access control On this page 
Ways to authorize a service principal 
Prerequisites 
Authenticate as a service principal using OAuth OBO 
Authorize with OAuth M2M using a client ID and secret 
Step 1: Create an OAuth secret 
Step 2: Use OAuth authorization 
Manually generate OAuth M2M access tokens 
Generate an account-level access token 
Generate a workspace-level access token 
Assume a role 
Call a Databricks REST API 
Troubleshoot OAuth M2M authentication 
Quick checks 
401 Unauthorized 
403 Forbidden 
Configuration problems 
Connectivity 
Additional resources Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 