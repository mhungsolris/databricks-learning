# databricks-foreachbatch

Source: https://docs.databricks.com/aws/en/structured-streaming/foreach
Retrieved: 2026-10-11

Use foreachBatch to write to arbitrary data sinks | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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
Lakeflow Connect 
Streaming connectors 
Stream from other sources 
Arbitrary sinks with foreachBatch On this page Last updated on Sep 11, 2026 
Use foreachBatch to write to arbitrary data sinks 
This page shows how to use foreachBatch with Structured Streaming to write the output of a streaming query to data sources that do not have an existing streaming sink. 
The code pattern streamingDF.writeStream.foreachBatch(...) allows you to apply batch functions to the output data of every micro-batch of the streaming query. Functions used with foreachBatch take two parameters: 
A DataFrame that has the output data of a micro-batch. 
The unique ID of the micro-batch. 
You must use foreachBatch for Delta Lake merge operations in Structured Streaming . See Upsert from streaming queries using foreachBatch . 
Apply additional DataFrame operations ​ 
Many DataFrame and Dataset operations are not supported in streaming DataFrames because Spark does not support generating incremental plans in those cases. Using foreachBatch() you can apply some of these operations on each micro-batch output. For example, you can use foreachBatch() and the SQL MERGE INTO operation to write the output of streaming aggregations into a Delta Lake table in update mode. See more details in MERGE INTO . important 
foreachBatch() provides only at-least-once write guarantees. However, you can use the batchId provided to the function as way to deduplicate the output and get an exactly-once guarantee. In either case, you will have to reason about the end-to-end semantics yourself. 
foreachBatch() does not work with the continuous processing mode as it fundamentally relies on the micro-batch execution of a streaming query. If you write data in continuous mode, use foreach() instead. 
When using foreachBatch with a stateful operator, it is important to completely consume each batch before processing is complete. See Completely consume each batch DataFrame 
Handle empty DataFrames ​ 
foreachBatch() might receive an empty DataFrame, and your code must handle this scenario. Otherwise, your query might fail. 
For example, when Delta Lake is the streaming source, these scenarios might pass an empty DataFrame to foreachBatch() : 
OPTIMIZE with no files to process: When an OPTIMIZE operation runs on the Delta Lake source table but there are no files to process, Structured Streaming writes an offset log entry to increment the table version. This produces an empty micro-batch on the sink even though no files are read. 
File pruning at the physical plan level: If predicate pushdown or file pruning eliminates all records at the physical plan level, the result is an empty commit to the sink. 
User code must handle empty DataFrames to allow for proper operation. See the examples below: 
Python 
Scala Python 
def process_batch ( output_df , batch_id ) : # Process valid DataFrames only if not output_df . isEmpty ( ) : # business logic pass streamingDF . writeStream . foreachBatch ( process_batch ) . start ( ) Scala 
. foreachBatch ( ( outputDf : DataFrame , bid : Long ) => { // Process valid DataFrames only if ( ! outputDf . isEmpty ) { // business logic } } ) . start ( ) 
Behavior changes for foreachBatch in Databricks Runtime 14.0 ​ 
In Databricks Runtime 14.0 and above on compute configured with standard access mode, the following behavior changes apply: 
print() commands write output to the driver logs. 
You cannot access the dbutils.widgets submodule inside the function. 
Any files, modules, or objects referenced in the function must be serializable and available on Spark. 
Reuse existing batch data sources ​ 
Using foreachBatch() , you can use existing batch data writers for data sinks that might not have Structured Streaming support. Here are a few examples: 
Cassandra Scala example 
Azure Synapse Analytics Python example 
Many other batch data sources can be used from foreachBatch() . See Connect to data sources and external services . 
Write to multiple locations ​ 
If you need to write the output of a streaming query to multiple locations, Databricks recommends using multiple Structured Streaming writers for best parallelization and throughput. 
Using foreachBatch to write to multiple sinks serializes the execution of streaming writes, which can increase latency for each micro-batch. 
If you do use foreachBatch to write to multiple Delta Lake tables, see Use foreachBatch for idempotent table writes . 
Completely consume each batch DataFrame ​ 
When you are using stateful operators (for example, using dropDuplicatesWithinWatermark ), each batch iteration must consume the entire DataFrame or restart the query. If you do not consume the entire DataFrame, the streaming query will fail with the next batch. 
This can happen in several cases. The following examples show how to fix queries that do not correctly consume a DataFrame. 
Intentionally using a subset of the batch ​ 
If you only care about a subset of the batch, you could have code such as the following. Python 
from pyspark . sql . functions import expr stream = spark . readStream . format ( "rate" ) . option ( "rowsPerSecond" , "100" ) . load ( ) # creates a stateful operator: streamWithWatermark = stream . withWatermark ( "timestamp" , "15 minutes" ) . dropDuplicatesWithinWatermark ( ) def partial_func ( batch_df , batch_id ) : batch_df . show ( 2 ) q = streamWithWatermark . writeStream \ . foreachBatch ( partial_func ) \ . option ( "checkpointLocation" , checkpoint_dir ) \ . trigger ( processingTime = '2 seconds' ) \ . start ( ) 
In this case, the batch_df.show(2) only handles the first two items in the batch, which is expected, but if there are more items, they must be consumed. The following code consumes the full DataFrame. Python 
from pyspark . sql . functions import expr stream = spark . readStream . format ( "rate" ) . option ( "rowsPerSecond" , "100" ) . load ( ) streamWithWatermark = stream . withWatermark ( "timestamp" , "15 minutes" ) . dropDuplicatesWithinWatermark ( ) # function to do nothing with a row def do_nothing ( row ) : pass def partial_func ( batch_df , batch_id ) : batch_df . show ( 2 ) batch_df . foreach ( do_nothing ) # silently consume the rest of the batch q = streamWithWatermark . writeStream \ . foreachBatch ( partial_func ) \ . option ( "checkpointLocation" , checkpoint_dir ) \ . trigger ( processingTime = '2 seconds' ) \ . start ( ) 
Here, the do_nothing function silently ignores the rest of the DataFrame. 
Handling an error in a batch ​ 
For error handling in foreachBatch , Databricks recommends that you allow the streaming query to fail fast and instead rely on the orchestration layer, such as Lakeflow Jobs or Apache Airflow, to manage the retry logic. This is much safer than building complex retry loops in your code, where data loss may occur. 
Here are guidelines based on your write target: 

Target 
Examples 
Guidance 

DataFrame operations 
Delta Lake tables 
You must use the txnAppId and txnVersion write options, binding txnVersion to batchId , to guarantee idempotency and protect data correctness on retries. Do not catch and retry exceptions locally. Instead, Databricks recommends that you allow errors to propagate so that Spark metrics stay accurate, data does not duplicate, and the orchestrator can cleanly retry the full batch. 

Custom code and external destinations 
.collect() , OLTP databases, message queues, APIs 
Implement your own idempotency. You must assume that any operation can and will be retried across batches. If the batchId stays the same, the result of your operation must remain the same. You may retry purely transient errors such as brief connection timeouts, but take extreme care to avoid partial or duplicate writes if the retry ultimately fails. The safest approach is to let errors propagate and allow the orchestrator to retry the entire batch. ← ✕ 

Target 
Examples 
Guidance 

DataFrame operations 
Delta Lake tables 
You must use the txnAppId and txnVersion write options, binding txnVersion to batchId , to guarantee idempotency and protect data correctness on retries. Do not catch and retry exceptions locally. Instead, Databricks recommends that you allow errors to propagate so that Spark metrics stay accurate, data does not duplicate, and the orchestrator can cleanly retry the full batch. 

Custom code and external destinations 
.collect() , OLTP databases, message queues, APIs 
Implement your own idempotency. You must assume that any operation can and will be retried across batches. If the batchId stays the same, the result of your operation must remain the same. You may retry purely transient errors such as brief connection timeouts, but take extreme care to avoid partial or duplicate writes if the retry ultimately fails. The safest approach is to let errors propagate and allow the orchestrator to retry the entire batch. 
Here are some examples of exception types and recommendations for how to handle them in foreachBatch : 

Exception type 
Examples 
Recommended action 

Transient sink errors 
SQLTransientConnectionException , HTTP 429, timeouts 
Catch : retry, or send to a dead-letter queue 

Duplicate or key constraint violations when the sink is idempotent 
SQLIntegrityConstraintViolationException 
Catch : log and suppress 

Custom retryable errors 
Wrapped socket exceptions, retriable database errors 
Catch : increment metrics and allow controlled continuation 

Logic or schema errors 
NullPointerException , AttributeError , schema mismatch 
Propagate : let Spark fail the query 

Non-retryable sink errors or uncaught logic bugs 
ValueError , PermissionError 
Propagate : let Spark fail the query 

Critical failures 
OutOfMemoryError , corrupted state, data integrity violations 
Propagate : let Spark fail the query ← ✕ 

Exception type 
Examples 
Recommended action 

Transient sink errors 
SQLTransientConnectionException , HTTP 429, timeouts 
Catch : retry, or send to a dead-letter queue 

Duplicate or key constraint violations when the sink is idempotent 
SQLIntegrityConstraintViolationException 
Catch : log and suppress 

Custom retryable errors 
Wrapped socket exceptions, retriable database errors 
Catch : increment metrics and allow controlled continuation 

Logic or schema errors 
NullPointerException , AttributeError , schema mismatch 
Propagate : let Spark fail the query 

Non-retryable sink errors or uncaught logic bugs 
ValueError , PermissionError 
Propagate : let Spark fail the query 

Critical failures 
OutOfMemoryError , corrupted state, data integrity violations 
Propagate : let Spark fail the query Code examples: exception handling ​ 
The following examples intentionally raise an error in foreach to show different approaches to handle the error: Python 
from pyspark . sql . functions import expr stream = spark . readStream . format ( "rate" ) . option ( "rowsPerSecond" , "100" ) . load ( ) # creates a stateful operator: streamWithWatermark = stream . withWatermark ( "timestamp" , "15 minutes" ) . dropDuplicatesWithinWatermark ( ) def foreach_func ( row ) : # handle the row, but in this case, for the sample, will just raise an error: raise Exception ( 'error' ) def partial_func ( batch_df , batch_id ) : try : batch_df . foreach ( foreach_func ) except Exception as e : print ( e ) # or whatever error handling you want to have q = streamWithWatermark . writeStream \ . foreachBatch ( partial_func ) \ . option ( "checkpointLocation" , checkpoint_dir ) \ . trigger ( processingTime = '2 seconds' ) \ . start ( ) 
The above code handles and silently suppresses the error, and may not consume the rest of the batch. There are two options for handling this situation. 
First, you can re-raise the error, which passes it up to your orchestration layer to retry the batch. This can solve the error, if it is a transient problem, or raise it for your operations team to try to manually fix. To do this, change the partial_func code to look like this: Python 
def partial_func ( batch_df , batch_id ) : try : batch_df . foreach ( foreach_func ) except Exception as e : print ( e ) # or whatever error handling you want to have raise e # re-raise the issue 
Second, if you want to catch the exception and ignore the rest of the batch, you can change the code to use the do_nothing function to silently ignore the rest of the batch. Python 
from pyspark . sql . functions import expr stream = spark . readStream . format ( "rate" ) . option ( "rowsPerSecond" , "100" ) . load ( ) # creates a stateful operator: streamWithWatermark = stream . withWatermark ( "timestamp" , "15 minutes" ) . dropDuplicatesWithinWatermark ( ) def foreach_func ( row ) : # handle the row, but in this case, for the sample, will just raise an error: raise Exception ( 'error' ) # function to do nothing with a row def do_nothing ( row ) : pass def partial_func ( batch_df , batch_id ) : try : batch_df . foreach ( foreach_func ) except Exception as e : print ( e ) # or whatever error handling you want to have batch_df . foreach ( do_nothing ) # silently consume the remainder of the batch q = streamWithWatermark . writeStream \ . foreachBatch ( partial_func ) \ . option ( "checkpointLocation" , checkpoint_dir ) \ . trigger ( processingTime = '2 seconds' ) \ . start ( ) 
Write failed records to a dead-letter queue ​ 
By default, queries fail immediately when bad records arrive. Avoid these interruptions by configuring a secondary Delta Lake table as a dead-letter queue (DLQ). 
With a DLQ, the system routes failed records to the secondary table and continues processing valid data uninterrupted. The DLQ table allows you to inspect and reprocess the bad records later. 
Use this method when: 
Your stream contains varied data that might violate schema constraints or business rules. 
Audit or compliance rules require that you preserve all records. 
Example ​ 
The following example uses foreachBatch to split each micro-batch into valid and invalid records, then writes each subset to its own Delta Lake table. note 
This runnable example creates tables in a dedicated main.streaming_examples schema so it can run without affecting your existing data. If you don't have permission to create schemas in the main catalog, change the catalog and schema to a location where you can create tables. 
Python 
Scala Python 
from pyspark . sql . functions import current_timestamp , lit import uuid source_table = "main.streaming_examples.raw_orders" main_table = "main.streaming_examples.orders" dlq_table = "main.streaming_examples.orders_dlq" app_id = "orders-streaming-job" # Create a dedicated schema for the example tables spark . sql ( "CREATE SCHEMA IF NOT EXISTS main.streaming_examples" ) # Seed the source with a mix of valid and invalid orders spark . sql ( f"DROP TABLE IF EXISTS { main_table } " ) spark . sql ( f"DROP TABLE IF EXISTS { dlq_table } " ) spark . sql ( f"DROP TABLE IF EXISTS { source_table } " ) spark . createDataFrame ( [ ( "ord1" , 100 , "cust1" ) , # valid ( "ord2" , - 50 , "cust2" ) , # invalid: non-positive amount ( "ord3" , 200 , None ) , # invalid: missing customer_id ( "ord4" , 300 , "cust4" ) , # valid ] , "order_id string, order_amount int, customer_id string" , ) . write . saveAsTable ( source_table ) def process_orders ( batch_df , batch_id ) : if batch_df . isEmpty ( ) : return valid_condition = "order_amount > 0 AND customer_id IS NOT NULL" # Write valid records to the main table with idempotency options batch_df . filter ( valid_condition ) . write \ . format ( "delta" ) \ . mode ( "append" ) \ . option ( "txnVersion" , batch_id ) \ . option ( "txnAppId" , app_id ) \ . saveAsTable ( main_table ) # Route invalid records to the dead-letter queue invalid_df = batch_df . filter ( f"NOT ( { valid_condition } )" ) if not invalid_df . isEmpty ( ) : invalid_df \ . withColumn ( "dlq_batch_id" , lit ( batch_id ) ) \ . withColumn ( "dlq_ingest_time" , current_timestamp ( ) ) \ . write \ . format ( "delta" ) \ . mode ( "append" ) \ . option ( "txnVersion" , batch_id ) \ . option ( "txnAppId" , app_id ) \ . saveAsTable ( dlq_table ) q = spark . readStream \ . format ( "delta" ) \ . table ( source_table ) \ . writeStream \ . foreachBatch ( process_orders ) \ . option ( "checkpointLocation" , f"/tmp/checkpoint_dlq_ { uuid . uuid4 ( ) } " ) \ . trigger ( availableNow = True ) \ . start ( ) q . awaitTermination ( ) # Valid orders (ord1, ord4) land in the main table; invalid orders (ord2, ord3) route to the DLQ display ( spark . sql ( f"SELECT * FROM { main_table } ORDER BY order_id" ) ) display ( spark . sql ( f"SELECT order_id, dlq_batch_id FROM { dlq_table } ORDER BY order_id" ) ) Scala 
import org . apache . spark . sql . DataFrame import org . apache . spark . sql . functions . { current_timestamp , lit } import org . apache . spark . sql . streaming . Trigger import spark . implicits . _ import java . util . UUID val sourceTable = "main.streaming_examples.raw_orders" val mainTable = "main.streaming_examples.orders" val dlqTable = "main.streaming_examples.orders_dlq" val appId = "orders-streaming-job" // Create a dedicated schema for the example tables spark . sql ( "CREATE SCHEMA IF NOT EXISTS main.streaming_examples" ) // Seed the source with a mix of valid and invalid orders spark . sql ( s "DROP TABLE IF EXISTS $ mainTable " ) spark . sql ( s "DROP TABLE IF EXISTS $ dlqTable " ) spark . sql ( s "DROP TABLE IF EXISTS $ sourceTable " ) Seq ( ( "ord1" , 100 , "cust1" ) , // valid ( "ord2" , - 50 , "cust2" ) , // invalid: non-positive amount ( "ord3" , 200 , null . asInstanceOf [ String ] ) , // invalid: missing customer_id ( "ord4" , 300 , "cust4" ) // valid ) . toDF ( "order_id" , "order_amount" , "customer_id" ) . write . saveAsTable ( sourceTable ) def processOrders ( batchDf : DataFrame , batchId : Long ) : Unit = { if ( batchDf . isEmpty ) return val validCondition = "order_amount > 0 AND customer_id IS NOT NULL" // Write valid records to the main table with idempotency options batchDf . filter ( validCondition ) . write . format ( "delta" ) . mode ( "append" ) . option ( "txnVersion" , batchId ) . option ( "txnAppId" , appId ) . saveAsTable ( mainTable ) // Route invalid records to the dead-letter queue val invalidDf = batchDf . filter ( s "NOT ( $ validCondition )" ) if ( ! invalidDf . isEmpty ) { invalidDf . withColumn ( "dlq_batch_id" , lit ( batchId ) ) . withColumn ( "dlq_ingest_time" , current_timestamp ( ) ) . write . format ( "delta" ) . mode ( "append" ) . option ( "txnVersion" , batchId ) . option ( "txnAppId" , appId ) . saveAsTable ( dlqTable ) } } val q = spark . readStream . format ( "delta" ) . table ( sourceTable ) . writeStream . foreachBatch ( processOrders _ ) . option ( "checkpointLocation" , s "/tmp/checkpoint_dlq_ ${ UUID . randomUUID ( ) } " ) . trigger ( Trigger . AvailableNow ( ) ) . start ( ) q . awaitTermination ( ) // Valid orders (ord1, ord4) land in the main table; invalid orders (ord2, ord3) route to the DLQ spark . sql ( s "SELECT * FROM $ mainTable ORDER BY order_id" ) . show ( ) spark . sql ( s "SELECT order_id, dlq_batch_id FROM $ dlqTable ORDER BY order_id" ) . show ( ) 
Both writes use txnVersion and txnAppId to guarantee idempotency. If Spark replays a batch with the same batchId , Delta Lake skips the duplicate write. See Use foreachBatch for idempotent table writes . On this page 
Apply additional DataFrame operations 
Handle empty DataFrames 
Behavior changes for foreachBatch in Databricks Runtime 14.0 
Reuse existing batch data sources 
Write to multiple locations 
Completely consume each batch DataFrame 
Intentionally using a subset of the batch 
Handling an error in a batch 
Write failed records to a dead-letter queue 
Example Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 