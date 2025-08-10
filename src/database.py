from pymongo import MongoClient
from dotenv import load_dotenv
import os

class Database:
    def __init__(self):
        load_dotenv()
        self.client = MongoClient(os.getenv('MONGO_URI'))
        self.db = self.client["marketing_scraper"]
        if self.db is not None:
            print("Database connection established successfully.")
        self.collection = self.db["tyres"] 
        
    def insert_tyre_data(self, tyre_data):
        try:
            result = self.collection.insert_one(tyre_data)
            print(f"Data inserted with id: {result.inserted_id}")
            return result.inserted_id
        except Exception as e:
            print(f"Error inserting data: {e}")
            return None
        
    def get_all_tyres(self):
        try:
            tyres = list(self.collection.find())
            print(f"Retrieved {len(tyres)} tyre records.")
            return tyres
        except Exception as e:
            print(f"Error retrieving data: {e}")
            return []
    
    def close_connection(self):
        try:
            self.client.close()
            print("Database connection closed.")
        except Exception as e:
            print(f"Error closing connection: {e}")
            