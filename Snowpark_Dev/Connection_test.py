import os
import snowflake.snowpark.functions
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col

connection_parameters = {"account":"vbb48100.us-east-1",\
"user":"VISHNU",\
"password": "Transform@24",\
"role":"SYSADMIN",\
"warehouse":"COMPUTE_WH",\
"database":"DEMO_DB",\
"schema":"PUBLIC"\
}

test_session = Session.builder.configs(connection_parameters).create()


print(test_session.sql("select current_warehouse(), current_database(), current_schema()").collect())

session = Session.builder.configs(connection_parameters).create()