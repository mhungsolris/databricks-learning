# parquet-concepts

Source: https://parquet.apache.org/docs/concepts/
Retrieved: 2026-10-10

Concepts | Parquet Parquet 
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
Unit of parallelization Categories 
Features 4 
Documentation 
Concepts 
Concepts Glossary of relevant terminology. 

Block (HDFS block) : This means a block in HDFS and the meaning is
unchanged for describing this file format. The file format is
designed to work well on top of HDFS. 

File : A HDFS file that must include the metadata for the file.
It does not need to actually contain the data. 

Row group : A logical horizontal partitioning of the data into rows.
There is no physical structure that is guaranteed for a row group.
A row group consists of a column chunk for each column in the dataset. 

Column chunk : A chunk of the data for a particular column. They live
in a particular row group and are guaranteed to be contiguous in the file. 

Page : Column chunks are divided up into pages. A page is conceptually
an indivisible unit (in terms of compression and encoding). There can
be multiple page types which are interleaved in a column chunk. 
Hierarchically, a file consists of one or more row groups. A row group
contains exactly one column chunk per column. Column chunks contain one or
more pages. 
Unit of parallelization 
MapReduce - File/Row Group 
IO - Column chunk 
Encoding/Compression - Page Last modified March 8, 2024: Update to new website (b3b81ce) The contents of this website are © 2026 Apache Software Foundation
under the terms of the Apache License v2 .
Apache Parquet, Parquet, and the Parquet logo are either registered trademarks or trademarks of
The Apache Software Foundation in the United States and other countries. Security | Donate | Thanks | Events | License | Privacy 