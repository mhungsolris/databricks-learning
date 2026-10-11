# bq-pricing

Source: https://cloud.google.com/bigquery/pricing
Retrieved: 2026-10-10

BigQuery | Google Cloud Page Contents 
BigQuery pricing 
BigQuery is a serverless data analytics platform. You don't need to provision individual instances or virtual machines to use BigQuery. Instead, BigQuery automatically allocates computing resources as you need them. You can also reserve compute capacity ahead of time in the form of slots, which represent virtual CPUs. The pricing structure of BigQuery reflects this design. 

Overview of BigQuery pricing 
BigQuery pricing has two main components: 
Compute pricing is the cost to process queries, including SQL queries, user-defined functions, scripts, and certain data manipulation language (DML) and data definition language (DDL) statements. 
Storage pricing is the cost to store data that you load into BigQuery. 
BigQuery charges for other operations, including using BigQuery Omni , BigQuery ML , BI Engine , and streaming reads and writes . 
In addition, BigQuery has free operations and a free usage tier . 
Every project that you create has a billing account attached to it. Any charges incurred by BigQuery jobs run in the project are billed to the attached billing account. BigQuery storage charges are also billed to the attached billing account. You can view BigQuery costs and trends by using the Cloud Billing reports page in the Google Cloud console. 
Key Point: Pricing models apply to accounts, not individual projects, unless otherwise specified. 

Compute pricing models 
BigQuery offers a choice of two compute pricing models for running queries: 
On-demand pricing (per TiB). With this pricing model, you are charged for the number of bytes processed by each query. The first 1 TiB of query data processed per month is free. 
Capacity pricing (per slot-hour). With this pricing model, you are charged for compute capacity used to run queries, measured in slots (virtual CPUs) over time. This model takes advantage of BigQuery editions . You can use the BigQuery autoscaler or purchase slot commitments, which are dedicated capacity that is always available for your workloads, at a lower price. 
For more information about which pricing to choose for your workloads, see Workload management using Reservations . 

Gemini in BigQuery pricing 
See Gemini in BigQuery Pricing Overview for information about pricing for Gemini in BigQuery. 
On-demand compute pricing 
By default, queries are billed using the on-demand (per TiB) pricing model, where you pay for the data scanned by your queries. 
With on-demand pricing, you will generally have access to up to 2,000 concurrent slots, shared among all queries in a single project. Periodically, BigQuery will temporarily burst beyond this limit to accelerate smaller queries. In addition, you might have fewer slots available if there is a high amount of contention for capacity in a specific location. 
On-demand (per TiB) query pricing is as follows: Iowa (us-central1) 
Johannesburg (africa-south1) 
Taiwan (asia-east1) 
Hong Kong (asia-east2) 
Tokyo (asia-northeast1) 
Osaka (asia-northeast2) 
Seoul (asia-northeast3) 
Mumbai (asia-south1) 
Delhi (asia-south2) 
Singapore (asia-southeast1) 
Jakarta (asia-southeast2) 
Bangkok (asia-southeast3) 
Kuala Lumpur (asia-southeast4) 
Sydney (australia-southeast1) 
Melbourne (australia-southeast2) 
Europe (eu) 
Warsaw (europe-central2) 
Finland (europe-north1) 
Stockholm (europe-north2) 
Madrid (europe-southwest1) 
Belgium (europe-west1) 
Berlin (europe-west10) 
Turin (europe-west12) 
London (europe-west2) 
Frankfurt (europe-west3) 
Netherlands (europe-west4) 
Zurich (europe-west6) 
Milan (europe-west8) 
Paris (europe-west9) 
Doha (me-central1) 
Dammam (me-central2) 
Tel Aviv (me-west1) 
Montreal (northamerica-northeast1) 
Toronto (northamerica-northeast2) 
Mexico (northamerica-south1) 
Sao Paulo (southamerica-east1) 
Santiago (southamerica-west1) 
US (us) 
Iowa (us-central1) 
South Carolina (us-east1) 
Northern Virginia (us-east4) 
Columbus (us-east5) 
Alabama (us-east7) 
Dallas (us-south1) 
Oregon (us-west1) 
Los Angeles (us-west2) 
Salt Lake City (us-west3) 
Las Vegas (us-west4) 
Phoenix (us-west8) 

Operation 
Price (USD) 
Details 

Queries (on-demand) 0 tebibyte to 1 tebibyte Free per 1 month / account 1 tebibyte and above $6.25 / 1 tebibyte, per 1 month / account 
The first 1 TiB per month is free. 
If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply. 

Pricing details 
Note the following regarding on-demand (per TiB) query charges: 
BigQuery uses a columnar data structure . You're charged according to the total data processed in the columns you select, and the total data per column is calculated based on the types of data in the column. For more information about how your data size is calculated, see Estimate query costs . 
You are charged for queries run against shared data. The data owner is not charged when their data is accessed. 
You aren't charged for queries that return an error or for queries that retrieve results from the cache . For procedural language jobs this consideration is provided at a per-statement level. 
Charges are rounded up to the nearest MB, with a minimum 10 MB data processed per table referenced by the query, and with a minimum 10 MB data processed per query. 
Canceling a running query job might incur charges up to the full cost for the query if you let the query run to completion. 
When you run a query, you're charged according to the data processed in the columns you select, even if you set an explicit LIMIT on the results. 
Partitioning and clustering your tables can help reduce the amount of data processed by queries. As a best practice, use partitioning and clustering whenever possible. 
On-demand (per TiB) pricing is referred to as analysis pricing on the Google Cloud SKUs page. 
When you run a query against a clustered table, and the query includes a filter on the clustered columns, BigQuery uses the filter expression to prune the blocks scanned by the query. This can reduce the number of scanned bytes. 
BigQuery provides cost control mechanisms that enable you to cap your query costs. You can set: 
User-level and project-level custom cost controls 
The maximum bytes billed by a query 
For detailed examples of how to calculate the number of bytes processed, see Query size calculation . 
Capacity compute pricing 
BigQuery offers a capacity-based compute pricing model for customers who need additional capacity or prefer a predictable cost for query workloads rather than the on-demand price (per TiB of data processed). The capacity compute model offers pay-as-you-go pricing (with autoscaling) and optional one year and three year commitments that provide discounted prices. You pay for query processing capacity, measured in slots (virtual CPUs) over time. 
To enable capacity pricing, use BigQuery reservations . 
BigQuery slot capacity: 
is available in 3 editions: Standard, Enterprise, and Enterprise Plus. 
applies to query costs, including BigQuery ML, DML, and DDL statements. 
does not apply to storage costs or BI Engine costs. 
does not apply to streaming inserts and using the BigQuery Storage API . 
can leverage the BigQuery autoscaler. 
is billed per second with a one-minute minimum duration by default. You can opt in to BigQuery fluid scaling at the reservation level for per-second billing with no minimum duration. 
Optional BigQuery slot commitments : 
are available for one or three year periods. 
are available in Enterprise and Enterprise Plus editions. 
are regional capacity. Commitments in one region (either customer selected single region or BigQuery selected single region on the customer’s behalf when the customer chooses multi-region) cannot be used in another region. 
can be shared across your entire organization. There is no need to buy slot commitments for every project. 
are offered with a 50-slot minimum and increments of 50 slots. 
are automatically renewed unless set to cancel at the end of the period. 

Standard Edition 
The following table shows the cost of slots in Standard edition. Iowa (us-central1) 
Johannesburg (africa-south1) 
Taiwan (asia-east1) 
Hong Kong (asia-east2) 
Tokyo (asia-northeast1) 
Osaka (asia-northeast2) 
Seoul (asia-northeast3) 
Mumbai (asia-south1) 
Delhi (asia-south2) 
Singapore (asia-southeast1) 
Jakarta (asia-southeast2) 
Bangkok (asia-southeast3) 
Kuala Lumpur (asia-southeast4) 
Sydney (australia-southeast1) 
Melbourne (australia-southeast2) 
Europe (eu) 
Warsaw (europe-central2) 
Finland (europe-north1) 
Stockholm (europe-north2) 
Madrid (europe-southwest1) 
Belgium (europe-west1) 
Berlin (europe-west10) 
Turin (europe-west12) 
London (europe-west2) 
Frankfurt (europe-west3) 
Netherlands (europe-west4) 
Galaxy Frankfurt (europe-west5) 
Zurich (europe-west6) 
Milan (europe-west8) 
Paris (europe-west9) 
Doha (me-central1) 
Dammam (me-central2) 
Tel Aviv (me-west1) 
Montreal (northamerica-northeast1) 
Toronto (northamerica-northeast2) 
Mexico (northamerica-south1) 
Sao Paulo (southamerica-east1) 
Santiago (southamerica-west1) 
US (us) 
Iowa (us-central1) 
Oklahoma (us-central2) 
South Carolina (us-east1) 
Northern Virginia (us-east4) 
Columbus (us-east5) 
Alabama (us-east7) 
Dallas (us-south1) 
Oregon (us-west1) 
Los Angeles (us-west2) 
Salt Lake City (us-west3) 
Las Vegas (us-west4) 
Phoenix (us-west8) Show discount options Hourly Hourly Monthly Monthly 

Default * (USD) info 
Consumption model ID: 7754-699E-0EBF BigQuery CUD - 1 Year * (USD) info 
Consumption model ID: DD83-D9A3-79AF BigQuery CUD - 3 Year * (USD) info 
Consumption model ID: 4D8D-49A7-C5B1 
Details 
$0.04 / 1 hour $0.036 / 1 hour $0.032 / 1 hour 
No commitment. Billed per second with a 1-minute minimum. Opt-in to Fluid scaling for no-minimum, per-second billing * Each consumption model has a unique ID. You may need to opt-in to be eligible for consumption model discounts. Click here to learn more. 
* Prices reflect Pay as you go 

Enterprise Edition 
The following table shows the cost of slots in Enterprise edition. Iowa (us-central1) 
Seoul (AWS) (aws-ap-northeast-2) 
Sydney (AWS) (aws-ap-southeast-2) 
Frankfurt (AWS) (aws-eu-central-1) 
Ireland (AWS) (aws-eu-west-1) 
Northern Virginia (AWS) (aws-us-east-1) 
Oregon (AWS) (aws-us-west-2) 
Virginia (Azure) (azure-us-east2) 
Washington (Azure) (azure-westus2) 
Johannesburg (africa-south1) 
Taiwan (asia-east1) 
Hong Kong (asia-east2) 
Tokyo (asia-northeast1) 
Osaka (asia-northeast2) 
Seoul (asia-northeast3) 
Mumbai (asia-south1) 
Delhi (asia-south2) 
Singapore (asia-southeast1) 
Jakarta (asia-southeast2) 
Bangkok (asia-southeast3) 
Kuala Lumpur (asia-southeast4) 
Sydney (australia-southeast1) 
Melbourne (australia-southeast2) 
Europe (eu) 
Warsaw (europe-central2) 
Finland (europe-north1) 
Stockholm (europe-north2) 
Madrid (europe-southwest1) 
Belgium (europe-west1) 
Berlin (europe-west10) 
Turin (europe-west12) 
London (europe-west2) 
Frankfurt (europe-west3) 
Netherlands (europe-west4) 
Galaxy Frankfurt (europe-west5) 
Zurich (europe-west6) 
Milan (europe-west8) 
Paris (europe-west9) 
Doha (me-central1) 
Dammam (me-central2) 
Tel Aviv (me-west1) 
Montreal (northamerica-northeast1) 
Toronto (northamerica-northeast2) 
Mexico (northamerica-south1) 
Sao Paulo (southamerica-east1) 
Santiago (southamerica-west1) 
US (us) 
Iowa (us-central1) 
Oklahoma (us-central2) 
South Carolina (us-east1) 
Northern Virginia (us-east4) 
Columbus (us-east5) 
Alabama (us-east7) 
Dallas (us-south1) 
Oregon (us-west1) 
Los Angeles (us-west2) 
Salt Lake City (us-west3) 
Las Vegas (us-west4) 
Phoenix (us-west8) Show discount options Hourly Hourly Monthly Monthly 

Default* (USD) info 
Consumption model ID: 7754-699E-0EBF BigQuery CUD - 1 Year * (USD) info 
Consumption model ID: DD83-D9A3-79AF BigQuery CUD - 3 Year * (USD) info 
Consumption model ID: 4D8D-49A7-C5B1 
Resource CUDs - 1 Year (USD) 
Resource CUDs - 3 Year (USD) 
$0.06 / 1 hour $0.054 / 1 hour $0.048 / 1 hour $0.048 / 1 hour $0.036 / 1 hour * Each consumption model has a unique ID. You may need to opt-in to be eligible for consumption model discounts. Click here to learn more. 
* Prices reflect Pay as you go 
1 Billed per second with a 1 minute minimum 

Enterprise Plus Edition 
The following table shows the cost of slots in Enterprise plus edition. Iowa (us-central1) 
Seoul (AWS) (aws-ap-northeast-2) 
Sydney (AWS) (aws-ap-southeast-2) 
Frankfurt (AWS) (aws-eu-central-1) 
Ireland (AWS) (aws-eu-west-1) 
Northern Virginia (AWS) (aws-us-east-1) 
Oregon (AWS) (aws-us-west-2) 
Virginia (Azure) (azure-us-east2) 
Washington (Azure) (azure-westus2) 
Johannesburg (africa-south1) 
Taiwan (asia-east1) 
Hong Kong (asia-east2) 
Tokyo (asia-northeast1) 
Osaka (asia-northeast2) 
Seoul (asia-northeast3) 
Mumbai (asia-south1) 
Delhi (asia-south2) 
Singapore (asia-southeast1) 
Jakarta (asia-southeast2) 
Bangkok (asia-southeast3) 
Kuala Lumpur (asia-southeast4) 
Sydney (australia-southeast1) 
Melbourne (australia-southeast2) 
Europe (eu) 
Warsaw (europe-central2) 
Finland (europe-north1) 
Stockholm (europe-north2) 
Madrid (europe-southwest1) 
Belgium (europe-west1) 
Berlin (europe-west10) 
Turin (europe-west12) 
London (europe-west2) 
Frankfurt (europe-west3) 
Netherlands (europe-west4) 
Galaxy Frankfurt (europe-west5) 
Zurich (europe-west6) 
Milan (europe-west8) 
Paris (europe-west9) 
Doha (me-central1) 
Dammam (me-central2) 
Tel Aviv (me-west1) 
Montreal (northamerica-northeast1) 
Toronto (northamerica-northeast2) 
Mexico (northamerica-south1) 
Sao Paulo (southamerica-east1) 
Santiago (southamerica-west1) 
US (us) 
Iowa (us-central1) 
Oklahoma (us-central2) 
South Carolina (us-east1) 
Northern Virginia (us-east4) 
Columbus (us-east5) 
Alabama (us-east7) 
Dallas (us-south1) 
Oregon (us-west1) 
Los Angeles (us-west2) 
Salt Lake City (us-west3) 
Las Vegas (us-west4) 
Phoenix (us-west8) Show discount options Hourly Hourly Monthly Monthly 

