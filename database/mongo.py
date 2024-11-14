from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['army_messages']

collection = db['all_messages']