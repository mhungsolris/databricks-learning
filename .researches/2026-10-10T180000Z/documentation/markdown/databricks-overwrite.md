# databricks-overwrite

Source: https://docs.databricks.com/aws/en/delta/selective-overwrite
Retrieved: 2026-10-11

Selectively overwrite data with Delta Lake | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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

Data engineering 
Concepts 
Selective overwrite On this page Last updated on Sep 11, 2026 
Selectively overwrite data with Delta Lake 
Delta Lake has the following distinct options for selective overwrites: 

Option 
Use case 
Supported compute types 
Minimum version 

REPLACE WHERE 
Atomically overwrite rows that match a predicate. Use for replacements with a fixed matching condition, such as colA = 5 or int_col IN (1, 2, 3) . 
All compute types. 
SQL in Databricks Runtime 12.2 LTS and above. Python and Scala in Databricks Runtime 9.1 LTS and above. 

REPLACE USING 
Dynamic data overwrite. Replaces all rows that match the specified columns, based on equality comparison of the column values, in the provided data set. 
All compute types. 
SQL in Databricks Runtime 16.3 and above. Python and Scala in Databricks Runtime 18.2 and above. 

REPLACE ON 
Dynamic data overwrite by boolean expression. Use for replacements with a complex or NULL-safe matching condition, such as s.colA <=> t.colA AND s.colB <=> t.colB . 
All compute types. 
SQL in Databricks Runtime 17.1 and above. Python and Scala in Databricks Runtime 18.2 and above. 

partitionOverwriteMode 
Legacy dynamic partition overwrite, which overwrites all the existing data in each partition for which the write will commit new data. Not recommended for new workloads. 
SQL supports classic compute only. Python and Scala supports all compute types. 
SQL, Python, and Scala in Databricks Runtime 11.3 LTS and above. ← ✕ 

Option 
Use case 
Supported compute types 
Minimum version 

REPLACE WHERE 
Atomically overwrite rows that match a predicate. Use for replacements with a fixed matching condition, such as colA = 5 or int_col IN (1, 2, 3) . 
All compute types. 
SQL in Databricks Runtime 12.2 LTS and above. Python and Scala in Databricks Runtime 9.1 LTS and above. 

REPLACE USING 
Dynamic data overwrite. Replaces all rows that match the specified columns, based on equality comparison of the column values, in the provided data set. 
All compute types. 
SQL in Databricks Runtime 16.3 and above. Python and Scala in Databricks Runtime 18.2 and above. 

REPLACE ON 
Dynamic data overwrite by boolean expression. Use for replacements with a complex or NULL-safe matching condition, such as s.colA <=> t.colA AND s.colB <=> t.colB . 
All compute types. 
SQL in Databricks Runtime 17.1 and above. Python and Scala in Databricks Runtime 18.2 and above. 

