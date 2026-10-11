# delta-quickstart

Source: https://docs.delta.io/quick-start/
Retrieved: 2026-10-10

Quick Start | Delta Lake Skip to content Delta Lake Search Ctrl K Cancel GitHub Select theme Dark Light Auto 
Introduction 
Apache Spark connector 
Quick Start 
Table batch reads and writes 
Table streaming reads and writes 
Table deletes, updates, and merges 
Change data feed 
Table utility commands 
Constraints 
How does Delta Lake manage feature compatibility? 
Delta default column values 
Delta column mapping 
Use liquid clustering for Delta tables 
What are deletion vectors? 
Use catalog-managed tables 
Drop Delta table features 
Use row tracking for Delta tables 
Delta Connect (aka Spark Connect Support in Delta) 
Storage configuration 
Delta type widening 
Universal Format (UniForm) 
Read Delta Sharing Tables 
Concurrency control 
Migration guide 
Best practices 
Frequently asked questions (FAQ) 
Optimizations 
Trino connector 
Starburst connector 
Presto connector 
AWS Redshift Spectrum connector 
Snowflake connector 
Google BigQuery connector 
Apache Flink connector 
Other connectors 
Delta Kernel 
Delta Standalone (deprecated) 
Delta Lake APIs 
Releases 
Delta Lake resources 
Delta Table Properties Reference 
Contribute GitHub Select theme Dark Light Auto On this page 
Overview 
Set up Apache Spark with Delta Lake 
Prerequisite: set up Java 
Set up interactive shell 
Set up project 
Create a table 
Read data 
Update table data 
Overwrite 
Conditional update without overwrite 
Read older versions of data using time travel 
Write a stream of data to a table 
Read a stream of changes from a table 
On this page 
Overview 
Set up Apache Spark with Delta Lake 
Prerequisite: set up Java 
Set up interactive shell 
Set up project 
Create a table 
Read data 
Update table data 
Overwrite 
Conditional update without overwrite 
Read older versions of data using time travel 
Write a stream of data to a table 
Read a stream of changes from a table 
Quick Start 
This guide helps you quickly explore the main features of Delta Lake. It provides code snippets that show how to read from and write to Delta tables from interactive, batch, and streaming queries. 
Set up Apache Spark with Delta Lake Section titled “Set up Apache Spark with Delta Lake” 
Follow these instructions to set up Delta Lake with Spark. You can run the steps in this guide on your local machine in the following two ways: 
Run interactively : Start the Spark shell (Scala or Python) with Delta Lake and run the code snippets interactively in the shell. 
Run as a project : Set up a Maven or SBT project (Scala or Java) with Delta Lake, copy the code snippets into a source file, and run the project. Alternatively, you can use the examples provided in the Github repository . 
Important! 
For all of the following instructions, make sure to install the correct
version of Spark or PySpark that is compatible with Delta Lake 4.0.0 . See the release compatibility matrix for details. 
Prerequisite: set up Java Section titled “Prerequisite: set up Java” 
As mentioned in the official Apache Spark installation instructions here , make sure you have a valid Java version installed (8, 11, or 17) and that Java is configured correctly on your system using either the system PATH or JAVA_HOME environmental variable. 
Windows users should follow the instructions in this blog , making sure to use the correct version of Apache Spark that is compatible with Delta Lake 4.0.0 . 
Set up interactive shell Section titled “Set up interactive shell” 
To use Delta Lake interactively within the Spark SQL, Scala, or Python shell, you need a local installation of Apache Spark. Depending on whether you want to use SQL, Python, or Scala, you can set up either the SQL, PySpark, or Spark shell, respectively. Spark SQL Shell Section titled “Spark SQL Shell” 
Download the compatible version of Apache Spark by following instructions from Downloading Spark , either using pip or by downloading and extracting the archive and running spark-sql in the extracted directory. Terminal window 
bin/spark-sql --packages io.delta:delta-spark_2.13:4.0.0 --conf " spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension " --conf " spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog " PySpark Shell Section titled “PySpark Shell” 

Install the PySpark version that is compatible with the Delta Lake version by running the following: Terminal window 
pip install pyspark==<compatible-spark-version> 

