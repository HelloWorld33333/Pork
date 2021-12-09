# 내 몽고 DB 주소
DB_URI = 'mongodb+srv://PTK:youn9900@cluster0.ttxhi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

import collections
from typing import Collection
from pymongo import MongoClient

# 몽고 DB 연결
client = MongoClient(DB_URI)

breakpoint()

print(client)