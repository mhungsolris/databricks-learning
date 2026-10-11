# flows

Source: https://docs.databricks.com/aws/en/dev-tools/ci-cd/flows
Retrieved: 2026-10-11

CI/CD workflows on Databricks | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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
CI/CD workflows On this page Last updated on Sep 11, 2026 
CI/CD workflows on Databricks 
CI/CD (Continuous Integration and Continuous Delivery) has become a cornerstone of modern data engineering and analytics, as it ensures that code changes are integrated, tested, and deployed rapidly and reliably. Databricks recognizes that you may have diverse CI/CD requirements shaped by your organizational preferences, existing workflows, and specific technology environment, and provides a flexible framework that supports various CI/CD options. 
This page describes recommended CI/CD workflows to help you design and build robust, customized CI/CD pipelines that align with your unique needs and constraints. By leveraging these insights, you can accelerate your data engineering and analytics initiatives, improve code quality, and reduce the risk of deployment failures. 
Core principles of CI/CD ​ 
Effective CI/CD pipelines share foundational principles regardless of implementation specifics. The following universal best practices apply across organizational preferences, developer workflows, and cloud environments, and ensure consistency across diverse implementations, whether your team prioritizes notebook-first development or infrastructure-as-code workflows. Adopt these principles as guardrails while tailoring specifics to your organization's technology stack and processes. 
Version control everything 
Store notebooks, scripts, infrastructure definitions (IaC), and job configurations in Git. 
Use branching strategies, such as Gitflow, that are aligned with standard development, staging, and production deployment environments. 
Automate testing 
Implement unit tests for business logic using libraries, such as pytest for Python and ScalaTest for Scala. 
Validate notebook and workflow functionality with tools, such as Databricks CLI bundle validate . 
Use integration tests for workflows and data pipelines, such as chispa for Spark DataFrames. 
Employ Infrastructure as Code (IaC) 
Define clusters, jobs, and workspace configurations with Declarative Automation Bundles YAML or Terraform . 
Parameterize instead of hardcoding environment-specific settings, such as cluster size and secrets. 
Isolate environments 
Maintain separate workspaces for development, staging, and production. 
Use MLflow Model Registry for model versioning across environments. 
Choose tools that match your cloud ecosystem: 
Azure: Azure DevOps and Declarative Automation Bundles or Terraform. 
AWS: GitHub Actions and Declarative Automation Bundles or Terraform. 
GCP: Cloud Build and Declarative Automation Bundles or Terraform. 
Monitor and automate rollbacks 
Track deployment success rates, job performance, and test coverage. 
Implement automated rollback mechanisms for failed deployments. 
Unify asset management 
Use Declarative Automation Bundles to deploy code, jobs, and infrastructure as a single unit. Avoid siloed management of notebooks, libraries, and workflows. note 
Databricks recommends workload identity federation for CI/CD authentication. Workload identity federation eliminates the need for Databricks secrets, which makes it the most secure way to authenticate your automated flows to Databricks. See Enable workload identity federation in CI/CD . 
Declarative Automation Bundles for CI/CD ​ 
Declarative Automation Bundles (formerly known as Databricks Asset Bundles) offer a powerful, unified approach to managing code, workflows, and infrastructure within the Databricks ecosystem and are recommended for your CI/CD pipelines. By bundling these elements into a single YAML-defined unit, bundles simplify deployment and ensure consistency across environments. However, for users accustomed to traditional CI/CD workflows, adopting bundles may require a shift in mindset. 
For example, Java developers are used to building JARs with Maven or Gradle, running unit tests with JUnit, and integrating these steps into CI/CD pipelines. Similarly, Python developers often package code into wheels and test with pytest, while SQL developers focus on query validation and notebook management. With bundles, these workflows converge into a more structured and prescriptive format, emphasizing bundling code and infrastructure for seamless deployment. 
The following sections explore how developers can adapt their workflows to leverage bundles effectively. 
To quickly get started with Declarative Automation Bundles , try a tutorial: Develop a job with Declarative Automation Bundles or Develop pipelines with Declarative Automation Bundles . 
Source control ​ 
Bundles enable you to easily contain everything - source code, build artifacts, and configuration files - and locate them in the same source code repository, but you can also separate bundle configuration files from code-related files. The choice depends on your team's workflow, project complexity, and CI/CD requirements, but to simplify workflows and best practices sharing, Databricks recommends that you use a single repository for both code and bundle configuration. 
In addition, Databricks recommends a trunk-based branching strategy to minimize merge conflicts and ensure the main branch is always in a deployable state, and always use versioned artifacts, such as Git commit hashes, when uploading to Databricks or external storage to ensure traceability and rollback capabilities. 
For more information about these best practices, see Source control . 
CI/CD workflow with bundles ​ 
A recommended simple workflow using Declarative Automation Bundles is the following: 
Compile and test the code 
Triggered on a pull request or a commit to the main branch. 
Compile code and run unit tests. 
Output a versioned file, for example, my-app-1.0.jar . 
Upload and store the compiled file, such as a JAR, to a Databricks Unity Catalog volume. 
Store the compiled file in a Databricks Unity Catalog volume or an artifact repository like AWS S3 or Azure Blob Storage. 
Use a versioning scheme tied to Git commit hashes or semantic versioning, for example, dbfs:/mnt/artifacts/my-app-${{ github.sha }}.jar . 
Validate the bundle 
Run databricks bundle validate to ensure that the databricks.yml configuration is correct. 
This step ensures that misconfigurations, for example, missing libraries, are caught early. 
Deploy the bundle 
Use databricks bundle deploy to deploy the bundle to a staging or production environment. 
Reference the uploaded compiled library in databricks.yml . For information about referencing libraries, see Declarative Automation Bundles library dependencies . 
CI/CD for machine learning ​ 
Machine learning projects introduce unique CI/CD challenges compared to traditional software development. When implementing CI/CD for ML projects, you will likely need to consider the following: 
Multi-team coordination: Data scientists, engineers, and MLOps teams often use different tools and workflows. Databricks unifies these processes with MLflow for experiment tracking, OpenSharing for data governance, and Declarative Automation Bundles for infrastructure-as-code. 
Data and model versioning: ML pipelines require tracking not just code but also training data schemas, feature distributions, and model artifacts. Delta Lake provides ACID transactions and time travel for data versioning, while MLflow Model Registry handles model lineage. 
Reproducibility across environments: ML models depend on specific data, code, and infrastructure combinations. Declarative Automation Bundles ensure atomic deployment of these components across development, staging, and production environments with YAML definitions. 
Continuous retraining and monitoring: Models degrade due to data drift. Lakeflow Jobs enable automated retraining pipelines, while MLflow integrates with Prometheus and Databricks Data Quality Monitoring for performance tracking. 
MLOps Stacks for ML CI/CD ​ 
Databricks addresses ML CI/CD complexity through MLOps Stacks , a production-grade framework that combines Declarative Automation Bundles , preconfigured CI/CD workflows, and modular ML project templates. These stacks enforce best practices while allowing flexibility for multi-team collaboration across data engineering, data science, and MLOps roles. 