Default* (USD) info 
Consumption model ID: 7754-699E-0EBF BigQuery CUD - 1 Year * (USD) info 
Consumption model ID: DD83-D9A3-79AF BigQuery CUD - 3 Year * (USD) info 
Consumption model ID: 4D8D-49A7-C5B1 
Resource CUDs - 1 Year (USD) 
Resource CUDs - 3 Year (USD) 
$0.10 / 1 hour $0.09 / 1 hour $0.08 / 1 hour $0.08 / 1 hour $0.06 / 1 hour * Each consumption model has a unique ID. You may need to opt-in to be eligible for consumption model discounts. Click here to learn more. 
*Prices reflect Pay as you go 
1 Billed per second with a 1 minute minimum 
BigQuery services pricing 
Additional services that are used as part of BigQuery will be billed using the BigQuery services SKU. These services include data transfer service. 
The following table shows the various services that are billed using BigQuery services SKU . 

Service 
How to Use 
Notes 

Earth Engine in BigQuery 
ST_RegionStats() calls in BigQuery scripts 
This function sends tasks to Earth Engine; Earth Engine Compute Units are translated to BigQuery services slot hours. 

Python UDF 
Refer to this link 
BigQuery customers are charged for building and executing Python UDFs. Build charges are proportional to the build-time and the execution charges are proportional to compute and memory usage of the UDF. 
To see pricing, select a region from the drop-down list above the following table: Iowa (us-central1) 
Johannesburg (africa-south1) 
Taiwan (asia-east1) 
Hong Kong (asia-east2) 
Tokyo (asia-northeast1) 
Osaka (asia-northeast2) 
Seoul (asia-northeast3) 
Mumbai (asia-south1) 
Delhi (asia-south2) 
Singapore (asia-southeast1) 
Jakarta (asia-southeast2) 
Sydney (australia-southeast1) 
Melbourne (australia-southeast2) 
Warsaw (europe-central2) 
Finland (europe-north1) 
Stockholm (europe-north2) 
Madrid (europe-southwest1) 
Belgium (europe-west1) 
Berlin (europe-west10) 
Turin (europe-west12) 
London (europe-west2) 
Frankfurt (europe-west3) 
Netherlands (europe-west4) 
Galaxy Frankfurt (europe-west5) 
Zurich (europe-west6) 
Milan (europe-west8) 
Paris (europe-west9) 
Doha (me-central1) 
Dammam (me-central2) 
Tel Aviv (me-west1) 
Montreal (northamerica-northeast1) 
Toronto (northamerica-northeast2) 
Mexico (northamerica-south1) 
Sao Paulo (southamerica-east1) 
Santiago (southamerica-west1) 
Iowa (us-central1) 
Oklahoma (us-central2) 
South Carolina (us-east1) 
Northern Virginia (us-east4) 
Columbus (us-east5) 
Alabama (us-east7) 
Dallas (us-south1) 
Oregon (us-west1) 
Los Angeles (us-west2) 
Salt Lake City (us-west3) 
Las Vegas (us-west4) 
Phoenix (us-west8) Show discount options Hourly Hourly Monthly Monthly 

Metric 
Price (USD) * info 
Consumption model ID: 7754-699E-0EBF BigQuery CUD - 1 Year * (USD) info 
Consumption model ID: DD83-D9A3-79AF BigQuery CUD - 3 Year * (USD) info 
Consumption model ID: 4D8D-49A7-C5B1 

Compute (per slot-hour) $0.06 / 1 hour $0.054 / 1 hour $0.048 / 1 hour * Each consumption model has a unique ID. You may need to opt-in to be eligible for consumption model discounts. Click here to learn more. 
Storage pricing 
Storage pricing is the cost to store data that you load into BigQuery. You pay for active storage and long-term storage. 
Active storage includes any table or table partition that has been modified in the last 90 days. 
Long-term storage includes any table or table partition that has not been modified for 90 consecutive days. The price of storage for that table automatically drops by approximately 50%. There is no difference in performance, durability, or availability between active and long-term storage. Iowa (us-central1) 
Johannesburg (africa-south1) 
Taiwan (asia-east1) 
Hong Kong (asia-east2) 
Tokyo (asia-northeast1) 
Osaka (asia-northeast2) 
Seoul (asia-northeast3) 
Mumbai (asia-south1) 
Delhi (asia-south2) 
Singapore (asia-southeast1) 
Jakarta (asia-southeast2) 
Bangkok (asia-southeast3) 
Kuala Lumpur (asia-southeast4) 
Sydney (australia-southeast1) 
Melbourne (australia-southeast2) 
Europe (eu) 
Warsaw (europe-central2) 
Finland (europe-north1) 
Stockholm (europe-north2) 
Madrid (europe-southwest1) 
Belgium (europe-west1) 
Berlin (europe-west10) 
Turin (europe-west12) 
London (europe-west2) 
Frankfurt (europe-west3) 
Netherlands (europe-west4) 
Zurich (europe-west6) 
Milan (europe-west8) 
Paris (europe-west9) 
Doha (me-central1) 
Dammam (me-central2) 
Tel Aviv (me-west1) 
Montreal (northamerica-northeast1) 
Toronto (northamerica-northeast2) 
Mexico (northamerica-south1) 
Sao Paulo (southamerica-east1) 
Santiago (southamerica-west1) 
US (us) 
Iowa (us-central1) 
South Carolina (us-east1) 
Northern Virginia (us-east4) 
Columbus (us-east5) 
Alabama (us-east7) 
Dallas (us-south1) 
Oregon (us-west1) 
Los Angeles (us-west2) 
Salt Lake City (us-west3) 
Las Vegas (us-west4) 
Phoenix (us-west8) Hourly Hourly Monthly Monthly 

Operation 
Price (USD) 
Details 

Active logical storage $0.000031507 / 1 gibibyte hour, per 1 month / account 
The first 10 GiB is free each month. 

Long-term logical storage $0.000021918 / 1 gibibyte hour, per 1 month / account 
The first 10 GiB is free each month. 

Active physical storage $0.000054795 / 1 gibibyte hour, per 1 month / account 
The first 10 GiB is free each month. 

Long-term physical storage $0.000027397 / 1 gibibyte hour, per 1 month / account 
The first 10 GiB is free each month. 
If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply. 
See the physical storage documentation for eligibility criteria. 

Pricing details﻿ 
Storage pricing is based on the amount of data stored in your tables . Temporary session tables and temporary multi-statement tables are charged for active storage only. There are no storage charges for temporary cached query result tables . There are no charges for time travel and failsafe storage for logical storage. Time travel and failsafe storage charges apply for physical storage . 
The size of the data is calculated based on the data types of the individual columns. For a detailed explanation of how data size is calculated, see Data size calculation . 
Storage pricing is prorated per MiB, per second. For example, if you are using active logical storage in us-central1: 
For 512 MiB for half a month, you pay $0.00575 USD 
For 100 GiB for half a month, you pay $1.15 USD 
For 1 TiB for a full month, you pay $23.552 USD 
Storage usage is calculated in gibibytes months (GiB months) , where 1 GiB is 2 30 bytes (1,024 MiB). Similarly, 1 tebibyte (TiB) is 2 40 bytes (1,024 GiB). The final usage value is the product of data size in gibibytes and storage use time in months. 
If the data in a table is not modified or deleted within 90 consecutive days, it is billed at the long-term storage rate. There is no degradation of performance, durability, availability, or any other functionality when a table is considered long-term storage. 
Each partition of a partitioned table is considered separately for long-term storage pricing. If a partition hasn't been modified in the last 90 days, the data in that partition is considered long term storage and is charged at the discounted price. 
If the table is edited, the price reverts back to the regular storage pricing, and the 90-day timer starts counting from zero. Anything that modifies the data in a table resets the timer, including: 

Action 
Details 

Loading data into a table 
Any load or query job that appends data to a destination table or overwrites a destination table. 

Copying data into a table 
Any copy job appends data to a destination table or overwrites a destination table. 

Writing query results to a table 
Any query job that appends data to a destination table or overwrites a destination table. 

Using data manipulation language (DML) 
Using a DML statement to modify table data. 

Using data definition language (DDL) 
Using a CREATE OR REPLACE TABLE statement to replace a table. 

Streaming data into the table 
Ingesting data using the Storage Write API (REST) call. 
All other actions do not reset the timer, including the following: 
Querying a table 
Creating a view that queries a table 
Exporting data from a table 
Copying a table (to another destination table) 
Patching or updating a table resource 
For tables that reach the 90-day threshold during a billing cycle, the price is prorated accordingly. 
Long-term storage pricing applies only to BigQuery storage, not to data stored in external data sources such as Bigtable, Cloud Storage, and Google Drive. 

Data size calculation 
When you load data into BigQuery or query the data, you're charged according to the data size. Data size is calculated based on the size of each column's data type . 
The size of your stored data and the size of the data processed by your queries is calculated in gibibytes (GiB) , where 1 GiB is 2 30 bytes (1,024 MiB). Similarly, 1 tebibyte (TiB) is 2 40 bytes (1,024 GiB). 
For more information, see Data type sizes . 
Data Transfer Service pricing 
You are charged for the compute resources consumed by your data transfers, which is measured in slot-hours. 
The total cost for a transfer consists of two components: 
Transfer Orchestration : The resources used to manage the connector execution. 
Data Loading & Processing : The resources used to load and merge data into the destination table. 

Transfer Orchestration﻿ 
You are charged as follows: 

Type 
Billing Model 
Connectors 

Free connectors 
Alphabet sources (excl. Google Play) 
Object storage sources 
Migration connectors 
No charge. 
Campaign Manager , Cloud Storage , Amazon S3 1 , Google Ads , Google Ad Manager , Google Merchant Center , Search Ads 360 , YouTube Channel , YouTube Content Owner , Amazon Redshift 1 , Teradata 12 , Azure Blob Storage , Display & Video 360 , Google Analytics 4 , Comparison Shopping Service (CSS) Center PREVIEW , Google Merchant Center PREVIEW , Hive Managed Tables PREVIEW and Snowflake Migration PREVIEW . 


﻿Paid connectors 
All other sources 
Consumption-based, measured in slot-hours. See details. 

Note: Connectors in “Preview” will not be charged. Billing will start once connector are GA. 
GA Connectors: 
Salesforce , ServiceNow , Salesforce Marketing Cloud (SFMC) , Facebook Ads , MySQL , PostgreSQL and Oracle . 

Preview Connectors: 
Stripe , Paypal , HubSpot , Klaviyo and SQL Server . 

$25 per unique Package Name in the Installs_country table. See details. 
Google Play 

Connectors offered by partners 
Costs apply. See details. 
For more information refer to individual connectors in the Marketplace . 
Notes on transfer pricing 
1. Costs can be incurred outside of Google Cloud by using the BigQuery Data Transfer Service, such as AWS or Azure data transfer charges. 
2. Data is not automatically deleted from your Cloud Storage bucket after it is uploaded to BigQuery. Consider deleting the data from your Cloud Storage bucket to avoid additional storage costs. See Cloud Storage pricing 

Consumption-based pricing 
You are charged for the compute resources consumed by your data transfers, which is measured in slot-hours. 
The following table shows the cost of slots. Iowa (us-central1) 
Johannesburg (africa-south1) 
Taiwan (asia-east1) 
Hong Kong (asia-east2) 
Tokyo (asia-northeast1) 
Osaka (asia-northeast2) 
Seoul (asia-northeast3) 
Mumbai (asia-south1) 
Delhi (asia-south2) 
Singapore (asia-southeast1) 
Jakarta (asia-southeast2) 
Sydney (australia-southeast1) 
Melbourne (australia-southeast2) 
Warsaw (europe-central2) 
Finland (europe-north1) 
Stockholm (europe-north2) 
Madrid (europe-southwest1) 
Belgium (europe-west1) 
Berlin (europe-west10) 
Turin (europe-west12) 
London (europe-west2) 
Frankfurt (europe-west3) 
Netherlands (europe-west4) 
Galaxy Frankfurt (europe-west5) 
Zurich (europe-west6) 
Milan (europe-west8) 
Paris (europe-west9) 
Doha (me-central1) 
Dammam (me-central2) 
Tel Aviv (me-west1) 
Montreal (northamerica-northeast1) 
Toronto (northamerica-northeast2) 
Mexico (northamerica-south1) 
Sao Paulo (southamerica-east1) 
Santiago (southamerica-west1) 
Iowa (us-central1) 
Oklahoma (us-central2) 
South Carolina (us-east1) 
Northern Virginia (us-east4) 
Columbus (us-east5) 
Alabama (us-east7) 
Dallas (us-south1) 
Oregon (us-west1) 
Los Angeles (us-west2) 
Salt Lake City (us-west3) 
Las Vegas (us-west4) 
Phoenix (us-west8) Show discount options Hourly Hourly Monthly Monthly 

Default* (USD) info 
Consumption model ID: 7754-699E-0EBF BigQuery CUD - 1 Year * (USD) info 
Consumption model ID: DD83-D9A3-79AF BigQuery CUD - 3 Year * (USD) info 
Consumption model ID: 4D8D-49A7-C5B1 
$0.06 / 1 hour $0.054 / 1 hour $0.048 / 1 hour * Each consumption model has a unique ID. You may need to opt-in to be eligible for consumption model discounts. Click here to learn more. 

Cost Estimation 
To estimate costs, you can use a conservative guideline of up to 20 slot-hours for each hour of a transfer’s run time. In the us-central1 region, this is equivalent to an estimated upper bound of $1.20 per hour of transfer run time. This is for planning purposes, and actual slot-hour consumption may differ. 

Google Play Package Name 
Every Android app has a unique application ID that looks like a Java package name, such as com.example.myapp. The Installs report contains a column of "Package Name". The number of unique package names is used for calculating usage of transfers. 
Each transfer you create generates one or more runs per day. Package names are only counted on the day a transfer run completes. For example, if a transfer run begins on July 14th but completes on July 15th, the package names are counted on July 15th. 
If a unique package name is encountered in more than one transfer run on a particular day, it is counted only once. Package names are counted separately for different transfer configurations. If a unique package name is encountered in runs for two separate transfer configurations, the package name is counted twice. 
If a package name appeared every day for an entire month, you would be charged the full $25 for that month. Otherwise, if it appeared for a part of the month, the charge would be prorated. 
Example#1: If we sync for 1 application - com.smule.singandroid, will it cost us $25 per month + storage price for BigQuery? 
The answer is $25 per month (prorated) + storage/querying costs from BigQuery. 
Example#2: If we sync all historic data (for 10 years), will we be charged for 120 months or for 1 month, because we transferred them at once? 
The answer is still $25 per month (prorated) + storage/querying costs from BigQuery, since we charge $25 per unique Package Name in the Installs_country table, regardless of how many years the historic data goes back to that unique Package Name. 

Third-party Connectors 
Costs apply for connectors provided by third-party partners. The pricing model differs for different partners and connectors. For more pricing details, refer to individual connectors when enrolling in Marketplace . 

Data Loading & Processing 
You are charged as follows: 

