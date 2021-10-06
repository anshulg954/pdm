import json
import glob
import os
from pymongo import MongoClient

class CRUD:
    def __init__(self, path):
        self.directory = path
        # Making Connection
        self.client = MongoClient("mongodb+srv://anshul:anshul-dic@cluster0.qxxg7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority") 
    
    def insert(self):
        # database 
        db = self.client["pdmDIC"]

        # Created or Switched to collection 
        Collection = db["IMSbearing"]

        # Loading or Opening the json file
        for file_name in glob.glob(os.path.join(self.directory, '*.json')):
            with open(file_name) as file:
                read_data = file.read()
            print(file_name)
            file_data = json.loads(read_data)
            try:
                Collection.insert_many(file_data)
            except Exception as e:
                print(e)