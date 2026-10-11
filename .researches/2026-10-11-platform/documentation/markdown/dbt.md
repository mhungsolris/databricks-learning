# dbt

Source: https://docs.getdbt.com/docs/build/models
Retrieved: 2026-10-11

About dbt models | dbt Developer Hub Skip to main content Relive the best of dbt Summit! Get access to the keynotes and breakout sessions from dbt Summit 2026. See the latest product innovations from dbt, and hear how data teams are leveling up for the agentic era. dbt version ▾ 
v2 
v1 
1.12 
1.11 
On dbt platform? v2 = dbt v2 release tracks v1 = dbt v1 release tracks Docs 
Product docs 
References 
Best practices 
Developer blog Guides APIs Help 
Release notes 
FAQs 
Support and billing 
Licensing 
Courses Community 
Join the dbt Community 
Become a contributor 
Community forum 
Webinars 
Events Account 
Log in to dbt 
Create a free account Get started with dbt Search 
About 
About dbt 
Get started 
Feature availability 
Supported features 
dbt releases 
About the dbt platform 
Supported data platforms 
Get started 
dbt Quickstarts 
Get started with dbt 
AI and dbt 
About AI and dbt 
dbt Wizard 
Skills from packages 
dbt Copilot 
dbt MCP server 
dbt AI FAQs 
Build and develop 
Develop with dbt 
Build dbt projects 
About dbt projects 
About static analysis 
About dbt Information Schema 
dbt tips and tricks 
Build your DAG 
Models 
About dbt models 
SQL models 
Python models 
Tests 
Checks 
Documentation 
Snapshots 
Seeds 
Jinja and macros 
User-defined functions 
Sources 
Exposures 
Groups 
Analyses 
Build your metrics 
Enhance your models 
Enhance your code 
Organize your outputs 
Optimize development 
Build dbt Mesh 
Deploy and explore 
Deploy dbt 
Optimize builds with dbt State 
Explore your data 
Use the dbt Semantic Layer 
Compute 
About Lake Compute 
Onboarding to Lake Compute 
Lake Compute FAQs 
Business intelligence 
dbt Charts 
Additional tools 
dbt integrations 
Release information 
Available dbt versions 
dbt release notes 


Build dbt projects 
Build your DAG Copy page Copy page Copy page as Markdown for LLMs View as Markdown View this page as plain Markdown Open in ChatGPT Ask questions about this page Open in Claude Ask questions about this page Open in Perplexity Ask questions about this page On this page 
About dbt models 
Self-hosted and cloud-hosted dbt are composed of different moving parts working harmoniously. All of them are important to what dbt does — transforming data—the 'T' in ELT. When you execute dbt run , you are running a model that will transform your data without that data ever leaving your warehouse. 
Models are where your developers spend most of their time within a dbt environment. Models are primarily written as a select statement and saved as a .sql file. While the definition is straightforward, the complexity of the execution will vary from environment to environment.  Models will be written and rewritten as needs evolve and your organization finds new ways to maximize efficiency. 
SQL is the language most dbt users will utilize, but it is not the only one for building models. Starting in version 1.3, dbt v1 and dbt support Python models. Python models are useful for training or deploying data science models, complex transformations, or where a specific Python package meets a need — such as using the dateutil library to parse dates. 
Models and modern workflows ​ 
The top level of a dbt workflow is the project. A project is a directory of a .yml file (the project configuration) and either .sql or .py files (the models). The project file tells dbt the project context, and the models let dbt know how to build a specific data set. For more details on projects, refer to About dbt projects . 
Your organization may need only a few models, but more likely you’ll need a complex structure of nested models to transform the required data. A model is a single file containing a final select statement, and a project can have multiple models, and models can even reference each other. Add to that, numerous projects and the level of effort required for transforming complex data sets can improve drastically compared to older methods. 
Learn more about models in SQL models and Python models pages. If you'd like to begin with a bit of practice, visit our Getting Started Guide for instructions on setting up the Jaffle_Shop sample data so you can get hands-on with the power of dbt. 
Was this page helpful? Yes No Privacy policy Create a GitHub issue 
This site is protected by reCAPTCHA and the Google Privacy Policy and Terms of Service apply. 0 Edit this page Last updated on Sep 8, 2026 Next SQL models Get started 
Start building with dbt. 
The free dbt VS Code extension is the best way to develop locally with dbt. Install free extension Request your demo Resources VS Code Extension Resource Hub dbt Learn Certification Developer Blog Community Join the Community Become a Contributor Open Source dbt Packages Community Forum Support Contact Support Professional Services Find a Partner System Status Connect with Us © 2026 dbt Labs, LLC. All Rights Reserved. Terms of Service Privacy Policy Security Cookie Settings 