Team 
Responsibilities 
Example bundle components 
Example artifacts 

Data engineers 
Build ETL pipelines, enforce data quality 
Lakeflow pipelines YAML, cluster policies 
etl_pipeline.yml , feature_store_job.yml 

Data scientists 
Develop model training logic, validate metrics 
MLflow Projects, notebook-based workflows 
train_model.yml , batch_inference_job.yml 

MLOps engineers 
Orchestrate deployments, monitor pipelines 
Environment variables, monitoring dashboards 
databricks.yml , lakehouse_monitoring.yml ← ✕ 

Team 
Responsibilities 
Example bundle components 
Example artifacts 

Data engineers 
Build ETL pipelines, enforce data quality 
Lakeflow pipelines YAML, cluster policies 
etl_pipeline.yml , feature_store_job.yml 

Data scientists 
Develop model training logic, validate metrics 
MLflow Projects, notebook-based workflows 
train_model.yml , batch_inference_job.yml 

MLOps engineers 
Orchestrate deployments, monitor pipelines 
Environment variables, monitoring dashboards 
databricks.yml , lakehouse_monitoring.yml 
ML CI/CD collaboration might look like: 
Data engineers commit ETL pipeline changes to a bundle, triggering automated schema validation and a staging deployment. 
Data scientists submit ML code, which runs unit tests and deploys to a staging workspace for integration testing. 
MLOps engineers review validation metrics and promote vetted models to production using the MLflow Registry. 
For implementation details, see: 
MLOps Stacks bundle : Step-by-step guidance for bundle initialization and deployment. 
MLOps Stacks GitHub repository : Preconfigured templates for training, inference, and CI/CD. 
By aligning teams with standardized bundles and MLOps Stacks, organizations can streamline collaboration while maintaining auditability across the ML lifecycle. 
CI/CD for SQL developers ​ 
SQL developers using Databricks SQL to manage streaming tables and materialized views can leverage Git integration and CI/CD pipelines to streamline their workflows and maintain high-quality pipelines. With the introduction of Git support for queries, SQL developers can focus on writing queries while leveraging Git to version control their .sql files, which enables collaboration and automation without needing deep infrastructure expertise. In addition, the SQL editor enables real-time collaboration and integrates seamlessly with Git workflows. 
For SQL-centric workflows: 

