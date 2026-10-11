# databricks-feature-compatibility

Source: https://docs.databricks.com/aws/en/tables/features/feature-compatibility
Retrieved: 2026-10-10

Delta Lake feature compatibility and protocols | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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
Feature compatibility On this page Last updated on Sep 11, 2026 
Delta Lake feature compatibility and protocols 
Delta Lake table protocols specify which features a client must support to read or write a table. This page covers protocol versions, table features, compatibility requirements, and how Databricks manages protocol upgrades. See also Review table details with describe detail . 
Table protocol and compatibility ​ 
Every Delta Lake table has a protocol specification which indicates the set of capabilities required to read from and write to the table. Applications use the protocol specification to determine if they can support all the features that the table uses. If an application can't support a feature in the current protocol of a table, then that application can't read or write that table. 
Most new capabilities Delta Lake require you to upgrade the table protocol. 
The following table lists key terms that describe Delta Lake protocols: 

Term 
Description 

Delta Lake client 
Any system that reads or writes to a Delta Lake table. 

Read protocol 
Specifies the support required for a Delta Lake client to read a table. 

Write protocol 
Specifies the support required for a Delta Lake client to write to a table. 

minReaderVersion 
Integer value of the reader protocol. Valid values are 1 , 2 , or 3 . 

minWriterVersion 
Integer value of the writer protocol. Valid values are integers 2 through 7 . 

Table feature 
A fine-grained alternative to protocol versions used when minReaderVersion = 3 and minWriterVersion = 7. Table features map to optionally enabled Delta Lake features. 

Writer feature 
A table feature that requires write client support but does not block read-only access. 

Reader feature 
A table feature that requires both read and write client support. See Protocol versions and table features . ← ✕ 

Term 
Description 

Delta Lake client 
Any system that reads or writes to a Delta Lake table. 

Read protocol 
Specifies the support required for a Delta Lake client to read a table. 

Write protocol 
Specifies the support required for a Delta Lake client to write to a table. 

minReaderVersion 
Integer value of the reader protocol. Valid values are 1 , 2 , or 3 . 

minWriterVersion 
Integer value of the writer protocol. Valid values are integers 2 through 7 . 

Table feature 
A fine-grained alternative to protocol versions used when minReaderVersion = 3 and minWriterVersion = 7. Table features map to optionally enabled Delta Lake features. 

Writer feature 
A table feature that requires write client support but does not block read-only access. 