Run PySpark with the Delta Lake package and additional configurations: Terminal window 
pyspark --packages io.delta:delta-spark_2.13:4.0.0 --conf " spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension " --conf " spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog " Spark Scala Shell Section titled “Spark Scala Shell” 
Download the compatible version of Apache Spark by following instructions from Downloading Spark , either using pip or by downloading and extracting the archive and running spark-shell in the extracted directory. Terminal window 
bin/spark-shell --packages io.delta:delta-spark_2.13:4.0.0 --conf " spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension " --conf " spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog " 
Set up project Section titled “Set up project” 
If you want to build a project using Delta Lake binaries from Maven Central Repository, you can use the following Maven coordinates. Maven Section titled “Maven” 
You include Delta Lake in your Maven project by adding it as a dependency in your POM file. Delta Lake compiled with Scala 2.13. 
XML 
< dependency > < groupId > io.delta </ groupId > < artifactId > delta-spark_2.13 </ artifactId > < version > 4.0.0 </ version > </ dependency > SBT Section titled “SBT” 
You include Delta Lake in your SBT project by adding the following line to your build.sbt file: 
Scala 
libraryDependencies += " io.delta " %% " delta-spark " % " 4.0.0 " Python Section titled “Python” 
To set up a Python project (for example, for unit testing), you can install Delta Lake using pip install delta-spark==4.0.0 and then configure the SparkSession with the configure_spark_with_delta_pip() utility function in Delta Lake. 
Python 
import pyspark from delta import * builder = pyspark.sql.SparkSession.builder. appName ( " MyApp " ) \ . config ( " spark.sql.extensions " , " io.delta.sql.DeltaSparkSessionExtension " ) \ . config ( " spark.sql.catalog.spark_catalog " , " org.apache.spark.sql.delta.catalog.DeltaCatalog " ) spark = configure_spark_with_delta_pip ( builder ). getOrCreate () 
Create a table Section titled “Create a table” 
To create a Delta table, write a DataFrame out in the delta format. You can use existing Spark SQL code and change the format from parquet , csv , json , and so on, to delta . 
SQL 
Python 
Scala 
Java 
CREATE TABLE delta . ` /tmp/delta-table ` USING DELTA AS SELECT col1 as id FROM VALUES 0 , 1 , 2 , 3 , 4 ; 
data = spark. range ( 0 , 5 ) data.write. format ( " delta " ). save ( " /tmp/delta-table " ) 
val data = spark.range( 0 , 5 ) data.write.format( " delta " ).save( " /tmp/delta-table " ) 
import org.apache.spark.sql.SparkSession ; import org.apache.spark.sql.Dataset ; import org.apache.spark.sql.Row ; SparkSession spark = ... // create SparkSession Dataset < Row > data = spark . range ( 0 , 5 ) ; data . write () . format ( " delta " ) . save ( " /tmp/delta-table " ) ; 
These operations create a new Delta table using the schema that was inferred from your DataFrame. For the full set of options available when you create a new Delta table, see Create a table and Write to a table . 
Note 
This quickstart uses local paths for Delta table locations. For configuring
HDFS or cloud storage for Delta tables, see Storage
configuration . 
Read data Section titled “Read data” 
You read data in your Delta table by specifying the path to the files: "/tmp/delta-table" : 
SQL 
Python 
Scala 
Java 
SELECT * FROM delta. ` /tmp/delta-table ` ; 
df = spark.read. format ( " delta " ). load ( " /tmp/delta-table " ) df. show () 
val df = spark.read.format( " delta " ).load( " /tmp/delta-table " ) df.show() 
Dataset < Row > df = spark . read () . format ( " delta " ) . load ( " /tmp/delta-table " ) ; df . show () ; 
Update table data Section titled “Update table data” 
Delta Lake supports several operations to modify tables using standard DataFrame APIs. This example runs a batch job to overwrite the data in the table: 
Overwrite Section titled “Overwrite” 
SQL 
Python 
Scala 
Java 
INSERT OVERWRITE delta. ` /tmp/delta-table ` SELECT col1 as id FROM VALUES 5 , 6 , 7 , 8 , 9 ; 
data = spark. range ( 5 , 10 ) data.write. format ( " delta " ). mode ( " overwrite " ). save ( " /tmp/delta-table " ) 
val data = spark.range( 5 , 10 ) data.write.format( " delta " ).mode( " overwrite " ).save( " /tmp/delta-table " ) df.show() 
Dataset < Row > data = spark . range ( 5 , 10 ) ; data . write () . format ( " delta " ) . mode ( " overwrite " ) . save ( " /tmp/delta-table " ) ; 
If you read this table again, you should see only the values 5-9 you have added because you overwrote the previous data. 
Conditional update without overwrite Section titled “Conditional update without overwrite” 
Delta Lake provides programmatic APIs to conditional update, delete, and merge (upsert) data into tables. Here are a few examples. 
SQL 
Python 
Scala 
Java 
-- Update every even value by adding 100 to it UPDATE delta. ` /tmp/delta-table ` SET id = id + 100 WHERE id % 2 == 0 ; -- Delete every even value DELETE FROM delta. ` /tmp/delta-table ` WHERE id % 2 == 0 ; -- Upsert (merge) new data CREATE TEMP VIEW newData AS SELECT col1 AS id FROM VALUES 1 , 3 , 5 , 7 , 9 , 11 , 13 , 15 , 17 , 19 ; MERGE INTO delta. ` /tmp/delta-table ` AS oldData USING newData ON oldData . id = newData . id WHEN MATCHED THEN UPDATE SET id = newData . id WHEN NOT MATCHED THEN INSERT (id) VALUES ( newData . id ); SELECT * FROM delta. ` /tmp/delta-table ` ; 
from delta.tables import * from pyspark.sql.functions import * deltaTable = DeltaTable. forPath ( spark , " /tmp/delta-table " ) # Update every even value by adding 100 to it deltaTable. update ( condition = expr ( " id % 2 == 0 " ) , set = { " id " : expr ( " id + 100 " ) } ) # Delete every even value deltaTable. delete ( condition = expr ( " id % 2 == 0 " )) # Upsert (merge) new data newData = spark. range ( 0 , 20 ) deltaTable. alias ( " oldData " ) \ . merge ( newData. alias ( " newData " ) , " oldData.id = newData.id " ) \ . whenMatchedUpdate ( set = { " id " : col ( " newData.id " ) } ) \ . whenNotMatchedInsert ( values = { " id " : col ( " newData.id " ) } ) \ . execute () deltaTable. toDF (). show () 
import io.delta.tables._ import org.apache.spark.sql.functions._ val deltaTable = DeltaTable .forPath( " /tmp/delta-table " ) // Update every even value by adding 100 to it deltaTable.update( condition = expr( " id % 2 == 0 " ), set = Map ( " id " -> expr( " id + 100 " ))) // Delete every even value deltaTable.delete(condition = expr( " id % 2 == 0 " )) // Upsert (merge) new data val newData = spark.range( 0 , 20 ).toDF deltaTable.as( " oldData " ) .merge( newData.as( " newData " ), " oldData.id = newData.id " ) .whenMatched .update( Map ( " id " -> col( " newData.id " ))) .whenNotMatched .insert( Map ( " id " -> col( " newData.id " ))) .execute() deltaTable.toDF.show() 
import io.delta.tables. * ; import org.apache.spark.sql.functions ; import java.util.HashMap ; DeltaTable deltaTable = DeltaTable . forPath ( " /tmp/delta-table " ) ; // Update every even value by adding 100 to it deltaTable . update ( functions . expr ( " id % 2 == 0 " ) , new HashMap < String , Column >() {{ put ( " id " , functions .expr ( " id + 100 " )) ; }} ) ; // Delete every even value deltaTable . delete ( condition = functions . expr ( " id % 2 == 0 " )) ; // Upsert (merge) new data Dataset < Row > newData = spark . range ( 0 , 20 ) . toDF () ; deltaTable . as ( " oldData " ) . merge ( newData . as ( " newData " ) , " oldData.id = newData.id " ) . whenMatched () . update ( new HashMap < String , Column >() {{ put ( " id " , functions .col ( " newData.id " )) ; }} ) . whenNotMatched () . insertExpr ( new HashMap < String , Column >() {{ put ( " id " , functions .col ( " newData.id " )) ; }} ) . execute () ; deltaTable . toDF () . show () ; 
You should see that some of the existing rows have been updated and new rows have been inserted. 
For more information on these operations, see Table deletes, updates, and merges . 
Read older versions of data using time travel Section titled “Read older versions of data using time travel” 
You can query previous snapshots of your Delta table by using time travel. If you want to access the data that you overwrote, you can query a snapshot of the table before you overwrote the first set of data using the versionAsOf option. 
SQL 
Python 
Scala 
Java 
SELECT * FROM delta. ` /tmp/delta-table ` VERSION AS OF 0 ; 
df = spark.read. format ( " delta " ). option ( " versionAsOf " , 0 ). load ( " /tmp/delta-table " ) df. show () 
val df = spark.read.format( " delta " ).option( " versionAsOf " , 0 ).load( " /tmp/delta-table " ) df.show() 
Dataset < Row > df = spark . read () . format ( " delta " ) . option ( " versionAsOf " , 0 ) . load ( " /tmp/delta-table " ) ; df . show () ; 
You should see the first set of data, from before you overwrote it. Time travel takes advantage of the power of the Delta Lake transaction log to access data that is no longer in the table. Removing the version 0 option (or specifying version 1 ) would let you see the newer data again. For more information, see Query an older snapshot of a table (time travel) . 
Write a stream of data to a table Section titled “Write a stream of data to a table” 
You can also write to a Delta table using Structured Streaming. The Delta Lake transaction log guarantees exactly-once processing, even when there are other streams or batch queries running concurrently against the table. By default, streams run in append mode, which adds new records to the table: 
Python 
Scala 
Java 
streamingDf = spark.readStream. format ( " rate " ). load () stream = streamingDf. selectExpr ( " value as id " ).writeStream. format ( " delta " ). option ( " checkpointLocation " , " /tmp/checkpoint " ). start ( " /tmp/delta-table " ) 
val streamingDf = spark.readStream.format( " rate " ).load() val stream = streamingDf.select($ " value " as " id " ).writeStream.format( " delta " ).option( " checkpointLocation " , " /tmp/checkpoint " ).start( " /tmp/delta-table " ) 
import org.apache.spark.sql.streaming.StreamingQuery ; Dataset < Row > streamingDf = spark . readStream () . format ( " rate " ) . load () ; StreamingQuery stream = streamingDf . selectExpr ( " value as id " ) . writeStream () . format ( " delta " ) . option ( " checkpointLocation " , " /tmp/checkpoint " ) . start ( " /tmp/delta-table " ) ; 
While the stream is running, you can read the table using the earlier commands. 
Note 
If you’re running this in a shell, you may see the streaming task progress,
which make it hard to type commands in that shell. It may be useful to start
another shell in a new terminal for querying the table. 
You can stop the stream by running stream.stop() in the same terminal that started the stream. 
For more information about Delta Lake integration with Structured Streaming, see Table streaming reads and writes . See also the Structured Streaming Programming Guide on the Apache Spark website. 
Read a stream of changes from a table Section titled “Read a stream of changes from a table” 
While the stream is writing to the Delta table, you can also read from that table as streaming source. For example, you can start another streaming query that prints all the changes made to the Delta table. You can specify which version Structured Streaming should start from by providing the startingVersion or startingTimestamp option to get changes from that point onwards. See Structured Streaming for details. 
Python 
Scala 
Java 
stream2 = spark.readStream. format ( " delta " ). load ( " /tmp/delta-table " ).writeStream. format ( " console " ). start () 
val stream2 = spark.readStream.format( " delta " ).load( " /tmp/delta-table " ).writeStream.format( " console " ).start() 
StreamingQuery stream2 = spark . readStream () . format ( " delta " ) . load ( " /tmp/delta-table " ) . writeStream () . format ( " console " ) . start () ; Edit page Previous Introduction Next Table batch reads and writes 