Destination Type 
Operation Type 
Data Loading & Processing Billing Model 
Details 

BigQuery Native Tables 
Load 
Free 
Standard load jobs into BigQuery native tables. 

Merge 
Standard BigQuery Rates 
Standard merge jobs into BigQuery native tables. 

Lakehouse for Apache Iceberg tables 
Load & Merge 
Standard Lakehouse for Apache Iceberg Rates 
Standard load and merge jobs into Lakehouse for Apache Iceberg tables. 

How to Track Costs 
To view the total cost of your transfers—aggregating both Transfer Orchestration and Data Loading & Processing—filter your billing reports by the following label: 
Key: goog-bq-feature-type 
Value: DATA_TRANSFER_SERVICE 
Note : Starting August 11, 2026, all Data Transfer Service SKUs will be unified under the label value: data_transfer_service 
BigQuery Omni pricing 
BigQuery Omni offers the following pricing models depending on your workloads and needs. 

On-Demand compute pricing 
Similar to BigQuery on-demand analysis model, BigQuery Omni queries, by default are billed using the on-demand (per TiB) pricing model, where you pay for the data scanned by your queries. 
With on-demand pricing, you will generally have access to a large pool of concurrent slots, shared among all queries in a single project. Periodically, BigQuery Omni will temporarily burst beyond this limit to accelerate smaller queries. In addition, you might have fewer slots available if there is a high amount of contention for capacity in a specific location. 
BigQuery Omni on-demand (per TiB) query pricing is as follows: Seoul (AWS) (aws-ap-northeast-2) 
Seoul (AWS) (aws-ap-northeast-2) 
Sydney (AWS) (aws-ap-southeast-2) 
Frankfurt (AWS) (aws-eu-central-1) 
Ireland (AWS) (aws-eu-west-1) 
Northern Virginia (AWS) (aws-us-east-1) 
Oregon (AWS) (aws-us-west-2) 
Virginia (Azure) (azure-us-east2) 
Washington (Azure) (azure-westus2) 

Item 
Price (USD) 

BigQuery Omni on-demand $9.125 / 1 tebibyte 
If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply. 

Pricing details 
The details and limitations are similar to BigQuery analysis pricing. Note the following regarding on-demand (per TiB) query charges: 
BigQuery uses a columnar data structure. You're charged according to the total data processed in the columns you select, and the total data per column is calculated based on the types of data in the column. For more information about how your data size is calculated, see Data size calculation. 
You aren't charged for queries that return an error or for queries that retrieve results from the cache. For procedural language jobs this consideration is provided at a per-statement level. 
Charges are rounded up to the nearest MB, with a minimum 10 MB data processed per table referenced by the query, and with a minimum 10 MB data processed per query. 
Canceling a running query job might incur charges up to the full cost for the query if you let the query run to completion. 
When you run a query, you're charged according to the data processed in the columns you select, even if you set an explicit LIMIT on the results. 
Partitioning and clustering your tables can help reduce the amount of data processed by queries. As a best practice, use partitioning and clustering whenever possible. 
On-demand (per TiB) pricing is referred to as analysis pricing on the Google Cloud SKUs page. 
When you run a query against a clustered table, and the query includes a filter on the clustered columns, BigQuery uses the filter expression to prune the blocks scanned by the query. This can reduce the number of scanned bytes. 
BigQuery provides cost control mechanisms that enable you to cap your query costs. You can set: 
User-level and project-level custom cost controls. 
The maximum bytes billed by a query 

BigQuery Omni with editions 
BigQuery Omni regions support BigQuery editions . At present only Enterprise Edition is supported in Omni regions 
The following table shows the cost of slots in Omni regions Seoul (AWS) (aws-ap-northeast-2) 
Seoul (AWS) (aws-ap-northeast-2) 
Sydney (AWS) (aws-ap-southeast-2) 
Frankfurt (AWS) (aws-eu-central-1) 
Ireland (AWS) (aws-eu-west-1) 
Northern Virginia (AWS) (aws-us-east-1) 
Oregon (AWS) (aws-us-west-2) 
Virginia (Azure) (azure-us-east2) 
Washington (Azure) (azure-westus2) Show discount options Hourly Hourly Monthly Monthly 

Number of slots 
PAYG (No commitment) (USD) 
Resource CUDs - 1 Year (USD) 
Resource CUDs - 3 Year (USD) 

100 $7.50 / 1 hour $6.00 / 1 hour $4.50 / 1 hour 

Omni Cross Cloud Data Transfer 
When using Omni’s Cross Cloud capabilities (Cross Cloud Transfer, Create Table as Select, Insert Into Select, Cross Cloud Joins, and Cross Cloud Materialized Views) that involve data moving from AWS or Azure to Google Cloud, there will be additional charges for data transfer. 
Specifically for Cross-Cloud Materialized Views, Create Table as Select, Insert Into Select, and Cross Cloud Joins there are no charges during Preview. Starting 29 February 2024, these services will be generally available and you will be charged for data transfer. You will be charged for data transfer only when using any of the above listed services from an AWS or Azure region to a Google Cloud BigQuery region. You will be charged on a per GiB rate based on the amount of data transferred from AWS or Azure to Google Cloud. 

SKU 
Billing model 
Price (USD) 

Cross-cloud data transfer from AWS North Virginia (aws-us-east-1) to Google Cloud North America 
usage-based $0.09 / 1 gibibyte 

Cross-cloud data transfer from Azure North Virginia (azure-eastus2) to Google Cloud North America 
usage-based $0.0875 / 1 gibibyte 

Cross-cloud data transfer from AWS Seoul (aws-ap-northeast-2) to Google Cloud Asia 
usage-based $0.126 / 1 gibibyte 

Cross-cloud data transfer from AWS Oregon (aws-us-west-2) to Google Cloud North America 
usage-based $0.09 / 1 gibibyte 

Cross-cloud data transfer from AWS Ireland (aws-eu-west-1) to Google Cloud Europe 
usage-based $0.09 / 1 gibibyte 

Cross-cloud data transfer from AWS Sydney (aws-ap-southeast-2) to Google Cloud Oceania 
usage-based $0.114 / 1 gibibyte 

Cross-cloud data transfer from AWS Frankfurt (aws-eu-central-1) to Google Cloud Europe 
usage-based $0.09 / 1 gibibyte 

Omni Managed Storage 
When using Omni’s Cross Cloud Materialized Views capability, you will also be charged for creation of local materialized views which is on BigQuery Managed Storage on AWS. You will be charged a per GiB for the amount of physical storage that is used for the local materialized view. Seoul (AWS) (aws-ap-northeast-2) 
Seoul (AWS) (aws-ap-northeast-2) 
Sydney (AWS) (aws-ap-southeast-2) 
Frankfurt (AWS) (aws-eu-central-1) 
Ireland (AWS) (aws-eu-west-1) 
Northern Virginia (AWS) (aws-us-east-1) 
Oregon (AWS) (aws-us-west-2) Hourly Hourly Monthly Monthly 

Operation 
Price (USD) 

Active physical storage $0.000071233 / 1 gibibyte hour 

Long-term physical storage $0.000035616 / 1 gibibyte hour 
Data ingestion pricing 
BigQuery offers two modes of data ingestion: 
Batch loading . Load source files into one or more BigQuery tables in a single batch operation. 
Streaming . Stream data one record at a time or in small batches using the BigQuery Storage Write API (gRPC) or Storage Write API (REST) . 
For more information about which mode to choose, see Introduction to loading data . Iowa (us-central1) 
Johannesburg (africa-south1) 
Taiwan (asia-east1) 
Hong Kong (asia-east2) 
Tokyo (asia-northeast1) 
Osaka (asia-northeast2) 
Seoul (asia-northeast3) 
Mumbai (asia-south1) 
Delhi (asia-south2) 
Singapore (asia-southeast1) 
Jakarta (asia-southeast2) 
Bangkok (asia-southeast3) 
Kuala Lumpur (asia-southeast4) 
Sydney (australia-southeast1) 
Melbourne (australia-southeast2) 
Warsaw (europe-central2) 
Finland (europe-north1) 
Stockholm (europe-north2) 
Madrid (europe-southwest1) 
Belgium (europe-west1) 
Berlin (europe-west10) 
Turin (europe-west12) 
London (europe-west2) 
Frankfurt (europe-west3) 
Netherlands (europe-west4) 
Zurich (europe-west6) 
Milan (europe-west8) 
Paris (europe-west9) 
Doha (me-central1) 
Dammam (me-central2) 
Tel Aviv (me-west1) 
Montreal (northamerica-northeast1) 
Toronto (northamerica-northeast2) 
Mexico (northamerica-south1) 
Sao Paulo (southamerica-east1) 
Santiago (southamerica-west1) 
Iowa (us-central1) 
South Carolina (us-east1) 
Northern Virginia (us-east4) 
Columbus (us-east5) 
Alabama (us-east7) 
Dallas (us-south1) 
Oregon (us-west1) 
Los Angeles (us-west2) 
Salt Lake City (us-west3) 
Las Vegas (us-west4) 
Phoenix (us-west8) 

Operation 
Pricing 
Details 

Batch Loading 
Free using the shared slot pool named default-pipeline. 
Customers can choose editions pricing for guaranteed capacity. Once the data is loaded into BigQuery, you are charged for storage. 

Streaming inserts (Storage Write API (REST)) $0.01 / 200 mebibyte 
You are charged for rows that are successfully inserted. Individual rows are calculated using a 1 KB minimum size. 

BigQuery Storage Write API (gRPC) $0.025 / 1 gibibyte, per 1 month / account 
The first 2 TiB per month are free. 
If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply. 

Pricing details 
By default, you are not charged for batch loading data from Cloud Storage or from local files into BigQuery. Cross-region load jobs are billed for network usage under Network Data Transfer SKUs . 
Load jobs by default use a shared pool of slots. BigQuery does not make guarantees about the available capacity of this shared pool or the throughput you will see. Alternatively, you can purchase dedicated slots to run load jobs. You are charged capacity-based pricing for dedicated slots. When load jobs are assigned to a reservation, they lose access to the free pool. For more information, see Assignments . 
Once your data is loaded into BigQuery, it is subject to BigQuery storage pricing . If you load data from Cloud Storage, you are charged for storing the data in Cloud Storage. For details, see Data storage on the Cloud Storage pricing page. 
Data extraction pricing 
BigQuery offers the following modes of data extraction: 
Batch export . Use an an extract job to export table data to Cloud Storage . There is no processing charge for exporting data from a BigQuery table using an extract job. Cross-region extract jobs are billed under General Data Transfer Networking Traffic for Google Cloud Cross Region SKUs . 
Export query results . Use the EXPORT DATA statement to export query results to Cloud Storage , Bigtable , or Spanner . You are billed for the compute cost to process the query statement. 
Streaming reads . Use the Storage Read API to perform high-throughput reads of table data. You are billed for the amount of data read. 
Note: You are not charged for data extraction or data transfer when accessing query results in the Google Cloud console, BigQuery API, or any other clients, such as Looker. Iowa (us-central1) 
Johannesburg (africa-south1) 
Taiwan (asia-east1) 
Hong Kong (asia-east2) 
Tokyo (asia-northeast1) 
Osaka (asia-northeast2) 
Seoul (asia-northeast3) 
Mumbai (asia-south1) 
Delhi (asia-south2) 
Singapore (asia-southeast1) 
Jakarta (asia-southeast2) 
Bangkok (asia-southeast3) 
Kuala Lumpur (asia-southeast4) 
Sydney (australia-southeast1) 
Melbourne (australia-southeast2) 
Europe (eu) 
Warsaw (europe-central2) 
Finland (europe-north1) 
Stockholm (europe-north2) 
Madrid (europe-southwest1) 
Belgium (europe-west1) 
Berlin (europe-west10) 
Turin (europe-west12) 
London (europe-west2) 
Frankfurt (europe-west3) 
Netherlands (europe-west4) 
Zurich (europe-west6) 
Milan (europe-west8) 
Paris (europe-west9) 
Doha (me-central1) 
Dammam (me-central2) 
Tel Aviv (me-west1) 
Montreal (northamerica-northeast1) 
Toronto (northamerica-northeast2) 
Mexico (northamerica-south1) 
Sao Paulo (southamerica-east1) 
Santiago (southamerica-west1) 
US (us) 
Iowa (us-central1) 
South Carolina (us-east1) 
Northern Virginia (us-east4) 
Columbus (us-east5) 
Alabama (us-east7) 
Dallas (us-south1) 
Oregon (us-west1) 
Los Angeles (us-west2) 
Salt Lake City (us-west3) 
Las Vegas (us-west4) 
Phoenix (us-west8) 

Operation 
Pricing 
Details 

Batch exports 
Free using the shared slot pool. 
You can export up to 50 tebibytes per day for free using the shared slot pool. You are charged for the data stored in Cloud Storage. 

Streaming reads (BigQuery Storage Read API) $1.10 / 1 tebibyte, per 1 month / account 
Customers can read up to 300 TiB of data per month at no charge. 
If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply. 

Batch export data transfer pricing 
You are charged for data transfer when you export data in batch from BigQuery to a Cloud Storage bucket or Spanner table in another region, as follows: 

Case 
Example 
Rate 

Export within the same location 
From us-east1 to us-east1 
Free 

Export from BigQuery US multi-region 
From US multi-region to us-central1 (Iowa) 
Free 

Export from BigQuery US multi-region 
From US multi-region to any region (except us-central1 (Iowa)) 
See following table 

Export from BigQuery EU multi-region 
From EU multi-region to europe-west4 (Netherlands) 
Free 

Export from BigQuery EU multi-region 
From EU multi-region to any region (except europe-west4 (Netherlands)) 
See following table 

Export across locations 
From us-east1 to us-central1 
See following table 
Note: All prices are in $/GiB and all GiB are in physical bytes. 

North America 
Europe 
Asia 
Indonesia 
Oceania 
Middle East 
Latin America 
Africa 

North America $0.02 $0.05 $0.08 $0.10 $0.10 $0.11 $0.14 $0.11 

Europe $0.05 $0.02 $0.08 $0.10 $0.10 $0.11 $0.14 $0.11 

Asia $0.08 $0.08 $0.08 $0.10 $0.10 $0.11 $0.14 $0.11 

Indonesia $0.10 $0.10 $0.10 $0.08 $0.08 $0.11 $0.14 $0.14 

Oceania $0.10 $0.10 $0.10 $0.08 $0.08 $0.11 $0.14 $0.14 

Middle East $0.11 $0.11 $0.11 $0.11 $0.11 $0.08 $0.14 $0.11 

Latin America $0.14 $0.14 $0.14 $0.14 $0.14 $0.14 $0.20 $0.14 

Africa $0.11 $0.11 $0.11 $0.14 $0.14 $0.11 $0.14 $0.11 

Storage Read API data transfer within Google Cloud 

Case 
Examples 
Rate 

Accessing cached query results from temporary tables 
Temporary tables "anonymous dataset" 
Free 

Data reads within the same location 
From us-east1 to us-east1 
Free 

