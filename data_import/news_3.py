from selenium import webdriver
import chromedriver_autoinstaller
import time, json

# 크롬 버전 확인
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')

driver.implicitly_wait(10)


news_id = ['0003070867', '0001054988', '0003598489']

# news_id[2]
driver.get(f'https://news.naver.com/main/read.naver?m_view=1&includeAllCount=true&mode=LSD&mid=sec&sid1=105&oid=023&aid=0003598489')

#더보기 클릭
while True:
    try:
        btn_more = driver.find_element_by_css_selector('a.u_cbox_btn_more')
        btn_more.click()
        time.sleep(1)
    except:
        break

#뉴스 기사 이름
news_title = driver.find_element_by_css_selector('div.article_info > h3 > a')

#뉴스 기사 날짜
news_day = driver.find_element_by_css_selector('div.sponsor > span.t11')

# 뉴스 기사 댓글
news_comment = driver.find_elements_by_css_selector('span.u_cbox_contents')

comment_list = []

for i in news_comment:
    comment_list.append(i.text)

news_3 = {
    "_id" : news_id[2],
    "title" : news_title.text,
    "day" : news_day.text,
    "comment" : comment_list
}

new3 = json.dumps(news_3, ensure_ascii=False)

print(new3)


driver.quit()