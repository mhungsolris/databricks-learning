# ucRest

Source: https://docs.databricks.com/aws/en/external-access/iceberg
Retrieved: 2026-10-11

Access Databricks tables from Apache Iceberg clients | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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

Data guides 
Access data using external systems 
Iceberg client access On this page Last updated on Sep 24, 2026 
Access Databricks tables from Apache Iceberg clients 
The Apache Iceberg REST catalog lets supported clients, such as Apache Spark , Apache Flink, and Trino, read from and write to Unity Catalog -registered Iceberg tables on Databricks . 
For a full list of supported integrations, see Unity Catalog integrations . note 
Unity Catalog also has a read-only Iceberg REST Catalog API endpoint. This is a legacy endpoint. See Read Databricks tables from Apache Iceberg clients (legacy) . 
Use the Unity Catalog Iceberg catalog endpoint ​ 
Unity Catalog provides an implementation of the Iceberg REST catalog API specification. 
Configure access using the endpoint /api/2.1/unity-catalog/iceberg-rest . See the Iceberg REST API spec for details on using this REST API. note 
Databricks has introduced credential vending for some Iceberg reader clients. Databricks recommends using credential vending to control access to cloud storage locations for supported systems. See Unity Catalog credential vending for external system access and Access Iceberg tables using external systems . 
If credential vending is unsupported for your client, you must configure access from the client to the storage location containing the files and metadata for the Delta or Iceberg table. Refer to documentation for your Iceberg client for configuration details. 
Requirements ​ 
Databricks supports Iceberg REST catalog access to tables as part of Unity Catalog . You must have Unity Catalog enabled in your workspace to use these endpoints. The following table types are accessible using the Iceberg REST Catalog: 

Topic 
Read 
Write 

Managed Iceberg 
Yes 
Yes 

Foreign Iceberg 
Yes 
No 

Managed Delta (with Iceberg reads enabled) 
Yes 
No 

External Delta (with Iceberg reads enabled) 
Yes 
No ← ✕ 

Topic 
Read 
Write 

Managed Iceberg 
Yes 
Yes 

Foreign Iceberg 
Yes 
No 

Managed Delta (with Iceberg reads enabled) 
Yes 
No 

