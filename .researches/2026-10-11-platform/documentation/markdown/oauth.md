# oauth

Source: https://docs.databricks.com/aws/en/dev-tools/auth/oauth-u2m
Retrieved: 2026-10-11

Authorize user access to Databricks with OAuth | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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
Authenticate as a user On this page Last updated on Oct 9, 2026 
Authorize user access to Databricks with OAuth 
This page explains how to authorize user access to Databricks resources when using the Databricks CLI or Databricks REST APIs. 
Databricks uses OAuth 2.0 as the preferred protocol for user authorization and authentication outside of the UI. Unified client authentication automates token generation and refresh. After a user signs in and grants consent, OAuth issues an access token for the CLI, SDK, or other tool to use on the user’s behalf. Each access token is valid for one hour, after which a new token is automatically requested. 
In this page, authorization refers to using OAuth to grant access to Databricks resources, while authentication refers to validating credentials through access tokens. 
For more high-level details, see Authorize access to Databricks resources . 
Ways to authorize access to Databricks resources ​ 
Databricks supports two ways to authorize user accounts with OAuth: 

Automatic (recommended): Use unified authentication if you're working with supported tools and SDKs, such as the Databricks Terraform SDK. This approach handles token generation and refresh automatically. 

Manual: Generate a code verifier and challenge, then exchange them for an OAuth token. Use this method if your tool doesn't support unified authentication. For details, see Manually generate OAuth U2M access tokens . 
Automatic authorization with unified authentication ​ note 
Before you configure authorization, review the ACL permissions for the type of workspace operations you plan to perform and confirm that your account has the required access level. For details, see Access control lists . 
To perform OAuth authorization with Databricks SDK s and tools that support unified authentication, integrate the following within your code: 
Environment 
Profile 
CLI 
VS Code 
Connect 
Terraform 
Python 
Java 
Go 
To use environment variables for a specific Databricks authentication type with a tool or SDK, see Authorize access to Databricks resources or the tool's or SDK's documentation. See also Environment variables and fields for unified authentication and the Authentication method priority . 
For account-level operations , set the following environment variables: 
DATABRICKS_HOST , set to the value of your Databricks account console URL, https://accounts.cloud.databricks.com . 
DATABRICKS_ACCOUNT_ID 
For workspace-level operations , set the following environment variables: 
DATABRICKS_HOST , set to the value of your Databricks workspace URL , for example https://dbc-a1b2345c-d6e7.cloud.databricks.com . 
Create or identify a Databricks configuration profile with the following fields in your .databrickscfg file. If you create the profile, replace the placeholders with the appropriate values. To use the profile with a tool or SDK, see Authorize access to Databricks resources or the tool's or SDK's documentation. See also Environment variables and fields for unified authentication and the Authentication method priority . 
For account-level operations , set the following values in your .databrickscfg file. In this case, the Databricks account console URL is https://accounts.cloud.databricks.com : 
[<some-unique-configuration-profile-name>] host       = <account-console-url> account_id = <account-id> 
For workspace-level operations , set the following values in your .databrickscfg file. In this case, the host is the Databricks workspace URL , for example https://dbc-a1b2345c-d6e7.cloud.databricks.com : 
[<some-unique-configuration-profile-name>] host = <workspace-url> 
For the Databricks CLI , run the databricks auth login command with the following options: 
For account-level operations , --host https://accounts.cloud.databricks.com --account-id <account-id> . 
For workspace-level operations , --host <workspace-url> . 
Then follow the instructions in your web browser to log in to your Databricks account or workspace. 
For more details, see OAuth authorization with the Databricks CLI . 
For the Databricks IDE extension , follow the steps in Set up authorization for the Databricks extension for Visual Studio Code . 
OAuth U2M authentication is supported in Databricks Connect for Python starting with Databricks Runtime 13.1 and for Scala starting with Databricks Runtime 13.3 LTS. 
For Databricks Connect , you can either: 
Use a config profile: Set workspace-level values in your .databrickscfg file as described on the Profile tab. Also set the cluster_id to your workspace instance URL. 
Use environment variables: Set the same values as shown on the Environment tab. Also set the DATABRICKS_CLUSTER_ID to your workspace instance URL. 
Values in .databrickscfg take precedence over environment variables. 
To initialize Databricks Connect with these settings, see Compute configuration for Databricks Connect . 
Before you apply your Terraform configuration, you must run one of the databricks auth login commands on the CLI tab depending on whether your configuration uses workspace or account operations. These commands generate and cache the required OAuth token at .databricks/token-cache.json in your user's home folder. Account-level operations ​ 
For default authentication: 
provider "databricks" { alias = "account" } 
For direct configuration: 
provider "databricks" { alias      = "account" host       = <retrieve-account-console-url> account_id = <retrieve-account-id> } 
Replace the retrieve- placeholders with your own implementation to retrieve the values from the console or some other configuration store, such as HashiCorp Vault . See also Vault Provider . In this example, you can set account_id to the Databricks account console URL. Workspace-level operations ​ 
For default authentication: 
provider "databricks" { alias = "workspace" } 
For direct configuration: 
provider "databricks" { alias = "workspace" host  = <retrieve-workspace-url> } 
Before you run your code, you must run the databricks auth login command on the CLI tab with either workspace or account operations options. These commands generate and cache the required OAuth token at .databricks/token-cache.json in your user's home folder. Account-level operations ​ 
For default authentication: Python 
from databricks . sdk import AccountClient a = AccountClient ( ) # ... 
For direct configuration: Python 
from databricks . sdk import AccountClient a = AccountClient ( host = retrieveAccountConsoleUrl ( ) , account_id = retrieveAccountId ( ) ) # ... 
Replace the retrieve placeholders with your own implementation to retrieve the values from the console or some other configuration store, such as AWS Systems Manager Parameter Store . Workspace-level operations ​ 
For default authentication: Python 
from databricks . sdk import WorkspaceClient w = WorkspaceClient ( ) # ... 
For direct configuration: Python 
from databricks . sdk import WorkspaceClient w = WorkspaceClient ( host = retrieve_workspace_url ( ) ) # ... 
For more information about authenticating with Databricks tools and SDKs that use Python and that implement Databricks unified authentication , see: 
Set up the Databricks Connect client for Python 
Set up authorization for the Databricks IDE extension 
Authenticate the Databricks SDK for Python with your Databricks account or workspace 
Before you run your code, you must run the databricks auth login command on the CLI tab with either workspace or account operations options. These commands generate and cache the required OAuth token at .databricks/token-cache.json in your user's home folder. Account-level operations ​ 
For default authentication: Java 
import com . databricks . sdk . AccountClient ; // ... AccountClient a = new AccountClient ( ) ; // ... 
For direct configuration: Java 
import com . databricks . sdk . AccountClient ; import com . databricks . sdk . core . DatabricksConfig ; // ... DatabricksConfig cfg = new DatabricksConfig ( ) . setHost ( retrieveAccountConsoleUrl ( ) ) . setAccountId ( retrieveAccountId ( ) ) ; AccountClient a = new AccountClient ( cfg ) ; // ... 
Replace the retrieve placeholders with your own implementation to retrieve the values from the console or some other configuration store, such as AWS Systems Manager Parameter Store . Workspace-level operations ​ 
For default authentication: Java 
import com . databricks . sdk . WorkspaceClient ; // ... WorkspaceClient w = new WorkspaceClient ( ) ; // ... 
For direct configuration: Java 
import com . databricks . sdk . WorkspaceClient ; import com . databricks . sdk . core . DatabricksConfig ; // ... DatabricksConfig cfg = new DatabricksConfig ( ) . setHost ( retrieveWorkspaceUrl ( ) ) WorkspaceClient w = new WorkspaceClient ( cfg ) ; // ... 
For more information about authorizing and authenticating with Databricks tools and SDKs that use Java and that implement Databricks unified authentication , see: 
Set up the Databricks Connect client for Scala (uses the Databricks SDK for Java for authentication) 
Authenticate the Databricks SDK for Java with your Databricks account or workspace 
Before you run your code, you must run the databricks auth login command on the CLI tab with either workspace or account operations options. These commands generate and cache the required OAuth token at .databricks/token-cache.json in your user's home folder. Account-level operations ​ 
For default authentication: Go 
import ( "github.com/databricks/databricks-sdk-go" ) // ... a := databricks . Must ( databricks . NewAccountClient ( ) ) // ... 
For direct configuration: Go 
import ( "github.com/databricks/databricks-sdk-go" ) // ... a := databricks . Must ( databricks . NewAccountClient ( & databricks . Config { Host : retrieveAccountConsoleUrl ( ) , AccountId : retrieveAccountId ( ) , } ) ) // ... 
Replace the retrieve placeholders with your own implementation to retrieve the values from the console or some other configuration store, such as AWS Systems Manager Parameter Store . Workspace-level operations ​ 
For default authentication: Go 
import ( "github.com/databricks/databricks-sdk-go" ) // ... w := databricks . Must ( databricks . NewWorkspaceClient ( ) ) // ... 
For direct configuration: Go 
import ( "github.com/databricks/databricks-sdk-go" ) // ... w := databricks . Must ( databricks . NewWorkspaceClient ( & databricks . Config { Host : retrieveWorkspaceUrl ( ) , } ) ) // ... 
For more information about authenticating with Databricks tools and SDKs that use Go and that implement Databricks client unified authentication , see Authenticate the Databricks SDK for Go with your Databricks account or workspace . 
Manually generate OAuth U2M access tokens ​ 
This section is for users working with third-party tools or services that don't support the Databricks unified authentication standard. If you need to manually generate, refresh, or use Databricks OAuth tokens for OAuth U2M authentication, follow the steps in this section. 
Step 1: Generate a code verifier and challenge ​ 
To generate OAuth U2M access tokens manually, start by creating a code verifier and a matching code challenge . You'll use the challenge in Step 2 to get an authorization code, and the verifier in Step 3 to exchange that code for an access token. note 
Follow the OAuth PKCE standard : 
The code verifier is a cryptographically random string (43–128 characters) using characters A–Z , a–z , 0–9 , -._~ . 
The code challenge is a Base64 URL-encoded SHA256 hash of the verifier. 
For more information, see Authorization Request . 
The following Python script generates a verifier and challenge. Although you can use them multiple times, Databricks recommends generating a new pair each time you manually generate access tokens. Python 
import hashlib , base64 , secrets , string # Allowed characters for the code verifier, per PKCE spec allowed_chars = string . ascii_letters + string . digits + "-._~" # Generate a secure code verifier (43–128 characters) code_verifier = '' . join ( secrets . choice ( allowed_chars ) for _ in range ( 64 ) ) # Create the SHA256 hash of the code verifier sha256_hash = hashlib . sha256 ( code_verifier . encode ( ) ) . digest ( ) # Base64-url-encode the hash and strip any trailing '=' padding code_challenge = base64 . urlsafe_b64encode ( sha256_hash ) . decode ( ) . rstrip ( "=" ) # Output values print ( f"code_verifier: { code_verifier } " ) print ( f"code_challenge: { code_challenge } " ) 
Step 2: Generate an authorization code ​ 
To get a Databricks OAuth access token, you must first generate an OAuth authorization code. This code expires immediately after use. You can generate the code at either the account or workspace level: 
Account level: Use to call both account-level and workspace-level REST APIs across all workspaces that your user can access. 
Workspace level: Use to call REST APIs within a single workspace. note 
These examples use databricks-cli as the client ID. If you're not using a built-in Databricks tool such as the CLI or SDKs, you must enable a custom OAuth application and use its client_id in your requests. See Enable or disable partner OAuth applications . Generate an account-level authorization code ​ 