Data read from a BigQuery multi-region to a different BigQuery location, and both locations are on the same continent. 
From us to us-east1 
From eu to europe-west1 
Free 

Data read between different locations on the same continent (assuming none of the above free cases apply) 
From us-east1 to northamerica-northeast1 
From europe-west1 to europe-north1 $0.01 / 1 gibibyte 

Data moves between different continents within Google cloud and neither is Australia. 
From us to asia 
From europe-west1 to southamerica-east1 $0.08 / 1 gibibyte 

Data moves between different continents within Google cloud and one is Australia. 
From us to australia-southeast1 
From australia-southeast1 to europe-west1 $0.15 / 1 gibibyte 
If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply. 

Storage Read API general network usage 

Price (USD) 

Data Transfer to Worldwide Destinations (excluding Asia & Australia) 0 tebibyte to 1 tebibyte $0.12 / 1 gibibyte, per 1 month / account 1 tebibyte to 10 tebibyte $0.11 / 1 gibibyte, per 1 month / account 10 tebibyte and above $0.08 / 1 gibibyte, per 1 month / account 

Data Transfer to Asia Destinations (excluding China, but including Hong Kong) 0 tebibyte to 1 tebibyte $0.12 / 1 gibibyte, per 1 month / account 1 tebibyte to 10 tebibyte $0.11 / 1 gibibyte, per 1 month / account 10 tebibyte and above $0.08 / 1 gibibyte, per 1 month / account 

Data Transfer to China Destinations (excluding Hong Kong) 0 tebibyte to 1 tebibyte $0.19 / 1 gibibyte, per 1 month / account 1 tebibyte to 10 tebibyte $0.18 / 1 gibibyte, per 1 month / account 10 tebibyte and above $0.15 / 1 gibibyte, per 1 month / account 

Data Transfer to Australia Destinations 0 tebibyte to 1 tebibyte $0.19 / 1 gibibyte, per 1 month / account 1 tebibyte to 10 tebibyte $0.18 / 1 gibibyte, per 1 month / account 10 tebibyte and above $0.15 / 1 gibibyte, per 1 month / account 

Data transfer in 
Free 
If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply. 

Storage Read API pricing details 
The Storage Read API has an on-demand price model. With on-demand pricing, BigQuery charges for the number of bytes processed (also referred to as bytes read). On-demand pricing is solely based on usage, with a bytes read free tier of 300 TiB per month for each billing account. Bytes scanned as part of reads from temporary tables are free and do not count against the 300TiB free tier. This free bytes read 300 TiB is on the bytes-read component, and does not apply to associated outbound data transfer. 
Note the following regarding Storage Read API charges: 
You are charged according to the total amount of data read. The total data read per column is calculated based on the type of data in the column, and the size of the data is calculated based on the column's data type. For a detailed explanation of how data size is calculated, see Data size calculation . 
You are charged for any data read in a read session even if a ReadRows call fails. 
If you cancel a ReadRows call before the end of the stream is reached, you are charged for any data read before the cancellation. Your charges can include data that was read but not returned to you before the cancellation of the ReadRows call. 
As a best practice, use partitioned and clustered tables whenever possible. You can reduce the amount of data read by using a WHERE clause to prune partitions. For more information, see Querying partitioned tables . 
When using Interconnect, Cloud Interconnect pricing applies instead of BigQuery Storage Read API General Network Usage prices. 
Data replication pricing 
Besides copy operations within the same region, BigQuery offers two modes of replicating (copying) data between regions. You can perform a one-time copy operation, or use incremental, ongoing replication. Your options for copying data across regions include the following: 
Cross-region copy . One time or scheduled copy of table data to between regions or multi-regions, see copy datasets or copy tables . Cross-region copy is billed under General Data Transfer Networking Traffic for Google Cloud Cross Region SKUs . 
Cross-region replication . Ongoing, incremental replication of a dataset between two or more different regions or multi-regions, see cross-region dataset replication . 
Cross-region Turbo replication . High performance, ongoing, incremental replication of a dataset between two or more different regions or multi-regions. Available only with managed disaster recovery . 
Both cross-region replication and cross-region Turbo replication are billed under the BigQuery Network Egress Replication SKUs . 

Storage for replicated data 
Replicated data stored in the destination region or multi-region is charged according to BigQuery storage pricing . 

Data transfer pricing for replicated data 
You are charged for data transfer for the volume of data replicated. The use cases and breakdown of data transfer charges are provided as follows: 

Case 
Example 
Rate 

Replicate within the same location 
From us-east1 to us-east1, From US multi-region to US multi-region, From EU multi-region to EU multi-region 
Free 

Replicate from BigQuery US multi-region to us-central1 or vice-versa 
US multi-region to us-central1 (Iowa), us-central1 (Iowa) to US multi-region 
Free 

Replicate from BigQuery US multi-region to any other region not in US multi-region 
From US multi-region to any region (except us-central1 (Iowa)) 
See following table 

Replicate from BigQuery EU multi-region or vice-versa 
From EU multi-region to europe-west4 (Netherlands), europe-west4 (Netherlands) to EU multi-region 
Free 

Replicate from BigQuery EU multi-region to any other region not in EU multi-region 
From EU multi-region to any region (except europe-west4 (Netherlands)) 
See following table 

Replicate across locations 
From us-east1 to us-central1 
See following table 
Note: All prices are in $/GiB and all GiB are in physical bytes. 

North America 
Europe 
Asia 
Indonesia 
Oceania 
Middle East 
Latin America 
Africa 

North America $0.02 $0.05 $0.08 $0.10 $0.10 $0.11 $0.14 $0.11 

Europe $0.05 $0.02 $0.08 $0.10 $0.10 $0.11 $0.14 $0.11 

Asia $0.08 $0.08 $0.08 $0.10 $0.10 $0.11 $0.14 $0.11 

Indonesia $0.10 $0.10 $0.10 $0.08 $0.08 $0.11 $0.14 $0.14 

Oceania ﻿ $0.10 $0.10 $0.10 $0.08 $0.08 $0.11 $0.14 $0.14 

Middle East $0.11 $0.11 $0.11 $0.11 $0.11 $0.08 $0.14 $0.11 

Latin America $0.14 $0.14 $0.14 $0.14 $0.14 $0.14 $0.20 $0.14 

Africa $0.11 $0.11 $0.11 $0.14 $0.14 $0.11 $0.14 $0.11 
Notebook runtime pricing 
BigQuery Studio Notebooks rely on a default notebook runtime that uses a Colab Enterprise runtime to enable notebook code execution. The default Colab Enterprise runtime consumes compute and disk (both SSD and PD) resources. 
Billing for these resources is metered as pay-as-you go slots as outlined below. These slots are billed under the BigQuery Standard Edition SKU . 
Notebooks that use a non-default runtime are billed under Gemini platform SKUs. 
The default notebook runtime is a Google-provisioned virtual machine (VM) that can run the code in your notebook (IPYNB file). This allows BigQuery customers to execute python script and is not charged after idle time. Iowa (us-central1) 
Johannesburg (africa-south1) 
Taiwan (asia-east1) 
Hong Kong (asia-east2) 
Tokyo (asia-northeast1) 
Seoul (asia-northeast3) 
Mumbai (asia-south1) 
Singapore (asia-southeast1) 
Jakarta (asia-southeast2) 
Sydney (australia-southeast1) 
Warsaw (europe-central2) 
Finland (europe-north1) 
Madrid (europe-southwest1) 
Belgium (europe-west1) 
Turin (europe-west12) 
London (europe-west2) 
Frankfurt (europe-west3) 
Netherlands (europe-west4) 
Zurich (europe-west6) 
Milan (europe-west8) 
Doha (me-central1) 
Dammam (me-central2) 
Tel Aviv (me-west1) 
Montreal (northamerica-northeast1) 
Sao Paulo (southamerica-east1) 
Iowa (us-central1) 
South Carolina (us-east1) 
Northern Virginia (us-east4) 
Columbus (us-east5) 
Dallas (us-south1) 
Oregon (us-west1) 
Los Angeles (us-west2) 
Las Vegas (us-west4) Show discount options Hourly Hourly Monthly Monthly 

Resource 
Pricing (USD) 

Default notebook runtime compute $0.160827408 / 1 hour $0.14474466 / 1 hour $0.128661928 / 1 hour 
*The Pay as you go slots, will be metered in the edition that is being used at the project level. 
The default notebook allocates PD and SSD in the background to help users install new data science packages and maintain their work beyond the Python code they execute. Once the PD and SSD is released, you will not see charges. Iowa (us-central1) 
Johannesburg (africa-south1) 
Taiwan (asia-east1) 
Hong Kong (asia-east2) 
Tokyo (asia-northeast1) 
Seoul (asia-northeast3) 
Mumbai (asia-south1) 
Singapore (asia-southeast1) 
Jakarta (asia-southeast2) 
Sydney (australia-southeast1) 
Warsaw (europe-central2) 
Finland (europe-north1) 
Stockholm (europe-north2) 
Madrid (europe-southwest1) 
Belgium (europe-west1) 
Turin (europe-west12) 
London (europe-west2) 
Frankfurt (europe-west3) 
Netherlands (europe-west4) 
Zurich (europe-west6) 
Milan (europe-west8) 
Doha (me-central1) 
Dammam (me-central2) 
Tel Aviv (me-west1) 
Montreal (northamerica-northeast1) 
Sao Paulo (southamerica-east1) 
Iowa (us-central1) 
South Carolina (us-east1) 
Northern Virginia (us-east4) 
Columbus (us-east5) 
Dallas (us-south1) 
Oregon (us-west1) 
Los Angeles (us-west2) 
Las Vegas (us-west4) Hourly Hourly Monthly Monthly 

Resource 
Pricing (USD) 

Default notebook SSD $0.000279452 / 1 gibibyte hour 

Default notebook PD $0.000065753 / 1 gibibyte hour 
BigQuery Studio notebook pricing details: 
Default runtime configuration may change to improve usability. Details can be found here . 
Colab Enterprise runtimes shut down after 180 minutes of inactivity by default. This page describes the idle shutdown feature and how to change the default idle shutdown settings or turn the feature off when you create a runtime template. 
BigQuery ML pricing 
BigQuery ML models can be classified into two different categories: built-in models and external models. BigQuery ML built-in models are trained within BigQuery, such as linear regression, logistic regression, k-means, matrix factorization, PCA, and ARIMA models. The pre trained TimesFM model is also considered a built-in model. BigQuery ML external models are trained utilizing other Google Cloud services, DNN, boosted tree and random forest (which are trained on Gemini platform ) and AutoML models (which are trained on the Gemini platform tables backend ). BigQuery ML model training pricing is based on the model type and your usage pattern, as well as your pricing model: editions or on-demand. BigQuery ML prediction and evaluation functions are executed within BigQuery ML for all model types, priced as explained below. 

BigQuery ML editions pricing 
BigQuery ML is available in Enterprise and Enterprise Plus Editions for customers who prefer a compute capacity (number of slots) based pricing model over the on-demand (number of bytes processed) model. Customers can use Enterprise or Enterprise Plus reservations to use all features of BigQuery ML. BigQuery ML usage will be included in the BigQuery Editions usage. 

Reservations to create built-in models 
BigQuery has three job types for reservation assignment: QUERY, PIPELINE, and ML_EXTERNAL. QUERY assignments, which are used for analytical queries, are also used to run CREATE MODEL queries for BigQuery ML built-in models. Built-in model training and analytical queries share the same pool of resources in their assigned reservations, and have the same behavior regarding being preemptible, and using idle slots from other reservations. 

Reservations to create external models 
Because external models are trained outside of BigQuery, these workloads are not preemptible. As a result, to ensure other workloads are not impacted, only reservations with ML_EXTERNAL job type assignment can be used for these external jobs. Reservations workload management describes how to create reservations for external model training jobs. The slots usage per job is calculated to maintain the price parity between BigQuery slots and external Google Cloud service costs. 
Note: You can add a ML_EXTERNAL job type assignment to reservations that you want to use for building BigQuery ML external models. When slots in the reservation are shared by both QUERY / PIPELINE and ML_EXTERNAL jobs, QUERY / PIPELINE jobs can use the slots only when they are available. Thus, it is important to ensure all critical QUERY and PIPELINE jobs run in their own reservations, as ML_EXTERNAL jobs are not preemptible. ML_EXTERNAL jobs cannot use idle slots from other reservations. On the other hand, if slots in this reservation (with ML_EXTERNAL assignment) are available, jobs from other reservations (with ignore_idle_slots=false) can use them. 
Note: To create an AutoML Tables model, you need approximately 1000 ML_EXTERNAL slots. The number of slots is subject to change based on Gemini platform tables backend pricing. Meanwhile, the number of external slots used to train other BigQuery ML external models (such as DNN, Boosted Tree, Random Forest etc.) is dynamically determined in order to scale the training job horizontally. More specifically, the Gemini platform training scale tier (Virtual Machine configurations for chief worker, parameter servers and workers) is determined at runtime based on the training data size and model type. The BigQuery ML service then reserves a number of slots equivalent to the total VM price from your ML_EXTERNAL reservations. 

BigQuery ML on-demand pricing﻿ 
BigQuery ML pricing for on-demand queries depends on the type of operation: model type, model creation, model evaluation, model inspection, or model prediction. For the models that support it, hyperparameter tuning is billed at the same rate as model creation. The cost of the model training associated with hyperparameter tuning is the sum of the cost of all executed trials. 
Note: Matrix factorization models are only available to editions customers or customers with reservations . 
BigQuery ML on-demand pricing is as follows: Iowa (us-central1) 
Johannesburg (africa-south1) 
Taiwan (asia-east1) 
Hong Kong (asia-east2) 
Tokyo (asia-northeast1) 
Osaka (asia-northeast2) 
Seoul (asia-northeast3) 
Mumbai (asia-south1) 
Delhi (asia-south2) 
Singapore (asia-southeast1) 
Jakarta (asia-southeast2) 
Bangkok (asia-southeast3) 
Kuala Lumpur (asia-southeast4) 
Sydney (australia-southeast1) 
Melbourne (australia-southeast2) 
Europe (eu) 
Warsaw (europe-central2) 
Finland (europe-north1) 
Stockholm (europe-north2) 
Madrid (europe-southwest1) 
Belgium (europe-west1) 
Berlin (europe-west10) 
Turin (europe-west12) 
London (europe-west2) 
Frankfurt (europe-west3) 
Netherlands (europe-west4) 
Zurich (europe-west6) 
Milan (europe-west8) 
Paris (europe-west9) 
Doha (me-central1) 
Dammam (me-central2) 
Tel Aviv (me-west1) 
Montreal (northamerica-northeast1) 
Toronto (northamerica-northeast2) 
Mexico (northamerica-south1) 
Sao Paulo (southamerica-east1) 
Santiago (southamerica-west1) 
US (us) 
Iowa (us-central1) 
South Carolina (us-east1) 
Northern Virginia (us-east4) 
Columbus (us-east5) 
Alabama (us-east7) 
Dallas (us-south1) 
Oregon (us-west1) 
Los Angeles (us-west2) 
Salt Lake City (us-west3) 
Las Vegas (us-west4) 
Phoenix (us-west8) 

