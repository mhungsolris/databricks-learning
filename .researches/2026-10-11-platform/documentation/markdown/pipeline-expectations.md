# pipeline-expectations

Source: https://docs.databricks.com/aws/en/ldp/developer/ldp-python-ref-expectations
Retrieved: 2026-10-11

Expectations | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
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
Lakeflow pipelines 
Developers 
Python language reference 
expect On this page Last updated on Sep 11, 2026 
Expectations 
Expectation decorators declare data quality constraints on materialized views , streaming tables , or temporary views created in a pipeline. 
The dp module includes six decorators to control expectations behavior. The following table describes the dimensions on which these permutations differ: 

Behavior 
Options 

Action on violation 
Include the row in the target dataset. The count of valid and invalid records is logged alongside other dataset metrics. 
Drop the row before writing to the target dataset. The count of dropped records is logged alongside other dataset metrics. 
Immediately stop the update. This expectation causes a failure of a single flow and does not cause other flows in your pipeline to fail. 

Number of expectations 
A single expectation or multiple expectations. ← ✕ 

Behavior 
Options 

Action on violation 
Include the row in the target dataset. The count of valid and invalid records is logged alongside other dataset metrics. 
Drop the row before writing to the target dataset. The count of dropped records is logged alongside other dataset metrics. 
Immediately stop the update. This expectation causes a failure of a single flow and does not cause other flows in your pipeline to fail. 

Number of expectations 
A single expectation or multiple expectations. 
You can add multiple expectation decorators to your datasets, providing flexibility in strictness for your data quality constraints. 
When you use expect_all decorators, each expectation has its own description and reports granular metrics. 
Syntax ​ 
Expectation decorators come after a @dp.table() , @dp.materialized_view or @dp.temporary_view() decorator and before a dataset definition function, as in the following example: Python 
from pyspark import pipelines as dp @dp . table ( ) @dp . expect ( description , constraint ) @dp . expect_or_drop ( description , constraint ) @dp . expect_or_fail ( description , constraint ) @dp . expect_all ( { description : constraint , . . . } ) @dp . expect_all_or_drop ( { description : constraint , . . . } ) @dp . expect_all_or_fail ( { description : constraint , . . . } ) def < function - name > ( ) : return ( < query > ) 
Parameters ​ 

Parameter 
Type 
Description 

description 
str 
Required. A description that identifies the constraint. Constraint descriptions must be unique for each dataset. 

constraint 
str 
Required. The constraint clause is a SQL conditional statement that must evaluate to true or false for each record. The constraint contains the actual logic for what is being validated. When a record fails this condition, the expectation is triggered. ← ✕ 

Parameter 
Type 
Description 

description 
str 
Required. A description that identifies the constraint. Constraint descriptions must be unique for each dataset. 

constraint 
str 
Required. The constraint clause is a SQL conditional statement that must evaluate to true or false for each record. The constraint contains the actual logic for what is being validated. When a record fails this condition, the expectation is triggered. 
The expect_all decorators require descriptions and constraints to be passed as a dict of key-value pairs. On this page 
Syntax 
Parameters Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 