# cliRelease

Source: https://github.com/databricks/cli/releases/tag/v1.20.0
Retrieved: 2026-10-11

Release v1.20.0 · databricks/cli · GitHub Skip to content 
Navigation Menu Sign in Appearance settings 
Platform 
AI CODE CREATION 
GitHub Copilot Write better code with AI 
GitHub Copilot app Direct agents from issue to merge 
MCP Registry Integrate external tools 
DEVELOPER WORKFLOWS 
Actions Automate any workflow 
Codespaces Instant dev environments 
Issues Plan and track work 
Code Review Manage code changes 
Code Quality Enforce quality at merge 
APPLICATION SECURITY 
GitHub Advanced Security Find and fix vulnerabilities 
Code security Secure your code as you build 
Secret protection Stop leaks before they start 
EXPLORE 
Why GitHub 
Documentation 
Blog 
Changelog 
Marketplace View all features 
Solutions 
BY COMPANY SIZE 
Enterprises 
Small and medium teams 
Startups 
Nonprofits 
BY USE CASE 
App Modernization 
DevSecOps 
DevOps 
CI/CD 
View all use cases 
BY INDUSTRY 
Healthcare 
Financial services 
Manufacturing 
Government 
View all industries View all solutions 
Resources 
EXPLORE BY TOPIC 
AI 
Software Development 
DevOps 
Security 
View all topics 
EXPLORE BY TYPE 
Customer stories 
Events & webinars 
Ebooks & reports 
Business insights 
GitHub Skills 
SUPPORT & SERVICES 
Documentation 
Customer support 
Community forum 
Trust center 
Partners View all resources 
Open Source 
COMMUNITY 
GitHub Sponsors Fund open source developers 
PROGRAMS 
Security Lab 
Maintainer Community 
GitHub Stars 
Archive Program 
REPOSITORIES 
Topics 
Trending 
Collections 
Enterprise 
ENTERPRISE SOLUTIONS 
Enterprise platform AI-powered developer platform 
AVAILABLE ADD-ONS 
GitHub Advanced Security Enterprise-grade security features 
Copilot for Business Enterprise-grade AI features 
Premium Support Enterprise-grade 24/7 support 
Pricing Search / Sign in Sign up Appearance settings You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert {{ message }} 
databricks 
cli 
Repository navigation 

Code 
Issues 93 ( 93 ) 
Pull requests 234 ( 234 ) 
Actions 
Projects 
Security and quality 
Insights More items 
Releases 
v1.20.0 
v1.20.0 Latest Latest Compare 
Choose a tag to compare 

Sorry, something went wrong. Filter Loading 
Sorry, something went wrong. 
Uh oh! 

There was an error while loading. Please reload this page . 
No results found View all tags oss-cli released this 07 Oct 12:16 Immutable release. Only release title and notes can be modified. v1.20.0 5ed9313 This commit was created on GitHub.com and signed with GitHub’s verified signature . GPG key ID: B5690EEEBB952194 Verified Learn about vigilant mode . 
Release v1.20.0 
Notable Changes 
Remove the Terraform deployment engine. bundle.engine: terraform and DATABRICKS_BUNDLE_ENGINE=terraform now error, and a failed migration of existing Terraform state is reported as an error instead of falling back to Terraform. To keep deploying with Terraform, use Databricks CLI v1.19.x. ( #6888 , #6889 ) 
CLI 
databricks aitools install now supports Kiro, installing Databricks agent skills into its skills directory. ( #6908 ) 
Fixed databricks api corrupting integers larger than 2^53 (such as job and pipeline ids) — request bodies and responses now preserve them exactly. ( #6884 ) 
Added --auth-mode and --set <plugin>.<resourceKey>.authMode=obo|sp|both to databricks apps init so AppKit resources can be accessed on behalf of the user, by the service principal, or both. The default stays service principal. ( #6886 ) 
databricks apps init now requires a value for every field a service principal resource binding references, prompting for missing values in an interactive terminal and otherwise failing with the --set key to use, instead of creating a project with unset variables. ( #6903 ) 
Add databricks apps init --package-manager <npm|pnpm> to select the package manager for Node.js templates. Infer the default quietly from template lockfiles and AppKit version, check prerequisites before creating files, and preserve template formatting and pnpm version pins. ( #6902 ) 
Select npm or pnpm from packageManager declarations and lockfiles for apps validate and project validation during apps deploy . ( #6892 ) 
Fix auth docker host reporting the credential helper as configured when its executable is missing from PATH . ( #6880 ) 
Warn when the CLI binary was built more than 6 months ago and recommend updating. ( #6898 ) 
AI Runtime 
Add an experimental rank-partitioned container images to AI Runtime jobs. ( #6841 ) 
Support snapshot fields directly under code_source without requiring type or a nested snapshot block. ( #6927 ) 
Map AIR priority and Unity Catalog image fields when converting run configurations to bundles. ( #6905 ) 
Add workspace backend validation to air run --dry-run . ( #6934 ) 
Bundles 
Warn that bundle.terraform is deprecated and has no effect since the Terraform deployment engine was removed. ( #6940 ) 
Direct engine now detects and applies an explicitly configured zero-value boolean or float (e.g. gcp_attributes.use_preemptible_executors: false , azure_attributes.spot_bid_max_price: 0 ) added to a resource first deployed without the field, matching the existing handling of an explicit integer zero. ( #6882 ) 
Fix bundle deployment migrate failing with "no such file or directory" when the Terraform state has no resources or the configuration no longer declares any of them. ( #6958 ) 
bundle run and pipelines run now send the per-update development parameter for pipelines in development mode targets. Setting development on a pipeline is deprecated and now emits a warning; use mode: development instead. ( #6863 ) 
Remove the hidden bundle debug terraform command. ( #6933 ) 
Add support for run_as.group_name at the bundle and target levels for jobs and pipelines. ( #6676 ) 
Fix recreating a secret scope that was deleted outside of the bundle with the direct deployment engine. ( #6970 ) 
Accept title-case booleans ( True / False , as rendered by Azure Pipelines) for boolean variables, and accept the same boolean strings ( yes / no , on / off , ...) in Python bundles as in YAML. ( #6942 ) 
Dependency Updates 
Bump github.com/databricks/databricks-sdk-go from v0.182.0 to v0.185.0. ( #6928 ) Assets 17 Loading 
Uh oh! 

There was an error while loading. Please reload this page . All reactions 
Footer © 2026 GitHub, Inc. 
Footer navigation 
Terms 
Privacy 
Security 
Status 
Community 
Docs 
Contact 
Manage cookies 
Do not share my personal information You can’t perform that action at this time. 