Operation 
Pricing 
Details 

Logistic regression model creation 1 
Linear regression model creation 1 
K-means clustering model creation 1 
PCA model creation 
Time series model creation 1,2 
﻿ Contribution analysis model creation $312.50 / 1 tebibyte, per 1 month / account 
An additional label is added to the billing record to distinguish between BigQuery ML model creation and regular BigQuery costs. 
The key is bigquery.googleapis.com/bqml, and the value can be one of the following: 
bqml_linear_reg_training 
bqml_logistic_reg_training 
bqml_kmeans_training 
bqml_pca_training 
bqml_matrix_factorization_training 
bqml_arima_plus_training 
bqml_arima_plus_xreg_training 
bqml_contribution_analysis_training 

AutoML Tables model creation 1 
DNN model creation 1 
Wide-and-Deep model creation 1 
Boosted tree model creation 
Random forest model creation 
Autoencoder model creation 1 $6.25 / 1 tebibyte, per 1 month / account 
The total cost of a job is the sum of the following two costs: 
BigQuery data processing cost (for preprocessing) 
Passthrough Gemini platform cost (for training) 
The cost is converted to BigQuery ML bytes processed, and two billing records with different labels are reported for the job: 
For BigQuery cost, the key is bigquery.googleapis.com/bqml and the value is bqml_analytic. For external Gemini platform service costs, the key is bigquery.googleapis.com/bqml, and the value can be one of the following: 1) CAIP; 2) AUTOML_TABLES. 

Matrix factorization model creation 
Not supported 
Matrix factorization is only available to editions customers or customers with reservations (Enterprise or Enterprise+). 

Evaluation, inspection, and prediction (all model types except remote model 3 ) $6.25 / 1 tebibyte, per 1 month / account 
Charges from evaluation, inspection, and prediction queries are included in the 1 TiB of data per month under the BigQuery analysis free tier. 
If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply. 
1 The CREATE MODEL statement stops at 50 iterations for iterative models. This applies to both on-demand and editions pricing. 
2 For time series models, when auto-arima is enabled for automatic hyper-parameter tuning, multiple candidate models are fitted and evaluated during the training phase. In this case, the number of bytes processed by the input SELECT statement is multiplied by the number of candidate models, which can be controlled by the AUTO_ARIMA_MAX_ORDER training option for ARIMA_PLUS or the AUTO_ARIMA_MAX_ORDER training option for ARIMA_PLUS_XREG . This applies to both on-demand and editions pricing. The following notes apply to time series model creation: 
For single time series forecasting with auto-arima enabled, when AUTO_ARIMA_MAX_ORDER is (1, 2, 3, 4, 5), the number of candidate models is (6, 12, 20, 30, 42) respectively if non-seasonal d equals one; otherwise, the number of candidate models is (3, 6, 10, 15, 21). 
For multiple time series forecasting using TIME_SERIES_ID_COL , the charge is for (6, 12, 20, 30, 42) candidate models when AUTO_ARIMA_MAX_ORDER is (1, 2, 3, 4, 5) respectively. 
Note that this model selection only applies to model creation. For model evaluation, inspection, and prediction, only the selected model is used, with regular query pricing. 
3 See BigQuery ML Remote Model Inference for details. 

TabFM on BigQuery 
TabFM on BigQuery will be moving to a token based pricing from 10/30/2026 onwards, whereby you will be charged for TabFM tokens consumed in your query and for BigQuery slot used/bytes processed for non model inference parts of the query. 
TabFM on BigQuery token computation and pricing is as follows: 
Input tokens = (train rows * columns + predict rows * (columns - 1)) * n_ensembles 
Output tokens = prediction rows * n_ensembles 
Where: 
train_row is the number of input training rows 
prediction_row is the number of rows to predict label 
columns is the number of feature columns and target label column referenced 
n_ensemble is the number of differently shuffled versions of data the model predicts on and averages to get a more accurate prediction 

Item 
Price (USD) 

Input tokens 
$0.05 / mtok 

Output tokens 
$0.20 / mtok 

TimesFM 3.0 on BigQuery 
TimesFM 3.0 on BigQuery will be moving to a token-based pricing from [Target Enforcement Date, 12/01/2026] onwards, whereby you will be charged for TimesFM 3.0 tokens consumed in your query and for BigQuery slots used/bytes processed for non-model inference parts of the query. (During Preview prior to token billing enforcement, usage is billed in standard BigQuery slots for Enterprise/Enterprise Plus editions or bytes processed for on-demand mode.) 
TimesFM 3.0 on BigQuery token computation and pricing is as follows (each data point equals 1 token): 
Input tokens = S * (L * (N_target + N_past_cov) + (L + H) * N_fut_cov) 
Output tokens = S * H * (N_target + N_past_cov) 
Where: 
S is the number of time series (entities / batches) 
L is the history context length (number of past time steps) 
H is the forecast horizon length (number of future time steps) 
N_target is the number of target columns 
N_past_cov is the number of past-only covariate columns 
N_fut_cov is the number of past and future covariate columns 

Item 
Price (USD) 

Input tokens 
$0.05 / mtok 

Output tokens 
$0.20 / mtok 

BigQuery ML remote model training, inference, and tuning 
BigQuery ML lets customers create a remote model that targets a Gemini platform foundation model , a Gemini platform online prediction endpoint, or a Cloud AI API, for example Cloud AI Vision API. 
The pricing for BigQuery ML remote model inference has the following parts: 
The bytes processed by BigQuery are billed according to standard pricing such as on-demand or editions pricing. 
In addition, costs are incurred for the remote endpoint as follows: 

Remote Model types 
Inference functions 
Pricing 

Google models hosted on Gemini platform 
ML.GENERATE_TEXT 
ML.GENERATE_EMBEDDING 
Generative AI in Gemini platform batch pricing . 

Anthropic's Claude models on Google Cloud 
ML.GENERATE_TEXT 
Generative AI in Gemini platform pricing 

Open models deployed to Gemini platform 
ML.GENERATE_TEXT 
Gemini platform pricing 

Gemini platform endpoints 
ML.PREDICT 
Gemini platform pricing 

Cloud Natural Language API 
ML.UNDERSTAND_TEXT 
Cloud Natural Language API pricing 

Cloud Translation API 
ML.TRANSLATE ﻿ 
Cloud Translation API pricing 

Cloud Vision API 
ML.ANNOTATE_IMAGE 
Cloud Vision API pricing 

Document AI API 
ML.PROCESS_DOCUMENT 
Document AI API pricing 

Speech-to-Text API 
ML.TRANSCRIBE 
Speech-to-Text API pricing 
For remote endpoint model pricing, you are billed directly by the above services. You may use the billing label billing_service = 'bigquery_ml' and the billing label bigquery_job_id_prefix to filter the exact charges. 

LLM supervised tuning costs﻿ 
When using supervised tuning with remote models over Gemini platform LLMs, costs are calculated based on the following: 
The bytes processed from the training data table specified in the AS SELECT clause . These charges are billed from BigQuery to your project. 
The GPU or TPU usage to tune the LLM. These charges are billed from Gemini platform to your project. For more information, see Gemini platform pricing . 

BigQuery ML dry run﻿ 
Due to the nature of the underlying algorithms of some model types and differences in billing, the bytes processed will not be calculated for some model types until after training is completed due to the complexity of calculating the initial estimate. 

BigQuery ML pricing example﻿ 
BigQuery ML charges are not itemized separately on your billing statement. For current models, if you have BigQuery Editions, BigQuery ML charges are included. 
If you are using on-demand pricing, BigQuery ML charges are included in the BigQuery analysis (query) charges. 
BigQuery ML jobs that perform inspection, evaluation, and prediction operations incur the same charges as on-demand query jobs. Because CREATE MODEL queries incur different charges, you must calculate CREATE MODEL job costs independently by using the Cloud logging audit logs. Using the audit logs, you can determine the bytes billed by the BigQuery ML service for each BigQuery ML CREATE MODEL job. Then, multiply the bytes billed by the appropriate cost for CREATE MODEL queries in your regional or multi-regional location. 
For example, to determine the cost of a query job in the US that includes a BigQuery ML CREATE MODEL statement: 
Open the Cloud Logging page in the Google Cloud console. 
Verify that the product is set to BigQuery. 
Click the drop-down arrow in the "Filter by label or text search" box and choose Convert to advanced filter . This adds the following text to the filter: 
Loading... resource.type = "bigquery_resource" content_copy 
Add the following text on line two below the resource.type line: 
Loading... protoPayload.serviceData.jobCompletedEvent.job.jobConfiguration.query.statementType="CREATE_MODEL" content_copy 
To the right of the Submit Filter button, choose the appropriate time frame from the drop-down list. For example, choosing Last 24 hours would display BigQuery ML CREATE MODEL jobs completed in the past 24 hours. 
Click Submit Filter to display the jobs completed in the given time window. 
After the data is populated, click View Options and choose Modify custom fields . 
In the Add custom fields dialog, enter: 
Loading... protoPayload.serviceData.jobCompletedEvent.job.jobStatistics.totalBilledBytes content_copy 
Click Save to update the results. 
To calculate the charges for the BigQuery ML CREATE MODEL job, multiply the bytes billed by the BigQuery ML on-demand price . In this example, the CREATE MODEL job processed 100873011200 bytes. To calculate the cost of this job in the US multi-regional location, divide the billed bytes by the number of bytes per TiB, and multiply it by the model creation cost: 
100873011200 / 1099511627776 x $312.5 = $28.669 
Note: Currently, Cloud logging metrics are not available for BigQuery ML. When available, Cloud logging metrics will allow you to view BigQuery ML bytes billed in graphs with custom aggregations. 
BI Engine pricing 
BI Engine accelerates SQL queries by caching BigQuery data in memory. The amount of data stored is constrained by the amount of capacity you purchase. To purchase BI Engine capacity, create a BI Engine reservation in the project where queries will be run. 
When BI Engine accelerates a query, the query stage that reads table data is free. Subsequent stages depend on the type of BigQuery pricing you're using: 
For on-demand pricing , stages that use BI Engine are charged for 0 scanned bytes. Subsequent stages will not incur additional on-demand charges. 
For editions pricing , the first stage consumes no BigQuery reservation slots. Subsequent stages use slots from the BigQuery reservation. 
BI Engine pricing is as follows: Iowa (us-central1) 
Johannesburg (africa-south1) 
Taiwan (asia-east1) 
Hong Kong (asia-east2) 
Tokyo (asia-northeast1) 
Osaka (asia-northeast2) 
Seoul (asia-northeast3) 
Mumbai (asia-south1) 
Delhi (asia-south2) 
Singapore (asia-southeast1) 
Jakarta (asia-southeast2) 
Bangkok (asia-southeast3) 
Kuala Lumpur (asia-southeast4) 
Sydney (australia-southeast1) 
Melbourne (australia-southeast2) 
Europe (eu) 
Warsaw (europe-central2) 
Finland (europe-north1) 
Stockholm (europe-north2) 
Madrid (europe-southwest1) 
Belgium (europe-west1) 
Berlin (europe-west10) 
Turin (europe-west12) 
London (europe-west2) 
Frankfurt (europe-west3) 
Netherlands (europe-west4) 
Galaxy Frankfurt (europe-west5) 
Zurich (europe-west6) 
Milan (europe-west8) 
Paris (europe-west9) 
Doha (me-central1) 
Dammam (me-central2) 
Tel Aviv (me-west1) 
Montreal (northamerica-northeast1) 
Toronto (northamerica-northeast2) 
Mexico (northamerica-south1) 
Sao Paulo (southamerica-east1) 
Santiago (southamerica-west1) 
Iowa (us-central1) 
Oklahoma (us-central2) 
South Carolina (us-east1) 
Northern Virginia (us-east4) 
Columbus (us-east5) 
Alabama (us-east7) 
Dallas (us-south1) 
Oregon (us-west1) 
Los Angeles (us-west2) 
Salt Lake City (us-west3) 
Las Vegas (us-west4) 
Phoenix (us-west8) Hourly Hourly Monthly Monthly 

Resource 
Pricing 
Details 

Memory capacity $0.0416 / 1 gibibyte hour 
You are charged per GiB/hour for each project in which you have reserved capacity . 
If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply. 

Editions commitment bundle 
When you are using BigQuery capacity compute pricing with BigQuery editions commitments, you are eligible to receive a limited amount of BI Engine capacity as part of your editions price, at no extra cost, as shown in the following chart. To receive BI Engine capacity at no additional cost, follow the instructions to reserve capacity in a project within the same organization as your editions reservation. To ensure a particular project’s BI Engine reservation is discounted toward this bundled capacity, there should be some slots assigned to the project. BI Engine reservation in an 'on-demand analysis' project will not be counted towards the free capacity. Free capacity is shown in your Billing Reports as a normal cost, but it is discounted as a "Spending-Based Discount". 

Number of slots purchased 
No-cost, additional BI Engine capacity (GiB) 

100 
5 

500 
25 

1000 
50 

1500 
75 

2000 
100 (maximum per organization) 
Free operations 
The following BigQuery operations are free of charge in every location. Quotas and limits apply to these operations. 
If you are copying tables across regions, you are charged for data replication . 

Operation 
Details 

Batch load data 
You are not charged for batch loading data using the shared slot pool. You can also create a reservation using editions pricing for guaranteed capacity. Once the data is loaded into BigQuery, you are charged for storage. For details, see Batch loading data . 

Copy data 
You are not charged for copying a table, but you do incur charges for storing the new table. For more information, see Copying an existing table . 

Export data 
You are not charged for exporting data using the shared slot pool, but you do incur charges for storing the data in Cloud Storage. You can also create a reservation using editions pricing for guaranteed capacity. When you use the EXPORT DATA SQL statement , you are charged for query processing. For details, see Exporting data . 

Delete operations 
You are not charged for deleting datasets or tables, deleting individual table partitions, deleting views, or deleting user-defined functions. 
Free usage tier 
As part of the Google Cloud Free Tier , BigQuery offers some resources free of charge up to a specific limit. These free usage limits are available during and after the free trial period. If you go over these usage limits and are no longer in the free trial period, you will be charged according to the pricing on this page. You can try BigQuery's free tier in the BigQuery sandbox without a credit card. 

Resource 
Monthly free usage limits 
Details 

Storage 
The first 10 GiB per month is free. 
BigQuery ML models and training data stored in BigQuery are included in the BigQuery storage free tier. 

Queries (analysis) 
The first 1 TiB of query data processed per month is free. 
BigQuery Editions pricing is also available for high-volume customers that prefer a stable, monthly cost. 
Flat-rate pricing 
Note: The BigQuery flat-rate pricing model is no longer offered as of July 5, 2023. It is described here for customers who have existing flat-rate commitments 

