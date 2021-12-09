import requests
from bs4 import BeautifulSoup

url = 'https://namu.wiki/w/%EB%B9%84%ED%8A%B8%EC%BD%94%EC%9D%B8/%EC%82%AC%EB%A7%9D%EC%84%A0%EA%B3%A0'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

head_contents = soup.find_all('a')

def get_html(url) :
    html = ""
    resp = requests.get(url)

    if resp.status_code == 200 :
        html = resp.text

html = get_html('https://namu.wiki/w/%EB%9D%BC%EC%9D%B4%ED%8A%B8%20%EB%85%B8%EB%B2%A8/%EC%8B%A0%EA%B0%84%20%EB%AA%A9%EB%A1%9D')
print(html)


source = "https://namu.wiki/RecentChanges"
req = requests.get(source)
html_2 = req.content

print(html_2)