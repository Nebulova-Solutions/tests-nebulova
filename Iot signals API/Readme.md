# ETL processing test

Complete the following three challenges.

1. Given the data.csv you have to complete the script named etl.py to pass the test in the footer of the file.
   1. You have to aggregate the data per month and show the max value in the field data in the output
   2. To define the condition when the machine is working you need to find temporal windows of 10 consecutive values where CONTROL_VAR1=1 & CONTROL_VAR2=1. Filter all the data using this condition.
   3. The meaning of the NaN values (or empty values) is that the last value registered in that variable (name in the .csv) has not changed, so you have to fill them with the last numeric value registered for that name.
   4. If you find some RD_VARX without any values at all, fill them with 0 (as you can see in RD_VAR1 and RD_VAR2)
   5. After the apply previous guidelines to fill the NaN values, drop the the rest of rows where you have at least one NaN.
2. Given the script named agg.py you have to modify the implementation to make it faster as possible.
3. Create a schema.yaml file following the OpenAPI specifications to deploy an API with the following specs. You have to define and API KEY to protect the resources and you can define the response in JSON format with the types you prefer.
   - Server address: api.nebulova.es
   - Resources:
     - GET /data_table
     - GET /timeline_graph
     - POST /change_parameters