Locate your account ID . 

In your browser, navigate to the URL with the following replacements: 
<account-id> : Your Databricks account ID 
<redirect-url> : A local redirect URI (for example, http://localhost:8020 ) 
<state> : Any plain-text string to validate the response 
<code-challenge> : The code challenge from Step 1 
https://accounts.cloud.databricks.com/oidc/accounts/<account-id>/v1/authorize ?client_id=databricks-cli &redirect_uri=<redirect-url> &response_type=code &state=<state> &code_challenge=<code-challenge> &code_challenge_method=S256 &scope=all-apis+offline_access 

Log in when prompted to access your Databricks account. 

After you sign in, the browser navigates to your redirect URL. If nothing is listening on that host and port (for example, http://localhost:8020 ), the page shows a connection error, which is expected. Copy the authorization code from the address bar. It's the substring after code= and before the next & in the query string. 
http://localhost:8020/?code=dcod...7fe6&state=<state> 
Verify that the state value matches what you originally provided. If it doesn’t, discard the code. 

Continue to Generate an account-level access token . Generate a workspace-level authorization code ​ 

In your browser, navigate to the URL with the following replacements: 
<databricks-instance> : Your <databricks-instance> with the Databricks workspace instance name , for example dbc-a1b2345c-d6e7.cloud.databricks.com 
<redirect-url> : A local redirect (for example, http://localhost:8020 ) 
<state> : Any plain-text value for response validation 
<code-challenge> : The challenge string from Step 1 
https://<databricks-instance>/oidc/v1/authorize ?client_id=databricks-cli &redirect_uri=<redirect-url> &response_type=code &state=<state> &code_challenge=<code-challenge> &code_challenge_method=S256 &scope=all-apis+offline_access 

Log in when prompted to access your Databricks account. 

After you sign in, the browser navigates to your redirect URL. If nothing is listening on that host and port (for example, http://localhost:8020 ), the page shows a connection error, which is expected. Copy the authorization code from the address bar. It’s the substring after code= and before the next & in the query string. 
http://localhost:8020/?code=dcod...7fe6&state=<state> 
Verify that the state value matches what you originally provided. If it doesn’t, discard the code. 

Continue to Generate a workspace-level access token . note 
To generate a token scoped to a role, add &assume_group=<group-id> to the authorization URL, where <group-id> is the ID of the role's backing group. The resulting token authorizes all operations as the role. See API (OAuth token exchange) . 
Step 3: Exchange the authorization code for an access token ​ 
To exchange the authorization code for a Databricks OAuth access token, choose the appropriate level: 
Account level: Use to call both account-level and workspace-level REST APIs across all workspaces your user can access. 
Workspace level: Use to call REST APIs within a single workspace. Generate an account-level access token ​ 

Use curl to exchange the account-level authorization code for an OAuth access token. 
Replace the following in the request: 
<account-id> : Your Databricks account ID 
<redirect-url> : The redirect URL from the previous step 
<code-verifier> : The verifier you generated earlier 
<authorization-code> : The authorization code from the previous step Bash 
curl --request POST \ https://accounts.cloud.databricks.com/oidc/accounts/ < account-id > /v1/token \ --data "client_id=databricks-cli" \ --data "grant_type=authorization_code" \ --data "scope=all-apis offline_access" \ --data "redirect_uri=<redirect-url>" \ --data "code_verifier=<code-verifier>" \ --data "code=<authorization-code>" 

Copy the access_token value from the response. For example: JSON 
{ "access_token" : "eyJr...Dkag" , "refresh_token" : "doau...f26e" , "scope" : "all-apis offline_access" , "token_type" : "Bearer" , "expires_in" : 3600 } 
The token is valid for one hour. 

Continue to Step 4: Call a Databricks REST API . Generate a workspace-level access token ​ 

Use curl to exchange the workspace-level authorization code for an OAuth access token. 
Replace the following in the request: 
<databricks-instance> : Your <databricks-instance> with the Databricks workspace instance name , for example dbc-a1b2345c-d6e7.cloud.databricks.com 
<redirect-url> : The redirect URL from the previous step 
<code-verifier> : The verifier you generated earlier 
<authorization-code> : The workspace-level authorization code Bash 
curl --request POST \ https:// < databricks-instance > /oidc/v1/token \ --data "client_id=databricks-cli" \ --data "grant_type=authorization_code" \ --data "scope=all-apis offline_access" \ --data "redirect_uri=<redirect-url>" \ --data "code_verifier=<code-verifier>" \ --data "code=<authorization-code>" 

Copy the access_token value from the response. For example: JSON 
{ "access_token" : "eyJr...Dkag" , "refresh_token" : "doau...f26e" , "scope" : "all-apis offline_access" , "token_type" : "Bearer" , "expires_in" : 3600 } 
The token is valid for one hour. 
Step 4: Call a Databricks REST API ​ 
Use the access token to call account-level or workspace-level REST APIs, depending on its scope. To call account-level APIs, your Databricks user must be an account admin. Example account-level REST API request ​ 
This example uses curl along with Bearer authentication to get a list of all workspaces associated with an account. 
Replace <oauth-access-token> with the account-level OAuth access token. 
Replace <account-id> with your account ID. Bash 
export OAUTH_TOKEN = < oauth-access-token > curl --request GET --header "Authorization: Bearer $OAUTH_TOKEN " \ "https://accounts.cloud.databricks.com/api/2.0/accounts/<account-id>/workspaces" Example workspace-level REST API request ​ 
This example uses curl along with Bearer authentication to list all available clusters in the specified workspace. 
Replace <oauth-access-token> with the account-level or workspace-level OAuth access token. 
Replace <databricks-instance> with the Databricks workspace instance name , for example dbc-a1b2345c-d6e7.cloud.databricks.com . Bash 
export OAUTH_TOKEN = < oauth-access-token > curl --request GET --header "Authorization: Bearer $OAUTH_TOKEN " \ "https://<databricks-instance>/api/2.0/clusters/list" 
Manage your OAuth consent ​ 
During the OAuth U2M authorization flow, your browser might display a consent screen asking you to approve the scopes requested by an application. You can view or revoke consent already granted. 
To view or revoke consent, you need the application's integration ID. If the application is a Databricks app , get the ID from the oauth2_app_client_id field by calling the Get an app REST API. To configure scopes for Databricks Apps , see Add scopes to an app . For other applications, contact your account admin. 
To view the scopes approved for an application: Bash 
curl --request GET \ --header "Authorization: Bearer $OAUTH_TOKEN " \ "https://<databricks-instance>/api/2.0/oauth-app-integrations/<app-integration-id>/user-consent/me" 
To revoke consent you granted to an application: Bash 
curl --request DELETE \ --header "Authorization: Bearer $OAUTH_TOKEN " \ "https://<databricks-instance>/api/2.0/oauth-app-integrations/<app-integration-id>/user-consent/me" note 
Revoking consent doesn't invalidate existing tokens. The application can still use existing refresh tokens to obtain new access tokens until those tokens expire. After expiration, the application can't initiate a new authorization flow to obtain fresh tokens. 
Replace the following: 
<databricks-instance> : Your <databricks-instance> with the Databricks workspace instance name , for example dbc-a1b2345c-d6e7.cloud.databricks.com 
<app-integration-id> : The application integration ID On this page 
Ways to authorize access to Databricks resources 
Automatic authorization with unified authentication 
Manually generate OAuth U2M access tokens 
Step 1: Generate a code verifier and challenge 
Step 2: Generate an authorization code 
Step 3: Exchange the authorization code for an access token 
Step 4: Call a Databricks REST API 
Manage your OAuth consent Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 