Flat-rate compute pricing 
When you use the flat-rate compute pricing model, you purchase dedicated query processing capacity, measured in BigQuery slots . Your queries consume this capacity, and you are not billed for bytes processed. If your capacity demands exceed your committed capacity, BigQuery will queue up queries, and you will not be charged additional fees. 
Flat-rate compute pricing: 
Applies to query costs, including BigQuery ML, DML, and DDL statements. 
Does not apply to storage costs or BI Engine costs. 
Does not apply to streaming inserts and using the BigQuery Storage API. 
Is purchased as a regional resource. Slot commitments purchased in one region or multi-region cannot be used in another region or multi-region and cannot be moved. 
Is available in per-second (flex), monthly, and annual commitments. 
Can be shared across your entire organization. There is no need to buy slot commitments for every project. 
Has a 100-slot minimum and is purchased in increments of 100 slots. 
Is billed per second until you cancel the commitment, which can be done at any time after the commitment end date. 

Monthly flat-rate commitments 
The following table shows the cost of your monthly flat-rate slot commitment. For more information, see Monthly commitments . Iowa (us-central1) 
Seoul (AWS) (aws-ap-northeast-2) 
Northern Virginia (AWS) (aws-us-east-1) 
Virginia (Azure) (azure-us-east2) 
Johannesburg (africa-south1) 
Taiwan (asia-east1) 
Hong Kong (asia-east2) 
Tokyo (asia-northeast1) 
Osaka (asia-northeast2) 
Seoul (asia-northeast3) 
Mumbai (asia-south1) 
Delhi (asia-south2) 
Singapore (asia-southeast1) 
Jakarta (asia-southeast2) 
Bangkok (asia-southeast3) 
Kuala Lumpur (asia-southeast4) 
Sydney (australia-southeast1) 
Melbourne (australia-southeast2) 
Europe (eu) 
Warsaw (europe-central2) 
Finland (europe-north1) 
Stockholm (europe-north2) 
Madrid (europe-southwest1) 
Belgium (europe-west1) 
Berlin (europe-west10) 
Turin (europe-west12) 
London (europe-west2) 
Frankfurt (europe-west3) 
Netherlands (europe-west4) 
Zurich (europe-west6) 
Milan (europe-west8) 
Paris (europe-west9) 
Doha (me-central1) 
Dammam (me-central2) 
Tel Aviv (me-west1) 
Montreal (northamerica-northeast1) 
Toronto (northamerica-northeast2) 
Mexico (northamerica-south1) 
Sao Paulo (southamerica-east1) 
Santiago (southamerica-west1) 
US (us) 
Iowa (us-central1) 
South Carolina (us-east1) 
Northern Virginia (us-east4) 
Columbus (us-east5) 
Alabama (us-east7) 
Dallas (us-south1) 
Oregon (us-west1) 
Los Angeles (us-west2) 
Salt Lake City (us-west3) 
Las Vegas (us-west4) 
Phoenix (us-west8) Hourly Hourly Monthly Monthly 

Number of slots 
Cost 

100 $2.739726027 / 1 hour 
If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply. 

Annual flat-rate commitments 
The following table shows the cost of your annual flate-rate slot commitment. For more information, see Annual commitments . Iowa (us-central1) 
Seoul (AWS) (aws-ap-northeast-2) 
Northern Virginia (AWS) (aws-us-east-1) 
Virginia (Azure) (azure-us-east2) 
Johannesburg (africa-south1) 
Taiwan (asia-east1) 
Hong Kong (asia-east2) 
Tokyo (asia-northeast1) 
Osaka (asia-northeast2) 
Seoul (asia-northeast3) 
Mumbai (asia-south1) 
Delhi (asia-south2) 
Singapore (asia-southeast1) 
Jakarta (asia-southeast2) 
Bangkok (asia-southeast3) 
Kuala Lumpur (asia-southeast4) 
Sydney (australia-southeast1) 
Melbourne (australia-southeast2) 
Europe (eu) 
Warsaw (europe-central2) 
Finland (europe-north1) 
Stockholm (europe-north2) 
Madrid (europe-southwest1) 
Belgium (europe-west1) 
Berlin (europe-west10) 
Turin (europe-west12) 
London (europe-west2) 
Frankfurt (europe-west3) 
Netherlands (europe-west4) 
Zurich (europe-west6) 
Milan (europe-west8) 
Paris (europe-west9) 
Doha (me-central1) 
Dammam (me-central2) 
Tel Aviv (me-west1) 
Montreal (northamerica-northeast1) 
Toronto (northamerica-northeast2) 
Mexico (northamerica-south1) 
Sao Paulo (southamerica-east1) 
Santiago (southamerica-west1) 
Iowa (us-central1) 
South Carolina (us-east1) 
Northern Virginia (us-east4) 
Columbus (us-east5) 
Alabama (us-east7) 
Dallas (us-south1) 
Oregon (us-west1) 
Los Angeles (us-west2) 
Salt Lake City (us-west3) 
Las Vegas (us-west4) 
Phoenix (us-west8) Hourly Hourly Monthly Monthly 

Number of slots 
Cost 

100 $2.328767123 / 1 hour 
If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply. 

Flex slots: short-term flat-rate commitments 
Flex slots are a special commitment type: 
Commitment duration is only 60 seconds. 
You can cancel flex slots any time thereafter. 
You are charged only for the seconds your commitment was deployed. 
Flex slots are subject to capacity availability. When you attempt to purchase flex slots, success of this purchase is not guaranteed. However, once your commitment purchase is successful, your capacity is guaranteed until you cancel it. For more information, see flex slots . 
The following table shows the cost of your Flex slot commitment. Iowa (us-central1) 
Seoul (AWS) (aws-ap-northeast-2) 
Northern Virginia (AWS) (aws-us-east-1) 
Virginia (Azure) (azure-us-east2) 
Johannesburg (africa-south1) 
Taiwan (asia-east1) 
Hong Kong (asia-east2) 
Tokyo (asia-northeast1) 
Osaka (asia-northeast2) 
Seoul (asia-northeast3) 
Mumbai (asia-south1) 
Delhi (asia-south2) 
Singapore (asia-southeast1) 
Jakarta (asia-southeast2) 
Bangkok (asia-southeast3) 
Kuala Lumpur (asia-southeast4) 
Sydney (australia-southeast1) 
Melbourne (australia-southeast2) 
Europe (eu) 
Warsaw (europe-central2) 
Finland (europe-north1) 
Stockholm (europe-north2) 
Madrid (europe-southwest1) 
Belgium (europe-west1) 
Berlin (europe-west10) 
Turin (europe-west12) 
London (europe-west2) 
Frankfurt (europe-west3) 
Netherlands (europe-west4) 
Zurich (europe-west6) 
Milan (europe-west8) 
Paris (europe-west9) 
Doha (me-central1) 
Dammam (me-central2) 
Tel Aviv (me-west1) 
Montreal (northamerica-northeast1) 
Toronto (northamerica-northeast2) 
Mexico (northamerica-south1) 
Sao Paulo (southamerica-east1) 
Santiago (southamerica-west1) 
US (us) 
Iowa (us-central1) 
South Carolina (us-east1) 
Northern Virginia (us-east4) 
Columbus (us-east5) 
Alabama (us-east7) 
Dallas (us-south1) 
Oregon (us-west1) 
Los Angeles (us-west2) 
Salt Lake City (us-west3) 
Las Vegas (us-west4) 
Phoenix (us-west8) Hourly Hourly Monthly Monthly 

Number of slots 
Cost 

100 $4.00 / 1 hour 

BigQuery Omni flat-rate pricing 
BigQuery Omni offers flat-rate pricing which provides a predictable cost for queries. To enable flat-rate pricing, use BigQuery Reservations. 
When you enroll in flat-rate pricing for BigQuery Omni, you purchase dedicated query processing capacity, measured in slots, on Amazon Web Services or Microsoft Azure. Your queries consume this capacity, and you are not billed for bytes processed. 
BigQuery Omni flat-rate pricing: 
Applies to query costs. Does not apply to storage costs . 
Slot commitments are purchased for a single multi-cloud region. Slots purchased in one region cannot be used in another region. 
Is available in monthly, and annual commitments. Is billed per second until you cancel the commitment, which can be done at any time after the commitment end date. 
Can be shared across your entire organization. There is no need to buy slot commitments for every project. 
Has a 100-slot minimum and is purchased in increments of 100 slots. 

Monthly flat-rate commitments 
The following table shows the cost of your monthly slot commitment. For more information, see Monthly commitments . Seoul (AWS) (aws-ap-northeast-2) 
Seoul (AWS) (aws-ap-northeast-2) 
Northern Virginia (AWS) (aws-us-east-1) 
Virginia (Azure) (azure-us-east2) Hourly Hourly Monthly Monthly 

Number of slots 
Cost 

100 $3.424657534 / 1 hour 

Annual flat-rate commitments 
The following table shows the cost of your annual slot commitment. For more information, see Annual commitments . Seoul (AWS) (aws-ap-northeast-2) 
Seoul (AWS) (aws-ap-northeast-2) 
Northern Virginia (AWS) (aws-us-east-1) 
Virginia (Azure) (azure-us-east2) Hourly Hourly Monthly Monthly 

Number of slots 
Cost 

100 $2.910958904 / 1 hour 

Flex slots: short-term commitments 
Flex slots are a special commitment type: 
Commitment duration is only 60 seconds. 
You can cancel flex slots any time thereafter. 
You are charged only for the seconds your commitment was deployed. 
Flex slots on BigQuery Omni are subject to capacity availability on AWS or Azure. When you attempt to purchase flex slots, success of this purchase is not guaranteed. However, once your commitment purchase is successful, your capacity is guaranteed until you cancel it. For more information, see flex slots . 
The following table shows the cost of your Flex slot commitment. Northern Virginia (AWS) (aws-us-east-1) 
Northern Virginia (AWS) (aws-us-east-1) 
Virginia (Azure) (azure-us-east2) Hourly Hourly Monthly Monthly 

Number of slots 
Cost 

100 $5.00 / 1 hour 

BI Engine flat-rate commitment bundle 
When you are using BigQuery flat-rate slot commitments, you are eligible to receive a limited amount of BI Engine capacity as part of your flat-rate price, at no extra cost, as shown in the following chart. To receive BI Engine capacity at no additional cost, follow the instructions to reserve capacity in a project within the same organization as your flat-rate reservation. To ensure a particular project's BI Engine reservation is discounted toward this bundled capacity, there should be some slots assigned to the project. A BI Engine reservation in an on-demand compute project don't counted towards free capacity. Free capacity is shown in your billing reports as a normal cost, but it is discounted as a "Spending-Based Discount". 

Number of slots purchased 
No-cost, additional BI Engine capacity (GiB) 

100 
5 

500 
25 

1000 
50 

1500 
75 

