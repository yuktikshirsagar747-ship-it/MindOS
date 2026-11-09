import os
from datetime import datetime, timezone

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
uri = os.getenv("MONGODB_URI")

client = MongoClient(uri, serverSelectionTimeoutMS=5000)
client.admin.command("ping")
print("Connected to MongoDB!")

db = client["mindos"]
result = db["connection_test"].insert_one(
    {"message": "hello from MindOS", "time": datetime.now(timezone.utc)}
)
print("Saved test record with id:", result.inserted_id)