Reader feature 
A table feature that requires both read and write client support. See Protocol versions and table features . 
Write protocols and writer features only affect compatibility with writer clients, allowing read-only access to the table from legacy workloads. 
Not all Delta Lake features are compatible with each other. 
Some table features can't be dropped once enabled. See Drop a Delta Lake table feature and downgrade table protocol . 
Protocol versions and table features ​ 
All Delta Lake tables include an integer-based protocol version represented by minReaderVersion and minWriterVersion . Each version bundles multiple features together, and features are cumulative across versions. To comply with the Delta Lake protocol, clients must implement support for all features in a given version, including all previously released features. 
In Databricks Runtime 12.2 LTS and above, table features replace the integer-based protocol with granular flags that indicate which features a table uses. This allows finer-grained compatibility checks between clients and tables. 
Table writer features affect the way data is written. They require minWriterVersion=7 but don't block reader clients. 
Table reader features affect the way data is read. All reader features are also writer features, and require minReaderVersion=3 and minWriterVersion=7 . A client can't write to a table that it can't read. 
When table features are enabled, they appear in the protocol as readerFeatures or writerFeatures . Delta Lake resolves the table protocol to the lowest version that supports all enabled features. See Lowest possible protocol . note 
Databricks includes non-breaking partial support for table features in all supported Databricks Runtime versions. OSS Delta Lake clients choose how to implement support for given features. 
Protocol changes ​ 
The protocol for a table changes under the following conditions: 
If a new feature is enabled, the protocol is upgraded. 
If a table feature is dropped, the protocol is downgraded. 
Turning off a table feature does not result in a protocol downgrade. You must drop the feature to fully remove it from the protocol. Not all table features can be dropped. See Drop a Delta Lake table feature and downgrade table protocol . 
All protocol change operations conflict with concurrent writes. Streaming reads fail when they encounter a commit that changes table metadata. To continue, restart the affected streams. For recommended methods, see Production considerations for Structured Streaming . note 
Databricks recommends that you never directly alter the minReaderVersion and minWriterVersion table properties. Changing these properties does not prevent protocol upgrades, and setting them to a lower value does not downgrade the table. See Drop a Delta Lake table feature and downgrade table protocol . 
What triggers a protocol upgrade ​ 
When you enable a feature, the table protocol is automatically upgraded. 
Protocol upgrades are triggered in the following ways: 
Enable automatically based on the syntax used in CREATE or ALTER statements. For example, CLUSTER BY in a CREATE TABLE statement automatically enables liquid clustering, and GENERATED ALWAYS AS enables generated columns. 
Enable explicitly through table properties. For example, setting 'delta.enableDeletionVectors' = true enables deletion vectors. 
Enabling a feature might automatically enable required features. For example, enabling Iceberg reads automatically enables column mapping, and enabling liquid clustering automatically enables checkpoint V2. Review the relevant Databricks documentation to determine which table features a given feature requires. 
Reader features upgrade both the read and write protocols. For example, column mapping is a reader feature and requires upgrading both protocols because data is stored differently in storage. 
Writer features, such as CHECK constraints, only upgrade the write protocol. warning 
Most protocol version upgrades are irreversible and might break existing Delta Lake table readers, writers, or both. Upgrade specific tables only when needed, and verify that all current and future production tools support the new protocol version. 
Protocol downgrades are available for some features. See Drop a Delta Lake table feature and downgrade table protocol . 
Lowest possible protocol ​ 
Delta Lake resolves the table protocol to the lowest version that supports all enabled features. This can only lower minReaderVersion or minWriterVersion , never raise them. Table features are never removed automatically. Use DROP FEATURE to remove a table feature from the protocol. 
If all enabled features are fully supported at a lower integer-based protocol version, the table might revert to that version and drop readerFeatures or writerFeatures from the protocol. This doesn't disable any features. Lower protocol versions increase compatibility because all clients must respect them. 
Databricks and Databricks Runtime compatibility ​ 
Databricks introduces support for new Delta Lake features in Databricks Runtime releases: 
Tables written by a lower Databricks Runtime version have full read and write support in higher Databricks Runtime versions. 
Tables written by a higher Databricks Runtime version might use table features not supported in lower Databricks Runtime versions. 
Some features allow writes from lower Databricks Runtime versions without fully applying all optimizations for the enabled feature. 
If you only use Delta Lake tables through Databricks , you only need to track feature support using minimum Databricks Runtime requirements. If you read or write tables from external systems, you must verify that those clients support the table features enabled on your tables. 
Backported table feature support ​ 
In Databricks Runtime 12.2 LTS and above, table features replaced the integer-based protocol with granular flags that indicate which features a table uses. 
Databricks has backported table feature support to Databricks Runtime 11.3 LTS and below, instead of only supporting integer protocol versions, but only for features already supported in that release. 
For example, you can read from and write to a table with generated columns enabled using table features in Databricks Runtime 9.1 LTS. However, you can't use Databricks Runtime 9.1 LTS to read from and write to a table with identity columns enabled using table features because identity columns requires Databricks Runtime 10.4 LTS and above. 
When using table features with backported support, some operations available in a given Databricks Runtime version might not be available in the corresponding OSS Delta Lake version. If your architecture includes OSS Delta Lake clients, test compatibility before enabling table features on production tables. 
Delta Lake features and required Databricks Runtime versions ​ 
The following table lists the lowest Databricks Runtime version with full support for each feature, such that all generally available capabilities for both reads and writes are supported. 

Feature 
Requires Databricks Runtime version or later 
Documentation 

CHECK constraints 
All supported Databricks Runtime versions 
CHECK constraint 

Change data feed 
All supported Databricks Runtime versions 
Use change data feed on Databricks 

Generated columns 
All supported Databricks Runtime versions 
Delta Lake generated columns 

Column mapping 
All supported Databricks Runtime versions 
Rename and drop columns with Delta Lake column mapping 

Identity columns 
All supported Databricks Runtime versions 
Identity columns 

Table features 
All supported Databricks Runtime versions 
Protocol versions and table features 

Deletion vectors 
All supported Databricks Runtime versions 
Deletion vectors in Databricks 

TimestampNTZ 
Databricks Runtime 13.3 LTS 
TIMESTAMP_NTZ type 

Iceberg reads 
Databricks Runtime 13.3 LTS 
Read Delta Lake tables with Iceberg clients 

Liquid clustering 
Databricks Runtime 13.3 LTS 
Use liquid clustering for tables 

Row tracking 
Databricks Runtime 14.3 LTS 
Row tracking in Databricks 

Type widening 
Databricks Runtime 15.4 LTS 
Type widening 

Variant 
Databricks Runtime 15.4 LTS 
Variant type support for Apache Iceberg and Delta Lake 

Collations 
Databricks Runtime 16.1 
Collation support for Delta Lake 

Protected checkpoints 
Databricks Runtime 16.3 
Drop a Delta Lake table feature and downgrade table protocol 

Catalog commits 
Databricks Runtime 16.4 LTS 
Catalog commits ← ✕ 

Feature 
Requires Databricks Runtime version or later 
Documentation 

CHECK constraints 
All supported Databricks Runtime versions 
CHECK constraint 

Change data feed 
All supported Databricks Runtime versions 
Use change data feed on Databricks 

Generated columns 
All supported Databricks Runtime versions 
Delta Lake generated columns 

Column mapping 
All supported Databricks Runtime versions 
Rename and drop columns with Delta Lake column mapping 

Identity columns 
All supported Databricks Runtime versions 
Identity columns 

