from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#uniform resourece identifier
uri = "mongodb+srv://pankajSingh:pankajSingh@cluster0.mourofo.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# create database name and collection name
DATABASE_NAME="sensor-fault-detection"
COLLECTION_NAME="waferfault"

#read data as a dataframe
df=pd.read_csv(r"E:\MLproject-main\sensor-fault-detection\sensor-fault-detection\notebooks\wafer_23012020_041211.csv")

# convert the data into json
json_record=list(json.loads(df.T.to_json).values())

# Now dump the data into database
client[DATABASE_NAME][COLLECTION_NAME]=json_record


