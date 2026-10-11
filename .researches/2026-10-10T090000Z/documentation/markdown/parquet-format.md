# parquet-format

Source: https://parquet.apache.org/docs/file-format/
Retrieved: 2026-10-10

File Format | Parquet Parquet 
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
Events View page source Edit this page Create child page Create documentation issue Print entire section Categories 
Features 4 
Documentation 
File Format 
File Format Documentation about the Parquet File Format. 
This file and the thrift definition should be read together to understand the format. 
4-byte magic number "PAR1"
    <Column 1 Chunk 1>
    <Column 2 Chunk 1>
    ...
    <Column N Chunk 1>
    <Column 1 Chunk 2>
    <Column 2 Chunk 2>
    ...
    <Column N Chunk 2>
    ...
    <Column 1 Chunk M>
    <Column 2 Chunk M>
    ...
    <Column N Chunk M>
    File Metadata
    4-byte length in bytes of file metadata (little endian)
    4-byte magic number "PAR1" 
In the above example, there are N columns in this table, split into M row
groups. The file metadata contains the locations of all the column chunk
start locations. More details on what is contained in the metadata can be found
in the Thrift definition. 
File metadata is written after the data to allow for single pass writing. 
Readers are expected to first read the file metadata to find all the column
chunks they are interested in. The columns chunks should then be read sequentially. 
The format is explicitly designed to separate the metadata from the data. This
allows splitting columns into multiple files, as well as having a single metadata
file reference multiple parquet files. 
Binary Protocol Extensions 
Configurations 
Extensibility 
Metadata 
Types 
Nested Encoding 
Bloom Filter 
Data Pages 
Nulls 
Page Index 
Implementation status 
Parquet format versions 
Last modified July 7, 2024: GH-68: Match language from parquet-format after merge of PARQUET-2139 (#69) (a407d81) The contents of this website are © 2026 Apache Software Foundation
under the terms of the Apache License v2 .
Apache Parquet, Parquet, and the Parquet logo are either registered trademarks or trademarks of
The Apache Software Foundation in the United States and other countries. Security | Donate | Thanks | Events | License | Privacy 