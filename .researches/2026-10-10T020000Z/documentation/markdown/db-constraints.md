# db-constraints

Source: https://docs.databricks.com/aws/en/tables/constraints
Retrieved: 2026-10-10

Constraints on Databricks | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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
Table constraints On this page Last updated on Sep 11, 2026 
Constraints on Databricks 
Databricks supports standard SQL constraint management clauses: 
Enforced constraints verify data integrity before adding rows to a table. 
Informational constraints (primary key, foreign key, and unique constraints) define relationships between fields in tables and aren't enforced. 
All constraints on Databricks require Delta Lake . 
For a related concept in Lakeflow pipelines , see Manage data quality with pipeline expectations . 
Enforced constraints ​ 
When a constraint is violated, the transaction fails with an error. Databricks supports two types of constraints: 
NOT NULL : indicates that values in specific columns cannot be null. 
CHECK : indicates that a specified boolean expression must be true for each input row. note 
Adding a constraint upgrades the table writer protocol if the current writer version is less than 3. This might affect compatibility with external Delta Lake clients. See Delta Lake feature compatibility and protocols . 
NOT NULL constraint ​ 
When you create a table, specify NOT NULL constraints in the schema. To drop or add NOT NULL constraints after creation, use the ALTER TABLE ... ALTER COLUMN command. The following example creates a people_demo table that the rest of this section reuses: SQL 
CREATE OR REPLACE TABLE main . default . people_demo ( id INT NOT NULL , firstName STRING , middleName STRING NOT NULL , lastName STRING , gender STRING , birthDate TIMESTAMP , ssn STRING , salary INT ) ; ALTER TABLE main . default . people_demo ALTER COLUMN middleName DROP NOT NULL ; ALTER TABLE main . default . people_demo ALTER COLUMN ssn SET NOT NULL ; 
Databricks verifies that all existing rows satisfy the constraint before adding a NOT NULL constraint to a table. 
If you specify a NOT NULL constraint on a column nested within a struct, the parent struct must also be not null. Columns nested within array or map types don't accept NOT NULL constraints. 
See CREATE TABLE [USING] and ALTER TABLE ALTER COLUMN . 
CHECK constraint ​ 
Manage CHECK constraints with the ALTER TABLE ADD CONSTRAINT and ALTER TABLE DROP CONSTRAINT commands. ALTER TABLE ADD CONSTRAINT verifies that all existing rows satisfy the constraint before adding the constraint to the table. 
The following restrictions apply to check constraints: 
A CHECK constraint expression can use any SQL functions in Spark that always return the same result when given the same argument values, except the following types of functions: 
User-defined functions. 
Aggregate functions. 
Window functions. 
Functions returning multiple rows. Add to an existing table ​ 
The following example adds a CHECK constraint to the people_demo table created in the previous section, then drops it: SQL 
ALTER TABLE main . default . people_demo ADD CONSTRAINT dateWithinRange CHECK ( birthDate > '1900-01-01' ) ; ALTER TABLE main . default . people_demo DROP CONSTRAINT dateWithinRange ; 
See ALTER TABLE ADD CONSTRAINT and ALTER TABLE DROP CONSTRAINT . View check constraint table properties ​ 
Use the DESCRIBE DETAIL and SHOW TBLPROPERTIES commands to see a table's CHECK constraints. The following example adds a constraint to people_demo , then displays it: SQL 
ALTER TABLE main . default . people_demo ADD CONSTRAINT validIds CHECK ( id > 1 and id < 99999999 ) ; DESCRIBE DETAIL main . default . people_demo ; SHOW TBLPROPERTIES main . default . people_demo ; Remove check constraints ​ 
In Databricks Runtime 15.4 LTS and above, use the DROP FEATURE command to remove check constraints from a table and downgrade the table protocol. 
See Drop a Delta Lake table feature and downgrade table protocol . 
Declare primary key, foreign key, and unique constraints ​ 
Primary key, foreign key, and unique constraints are informational only and aren't enforced. They might improve performance through query optimizations . 
Primary key and foreign key : available for Unity Catalog and Delta Lake tables in Databricks Runtime 13.3 LTS and above. GA in Databricks Runtime 15.2 and above. Foreign keys must reference a primary key or unique constraint in another table. 
Unique : available in Public Preview for Unity Catalog and Delta Lake tables in Databricks SQL and Databricks Runtime 18.2 and above. A table can have multiple unique constraints. Foreign keys can reference a unique column using REFERENCES parent_table(unique_col) . Unique columns can be nullable because NULL values are treated as distinct from each other. 
Query the information_schema , use DESCRIBE TABLE EXTENDED , or use SHOW CREATE TABLE to get details about how constraints are applied across a given catalog. 
Add to new tables ​ 
Declare primary keys, foreign keys, and unique constraints as part of the table specification clause during table creation: SQL 
CREATE OR REPLACE TABLE main . default . T ( pk1 INTEGER NOT NULL , pk2 INTEGER NOT NULL , CONSTRAINT t_pk PRIMARY KEY ( pk1 , pk2 ) ) ; CREATE OR REPLACE TABLE main . default . S ( pk INTEGER NOT NULL PRIMARY KEY , fk1 INTEGER , fk2 INTEGER , CONSTRAINT s_t_fk FOREIGN KEY ( fk1 , fk2 ) REFERENCES main . default . T ) ; CREATE OR REPLACE TABLE main . default . U ( id INTEGER NOT NULL , email STRING NOT NULL , CONSTRAINT u_uq_email UNIQUE ( email ) ) ; 
CTAS statements don't support this constraint clause. 
Add to existing tables ​ 
Alternatively, add the same constraints to tables that already exist. This approach reaches the same result as the previous section. The following example recreates T , S , and U without constraints, then adds each constraint with ALTER TABLE ADD CONSTRAINT . Add a primary key before the foreign key that references it: SQL 
CREATE OR REPLACE TABLE main . default . T ( pk1 INTEGER NOT NULL , pk2 INTEGER NOT NULL ) ; CREATE OR REPLACE TABLE main . default . S ( pk INTEGER NOT NULL , fk1 INTEGER , fk2 INTEGER ) ; CREATE OR REPLACE TABLE main . default . U ( id INTEGER NOT NULL , email STRING NOT NULL ) ; ALTER TABLE main . default . T ADD CONSTRAINT t_pk PRIMARY KEY ( pk1 , pk2 ) ; ALTER TABLE main . default . S ADD CONSTRAINT s_t_fk FOREIGN KEY ( fk1 , fk2 ) REFERENCES main . default . T ; ALTER TABLE main . default . U ADD CONSTRAINT u_uq_email UNIQUE ( email ) ; 
Additional resources ​ 
ALTER TABLE 
ADD CONSTRAINT 
DROP CONSTRAINT 
CONSTRAINT clause On this page 
Enforced constraints 
NOT NULL constraint 
CHECK constraint 
Declare primary key, foreign key, and unique constraints 
Add to new tables 
Add to existing tables 
Additional resources Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 