Table features 
All supported Databricks Runtime versions 
Protocol versions and table features 

Deletion vectors 
All supported Databricks Runtime versions 
Deletion vectors in Databricks 

TimestampNTZ 
Databricks Runtime 13.3 LTS 
TIMESTAMP_NTZ type 

Iceberg reads 
Databricks Runtime 13.3 LTS 
Read Delta Lake tables with Iceberg clients 

Liquid clustering 
Databricks Runtime 13.3 LTS 
Use liquid clustering for tables 

Row tracking 
Databricks Runtime 14.3 LTS 
Row tracking in Databricks 

Type widening 
Databricks Runtime 15.4 LTS 
Type widening 

Variant 
Databricks Runtime 15.4 LTS 
Variant type support for Apache Iceberg and Delta Lake 

Collations 
Databricks Runtime 16.1 
Collation support for Delta Lake 

Protected checkpoints 
Databricks Runtime 16.3 
Drop a Delta Lake table feature and downgrade table protocol 

Catalog commits 
Databricks Runtime 16.4 LTS 
Catalog commits 
See Databricks Runtime release notes versions and compatibility . note 
Lakeflow pipelines and Databricks SQL automatically upgrade runtime environments with regular releases to support new features. See Lakeflow pipelines release notes and the release upgrade process and Databricks SQL release notes . 
Features by protocol version ​ note 
For Databricks Runtime compatibility, see Databricks and Databricks Runtime compatibility . 
Delta Lake uses separate minReaderVersion and minWriterVersion values to specify protocol capabilities. The open source Delta Lake protocol has standardized on table features, but some clients still use legacy protocol versioning. Because some clients might not support all features, Databricks recommends that you verify with your client documentation and test compatibility before enabling new features on production tables. 
Apache Iceberg uses a single format-version instead of separate reader and writer versions. An Iceberg format version indicates which features are available but doesn't mandate their use. Features are opt-in, except for row tracking which is mandatory in format version 3. When a feature shows N/A in the Iceberg column, it's a Delta-specific feature without a direct Iceberg equivalent. 
The following table lists protocol version requirements for Delta Lake and Apache Iceberg table features. The feature type indicates whether a feature must be respected for writes only or for both reads and writes. 

Feature 
Delta minWriterVersion 
Delta minReaderVersion 
Iceberg format-version 
Feature type 

Basic functionality 
2 
1 
1 
Writer 

CHECK constraints 
3 
1 
N/A 
Writer 

Change data feed 
4 
1 
N/A 
Writer 

Generated columns 
4 
1 
N/A 
Writer 

Column mapping 
5 
2 
N/A 
Reader and writer 

Identity columns 
6 
1 
N/A 
Writer 

Row tracking 
7 
1 
3 
Writer 

Deletion vectors 
7 
3 
3 
Reader and writer 

TimestampNTZ 
7 
3 
1 
Reader and writer 

Liquid clustering 
7 
3 
1 
Reader and writer (1) 

Iceberg reads 
7 
2 
N/A 
Writer (2) 

Type widening 
7 
3 
N/A 
Reader and writer 

Variant 
7 
3 
3 
Reader and writer 

Variant shredding 
7 
3 
3 
Reader and writer 

Collations 
7 
3 
N/A 
Reader and writer 

Protected checkpoints 
7 
1 
N/A 
Writer 

Catalog commits 
7 
3 
N/A 
Reader and writer ← ✕ 

Feature 
Delta minWriterVersion 
Delta minReaderVersion 
Iceberg format-version 
Feature type 

Basic functionality 
2 
1 
1 
Writer 

CHECK constraints 
3 
1 
N/A 
Writer 

Change data feed 
4 
1 
N/A 
Writer 

Generated columns 
4 
1 
N/A 
Writer 

Column mapping 
5 
2 
N/A 
Reader and writer 

Identity columns 
6 
1 
N/A 
Writer 

Row tracking 
7 
1 
3 
Writer 

Deletion vectors 
7 
3 
3 
Reader and writer 

TimestampNTZ 
7 
3 
1 
Reader and writer 

Liquid clustering 
7 
3 
1 
Reader and writer (1) 

Iceberg reads 
7 
2 
N/A 
Writer (2) 

Type widening 
7 
3 
N/A 
Reader and writer 

Variant 
7 
3 
3 
Reader and writer 

Variant shredding 
7 
3 
3 
Reader and writer 

Collations 
7 
3 
N/A 
Reader and writer 

Protected checkpoints 
7 
1 
N/A 
Writer 

Catalog commits 
7 
3 
N/A 
Reader and writer 
(1) : Liquid clustering implements hidden partitioning. 
(2) : Requires column mapping to be enabled. On this page 
Table protocol and compatibility 
Protocol versions and table features 
Protocol changes 
What triggers a protocol upgrade 
Lowest possible protocol 
Databricks and Databricks Runtime compatibility 
Backported table feature support 
Delta Lake features and required Databricks Runtime versions 
Features by protocol version Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 