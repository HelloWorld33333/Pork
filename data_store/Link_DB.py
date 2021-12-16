import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


# news 데이터 가져오기, 굳이 json 형태로 변경 안해도 됬음, 그냥 json도 인코딩, 디코딩 있다는 것을 알았다는 사실에 감사하자
# 근데 왜 파일이 실행되지..
from data_import import news_1 as n1
from data_import import news_2 as n2
from data_import import news_3 as n3

new1 = n1.news_1
new2 = n2.news_2
new3 = n3.news_3

# 내 몽고 DB 주소
DB_URI = 'mongodb+srv://PTK:youn9900@cluster0.ttxhi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

import collections
from typing import Collection
from pymongo import MongoClient

# 몽고 DB URI 연결
client = MongoClient(DB_URI)

# 몽고 DB 연결
DATABASE = 'myFirstDatabase'
database = client[DATABASE]

# 몽고 collection(Tabel과 의미가 같음)
COLLECTION = 'Project3_data_store'
collection = database[COLLECTION]

# 몽고 DB URI 접속, myFirstDatabase 연결, Project3_data_store collection 생성, 데이터 적재
# id 를 _id로 수정하는 센스 캬
collection.insert_one(document=new1)
collection.insert_one(document=new2)
collection.insert_one(document=new3)


# 몽고 DB Cluster0 Collections에 보면 데이터가 추가되어 있음을 알 수 있다