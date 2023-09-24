import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_PORT = os.getenv('MONGO_PORT')
MONGO_USERNAME = os.getenv('MONGO_USERNAME')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')

client = MongoClient(MONGO_HOST, int(MONGO_PORT), username=MONGO_USERNAME, password=MONGO_PASSWORD)

db = client.flask_db
vehicles = db.vehicles