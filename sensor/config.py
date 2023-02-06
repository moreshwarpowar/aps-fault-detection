import pymongo
import pandas as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
import os
@dataclass
class EnviromentVariable():
    mongo_db_url:str = os.getenv("MONGO_DB_URL")
    aws_access_key_id:str = os.getenv("AWS_ACCESS_KEY_ID")
    aws_access_secret_key 

client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")