# uniform

Source: https://docs.databricks.com/aws/en/delta/iceberg-reads
Retrieved: 2026-10-11

Read Delta Lake tables with Iceberg clients | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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

Tables 
Table functionality 
Table features 
Iceberg reads for Delta Lake On this page Last updated on Sep 11, 2026 
Read Delta Lake tables with Iceberg clients 
Available in Databricks Runtime 14.3 LTS and above, Iceberg reads configure Delta Lake tables to automatically generate Iceberg metadata, so Iceberg clients can read Delta Lake data without rewriting files. 
You can configure an external connection to have Unity Catalog act as an Iceberg catalog. See Access Databricks tables from Apache Iceberg clients . 
How Iceberg reads work ​ 
Both Delta Lake and Apache Iceberg consist of Parquet data files and a metadata layer. When you enable Iceberg reads, Databricks configures your tables to use the Universal Format (UniForm) for the metadata layer. UniForm automatically generates Iceberg metadata asynchronously alongside the Delta Lake metadata, without rewriting the Parquet data files. A single copy of the data files supports both Delta and Iceberg clients. 
When using Iceberg reads, consider the following: 
Delta Lake tables with Iceberg reads enabled use Zstandard instead of Snappy as the compression codec for underlying Parquet data files. 
Iceberg metadata generation runs asynchronously on the compute used to write data to Delta Lake tables, which might increase the driver resource usage. 
For documentation about the legacy UniForm IcebergCompatV1 table feature, see Legacy UniForm IcebergCompatV1 . 
Requirements ​ 
To enable Iceberg reads, the following requirements must be met: 
The Delta Lake table must be registered to Unity Catalog . Both managed and external tables are supported. 
The table must have column mapping enabled. See Rename and drop columns with Delta Lake column mapping . 
After IcebergCompatV2 is enabled for a table, you can't drop the columnMapping table feature. 
The Delta Lake table must have a minReaderVersion >= 2 and minWriterVersion >= 7. See Delta Lake feature compatibility and protocols . 
Writes to the table must use Databricks Runtime 14.3 LTS or above. note 
You cannot enable deletion vectors on a table with Iceberg reads enabled. 
Use REORG to turn off and purge deletion vectors while enabling Iceberg reads on an existing table with deletion vectors enabled. See Enable or upgrade Iceberg read support using REORG . 
Enable Iceberg reads ​ note 
Enabling Iceberg reads adds the IcebergCompatV2 write protocol feature and upgrades the writer protocol. Only clients that support this table feature can write to the table. This might affect compatibility with external Delta Lake clients. See Delta Lake feature compatibility and protocols . 
When you first enable Iceberg reads, asynchronous metadata generation begins. This task must complete before external clients can query the table using Iceberg. See Check Iceberg metadata generation status . 
For a list of limitations, see Limitations . 
During table creation ​ 
Column mapping is enabled automatically when you enable Iceberg reads during table creation: SQL 
CREATE TABLE T ( c1 INT ) TBLPROPERTIES ( 'delta.columnMapping.mode' = 'id' , 'delta.enableIcebergCompatV2' = 'true' , 'delta.universalFormat.enabledFormats' = 'iceberg' ) ; 
Databricks recommends you set delta.columnMapping.mode = id for compatibility purposes. See Rename and drop columns with Delta Lake column mapping . 
On an existing table ​ 
To enable Iceberg reads on an existing table on Databricks Runtime 15.4 LTS and above: SQL 
ALTER TABLE table_name SET TBLPROPERTIES ( 'delta.columnMapping.mode' = 'name' , 'delta.enableIcebergCompatV2' = 'true' , 'delta.universalFormat.enabledFormats' = 'iceberg' ) ; 
For details on the name column mapping mode, see Column mapping modes . 
Enable or upgrade Iceberg read support using REORG ​ 
Use REORG to enable Iceberg reads if any of the following are true: 
You enabled deletion vectors on your table. 
You previously enabled the IcebergCompatV1 version of UniForm Iceberg. 
You need to read from Iceberg engines that don't support Hive-style Parquet files, such as Athena or Redshift. 
To enable Iceberg reads and rewrite underlying data files, use REORG like the following example: SQL 
REORG TABLE table_name APPLY ( UPGRADE UNIFORM ( ICEBERG_COMPAT_VERSION = 2 ) ) ; 
Verify that Iceberg reads are enabled ​ 
Use DESCRIBE EXTENDED to verify that Iceberg reads are enabled for your table: SQL 
DESCRIBE EXTENDED catalog_name . schema_name . table_name ; 
Look for the Delta Uniform Iceberg section in the output. If this section is present, Iceberg reads are enabled on your table. 
Alternatively, you can use SHOW TBLPROPERTIES : SQL 
SHOW TBLPROPERTIES catalog_name . schema_name . table_name ; 
Check for the following properties: 
delta.enableIcebergCompatV2 = true 
delta.universalFormat.enabledFormats = iceberg 
If both properties are present with these values, Iceberg reads are enabled. 
Turn off Iceberg reads ​ 
You can turn off Iceberg reads by unsetting the delta.universalFormat.enabledFormats table property: SQL 
ALTER TABLE table_name UNSET TBLPROPERTIES ( 'delta.universalFormat.enabledFormats' ) ; 
Upgrades to Delta Lake reader and writer protocol versions can't be undone. See Delta Lake feature compatibility and protocols . 
Iceberg metadata generation ​ 
Databricks triggers metadata generation asynchronously after a Delta Lake write transaction completes. This metadata generation process uses the same compute that completed the Delta Lake transaction. 
You can also manually trigger Iceberg metadata generation. See Manually trigger Iceberg metadata conversion . 
To avoid write latencies associated with metadata generation, Delta Lake tables with frequent commits might group multiple Delta Lake commits into a single commit to Iceberg metadata. 
Delta Lake ensures that only one metadata generation process is in progress on a given compute resource. Commits that would trigger a second concurrent metadata generation process successfully commit to Delta Lake but don't trigger asynchronous Iceberg metadata generation. This prevents cascading latency for metadata generation for workloads with frequent commits (seconds to minutes between commits). 
See Delta and Iceberg table versions . 
Delta and Iceberg table versions ​ 
Delta Lake and Iceberg allow time travel queries using table versions or timestamps stored in table metadata. 
Delta Lake table versions aren't guaranteed to align with Iceberg versions by either the commit timestamp or the version ID. To verify which version of a Delta Lake table that a given version of an Iceberg table corresponds to, use the corresponding table properties. See Check Iceberg metadata generation status . 
Check Iceberg metadata generation status ​ 
Enabling Iceberg reads on a table adds the following fields to Unity Catalog and Iceberg table metadata to track metadata generation status: 

