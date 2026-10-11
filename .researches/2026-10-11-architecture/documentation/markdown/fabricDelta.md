# fabricDelta

Source: https://learn.microsoft.com/en-us/fabric/fundamentals/delta-lake-interoperability
Retrieved: 2026-10-11

Delta Lake Table Format Interoperability - Microsoft Fabric | Microsoft Learn Skip to main content Skip to Ask Learn chat experience 
This browser is no longer supported. 
Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support. Download Microsoft Edge More info about Internet Explorer and Microsoft Edge Table of contents Exit editor mode Ask Learn Ask Learn Reading mode Table of contents Read in English Add Add to Plans Edit Copy Markdown Print 
Note 
Access to this page requires authorization. You can try signing in or changing directories . 
Access to this page requires authorization. You can try changing directories . 
Delta Lake table format interoperability Feedback Summarize this article for me 
In this article 
In Microsoft Fabric, the Delta Lake table format is the standard for analytics. Delta Lake is an open-source storage layer that brings ACID (Atomicity, Consistency, Isolation, Durability) transactions to big data and analytics workloads. 
All Fabric experiences natively generate and consume Delta Lake tables, providing a unified product experience. Delta Lake tables produced by one compute engine, such as Fabric Data Warehouse or Synapse Spark, can be consumed by any other engine, such as Power BI. When you ingest data into Fabric, it stores the data as Delta tables by default. You can easily integrate external data containing Delta Lake tables by using OneLake shortcuts. 
Delta Lake features and Fabric experiences 
To achieve interoperability, all the Fabric experiences align on the Delta Lake features and Fabric capabilities. Some experiences can only write to Delta Lake tables, while others can read from it. 
Writers : Data warehouses, eventstreams, and exported Power BI semantic models into OneLake 
Readers : SQL analytics endpoint and Power BI direct lake semantic models 
Writers and readers : Fabric Spark runtime, dataflows, pipelines, and Kusto Query Language (KQL) databases 
The following matrix shows key Delta Lake features and their availability on each Fabric experience. 
Fabric capability Column mappings Deletion vectors V-order writing Table optimization and maintenance Partitions 
Data warehouse Delta Lake export Name: Yes ID: No Yes Yes Yes Read: N/A (not applicable) Write: No 
SQL analytics endpoint Name: Yes ID: No Yes N/A (not applicable) N/A (not applicable) Read: Yes Write: N/A (not applicable) 
Lakehouse explorer and preview Name: Yes ID: No Yes N/A (not applicable) Yes Read: Yes Write: N/A (not applicable) 
Fabric Spark Runtime 2.0 Name: Yes ID: Yes Yes Yes Yes Read: Yes Write: Yes 
Fabric Spark Runtime 1.3 Name: Yes ID: Yes Yes Yes Yes Read: Yes Write: Yes 
Fabric Spark Runtime 1.2 Name: Yes ID: Yes Yes Yes Yes Read: Yes Write: Yes 
Fabric Spark Runtime 1.1 Name: Yes ID: Yes No Yes Yes Read: Yes Write: Yes 
Python notebooks Name: No ID: No No No Yes Read: Yes Write: Yes 
Dataflows Gen2 Name: Yes ID: No Yes Yes No Read: Yes Write: Yes 
Pipelines Name: No ID: No No Yes No Read: Yes Write: Yes, overwrite only 
Power BI direct lake semantic models Name: Yes ID: Yes Yes N/A (not applicable) N/A (not applicable) Read: Yes Write: N/A (not applicable) 
Export Power BI semantic models into OneLake Name: Yes ID: No N/A (not applicable) Yes No Read: N/A (not applicable) Write: No 
KQL databases Name: Yes ID: No Yes No No 1 Read: Yes Write: Yes 
Eventstreams Name: No ID: No No No No Read: N/A (not applicable) Write: Yes 
1 KQL databases provide certain table maintenance capabilities such as retention . Data is removed at the end of the retention period from OneLake. For more information, see One Logical copy . 
Fabric capability Liquid Clustering TIMESTAMP_NTZ Delta reader/writer version and default table features Type Widening 
Data warehouse Delta Lake export No No Reader: 3 Writer: 7 Deletion Vectors, Column Mappings (name) Yes 
SQL analytics endpoint Yes No N/A (not applicable) Yes 
Lakehouse explorer and preview Yes Yes N/A (not applicable) Yes 
Fabric Spark Runtime 2.0 Yes Yes Reader: 3 Writer: 7 Deletion Vectors Yes 
Fabric Spark Runtime 1.3 Yes Yes Reader: 1 Writer: 2 No 
Fabric Spark Runtime 1.2 Yes, read only Yes Reader: 1 Writer: 2 No 
Fabric Spark Runtime 1.1 Yes, read only No Reader: 1 Writer: 2 No 
Python notebooks No Yes Reader: 1 Writer: 2 No 
Dataflows Gen2 Yes, read only No Reader: 1 Writer: 2 Yes 
Pipelines Yes, read only No Reader: 1 Writer: 2 Yes: DI Data Pipelines (Copy, Lookup activity) No: DI CopyJob pipelines 
Power BI direct lake semantic models Yes No N/A (not applicable) Yes 
Export Power BI semantic models into OneLake No No Reader: 2 Writer: 5 Column Mappings (name) No 
KQL databases No No Reader: 1 Writer: 1 No 
Eventstreams No No Reader: 1 Writer: 2 No 
Note 
Fabric doesn't write column mappings by default, except where noted. The default Fabric experience generates tables that are compatible across the service. Delta Lake tables produced by third-party services might have incompatible table features. 
Some Fabric experiences don't offer table optimization and maintenance capabilities, such as bin-compaction, V-order, deletion vector merge (PURGE), and clean up of old unreferenced files (VACUUM). To keep Delta Lake tables optimal for analytics, follow the techniques in Run Delta table maintenance in Lakehouse for tables ingested using those experiences. 
For comprehensive cross-workload guidance on table maintenance strategies for different consumption scenarios, see Cross-workload table maintenance and optimization in Microsoft Fabric . 
Current limitations 
Currently, Fabric doesn't support these Delta Lake features: 
Delta Lake 3.x Uniform. This feature is supported only in the Data Engineering Spark-compute (Notebooks, Spark Jobs). 
Identity columns writing (Azure Databricks feature). 
Lakeflow Spark Declarative Pipelines (Azure Databricks feature). 
Delta Lake 4.x features outside of Lakehouse and Spark Notebooks and Jobs: collations, variant type, coordinated commits, and more. Type widening is supported where noted on the previous features matrix in this article. 
Python notebooks Delta Lake feature support : Python notebooks use delta-rs ( deltalake ), DuckDB , and Polars instead of the Spark Delta Lake reader and writer to read and write Delta Lake tables. The deltalake versions currently pinned by Fabric don't support some Delta Lake table features, including deletion vectors, column mapping, liquid clustering writes and optimization, and type widening. Polars read_delta and write_delta use deltalake as the backend, so they share the same limitations. 
Python notebooks Delta Lake workarounds and fallback : The DuckDB delta_scan function can provide a read-only workaround for some tables that deltalake can't read, such as tables with deletion vectors. If a Delta Lake capability isn't available or doesn't work in a Python notebook, use a PySpark notebook instead. PySpark notebooks provide the most complete Delta Lake support in Fabric and cover the Delta Lake scenarios listed for Fabric Spark runtimes in these tables. For more information, see Data interaction in Python notebooks and the Choosing between Python and PySpark Notebooks in Microsoft Fabric . 
Special characters on table names 
Fabric supports special characters as part of the table names. This feature allows the usage of Unicode characters to compose table names in Fabric experiences. 
The following special characters are either reserved or not compatible with at least one of Fabric technologies and must not be used as part of a table name: " (double quotes), ' (single quote), # , % , + , : , ? , or ` (backtick). 
Related content 
Delta Lake in Microsoft Fabric overview 
Cross-workload table maintenance and optimization in Microsoft Fabric 
Lakehouse and Delta Lake tables 
Direct Lake overview 
Querying tables from the Warehouse through its published Delta Lake Logs 
Feedback 
Was this page helpful? Yes No No 
Need help with this topic? 
Want to try using Ask Learn to clarify or guide you through this topic? Ask Learn Ask Learn Suggest a fix? 
Additional resources 
Last updated on 2026-10-07 
In this article 
Was this page helpful? 
Need help with this topic? 
Want to try using Ask Learn to clarify or guide you through this topic? Ask Learn Ask Learn Suggest a fix? en-us Your Privacy Choices Theme 
Light 
Dark 
High contrast 

AI Disclaimer 
Previous Versions 
Blog 
Contribute 
Privacy 
Consumer Health Privacy 
Terms of Use 
Trademarks 
© Microsoft 2026 