partitionOverwriteMode 
Legacy dynamic partition overwrite, which overwrites all the existing data in each partition for which the write will commit new data. Not recommended for new workloads. 
SQL supports classic compute only. Python and Scala supports all compute types. 
SQL, Python, and Scala in Databricks Runtime 11.3 LTS and above. 
For most use cases, Databricks recommends using REPLACE USING or REPLACE WHERE . Use REPLACE ON only if your use case requires complex or NULL-safe matching conditions. 
For detail on each option's replacement behavior, see INSERT . For a complete list of DataFrameWriter Delta Lake options, see Delta Lake and Apache Iceberg . 
In Scala and Python, replaceOn and replaceUsing can't be used in combination with replaceWhere , partitionOverwriteMode , or overwriteSchema . 
For empty source queries, both REPLACE USING and REPLACE ON do not delete data, however, REPLACE WHERE might delete data. important 
If data has been accidentally overwritten, you can use restore to undo the change. 
REPLACE WHERE ​ 
You can selectively overwrite only the data that matches an arbitrary expression with REPLACE WHERE . Beta 
To benefit from incremental refresh when running REPLACE WHERE , use REPLACE WHERE flows in Lakeflow pipelines . See Batch processing with REPLACE WHERE flows . 
REPLACE WHERE does not require the table to be partitioned on the columns in the predicate. The predicate is an arbitrary expression over the table's columns. 
The following examples use an events table seeded with rows inside and outside January 2017, and a replace_data source that holds new January 2017 rows. To create them, run the following: SQL 
CREATE OR REPLACE TABLE main . default . events ( event_id INT , start_date DATE , end_date DATE , payload STRING ) ; INSERT INTO main . default . events VALUES ( 1 , DATE '2017-01-05' , DATE '2017-01-10' , 'jan-original-a' ) , ( 2 , DATE '2017-01-20' , DATE '2017-01-25' , 'jan-original-b' ) , ( 3 , DATE '2017-02-05' , DATE '2017-02-10' , 'feb-unchanged' ) ; CREATE OR REPLACE TABLE main . default . replace_data ( event_id INT , start_date DATE , end_date DATE , payload STRING ) ; INSERT INTO main . default . replace_data VALUES ( 10 , DATE '2017-01-08' , DATE '2017-01-12' , 'jan-replacement-a' ) , ( 11 , DATE '2017-01-15' , DATE '2017-01-18' , 'jan-replacement-b' ) ; 
To atomically replace the January rows in events with the data in replace_data , run the following. The February row falls outside the predicate and is left unchanged: 
Python 
Scala 
SQL Python 
replace_data = spark . read . table ( "main.default.replace_data" ) ( replace_data . write . mode ( "overwrite" ) . option ( "replaceWhere" , "start_date >= '2017-01-01' AND end_date <= '2017-01-31'" ) . saveAsTable ( "main.default.events" ) ) Scala 
val replace_data = spark . read . table ( "main.default.replace_data" ) replace_data . write . mode ( "overwrite" ) . option ( "replaceWhere" , "start_date >= '2017-01-01' AND end_date <= '2017-01-31'" ) . saveAsTable ( "main.default.events" ) SQL 
INSERT INTO TABLE main . default . events REPLACE WHERE start_date >= '2017-01-01' AND end_date <= '2017-01-31' SELECT * FROM main . default . replace_data 
This sample code writes out the data in replace_data , validates that all rows match the predicate, and performs an atomic replacement using overwrite semantics. If any values in the operation fall outside the predicate, this operation fails with an error by default. 
On classic compute, to change this behavior to overwrite values within the predicate range and insert records outside the specified range, remove the constraint check by setting spark.databricks.delta.replaceWhere.constraintCheck.enabled to false : 
Python 
Scala 
SQL Python 
spark . conf . set ( "spark.databricks.delta.replaceWhere.constraintCheck.enabled" , False ) Scala 
spark . conf . set ( "spark.databricks.delta.replaceWhere.constraintCheck.enabled" , false ) SQL 
SET spark . databricks . delta . replaceWhere . constraintCheck . enabled = false note 
REPLACE WHERE accepts a boolean_expression with some restrictions. See INSERT in the SQL language reference. 
For empty source queries, REPLACE WHERE might delete table rows. Legacy behavior ​ 
Legacy replaceWhere is only available on classic compute. See Classic compute overview . 
If you use the legacy behavior of replaceWhere , queries overwrite data that matches a predicate only over partition columns. The following command would atomically replace the month January in the target table, which is partitioned by date , with the data in df : 
Python 
Scala Python 
( df . write . mode ( "overwrite" ) . option ( "replaceWhere" , "birthDate >= '2017-01-01' AND birthDate <= '2017-01-31'" ) . saveAsTable ( "people10m" ) ) Scala 
df . write . mode ( "overwrite" ) . option ( "replaceWhere" , "birthDate >= '2017-01-01' AND birthDate <= '2017-01-31'" ) . saveAsTable ( "people10m" ) 
To use legacy behavior, set spark.databricks.delta.replaceWhere.dataColumns.enabled to false : 
Python 
Scala 
SQL Python 
spark . conf . set ( "spark.databricks.delta.replaceWhere.dataColumns.enabled" , False ) Scala 
spark . conf . set ( "spark.databricks.delta.replaceWhere.dataColumns.enabled" , false ) SQL 
SET spark . databricks . delta . replaceWhere . dataColumns . enabled = false 
Dynamic data overwrites ​ 
Dynamic data overwrites selectively replace data that match the specified key columns or boolean expression, leaving all other data unchanged. Partitioned tables, unpartitioned tables, and tables with liquid clustering are all supported. 
Dynamic partition overwrites are a subset of dynamic data overwrite behavior. Dynamic partition overwrites replace all the existing data in each partition for which the write will commit new data and leaves all other partitions unchanged. Only partitioned tables are supported. 
REPLACE USING ​ 
SQL supported in Databricks Runtime 16.3 and above. Python and Scala supported in Databricks Runtime 18.2 and above. For behavior differences in Databricks Runtime 16.3 to 17.1 see Legacy behavior . 
REPLACE USING enables compute-independent, atomic overwrite behavior that works on Databricks SQL warehouses, serverless compute , and classic compute. REPLACE USING doesn't require that you set a Spark session configuration. 
REPLACE USING replaces rows when the specified columns compare equal under equality. All other data remains unchanged. 
The following examples reset the events table and use a source_data source. To create them, run the following: SQL 
CREATE OR REPLACE TABLE main . default . events ( event_id INT , start_date DATE , end_date DATE , payload STRING ) ; INSERT INTO main . default . events VALUES ( 1 , DATE '2017-01-05' , DATE '2017-01-10' , 'original-a' ) , ( 2 , DATE '2017-01-20' , DATE '2017-01-25' , 'original-b' ) , ( 3 , DATE '2017-02-05' , DATE '2017-02-10' , 'original-c' ) ; CREATE OR REPLACE TABLE main . default . source_data ( event_id INT , start_date DATE , end_date DATE , payload STRING ) ; INSERT INTO main . default . source_data VALUES ( 1 , DATE '2017-01-05' , DATE '2017-01-11' , 'replacement-a' ) , ( 4 , DATE '2017-03-01' , DATE '2017-03-02' , 'new-d' ) ; 
REPLACE USING (event_id, start_date) replaces the events row whose event_id and start_date match source_data (row 1), inserts the source row with a new key (row 4), and leaves the other rows unchanged. Use dynamic data overwrite with REPLACE USING : 
Python 
Scala 
SQL Python 
sourceDataDF = spark . read . table ( "main.default.source_data" ) ( sourceDataDF . write . mode ( "overwrite" ) . option ( "replaceUsing" , "event_id, start_date" ) . saveAsTable ( "main.default.events" ) ) Scala 
val sourceDataDF = spark . read . table ( "main.default.source_data" ) sourceDataDF . write . mode ( "overwrite" ) . option ( "replaceUsing" , "event_id, start_date" ) . saveAsTable ( "main.default.events" ) SQL 
INSERT INTO TABLE main . default . events REPLACE USING ( event_id , start_date ) SELECT * FROM main . default . source_data 
For empty source queries, REPLACE USING does not delete any table rows. 
For complex or NULL-safe matching conditions, use REPLACE ON instead. See REPLACE ON . 
See INSERT in the SQL language reference. Legacy behavior ​ 
In Databricks Runtime 16.3 to 17.1, REPLACE USING uses legacy behavior and only allows dynamic partition overwrites, whereas Databricks Runtime 17.2 and above allows for dynamic data overwrites. 
Keep the following constraints and behaviors in mind for REPLACE USING legacy behavior: 
You must specify the full set of the table's partition columns in the USING clause. 
Always validate that the data written touches only the expected partitions. A single row in the wrong partition can unintentionally overwrite the entire partition. 
REPLACE ON ​ 
SQL supported in Databricks Runtime 17.1 and above. Python and Scala supported in Databricks Runtime 18.2 and above. 
REPLACE ON replaces rows when they match a user-defined condition, unlike REPLACE USING , which replaces rows when the specified columns compare equal under equality. Use REPLACE ON when you need matching logic that REPLACE USING does not support, such as treating NULL values as equal. 
Optionally, use the targetAlias option to specify an alias for the target table and the .as() or .alias() APIs to specify an alias for the source data. 
For SQL syntax, see INSERT . 
The following examples reset the events table and source_data source, seeding a row with a NULL start_date in each to show NULL-safe matching. To create them, run the following: SQL 
CREATE OR REPLACE TABLE main . default . events ( event_id INT , start_date DATE , end_date DATE , payload STRING ) ; INSERT INTO main . default . events VALUES ( 1 , DATE '2017-01-05' , DATE '2017-01-10' , 'original-a' ) , ( 2 , NULL , DATE '2017-01-25' , 'original-null-key' ) , ( 3 , DATE '2017-02-05' , DATE '2017-02-10' , 'original-c' ) ; CREATE OR REPLACE TABLE main . default . source_data ( event_id INT , start_date DATE , end_date DATE , payload STRING ) ; INSERT INTO main . default . source_data VALUES ( 1 , DATE '2017-01-05' , DATE '2017-01-11' , 'replacement-a' ) , ( 2 , NULL , DATE '2017-01-26' , 'replacement-null-key' ) ; 
Because <=> treats two NULL values as equal, the row with a NULL start_date (row 2) is matched and replaced, along with row 1. Row 3 has no matching source row and is left unchanged: 
Python 
Scala 
SQL Python 
sourceDataDF = spark . read . table ( "main.default.source_data" ) ( sourceDataDF . alias ( "s" ) . write . mode ( "overwrite" ) . option ( "targetAlias" , "t" ) . option ( "replaceOn" , "s.event_id <=> t.event_id AND s.start_date <=> t.start_date" ) . saveAsTable ( "main.default.events" ) ) Scala 
val sourceDataDF = spark . read . table ( "main.default.source_data" ) sourceDataDF . as ( "s" ) . write . mode ( "overwrite" ) . option ( "targetAlias" , "t" ) . option ( "replaceOn" , "s.event_id <=> t.event_id AND s.start_date <=> t.start_date" ) . saveAsTable ( "main.default.events" ) SQL 
INSERT INTO TABLE main . default . events AS t REPLACE ON ( s . event_id <=> t . event_id AND s . start_date <=> t . start_date ) ( SELECT * FROM main . default . source_data ) AS s 
For empty source queries, REPLACE ON does not delete any table rows. 
Dynamic partition overwrites with partitionOverwriteMode (legacy) ​ Preview 
This feature is in Public Preview . 
Databricks Runtime 11.3 LTS and above supports dynamic partition overwrites for partitioned tables using overwrite mode: either INSERT OVERWRITE in SQL, or a DataFrame write with df.write.mode("overwrite") . This type of overwrite is only available for classic compute, not Databricks SQL warehouses or serverless compute . warning 
When possible, use INSERT REPLACE USING instead of partition overwrite INSERT OVERWRITE PARTITION and spark.sql.sources.partitionOverwriteMode=dynamic . Partition overwrite may use stale data when partitioning changes. 
To use dynamic partition overwrite mode, set the Spark session configuration spark.sql.sources.partitionOverwriteMode to dynamic . Alternatively, you can set the DataFrameWriter option partitionOverwriteMode to dynamic . If present, the query-specific option overrides the mode defined in the session configuration. The default value for spark.sql.sources.partitionOverwriteMode is static . 
The following example uses partitionOverwriteMode : 
SQL 
Python 
Scala SQL 
SET spark . sql . sources . partitionOverwriteMode = dynamic ; INSERT OVERWRITE TABLE default . people10m SELECT * FROM morePeople ; Python 
( df . write . mode ( "overwrite" ) . option ( "partitionOverwriteMode" , "dynamic" ) . saveAsTable ( "default.people10m" ) ) Scala 
df . write . mode ( "overwrite" ) . option ( "partitionOverwriteMode" , "dynamic" ) . saveAsTable ( "default.people10m" ) 
Keep the following constraints and behaviors in mind for partitionOverwriteMode : 
You can't set overwriteSchema to true . 
You can't specify both partitionOverwriteMode and replaceWhere in the same DataFrameWriter operation. 
If you specify a replaceWhere condition using a DataFrameWriter option, Delta Lake applies that condition to control which data is overwritten. This option takes precedence over the partitionOverwriteMode session-level configuration. 
Always validate that the data written touches only the expected partitions. A single row in the wrong partition can unintentionally overwrite the entire partition. On this page 
REPLACE WHERE 
Dynamic data overwrites 
REPLACE USING 
REPLACE ON 
Dynamic partition overwrites with partitionOverwriteMode (legacy) Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 