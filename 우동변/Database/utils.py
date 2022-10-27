import pymongo
from pymongo import MongoClient
from collections import deque
import os
import environ # django-environ


client = pymongo.MongoClient(os.environ['MONGO_DB_PATH'])
UDBdb = client['UDB']  # db_name
ca_collection = UDBdb['commissioned_area']
details = deque(ca_collection.find({}))  # CRUD 중 R, Cursor객체(pymongo에서 지원)를 list로 바꿨습니다.
# print(type(details[3]['city'])) # value's data type is str
# print(type(details))
print(details)  # class -> dictionary
# print(type(details[0]))


