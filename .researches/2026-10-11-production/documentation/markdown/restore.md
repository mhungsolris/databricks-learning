# restore

Source: https://docs.databricks.com/aws/en/sql/language-manual/delta-restore
Retrieved: 2026-10-11

RESTORE | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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

SQL language reference 
Delta Lake statements 
RESTORE On this page Last updated on Sep 11, 2026 
RESTORE 
Applies to: Databricks SQL Databricks Runtime 
Restores a Delta table to an earlier state. Restoring to an earlier version number or a timestamp is supported. 
This page contains details for using the correct syntax with the RESTORE command. See Work with table history for more guidance on navigating Delta Lake table versions with this command. 
Syntax ​ 
RESTORE [ TABLE ] table_name [ TO ] time_travel_version time_travel_version { TIMESTAMP AS OF timestamp_expression | VERSION AS OF version } 
Parameters ​ 

table_name 
Identifies the Delta table to be restored. The table name must not use a temporal specification or options specification . 
timestamp_expression can be any one of: 
'2018-10-18T22:15:12.013Z' , that is, a string that can be cast to a timestamp 
cast('2018-10-18 13:36:32 CEST' as timestamp) 
'2018-10-18' , that is, a date string 
current_timestamp() - interval 12 hours 
date_sub(current_date(), 1) 
Any other expression that is or can be cast to a timestamp 
version is a long value that can be obtained from the output of DESCRIBE HISTORY table_spec . 
Neither timestamp_expression nor version can be subqueries. 
Examples ​ SQL 
-- Restore the employee table to a specific timestamp > RESTORE TABLE employee TO TIMESTAMP AS OF '2022-08-02 00:00:00' ; table_size_after_restore num_of_files_after_restore num_removed_files num_restored_files removed_files_size restored_files_size 100 3 1 0 574 0 -- Restore the employee table to a specific version number retrieved from DESCRIBE HISTORY employee > RESTORE TABLE employee TO VERSION AS OF 1 ; table_size_after_restore num_of_files_after_restore num_removed_files num_restored_files removed_files_size restored_files_size 100 3 1 0 574 0 -- Restore the employee table to the state it was in an hour ago > RESTORE TABLE employee TO TIMESTAMP AS OF current_timestamp ( ) - INTERVAL '1' HOUR ; table_size_after_restore num_of_files_after_restore num_removed_files num_restored_files removed_files_size restored_files_size 100 3 1 0 574 0 
Related articles ​ 
Restore a Delta table . On this page 
Syntax 
Parameters 
Examples 
Related articles Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 