External Delta (with Iceberg reads enabled) 
Yes 
No 
Foreign Iceberg tables are not automatically refreshed when using the Iceberg REST Catalog API to read tables. To refresh, you must run REFRESH FOREIGN TABLE to read the latest snapshot. Credential vending on Foreign Iceberg tables is not supported. note 
You must configure Delta tables to be accessible using the Iceberg REST Catalog API. See Read Delta Lake tables with Iceberg clients . 
You must complete the following configuration steps to configure access to read from or write to Databricks tables from Iceberg clients using the Iceberg REST catalog: 
Enable External data access for your metastore. See Enable external data access on the metastore . 
Grant the principal configuring the integration the EXTERNAL USE SCHEMA privilege on the schema containing the tables. See Grant a principal Unity Catalog privileges . 
Authenticate using a Databricks personal access token or OAuth. See Authorize access to Databricks resources . note 
The Iceberg specification does not allow duplicate data files in a single table snapshot. To prevent this, when detected, Unity Catalog blocks external engines from committing duplicate data files to the table. note 
To read tables with row filters or column masks attached from an external Iceberg client, see Cross-engine attribute-based access controls (ABAC) for required client versions and configuration. 
Use Iceberg tables with Apache Spark ​ 
The following examples show how to configure Apache Spark to access Databricks tables through the Iceberg REST Catalog API. Databricks supports OAuth and personal access token (PAT) authentication. 
To access tables across multiple catalogs, you must configure each catalog separately. note 
You must include the Iceberg Spark runtime JAR and the cloud-specific bundle JAR in your Spark packages. The runtime JAR version must match your Spark and Scala versions. For example, for Spark 3.5 with Scala 2.12: 
org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:<iceberg-version> 
Plus the cloud-specific bundle: 
AWS: org.apache.iceberg:iceberg-aws-bundle:<iceberg-version> 
Azure: org.apache.iceberg:iceberg-azure-bundle:<iceberg-version> 
GCP: org.apache.iceberg:iceberg-gcp-bundle:<iceberg-version> 
For details, see the documentation for the Iceberg AWS integration for Spark . These JARs are not required when accessing Iceberg tables from Databricks clusters. 
When reading tables on AWS, the Iceberg client uses the AWS SDK and requires an explicit region. Before launching Spark, set the region using either the AWS_REGION environment variable or the spark.hadoop.fs.s3a.region Spark config. Without it, scans fail at runtime with Unable to load region from any of the providers in the chain . Bash 
export AWS_REGION = us-west-2 
OAuth authentication ​ 
CLI 
Python Bash 
pyspark \ --packages org.apache.iceberg:iceberg-spark-runtime-3.5_2.12: < iceberg-version > ,org.apache.iceberg:iceberg-aws-bundle: < iceberg-version > \ --conf "spark.sql.catalog.<spark-catalog-name>=org.apache.iceberg.spark.SparkCatalog" \ --conf "spark.sql.catalog.<spark-catalog-name>.type=rest" \ --conf "spark.sql.catalog.<spark-catalog-name>.rest.auth.type=oauth2" \ --conf "spark.sql.catalog.<spark-catalog-name>.uri=https://<workspace-url>/api/2.1/unity-catalog/iceberg-rest" \ --conf "spark.sql.catalog.<spark-catalog-name>.oauth2-server-uri=https://<workspace-url>/oidc/v1/token" \ --conf "spark.sql.catalog.<spark-catalog-name>.credential=<oauth_client_id>:<oauth_client_secret>" \ --conf "spark.sql.catalog.<spark-catalog-name>.warehouse=<uc-catalog-name>" \ --conf "spark.sql.catalog.<spark-catalog-name>.scope=all-apis" Python 
from pyspark . sql import SparkSession spark = SparkSession . builder \ . config ( "spark.jars.packages" , "org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:<iceberg-version>,org.apache.iceberg:iceberg-aws-bundle:<iceberg-version>" ) \ . config ( "spark.sql.catalog.<spark-catalog-name>" , "org.apache.iceberg.spark.SparkCatalog" ) \ . config ( "spark.sql.catalog.<spark-catalog-name>.type" , "rest" ) \ . config ( "spark.sql.catalog.<spark-catalog-name>.rest.auth.type" , "oauth2" ) \ . config ( "spark.sql.catalog.<spark-catalog-name>.uri" , "https://<workspace-url>/api/2.1/unity-catalog/iceberg-rest" ) \ . config ( "spark.sql.catalog.<spark-catalog-name>.oauth2-server-uri" , "https://<workspace-url>/oidc/v1/token" ) \ . config ( "spark.sql.catalog.<spark-catalog-name>.credential" , "<oauth_client_id>:<oauth_client_secret>" ) \ . config ( "spark.sql.catalog.<spark-catalog-name>.warehouse" , "<uc-catalog-name>" ) \ . config ( "spark.sql.catalog.<spark-catalog-name>.scope" , "all-apis" ) \ . getOrCreate ( ) 
Replace the following variables: 
<spark-catalog-name> : The name you want to assign the catalog in your Spark session. 
<uc-catalog-name> : The name of the catalog in Unity Catalog that contains your tables. 
<oauth_client_id> : OAuth client ID for the authenticating principal. 
<oauth_client_secret> : OAuth client secret for the authenticating principal. 
<iceberg-version> : The Iceberg version to use, for example 1.9.2 . 
<workspace-url> : The Databricks workspace URL . For example, cust-success.cloud.databricks.com . 
PAT authentication ​ 
CLI 
Python Bash 
pyspark \ --packages org.apache.iceberg:iceberg-spark-runtime-3.5_2.12: < iceberg-version > ,org.apache.iceberg:iceberg-aws-bundle: < iceberg-version > \ --conf "spark.sql.catalog.<spark-catalog-name>=org.apache.iceberg.spark.SparkCatalog" \ --conf "spark.sql.catalog.<spark-catalog-name>.type=rest" \ --conf "spark.sql.catalog.<spark-catalog-name>.uri=https://<workspace-url>/api/2.1/unity-catalog/iceberg-rest" \ --conf "spark.sql.catalog.<spark-catalog-name>.token=<token>" \ --conf "spark.sql.catalog.<spark-catalog-name>.warehouse=<uc-catalog-name>" Python 
from pyspark . sql import SparkSession spark = SparkSession . builder \ . config ( "spark.jars.packages" , "org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:<iceberg-version>,org.apache.iceberg:iceberg-aws-bundle:<iceberg-version>" ) \ . config ( "spark.sql.catalog.<spark-catalog-name>" , "org.apache.iceberg.spark.SparkCatalog" ) \ . config ( "spark.sql.catalog.<spark-catalog-name>.type" , "rest" ) \ . config ( "spark.sql.catalog.<spark-catalog-name>.uri" , "https://<workspace-url>/api/2.1/unity-catalog/iceberg-rest" ) \ . config ( "spark.sql.catalog.<spark-catalog-name>.token" , "<token>" ) \ . config ( "spark.sql.catalog.<spark-catalog-name>.warehouse" , "<uc-catalog-name>" ) \ . getOrCreate ( ) 
Replace the following variables: 
<spark-catalog-name> : The name you want to assign the catalog in your Spark session. 
<uc-catalog-name> : The name of the catalog in Unity Catalog that contains your tables. 
<token> : A personal access token (PAT) for the authenticating principal. See Authenticate with Databricks personal access tokens (legacy) . 
<iceberg-version> : The Iceberg version to use, for example 1.9.2 . 
<workspace-url> : The Databricks workspace URL . For example, cust-success.cloud.databricks.com . 
Access Databricks tables with Snowflake ​ 
Snowflake provides two options for accessing tables through the Iceberg REST catalog: using Snowflake's catalog-linked databases, or using external tables. 
For both options, first configure a Snowflake catalog integration. Databricks supports the following authentication methods for Snowflake catalog integrations: 
Bearer token : Uses a Databricks personal access token (PAT) or OAuth token. Supported on all clouds. 
Entra service principal OAuth (Azure only) : Uses a Microsoft Entra ID service principal to authenticate directly against the Entra token endpoint. 
For more details on Snowflake authentication options for REST catalog integrations, see the Snowflake documentation . 
Snowflake with bearer token authentication ​ 
The following example configures a Snowflake catalog integration using a bearer token. You can use a Databricks personal access token (PAT) or an OAuth token generated from a Databricks service principal. For details on generating OAuth tokens, see Authorize service principal access to Databricks with OAuth . SQL 
CREATE OR REPLACE CATALOG INTEGRATION < catalog - integration - name > CATALOG_SOURCE = ICEBERG_REST TABLE_FORMAT = ICEBERG CATALOG_NAMESPACE = '<uc-schema-name>' REST_CONFIG = ( CATALOG_URI = '<workspace-url>/api/2.1/unity-catalog/iceberg-rest' , WAREHOUSE = '<uc-catalog-name>' ACCESS_DELEGATION_MODE = VENDED_CREDENTIALS ) REST_AUTHENTICATION = ( TYPE = BEARER BEARER_TOKEN = '<token>' ) ENABLED = TRUE ; 
Replace the following variables: 
<catalog-integration-name> : The name you want to assign the catalog registered to Snowflake. 
<uc-schema-name> : The name of the schema in Unity Catalog that you need to access. 
<uc-catalog-name> : The name of the catalog in Unity Catalog that you need to access. 
<workspace-url> : The Databricks workspace URL . For example, https://cust-success.cloud.databricks.com or https://adb-1234567890123456.12.azuredatabricks.net . 
<token> : A personal access token (PAT) for the principal configuring the integration. 
Catalog-linked databases ​ 
Snowflake's catalog-linked databases automatically sync with Unity Catalog to detect schemas and Iceberg tables. This eliminates the need for manual metadata refresh. 
After configuring a Snowflake catalog integration, refer to the Snowflake documentation to create a catalog-linked database to access your tables. important 
Attempting to write from Snowflake to read-only Databricks tables can result in errors. Refer to the Snowflake documentation for supported operations. 
External tables ​ 
Alternatively, you can create external tables after creating a Snowflake catalog integration. This approach requires manually refreshing metadata to see updates. SQL 
CREATE OR REPLACE ICEBERG TABLE my_table CATALOG = '<catalog-integration-name>' CATALOG_TABLE_NAME = '<uc-table-name>' ; 
Use Databricks tables with PyIceberg ​ 
To use PyIceberg to access Databricks tables, you must install PyIceberg with the required dependencies. PyIceberg requires pyarrow for table operations such as reading data and inspecting table metadata. Install PyIceberg with the pyarrow extra: Bash 
pip install "pyiceberg[pyarrow]" note 
If you do not install pyarrow , operations such as describing or reading tables fail. For the full list of optional dependencies, see the PyIceberg documentation . 
The following is an example of the configuration settings to allow PyIceberg to access Databricks tables by connecting to the Iceberg REST Catalog in Unity Catalog : YAML 
catalog : unity_catalog : uri : https : //<workspace - url > /api/2.1/unity - catalog/iceberg - rest warehouse : <uc - catalog - name > token : <token > 
Replace the following variables: 
<workspace-url> : The Databricks workspace URL . For example, cust-success.cloud.databricks.com . 
<uc-catalog-name> : The name of the catalog in Unity Catalog that you need to access. 
<token> : A personal access token (PAT) for the principal configuring the integration. 
See the documentation for the PyIceberg REST catalog configuration . 
REST API curl example ​ 
The following curl example loads a table using the REST API: Bash 
curl -X GET -H "Authorization: Bearer $OAUTH_TOKEN " -H "Accept: application/json" \ https:// < workspace-instance > /api/2.1/unity-catalog/iceberg-rest/v1/catalogs/ < uc_catalog_name > /namespaces/ < uc_schema_name > /tables/ < uc_table_name > 
The response looks like this: 
{ "metadata-location": "s3://bucket/path/to/iceberg/table/metadata/file", "metadata": <iceberg-table-metadata-json>, "config": { "expires-at-ms": "<epoch-ts-in-millis>", "s3.access-key-id": "<temporary-s3-access-key-id>", "s3.session-token":"<temporary-s3-session-token>", "s3.secret-access-key":"<temporary-secret-access-key>", "client.region":"<aws-bucket-region-for-metadata-location>" } } note 
The expires-at-ms field indicates when the credentials expire. The default expiration time is one hour. For better performance, have the client cache the credentials until they expire before requesting new ones. 
Limitations ​ 
The following limitations apply when accessing managed Iceberg tables from external Iceberg clients: 
External Iceberg clients can't access views. 
External Iceberg clients can't create managed Iceberg tables with the following data types: UUID , Fixed(L) , TIME , and nested STRUCT with required fields. 
External Iceberg clients can't run table maintenance operations, such as expiring snapshots and removing orphan files. On this page 
Use the Unity Catalog Iceberg catalog endpoint 
Requirements 
Use Iceberg tables with Apache Spark 
OAuth authentication 
PAT authentication 
Access Databricks tables with Snowflake 
Snowflake with bearer token authentication 
Catalog-linked databases 
External tables 
Use Databricks tables with PyIceberg 
REST API curl example 
Limitations Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 