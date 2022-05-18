from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()

class DB():
    def get_db(self):
        client = MongoClient(
            host=os.getenv("MONGO_HOSTNAME"),
            port=os.getenv("MONGO_PORT"), 
            username=os.getenv("MONGO_USERNAME"), 
            password=os.getenv("MONGO_PASSWORD")
        )

        return client