import os
from dotenv import load_dotenv
from pymongo import MongoClient

from get_secrets import get_key_value

load_dotenv()

connection_string = get_key_value("ATLAS_CONNECTION_STR")
client = MongoClient(connection_string)
db = client[os.environ.get("ATLAS_MONGODB_DB")]
database_name = "cmarchive"
tasks_collection = db["tasks"]
mongo_collection = client["cmarchive"]["tasks"]