2000 
100 (maximum per organization) 
What's next 
For information on analyzing billing data using reports, see View your billing reports and cost trends . 
For information on analyzing your billing data in BigQuery, see Export Cloud Billing data to BigQuery . 
For information about estimating costs, see Estimating storage and query costs . 
Read the BigQuery documentation . 
Get started with BigQuery . 
Try the Pricing calculator . 
Learn about BigQuery solutions and use cases . 
Request a custom quote With Google Cloud's pay-as-you-go pricing, you only pay for the services you use. Connect with our sales team to get a custom quote for your organization. Contact sales menu Overview Solutions Products Pricing Resources Docs Support Contact us  search send Docs Support Console Sign in Start free Start free Contact us close 
Accelerate your digital transformation 
Whether your business is early in its journey or well on its way to digital transformation, Google Cloud can help solve your toughest challenges. 
Learn more 
Key benefits 
Why Google Cloud Top reasons businesses choose us. 
AI and Agents Get enterprise-ready AI. 
Multicloud Run your apps wherever you need them. 
Global infrastructure Build on the same infrastructure as Google. 
Data Cloud Make smarter decisions with unified data. 
Modern Infrastructure Cloud Next generation of cloud infrastructure. 
Security Protect your users, data, and apps. 
Productivity and collaboration Connect your teams with AI-powered apps. 
Reports and insights 
Executive insights Curated C-suite perspectives. 
Analyst reports Read what industry analysts say about us. 
Whitepapers Browse and download popular whitepapers. 
Customer stories Explore case studies and videos. close 
Industry Solutions 
Application Modernization 
Artificial Intelligence 
APIs and Applications 
Data Analytics 
Databases 
Infrastructure Modernization 
Productivity and Collaboration 
Security 
Startups and SMB See all solutions 
Industry Solutions Reduce cost, increase operational agility, and capture new market opportunities. 
Retail Analytics and collaboration tools for the retail value chain. 
Consumer Packaged Goods Solutions for CPG digital transformation and brand growth. 
Financial Services Computing, data management, and analytics tools for financial services. 
Healthcare and Life Sciences Advance research at scale and empower healthcare innovation. 
Media and Entertainment Solutions for content production and distribution operations. 
Telecommunications Hybrid and multi-cloud services to deploy and monetize 5G. 
Games AI-driven solutions to build and scale games faster. 
Manufacturing Migration and AI tools to optimize the manufacturing value chain. 
Supply Chain and Logistics Enable sustainable, efficient, and resilient data-driven operations across supply chain and logistics operations. 
Government Data storage, AI, and analytics solutions for government agencies. 
Education Teaching tools to provide more engaging learning experiences. 
Not seeing what you're looking for? 
See all industry solutions 
Application Modernization Modernize, automate, and scale your application and data portfolio using enterprise AI, intelligent engineering practices, and cloud-native infrastructure. 
Google Cloud Modernize Unified program and AI-powered tools for end-to-end cloud migration and modernization. 
Application Modernization with AI AI-assisted code refactoring, assessment, and transformation for legacy applications. 
Gemini for business Enterprise-ready generative AI and agents to accelerate innovation across your organization. 
AI Hypercomputer Integrated supercomputing architecture to train, tune, and serve AI workloads. 
Mainframe Modernization Automated tools and AI-driven guidance for moving your mainframe apps to the cloud. 
Database Modernization Fully managed database services to migrate, manage, and modernize enterprise data. 
Data Lake Modernization Unify and govern multimodal data on an open, high-performance cloud data lake. 
Data Warehouse Modernization Migrate and modernize your enterprise data warehouse for serverless analytics and AI. 
APIs Unlock legacy applications and build new digital channels using APIs and automation. 
Platform Eng Managed services and golden paths to build, manage, and scale internal developer platforms. 
DevOps Best Practices Processes and resources for implementing DevOps in your org. 
SRE Principles Tools and resources for adopting SRE in your org. 
Artificial Intelligence Add intelligence and efficiency to your business with AI and machine learning. 
Gemini for customer experience Build and manage agents that live across the entire customer lifecycle. 
Gemini for enterprise Unified agentic portfolio for your entire organization. 
AI Commerce Search Google-quality search and product recommendations for retailers. 
Google Cloud with Gemini AI assistants for application development, coding, and more. 
Physical AI Simulate, train, and operate the next generation of robots, autonomous vehicles, industrial devices, and machines. 
APIs and Applications Speed up the pace of innovation without coding, using APIs, apps, and automation. 
New Business Channels Using APIs Attract and empower an ecosystem of developers and partners. 
Unlocking Legacy Applications Using APIs Cloud services for extending and modernizing legacy apps. 
Open Banking APIx Simplify and accelerate secure delivery of open banking compliant APIs. 
Data Analytics Generate instant insights from data at any scale with a serverless, fully managed analytics platform that significantly simplifies analytics. 
Data Migration Migrate and modernize your data warehouse and data lakes with AI-powered migration services. 
Data Lakehouse Unify and govern your multimodal data with a high-performance and open data lakehouse. 
Real-time Analytics Insights from ingesting, processing, and analyzing event streams. 
Marketing Analytics Solutions for collecting, analyzing, and activating customer data. 
Datasets Data from Google, public, and commercial providers to enrich your analytics and AI initiatives. 
Business Intelligence Solutions for modernizing your BI stack and creating rich data experiences. 
Data Analytics Agents Built-in agents for data lifecycle and tools to build your own agents. 
Geospatial Analytics A comprehensive platform to solve for geospatial use cases at scale. 
Data Science Managed services and integrated workflows to build, manage, and scale data science. 
Databases Migrate and manage enterprise data with security, reliability, high availability, and fully managed data services. 
Database Migration Guides and tools to simplify your database migration life cycle. 
Database Modernization Upgrades to modernize your operational database infrastructure. 
Databases for Games Build global, live games with Google Cloud databases. 
Google Cloud Databases Database services to migrate, manage, and modernize data. 
Migrate Oracle workloads to Google Cloud Rehost, replatform, rewrite your Oracle workloads. 
Open Source Databases Fully managed open source databases with enterprise-grade support. 
SQL Server on Google Cloud Options for running SQL Server virtual machines on Google Cloud. 
Gemini for Databases Supercharge database development and management with AI. 
Infrastructure Modernization Migrate core systems rapidly and modernize enterprise workloads with AI-powered infrastructure and automated cloud solutions. 
Google Cloud Modernize Unified program and AI-powered tools for end-to-end cloud migration and modernization. 
Gemini for business Enterprise-ready generative AI and agents to accelerate innovation across your organization. 
AI Hypercomputer Integrated supercomputing architecture to train, tune, and serve AI workloads. 
Rapid Migration and Modernization Program (RaMP) End-to-end migration program to simplify and accelerate your path to the cloud. 
Data Center Exits Migration solutions for moving VMs, apps, databases, and workloads out of data centers. 
Application Modernization & Migration Discovery, assessment, and migration tools for moving and modernizing applications. 
Database Modernization & Migration Fully managed database services to migrate, manage, and modernize enterprise data. 
Cross-Cloud Networking Simplify hybrid and multicloud networking, and secure your workloads, data, and users. 
High Performance Computing (HPC) Compute, storage, and networking options to support any high-performance workload. 
VMware Fully managed, native VMware Cloud Foundation software stack on Google Cloud. 
SAP Certified infrastructure and AI solutions for running SAP applications and SAP HANA. 
Windows Tools, licenses, and partner solutions for running enterprise Windows workloads. 
Productivity and Collaboration Change the way teams work with solutions designed for humans and built for impact. 
Google Workspace Collaboration and productivity tools for enterprises. 
Google Workspace Essentials Secure video meetings and modern collaboration for teams. 
Cloud Identity Unified platform for IT admins to manage user devices and apps. 
Chrome Enterprise ChromeOS, Chrome Browser, and Chrome devices built for business. 
Security Detect, investigate, and respond to online threats to help protect your business. 
Agentic SOC Delivering better security outcomes with AI agents. 
Web App and API Protection Threat and fraud protection for your web applications and APIs. 
Security and Resilience Framework Solutions for each phase of the security and resilience life cycle. 
Risk and compliance as code (RCaC) Solution to modernize your governance, risk, and compliance function with automation. 
Software Supply Chain Security Solution for improving end-to-end software supply chain security. 
Security Foundation Recommended products to help achieve a strong security posture. 
Google Cloud Cybershield™ Strengthen nationwide cyber defense. 
Startups and SMB Accelerate startup and SMB growth with tailored solutions and programs. 
Startup Program Get financial, business, and technical support to take your startup to the next level. 
Small and Medium Business Explore solutions for web hosting, app development, AI, and analytics. 
Software as a Service Build better SaaS products, scale efficiently, and grow your business. close 
Featured Products 
AI and Machine Learning 
Business Intelligence 
Compute 
Containers 
Data Analytics 
Databases 
Developer Tools 
Distributed Cloud 
Hybrid and Multicloud 
Industry Specific 
Integration Services 
Management Tools 
Maps and Geospatial 
Media Services 
Migration 
Networking 
Operations 
Productivity and Collaboration 
Security and Identity 
Serverless 
Storage 
Web3 See all products (100+) 
Featured Products 
Gemini for business Secure platform to discover, create, run, and govern AI agents for employees. 
Gemini platform Unified platform for ML models, generative AI, and agent building. 
Compute Engine Virtual machines running in Google’s data center. 
Cloud Storage Object storage that’s secure, durable, and scalable. 
BigQuery Autonomous data to AI platform for analytics and data science. 
Cloud Run Fully managed environment for running containerized apps. 
Google Kubernetes Engine Managed environment for running containerized apps. 
Looker Platform for BI, data applications, and embedded analytics. 
Apigee API Management Manage the full life cycle of APIs anywhere with visibility and control. 
Cloud SQL Relational database services for MySQL, PostgreSQL and SQL Server. 
Cloud CDN Content delivery network for delivering web and video. 
Not seeing what you're looking for? 
See all products (100+) 
AI and Machine Learning 
Gemini platform Unified platform for ML models, generative AI, and agent building. 
Gemini for business Secure platform to discover, create, run, and govern AI agents for employees. 
Gemini for customer experience Build and manage agents that live across the entire customer lifecycle. 
Model Garden Single place to discover over 200 models from Google and Google partners. 
Customer Experience Agent Studio Build conversational AI with both deterministic and gen AI functionality. 
Agent Search Build Google-quality search for your enterprise apps and experiences. 
Speech-to-Text Speech recognition and transcription across 125 languages. 
Text-to-Speech Speech synthesis in 220+ voices and 40+ languages. 
Translation AI Language detection, translation, and glossary support. 
Vision AI Custom and pre-trained models to detect emotion, text, and more. 
Contact Center as a Service Omnichannel contact center solution that is native to the cloud. 
Not seeing what you're looking for? 
See all AI and machine learning products 
Business Intelligence 
Looker Platform for BI, data applications, and embedded analytics. 
Data Studio Interactive data suite for dashboarding, reporting, and analytics. 
Compute 
Compute Engine Virtual machines running in Google’s data center. 
App Engine Serverless application platform for apps and back ends. 
Cloud GPUs GPUs for ML, scientific computing, and 3D visualization. 
Migrate to Virtual Machines Server and virtual machine migration to Compute Engine. 
Spot VMs Compute instances for batch jobs and fault-tolerant workloads. 
Batch Fully managed service for scheduling batch jobs. 
Sole-Tenant Nodes Dedicated hardware for compliance, licensing, and management. 
Bare Metal Infrastructure to run specialized workloads on Google Cloud. 
Recommender Usage recommendations for Google Cloud products and services. 
VMware Engine Fully managed, native VMware Cloud Foundation software stack. 
Cloud Run Fully managed environment for running containerized apps. 
Not seeing what you're looking for? 
See all compute products 
Containers 
Google Kubernetes Engine Managed environment for running containerized apps. 
Cloud Run Fully managed environment for running containerized apps. 
Cloud Build Solution for running build steps in a Docker container. 
Artifact Registry Package manager for build artifacts and dependencies. 
Cloud Code IDE support to write, run, and debug Kubernetes applications. 
Cloud Deploy Fully managed continuous delivery to GKE and Cloud Run. 
Migrate to Containers Components for migrating VMs into system containers on GKE. 
Deep Learning Containers Containers with data science frameworks, libraries, and tools. 
Knative Components to create Kubernetes-native cloud-based software. 
Data Analytics 
BigQuery Autonomous data to AI platform for analytics and data science. 
Managed Service for Apache Spark Zero-ops serverless or managed clusters, accelerated by Lightning Engine. 
Dataflow Real-time analytics for stream and batch processing. 
Looker Platform for BI, data applications, and embedded analytics. 
Lakehouse Open lakehouse platform with enterprise storage and performance capabilities. 
Pub/Sub Messaging service for event ingestion and delivery. 
Managed Service for Apache Airflow Workflow orchestration service built on Apache Airflow. 
Knowledge Catalog Always-on catalog for AI that provides universal context for agents. 
Data Analytics Agents Built-in agents for data lifecycle and tools to build your own agents. 
Data Analytics Migration Services Free-to-use, cloud-native and AI-powered data migration services. 
Managed Service for Apache Kafka Managed Kafka service to operate highly available Apache Kafka clusters. 
Not seeing what you're looking for? 
See all data analytics products 
Databases 
AlloyDB for PostgreSQL Fully managed, PostgreSQL-compatible database for enterprise workloads. 
Cloud SQL Fully managed database for MySQL, PostgreSQL, and SQL Server. 
Firestore Highly scalable and serverless NoSQL document database, with MongoDB compatibility. 
Spanner Cloud-native relational database with unlimited scale and 99.999% availability. 
Bigtable Cloud-native wide-column database for large-scale, low-latency workloads. 
Datastream Serverless change data capture and replication service. 
Database Migration Service Serverless, minimal downtime migrations to Cloud SQL. 
Bare Metal Solution Fully managed infrastructure for your Oracle workloads. 
Memorystore Fully managed Redis and Memcached for sub-millisecond data access. 
Developer Tools 
Artifact Registry Universal package manager for build artifacts and dependencies. 
Cloud Code IDE support to write, run, and debug Kubernetes applications. 
Cloud Build Continuous integration and continuous delivery platform. 
Cloud Deploy Fully managed continuous delivery to GKE and Cloud Run. 
Cloud Deployment Manager Service for creating and managing Google Cloud resources. 
Cloud SDK Command-line tools and libraries for Google Cloud. 
Cloud Scheduler Cron job scheduler for task automation and management. 
Cloud Source Repositories Private Git repository to store, manage, and track code. 
Infrastructure Manager Automate infrastructure management with Terraform. 
Cloud Workstations Managed and secure development environments in the cloud. 
Gemini Code Assist AI-powered assistant available across Google Cloud and your IDE. 
Not seeing what you're looking for? 
See all developer tools 
Distributed Cloud 
Google Distributed Cloud Connected Distributed cloud services for edge workloads. 
Google Distributed Cloud Air-gapped Distributed cloud for air-gapped workloads. 
Hybrid and Multicloud 
Google Kubernetes Engine Managed environment for running containerized apps. 
Apigee API Management API management, development, and security platform. 
Migrate to Containers Tool to move workloads and existing applications to GKE. 
Cloud Build Service for executing builds on Google Cloud infrastructure. 
Observability Monitoring, logging, and application performance suite. 
Cloud Service Mesh Fully managed service mesh based on Envoy and Istio. 
Google Distributed Cloud Fully managed solutions for the edge and data centers. 
Industry Specific 
Anti Money Laundering AI Detect suspicious, potential money laundering activity with AI. 
Cloud Healthcare API Solution for bridging existing care systems and apps on Google Cloud. 
Device Connect for Fitbit Gain a 360-degree patient view with connected Fitbit data on Google Cloud. 
Telecom Network Automation Ready to use cloud-native automation for telecom networks. 
Telecom Data Fabric Telecom data management and analytics with an automated approach. 
Telecom Subscriber Insights Ingests data to improve subscriber acquisition and retention. 
Spectrum Access System (SAS) Controls fundamental access to the Citizens Broadband Radio Service (CBRS). 
Integration Services 
Application Integration Connect to 3rd party apps and enable data consistency without code. 
Workflows Workflow orchestration for serverless products and API services. 
Apigee API Management Manage the full life cycle of APIs anywhere with visibility and control. 
Cloud Tasks Task management service for asynchronous task execution. 
Cloud Scheduler Cron job scheduler for task automation and management. 
Managed Service for Apache Spark Zero-ops serverless or managed clusters, accelerated by Lightning Engine. 
Cloud Data Fusion Data integration for building and managing data pipelines. 
Managed Service for Apache Airflow Workflow orchestration service built on Apache Airflow. 
Pub/Sub Messaging service for event ingestion and delivery. 
Eventarc Build an event-driven architecture that can connect any service. 
Management Tools 
Cloud Shell Interactive shell environment with a built-in command line. 
Cloud console Web-based interface for managing and monitoring cloud apps. 
Cloud Endpoints Deployment and development management for APIs on Google Cloud. 
Cloud IAM Permissions management system for Google Cloud resources. 
Cloud APIs Programmatic interfaces for  Google Cloud services. 
Service Catalog Service catalog for admins managing internal enterprise solutions. 
Cost Management Tools for monitoring, controlling, and optimizing your costs. 
Observability Monitoring, logging, and application performance suite. 
Carbon Footprint Dashboard to view and export Google Cloud carbon emissions reports. 
Config Connector Kubernetes add-on for managing Google Cloud resources. 
Active Assist Tools for easily managing performance, security, and cost. 
Not seeing what you're looking for? 
See all management tools 
Maps and Geospatial 
Earth Engine Geospatial platform for Earth observation data and analysis. 
Google Maps Platform Create immersive location experiences and improve business operations. 
Media Services 
Cloud CDN Content delivery network for serving web and video content. 
Live Stream API Service to convert live video and package for streaming. 
OpenCue Open source render manager for visual effects and animation. 
Transcoder API Convert video files and package them for optimized delivery. 
Video Stitcher API Service for dynamic or server side ad insertion. 
Migration 
Migration Center Unified platform for migrating and modernizing with Google Cloud. 
Application Migration App migration to the cloud for low-cost refresh cycles. 
Migrate to Virtual Machines Components for migrating VMs and physical servers to Compute Engine. 
Cloud Foundation Toolkit Reference templates for Deployment Manager and Terraform. 
Database Migration Service Serverless, minimal downtime migrations to Cloud SQL. 
Migrate to Containers Components for migrating VMs into system containers on GKE. 
Data Analytics Migration Services Streamlined data warehouse and data lake migration tooling and incentives. 
Rapid Migration and Modernization Program End-to-end migration program to simplify your path to the cloud. 
Transfer Appliance Storage server for moving large volumes of data to Google Cloud. 
Storage Transfer Service Data transfers from online and on-premises sources to Cloud Storage. 
VMware Engine Migrate and run your VMware workloads natively on Google Cloud. 
Networking 
Cloud Armor Security policies and defense against web and DDoS attacks. 
Cloud CDN and Media CDN Content delivery network for serving web and video content. 
Cloud DNS Domain name system for reliable and low-latency name lookups. 
Cloud Load Balancing Service for distributing traffic across applications and regions. 
Cloud NAT NAT service for giving private instances internet access. 
Cloud Connectivity Connectivity options for VPN, peering, and enterprise needs. 
Network Connectivity Center Connectivity management to help simplify and scale networks. 
Network Intelligence Center Network monitoring, verification, and optimization platform. 
Network Service Tiers Cloud network options  based on performance, availability, and cost. 
Virtual Private Cloud Single VPC for an entire organization, isolated within projects. 
Private Service Connect Secure connection between your VPC and services. 
Not seeing what you're looking for? 
See all networking products 
Operations 
Cloud Logging Google Cloud audit, platform, and application logs management. 
Cloud Monitoring Infrastructure and application health with rich metrics. 
Error Reporting Application error identification and analysis. 
Managed Service for Prometheus Fully-managed Prometheus on Google Cloud. 
Cloud Trace Tracing system collecting latency data from applications. 
Cloud Profiler CPU and heap profiler for analyzing application performance. 
Cloud Quotas Manage quotas for all Google Cloud services. 
Productivity and Collaboration 
AppSheet No-code development platform to build and extend applications. 
AppSheet Automation Build automations and applications on a unified platform. 
Gemini for business Secure platform to discover, create, run, and govern AI agents for employees. 
Google Workspace Collaboration and productivity tools for individuals and organizations. 
Google Workspace Essentials Secure video meetings and modern collaboration for teams. 
Cloud Identity Unified platform for IT admins to manage user devices and apps. 
Chrome Enterprise ChromeOS, Chrome browser, and Chrome devices built for business. 
Security and Identity 
Cloud IAM Permissions management system for Google Cloud resources. 
Sensitive Data Protection Discover, classify, and protect your valuable data assets. 
Mandiant Managed Defense Find and eliminate threats with confidence 24x7. 
Google Threat Intelligence Know who’s targeting you. 
Security Command Center Platform for defending against threats to your Google Cloud assets. 
Cloud Key Management Manage encryption keys on Google Cloud. 
Mandiant Incident Response Minimize the impact of a breach. 
Chrome Enterprise Premium Get secure enterprise browsing with extensive endpoint visibility. 
Assured Workloads Compliance and security controls for sensitive workloads. 
Google Security Operations Detect, investigate, and respond to cyber threats. 
Mandiant Consulting Get expert guidance before, during, and after an incident. 
Not seeing what you're looking for? 
See all security and identity products 
Serverless 
Cloud Run Fully managed environment for running containerized apps. 
Cloud Functions Platform for creating functions that respond to cloud events. 
App Engine Serverless application platform for apps and back ends. 
Workflows Workflow orchestration for serverless products and API services. 
API Gateway Develop, deploy, secure, and manage APIs with a fully managed gateway. 
Storage 
Cloud Storage Object storage that’s secure, durable, and scalable. 
Block Storage High-performance storage for AI, analytics, databases, and enterprise applications. 
Filestore File storage that is highly scalable and secure. 
Persistent Disk Block storage for virtual machine instances running on Google Cloud. 
Cloud Storage for Firebase Object storage for storing and serving user-generated content. 
Local SSD Block storage that is locally attached for high-performance needs. 
Storage Transfer Service Data transfers from online and on-premises sources to Cloud Storage. 
Google Cloud Managed Lustre High performance managed parallel file service. 
Google Cloud NetApp Volumes File storage service for NFS, SMB, and multi-protocol environments. 
Backup and DR Service Service for centralized, application-consistent data protection. 
Web3 
Blockchain Node Engine Fully managed node hosting for developing on the blockchain. 
Blockchain RPC Enterprise-grade RPC for building on the blockchain. close 
Save money with our transparent approach to pricing 
Google Cloud's pay-as-you-go pricing offers automatic savings based on monthly usage and discounted rates for prepaid resources. Contact us today to get a quote. 
Request a quote 
Pricing overview and tools 
Google Cloud pricing Pay only for what you use with no lock-in. 
Pricing calculator Calculate your cloud savings. 
Google Cloud free tier Explore products with free monthly usage. 
Cost optimization framework Get best practices to optimize workload costs. 
Cost management tools Tools to monitor and control your costs. 
Product-specific Pricing 
Compute Engine 
Cloud SQL 
Google Kubernetes Engine 
Cloud Storage 
BigQuery 
See full price list with 100+ products close 
Learn & build 
Google Cloud Free Program $300 in free credits and 20+ free products. 
Solution Generator Get AI generated solution recommendations. 
Quickstarts Get tutorials and walkthroughs. 
Blog Read our latest product news and stories. 
Learning Hub Grow your career with role-based training. 
Google Cloud certification Prepare and register for certifications. 
Cloud computing basics Learn more about cloud computing basics. 
Cloud Architecture Center Get reference architectures and best practices. 
Connect 
Innovators Join Google Cloud's developer program. 
Developer Center Stay in the know and stay connected. 
Events and webinars Browse upcoming and on demand events. 
Google Cloud Community Ask questions, find answers, and connect. 
Consulting and Partners 
Google Cloud Consulting Work with our experts on cloud projects. 
Google Cloud Marketplace Deploy ready-to-go solutions in a few clicks. 
Find a partner Explore the benefits of working with a partner. 
Google Cloud partners Learn about the ecosystem and resources. close 
Overview 
arrow_forward 
Solutions 
arrow_forward 
Products 
arrow_forward 
Pricing 
arrow_forward 
Resources 
arrow_forward 
Docs 
Support 
Console 
Accelerate your digital transformation 
Learn more 
Key benefits 
Why Google Cloud 
AI and Agents 
Multicloud 
Global infrastructure 
Data Cloud 
Modern Infrastructure Cloud 
Security 
Productivity and collaboration 
Reports and insights 
Executive insights 
Analyst reports 
Whitepapers 
Customer stories 
Industry Solutions 
Retail 
Consumer Packaged Goods 
Financial Services 
Healthcare and Life Sciences 
Media and Entertainment 
Telecommunications 
Games 
Manufacturing 
Supply Chain and Logistics 
Government 
Education 
See all industry solutions 
See all solutions 
Application Modernization 
Google Cloud Modernize 
Application Modernization with AI 
Gemini for business 
AI Hypercomputer 
Mainframe Modernization 
Database Modernization 
Data Lake Modernization 
Data Warehouse Modernization 
APIs 
Platform Eng 
DevOps Best Practices 
SRE Principles 
Artificial Intelligence 
Gemini for customer experience 
Gemini for enterprise 
AI Commerce Search 
Google Cloud with Gemini 
Physical AI 
APIs and Applications 
New Business Channels Using APIs 
Unlocking Legacy Applications Using APIs 
Open Banking APIx 
Data Analytics 
Data Migration 
Data Lakehouse 
Real-time Analytics 
Marketing Analytics 
Datasets 
Business Intelligence 
Data Analytics Agents 
Geospatial Analytics 
Data Science 
Databases 
Database Migration 
Database Modernization 
Databases for Games 
Google Cloud Databases 
Migrate Oracle workloads to Google Cloud 
Open Source Databases 
SQL Server on Google Cloud 
Gemini for Databases 
Infrastructure Modernization 
Google Cloud Modernize 
Gemini for business 
AI Hypercomputer 
Rapid Migration and Modernization Program (RaMP) 
Data Center Exits 
Application Modernization & Migration 
Database Modernization & Migration 
Cross-Cloud Networking 
High Performance Computing (HPC) 
VMware 
SAP 
Windows 
Productivity and Collaboration 
Google Workspace 
Google Workspace Essentials 
Cloud Identity 
Chrome Enterprise 
Security 
Agentic SOC 
Web App and API Protection 
Security and Resilience Framework 
Risk and compliance as code (RCaC) 
Software Supply Chain Security 
Security Foundation 
Google Cloud Cybershield™ 
Startups and SMB 
Startup Program 
Small and Medium Business 
Software as a Service 
Featured Products 
Gemini for business 
Gemini platform 
Compute Engine 
Cloud Storage 
BigQuery 
Cloud Run 
Google Kubernetes Engine 
Looker 
Apigee API Management 
Cloud SQL 
Cloud CDN 
See all products (100+) 
AI and Machine Learning 
Gemini platform 
Gemini for business 
Gemini for customer experience 
Model Garden 
Customer Experience Agent Studio 
Agent Search 
Speech-to-Text 
Text-to-Speech 
Translation AI 
Vision AI 
Contact Center as a Service 
See all AI and machine learning products 
Business Intelligence 
Looker 
Data Studio 
Compute 
Compute Engine 
App Engine 
Cloud GPUs 
Migrate to Virtual Machines 
Spot VMs 
Batch 
Sole-Tenant Nodes 
Bare Metal 
Recommender 
VMware Engine 
Cloud Run 
See all compute products 
Containers 
Google Kubernetes Engine 
Cloud Run 
Cloud Build 
Artifact Registry 
Cloud Code 
Cloud Deploy 
Migrate to Containers 
Deep Learning Containers 
Knative 
Data Analytics 
BigQuery 
Managed Service for Apache Spark 
Dataflow 
Looker 
Lakehouse 
Pub/Sub 
Managed Service for Apache Airflow 
Knowledge Catalog 
Data Analytics Agents 
Data Analytics Migration Services 
Managed Service for Apache Kafka 
See all data analytics products 
Databases 
AlloyDB for PostgreSQL 
Cloud SQL 
Firestore 
Spanner 
Bigtable 
Datastream 
Database Migration Service 
Bare Metal Solution 
Memorystore 
Developer Tools 
Artifact Registry 
Cloud Code 
Cloud Build 
Cloud Deploy 
Cloud Deployment Manager 
Cloud SDK 
Cloud Scheduler 
Cloud Source Repositories 
Infrastructure Manager 
Cloud Workstations 
Gemini Code Assist 
See all developer tools 
Distributed Cloud 
Google Distributed Cloud Connected 
Google Distributed Cloud Air-gapped 
Hybrid and Multicloud 
Google Kubernetes Engine 
Apigee API Management 
Migrate to Containers 
Cloud Build 
Observability 
Cloud Service Mesh 
Google Distributed Cloud 
Industry Specific 
Anti Money Laundering AI 
Cloud Healthcare API 
Device Connect for Fitbit 
Telecom Network Automation 
Telecom Data Fabric 
Telecom Subscriber Insights 
Spectrum Access System (SAS) 
Integration Services 
Application Integration 
Workflows 
Apigee API Management 
Cloud Tasks 
Cloud Scheduler 
Managed Service for Apache Spark 
Cloud Data Fusion 
Managed Service for Apache Airflow 
Pub/Sub 
Eventarc 
Management Tools 
Cloud Shell 
Cloud console 
Cloud Endpoints 
Cloud IAM 
Cloud APIs 
Service Catalog 
Cost Management 
Observability 
Carbon Footprint 
Config Connector 
Active Assist 
See all management tools 
Maps and Geospatial 
Earth Engine 
Google Maps Platform 
Media Services 
Cloud CDN 
Live Stream API 
OpenCue 
Transcoder API 
Video Stitcher API 
Migration 
Migration Center 
Application Migration 
Migrate to Virtual Machines 
Cloud Foundation Toolkit 
Database Migration Service 
Migrate to Containers 
Data Analytics Migration Services 
Rapid Migration and Modernization Program 
Transfer Appliance 
Storage Transfer Service 
VMware Engine 
Networking 
Cloud Armor 
Cloud CDN and Media CDN 
Cloud DNS 
Cloud Load Balancing 
Cloud NAT 
Cloud Connectivity 
Network Connectivity Center 
Network Intelligence Center 
Network Service Tiers 
Virtual Private Cloud 
Private Service Connect 
See all networking products 
Operations 
Cloud Logging 
Cloud Monitoring 
Error Reporting 
Managed Service for Prometheus 
Cloud Trace 
Cloud Profiler 
Cloud Quotas 
Productivity and Collaboration 
AppSheet 
AppSheet Automation 
Gemini for business 
Google Workspace 
Google Workspace Essentials 
Cloud Identity 
Chrome Enterprise 
Security and Identity 
Cloud IAM 
Sensitive Data Protection 
Mandiant Managed Defense 
Google Threat Intelligence 
Security Command Center 
Cloud Key Management 
Mandiant Incident Response 
Chrome Enterprise Premium 
Assured Workloads 
Google Security Operations 
Mandiant Consulting 
See all security and identity products 
Serverless 
Cloud Run 
Cloud Functions 
App Engine 
Workflows 
API Gateway 
Storage 
Cloud Storage 
Block Storage 
Filestore 
Persistent Disk 
Cloud Storage for Firebase 
Local SSD 
Storage Transfer Service 
Google Cloud Managed Lustre 
Google Cloud NetApp Volumes 
Backup and DR Service 
Web3 
Blockchain Node Engine 
Blockchain RPC 
Save money with our transparent approach to pricing 
Request a quote 
Pricing overview and tools 
Google Cloud pricing 
Pricing calculator 
Google Cloud free tier 
Cost optimization framework 
Cost management tools 
Product-specific Pricing 
Compute Engine 
Cloud SQL 
Google Kubernetes Engine 
Cloud Storage 
BigQuery 
See full price list with 100+ products 
Learn & build 
Google Cloud Free Program 
Solution Generator 
Quickstarts 
Blog 
Learning Hub 
Google Cloud certification 
Cloud computing basics 
Cloud Architecture Center 
Connect 
Innovators 
Developer Center 
Events and webinars 
Google Cloud Community 
Consulting and Partners 
Google Cloud Consulting 
Google Cloud Marketplace 
Find a partner 
Google Cloud partners 

