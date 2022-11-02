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
# print(type(details)) # detail의 data type은 deque
# print(type(details[0])) # detail각 element의 data type은 딕셔너리
# print(details)

myquery = {'city': '강원'}
kangwon = ca_collection.find(myquery)
kangwon = deque(kangwon)
# for i, v in enumerate(kangwon):
#     print(i, v, type(v))

document_ = ca_collection.find_one()  # colleciton에서 한 document를 찾습니다.
field_names = list(document_.keys())  # dictionray 내장 메소드로, key를 뽑아서, 리스트로 변환했습니다.

city_names = field_names[1]  # "city" , "county" , "emd"
city_list = ca_collection.distinct(city_names)

city_county_mapping = dict()  # 시/도 -> 시/군/구 mapping
for i, city in enumerate(city_list):
    city_query = {'city': f'{city}'}
    temp_cities = ca_collection.find(city_query)
    city_county_mapping[city] = temp_cities.distinct(field_names[2])  # field_names[2] == "county", key & value mapping

county_list = ca_collection.distinct(field_names[2])
county_emd_mapping = dict()  # 시/군/군 -> 읍/면/동 Mapping
for i, county in enumerate(county_list):
    county_query = {'county': f'{county}'}
    temp_counties = ca_collection.find(county_query)
    county_emd_mapping[county] = temp_counties.distinct(field_names[3])