Metadata field 
Description 

converted_delta_version 
The latest version of the Delta Lake table for which Iceberg metadata was successfully generated. 

converted_delta_timestamp 
The timestamp of the latest Delta Lake commit for which Iceberg metadata was successfully generated. ← ✕ 

Metadata field 
Description 

converted_delta_version 
The latest version of the Delta Lake table for which Iceberg metadata was successfully generated. 

converted_delta_timestamp 
The timestamp of the latest Delta Lake commit for which Iceberg metadata was successfully generated. 
On Databricks , you can review these metadata fields by doing one of the following: 
Reviewing the Delta Uniform Iceberg section returned by DESCRIBE EXTENDED table_name . 
Reviewing table metadata with Catalog Explorer. 
See the documentation for your Iceberg reader client for how to review table properties outside Databricks . For OSS Apache Spark , you can see these properties using the following syntax: SQL 
SHOW TBLPROPERTIES < table - name > ; 
Manually trigger Iceberg metadata conversion ​ 
You can manually trigger Iceberg metadata generation for the latest version of the Delta Lake table. This operation runs synchronously. When it completes, the table contents available in Iceberg reflect the latest version of the Delta Lake table available when the conversion process started. 
This operation isn't necessary under normal conditions. Use it to recover from the following: 
A cluster terminates before automatic metadata generation succeeds. 
An error or job failure interrupts metadata generation. 
A client that doesn't support UniForm Iceberg metadata generation writes to the Delta Lake table. 
Use the following syntax to trigger Iceberg metadata generation manually: SQL 
MSCK REPAIR TABLE < table - name > SYNC METADATA 
See REPAIR TABLE . 
Read Iceberg using a metadata JSON path ​ 
Some Iceberg clients, such as BigQuery, require that you provide a path to versioned metadata files to register external Iceberg tables. Each time Databricks converts a new version of the Delta Lake table to Iceberg, it creates a new metadata JSON file. 
For configuration details, refer to the documentation for your specific Iceberg reader client. 
Delta Lake stores Iceberg metadata under the table directory using the following pattern: 
<table-path>/metadata/<version-number>-<uuid>.metadata.json 
On Databricks , you can review this metadata location by doing one of the following: 
Reviewing the Delta Uniform Iceberg section returned by DESCRIBE EXTENDED table_name . 
Reviewing table metadata with Catalog Explorer. important 
Path-based Iceberg reader clients might require manually updating and refreshing metadata JSON paths to read current table versions. You might encounter errors when querying Iceberg tables using out-of-date versions as Parquet data files are removed from the Delta Lake table with VACUUM . See VACUUM and Iceberg metadata cleanup . 
VACUUM and Iceberg metadata cleanup ​ 
On Delta Lake tables with Iceberg reads enabled, Iceberg metadata accumulates in the metadata/ directory as the table changes. OPTIMIZE and conversion to Iceberg operations don't delete the metadata for older table versions. Only VACUUM removes it. 
Available in Databricks Runtime 17.2 and above, VACUUM deletes untracked files in the metadata/ directory while keeping the Iceberg metadata that clients need to read current table versions. This cleanup runs in FULL mode, which is the default for VACUUM . 
To clean up metadata for older table versions, run VACUUM after the delta.deletedFileRetentionDuration retention period has elapsed: SQL 
VACUUM table_name FULL 
See Full versus lite mode for more about vacuum modes and Configure data retention for time travel queries for more about the retention period. 
If predictive optimization is enabled, Databricks automatically handles this cleanup, so you don't need to run VACUUM manually for Iceberg metadata cleanup. 
Limitations ​ 
The following limitations exist for all tables with Iceberg reads enabled: 
Iceberg client support is read-only. Writes are not supported. 
Iceberg reader clients might have individual limitations, regardless of Databricks support for Iceberg reads. See the documentation for your chosen client. 
Deletion vectors aren't supported for Iceberg v2 reads. However, Apache Iceberg v3 supports deletion vectors. See Use Apache Iceberg v3 features and Deletion vectors in Databricks . 
Iceberg reads can't be enabled on materialized views or streaming tables using IcebergCompatV2 . For pipeline-managed materialized views and streaming tables , you can enable external Iceberg access using IcebergCompatV3 . See Enable external data access to streaming tables and materialized views . 
The Delta Lake table must be accessed by name (not path) to automatically trigger Iceberg metadata generation. 
Delta Lake tables with Iceberg reads enabled don't support VOID types. 
Some Delta Lake table features used by Iceberg reads aren't supported by some OpenSharing reader clients. See What is OpenSharing ? . 
The recipients of OpenSharing can read Delta Lake tables with Iceberg reads enabled as Iceberg tables using the Iceberg REST Catalog API. This feature is in Public Preview . See Enable sharing to external Iceberg clients . 
Legacy change data feed works for Delta clients when Iceberg reads are enabled but doesn't have support in Iceberg. See Legacy change data feed for Delta Lake . On this page 
How Iceberg reads work 
Requirements 
Enable Iceberg reads 
During table creation 
On an existing table 
Enable or upgrade Iceberg read support using REORG 
Verify that Iceberg reads are enabled 
Turn off Iceberg reads 
Iceberg metadata generation 
Delta and Iceberg table versions 
Check Iceberg metadata generation status 
Manually trigger Iceberg metadata conversion 
Read Iceberg using a metadata JSON path 
VACUUM and Iceberg metadata cleanup 
Limitations Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 