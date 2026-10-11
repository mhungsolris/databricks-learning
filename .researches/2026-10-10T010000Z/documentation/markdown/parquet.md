# parquet

Source: https://parquet.apache.org/docs/overview/
Retrieved: 2026-10-10

Overview | Parquet Parquet 
Documentation 
Blog 
Community 
GitHub 
Documentation 
Overview 
Motivation 
Concepts 
File Format 
Binary Protocol Extensions 
Configurations 
Extensibility 
Metadata 
Types 
Geospatial Type 
Logical Types 
Variant Shredding 
Variant Type 
Nested Encoding 
Bloom Filter 
Data Pages 
Compression 
Encodings 
Encryption 
ALP Encoding 
Checksumming 
Column Chunks 
Error Recovery 
Nulls 
Page Index 
Implementation status 
Features and Versions 
Developer Guide 
Sub-Projects 
Building Parquet 
Contributing to Parquet-Java 
Releasing Parquet-Java 
Resources 
Blog Posts 
Presentations 
Spark Summit 2020 
Hadoop Summit 2014 
#CONF 2014 
Strata 2013 
Apache Software Foundation (ASF) 
License 
Security 
Sponsor 
Donate 
Events View page source Edit this page Create child page Create documentation issue Print entire section 

parquet-format (Specification) 
parquet-java 
Other Clients / Libraries / Tools Categories 
Features 4 
Documentation 
Overview 
Overview All about Parquet. 
Apache Parquet is an open source, column-oriented data file format designed for efficient data storage and retrieval.
It provides high performance compression and encoding schemes to handle complex data in bulk and is supported in many programming languages and analytics tools. 
parquet-format (Specification) 
The parquet-format repository hosts the official specification of the Parquet file format, defining how data is structured and stored. This specification, along with the parquet.thrift Thrift metadata definitions, is necessary for developing software to effectively read and write Parquet files. 
Note that the parquet-format repository does not contain source code for libraries to read or write Parquet files, but rather the formal definitions and documentation of the file format itself. 
parquet-java 
The parquet-java (formerly named parquet-mr ) repository is part of the Apache Parquet project and contains: 
Java libraries to read and write Parquet files in Java applications. 
Utilities and APIs for working with Parquet files, including tools for data import/export, schema management, and data conversion. 
Note that there are a number of other implementations of the Parquet format, some of which are listed below. 
Other Clients / Libraries / Tools 
The Parquet ecosystem is rich and varied, encompassing a wide array of tools, libraries, and clients, each offering different levels of feature support. It’s important to note that not all implementations support the same features of the Parquet format. When integrating multiple Parquet implementations within your workflow, it is crucial to conduct thorough testing to ensure compatibility and performance across different platforms and tools. 
You can find more information about the feature support of various Parquet implementations on the implementation status page. 
Here is a non-exhaustive list of open source Parquet implementations: 
Parquet-java 
Parquet C++, a subproject of Arrow C++ ( documentation ) 
Parquet Go, a subproject of Arrow Go ( documentation ) 
Parquet Rust, a subproject of Arrow Rust 
cuDF 
Apache Impala 
DuckDB 
fastparquet, a Python implementation of the Apache Parquet format Motivation 
Last modified November 12, 2025: Minor: Fix various typos on the site (#133) (a506efc) The contents of this website are © 2026 Apache Software Foundation
under the terms of the Apache License v2 .
Apache Parquet, Parquet, and the Parquet logo are either registered trademarks or trademarks of
The Apache Software Foundation in the United States and other countries. Security | Donate | Thanks | Events | License | Privacy 