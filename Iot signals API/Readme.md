# ETL processing test

Complete the following three challenges.

1. Given the data.csv you have to transform the data using the script named etl.py to pass the test in the footer of the file. Please, take care of the following considerations: 
   1. The information comes from the signals that have been saved from an industrial machine.
   2. You have to filter the data based in the condition that the machine has been working properly. In order to detect that condition, you have to find temporal windows of 10 consecutive values where CONTROL_VAR1=1 & CONTROL_VAR2=1.
   3. When a machine is working, but some value has not changed, you will see NaN values. For example, let's say you see the following timeserie: (1.0,*NaN*,*NaN*,*NaN*,2.0). You can assume that the three NaN values in the middle have the same seen value, so, the "real" data for this example would be: (1.0,*1.0*,*1.0*,*1.0*,2.0) 
   4. If you find some values that can't be filled in that way (like point 3), the rows should be dropped. For example, in the following timeserie you don't know the last value of the first NaN: (*NaN*,1.0,*NaN*,*NaN*,*NaN*,2.0). So, you have to drop the first row and fill the rest of the data as we have seen in point 3: (1.0,*1.0*,*1.0*,*1.0*,2.0)
   5. If you find some variable that doesn't have any data (as you can see in RD_VAR1 and RD_VAR2), you have to assume that the value will be zero in the output of the test.
   6. Finally, you have to aggregate the data per MACHINE_ID and by month using the max value in every group and adjusting your output according to the format that you can see in the test. Look at the following example:
```json
{
   MACHINE_ID: {
         "RD_VAR0": {"dates": ["YYYY-MM"], "data": [int]},
         "RD_VAR1": {"dates": ["YYYY-MM"], "data": [int]},
         "RD_VAR2": {"dates": ["YYYY-MM"], "data": [int]},
         "RD_VAR3": {"dates": ["YYYY-MM"], "data": [int]},
      }
   }
```
2. Given the script named agg.py you have to modify the implementation to make it faster as possible.
3. Create a schema.yaml file following the OpenAPI specifications to deploy an API with the following specs. You have to define and API KEY to protect the resources and you can define the response in JSON format with the types you prefer.
   - Server address: api.nebulova.es (this is an example server, not a valid one)
   - Resources:
     - GET /data_table
     - GET /timeline_graph
     - POST /change_parameters
