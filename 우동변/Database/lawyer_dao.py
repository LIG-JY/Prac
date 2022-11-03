import pymongo
from pymongo import MongoClient
import os
import environ # django-environ


client = pymongo.MongoClient(os.environ['MONGO_DB_PATH'])
UDBdb = client['UDB']  # db_name
ca_collection = UDBdb['commissioned_area']
# print(type(details[3]['city'])) # value's data type is str
# print(type(details)) # detail의 data type은 deque
# print(type(details[0])) # detail각 element의 data type은 딕셔너리
# print(details)
