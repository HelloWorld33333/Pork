import pymongo
from pymongo import MongoClient

# 내 몽고 DB 주소
# 아래 데이터는 data_store 에도 있는데 from import 하면 다른 폴더인 data_import의 파일이 실행되는 문제 발생 
DB_URI = 'mongodb+srv://PTK:youn9900@cluster0.ttxhi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

# 몽고 DB URI 연결
client = MongoClient(DB_URI)

# 몽고 DB 연결
DATABASE = 'myFirstDatabase'
database = client[DATABASE]

# 몽고 collection(Tabel과 의미가 같음)
COLLECTION = 'Project3_data_store'
collection = database[COLLECTION]

# 뉴스 Id 저장
news_id = []

for news in collection.find() :
    news_id.append(news['_id'])

# 뉴스 1 데이터 가져오기
news1 = collection.find_one({"_id" : news_id[0]})

# 토큰화 하기 위해 comment만 저장하는 변수 생성
news1_comm = []

for i in range(len(news1['comment'])) :
    news1_comm.append(news1['comment'][i])


# konlpy 이 친구 이거 설정하는게 사람 속 터지게하네
# 결국 java se 설치, 환경 변수 추가, jpype 설치
# 그래도 안되서 직접 jvm.py 에서 jvmpath 변수의 경로 절대 경로로 수정해서 고쳤음
# https://clsrn4561.tistory.com/1

# 가상환경에서 파이썬은 구현이 되는데 자바는 안되나?

from konlpy.tag import Kkma
kkma = Kkma()

"""print(kkma.sentences(u'네, 안녕하세요. 반갑습니다.'))
print(kkma.nouns(u'질문이나 건의사항은 깃헙 이슈 트래커에 남겨주세요.'))"""

# 아씨 설마 Json으로 받아오는데 이거 굳이 토큰화 할 필요가 없었나?
# https://www.youtube.com/watch?v=0upqJU0kJFo

"""

def implicit():
    from google.cloud import storage

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)

implicit()

# Imports the Google Cloud client library
from google.cloud import language_v1


# Instantiates a client
client = language_v1.LanguageServiceClient()

# The text to analyze
text = u"Hello, world!"
document = language_v1.Document(
    content=text, type_=language_v1.Document.Type.PLAIN_TEXT
)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(
    request={"document": document}
).document_sentiment

print("Text: {}".format(text))
print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))"""

"""
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

"""


import re

def apply_regular_expression(text):
    hangul = re.compile('[^ ㄱ-ㅣ 가-힣]')  # 한글 추출 규칙: 띄어 쓰기(1 개)를 포함한 한글
    result = hangul.sub('', text)           # 위에 설정한 "hangul"규칙을 "text"에 적용(.sub)시킴
    return result
"""
print(kkma.nouns(apply_regular_expression(news1['comment'][0])))


# TF-IDF 벡터화
from sklearn.feature_extraction.text import TfidfVectorizer
tfv = TfidfVectorizer()
tfv.fit(news1['comment'])
tfv_news1 = tfv.transform(news1['comment'])
print(tfv_news1)


from sklearn.linear_model import LogisticRegression # 이진 분류 알고리즘

clf = LogisticRegression(random_state=0)

"""


# 워드 클라우드
"""
from wordcloud import WordCloud

wc = WordCloud(width=1000, height=600, background_color="white", random_state=0)
plt.imshow(wc.generate_from_frequencies(fd_names))
plt.axis("off")
plt.show()"""


# 아니 먼 배치파일 실행하는데 명령어가 필요해 ㅋㅋ


from google.cloud import language


def analyze_text_sentiment(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    results = dict(
        text=text,
        score=f"{sentiment.score:.1%}",
        magnitude=f"{sentiment.magnitude:.1%}",
    )
    for k, v in results.items():
        print(f"{k:10}: {v}")
        
        
        
# 구글 doc 보기 힘드네
# 얼마나 감내해야 하는지