Version control SQL files 
Store .sql files in Git repositories using Databricks Git folders or external Git providers, for example, GitHub, Azure DevOps. 
Use branches (for example, development, staging, production) to manage environment-specific changes. 

Integrate .sql files into CI/CD pipelines to automate deployment: 
Validate syntax and schema changes during pull requests. 
Deploy .sql files to Databricks SQL workflows or jobs. 

Parameterize for environment isolation 

Use variables in .sql files to dynamically reference environment-specific resources, such as data paths or table names: SQL 
CREATE OR REFRESH STREAMING TABLE ${env}_sales_ingest AS SELECT * FROM read_files ( 's3://${env}-sales-data' ) 

Schedule and monitor refreshes 
Use SQL tasks in a Databricks Job to schedule updates to tables and materialized views ( REFRESH MATERIALIZED VIEW view_name ). 
Monitor refresh history using system tables. 
A workflow might be: 
Develop: Write and test .sql scripts locally or in the Databricks SQL editor, then commit them to a Git branch. 
Validate: During a pull request, validate syntax and schema compatibility using automated CI checks. 
Deploy: Upon merge, deploy the .sql scripts to the target environment using CI/CD pipelines, for example, GitHub Actions or Azure Pipelines. 
Monitor: Use Databricks dashboards and alerts to track query performance and data freshness. 
CI/CD for dashboard developers ​ 
Databricks supports integrating dashboards into CI/CD workflows using Declarative Automation Bundles . This capability enables dashboard developers to: 
Version-control dashboards, which ensures auditability and simplifies collaboration between teams. 
Automate deployments of dashboards alongside jobs and pipelines across environments, for end-to-end alignment. 
Reduce manual errors and ensure that updates are applied consistently across environments. 
Maintain high-quality analytics workflows while adhering to CI/CD best practices. 
For dashboards in CI/CD: 

Use the databricks bundle generate command to export existing dashboards as JSON files and generate the YAML configuration that includes it in the bundle: YAML 
resources : dashboards : sales_dashboard : display_name : 'Sales Dashboard' file_path : ./dashboards/sales_dashboard.lvdash.json warehouse_id : $ { var.warehouse_id } 

Store these .lvdash.json files in Git repositories to track changes and collaborate effectively. 

Automatically deploy dashboards in CI/CD pipelines with databricks bundle deploy . For example, the GitHub Actions step for deployment: YAML 
name : Deploy Dashboard run : databricks bundle deploy - - target=prod env : DATABRICKS_TOKEN : $ { { secrets.DATABRICKS_TOKEN } } 

Use variables, for example ${var.warehouse_id} , to parameterize configurations like SQL warehouses or data sources, ensuring seamless deployment across dev, staging, and production environments. 

Use the bundle generate --watch option to continuously sync local dashboard JSON files with changes made in the Databricks UI. If discrepancies occur, use the --force flag during deployment to overwrite remote dashboards with local versions. 
For information about dashboards in bundles, see dashboard resource . For details about bundle commands, see bundle command group . On this page 
Core principles of CI/CD 
Declarative Automation Bundles for CI/CD 
Source control 
CI/CD workflow with bundles 
CI/CD for machine learning 
MLOps Stacks for ML CI/CD 
CI/CD for SQL developers 
CI/CD for dashboard developers Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 