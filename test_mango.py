from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("MONGODB_URI")

print("URI loaded:", uri is not None)

client = MongoClient(uri)

client.admin.command("ping")

print("MongoDB connection successful!")