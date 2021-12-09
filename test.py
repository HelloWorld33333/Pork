from selenium import webdriver
import chromedriver_autoinstaller
import time

# 셀레니움을 사용하려면 반드시 크롬 드라이버가 필요한데 오토 인스톨러를 사용하면 내 크롬 버전을 알아서 확인해서 맞는 버전으로 다운로드 해준다.
# 아래 코드는 오토 인스톨러 자동화 코드이다

# 크롬 버전 확인
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')
    
    # 버전이 다를 경우
except:
    # 크롬 드라이버 다운로드
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')

driver.implicitly_wait(10)


name = "효연"

driver.get('https://namu.wiki/w/'+name)

print("+" * 100)
print(driver.title)
print(driver.current_url)
print("킹무위키 크롤링")
print("-" * 100)

time.sleep(2)

# 킹무위키 페이지 진입해서 프로필 테이블 추출

allProfileElement = driver.find_elements_by_css_selector( "div.wiki-table-wrap.table-right")

# 나무위키 페이지 크롤링
for item in allProfileElement:
    for itemSub in item.find_elements_by_css_selector('tr'):
        for lastItem in itemSub.find_elements_by_css_selector("td > div"):
            if(lastItem.find_elements_by_css_selector("strong")):
                print("\n"+lastItem.find_elements_by_css_selector("strong")[0].text,end=' : ')
                
            else : print(lastItem.text)
            
driver.quit()
