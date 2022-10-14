import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient('mongodb+srv://LIG_JY:msib2eE7DeG5izY@cluster1.l5grkif.mongodb.net/?retryWrites=true&w=majority')
UDBdb = client['UDB']  # db_name
ca_collection = UDBdb['commissioned_area']
details = ca_collection.find({})
for _ in details:
    print(_["city"], _["county"], _["con"], _["eon"], _["ln"], _["lt"])