Why Google 
Choosing Google Cloud 
Trust and security 
Modern Infrastructure Cloud 
Multicloud 
Global infrastructure 
Locations 
Customers and case studies 
Analyst reports 
Whitepapers 
Blog 

Products and pricing 
Google Cloud pricing 
Google Workspace pricing 
See all products 

Solutions 
Infrastructure modernization 
Databases 
Application modernization 
Smart analytics 
Artificial Intelligence 
Security 
Productivity & work transformation 
Industry solutions 
DevOps solutions 
Small business solutions 
See all solutions 

Resources 
Google Cloud Affiliate Program 
Google Cloud documentation 
Google Cloud quickstarts 
Google Cloud Marketplace 
Learn about cloud computing 
Support 
Code samples 
Cloud Architecture Center 
Training 
Certifications 
Google for Developers 
Google Cloud for Startups 
System status 
Release Notes 

Engage 
Contact sales 
Find a Partner 
Become a Partner 
Events 
Podcasts 
Developer Center 
Press Corner 
Google Cloud on YouTube 
Google Cloud Tech on YouTube 
Follow on X 
Join User Research 
We're hiring. Join Google Cloud! 
Community forums 
About Google 
Privacy 
Site terms 
Google Cloud terms 
Cookies management controls 
Our third decade of climate action: join us 
Sign up for the Google Cloud newsletter Subscribe language ‪English‬ 
‪English‬ 
‪Deutsch‬ 
‪Español‬ 
‪Español (Latinoamérica)‬ 
‪Français‬ 
‪Indonesia‬ 
‪Italiano‬ 
‪Português (Brasil)‬ 
‪简体中文‬ 
‪繁體中文‬ 
‪日本語‬ 
‪한국어‬ 