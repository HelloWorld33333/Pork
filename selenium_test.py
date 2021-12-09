from selenium import webdriver
import chromedriver_autoinstaller
import time

# 크롬 버전 확인
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')

driver.implicitly_wait(10)

driver.get('https://namu.wiki/w/%EB%B9%84%ED%8A%B8%EC%BD%94%EC%9D%B8/%EC%82%AC%EB%A7%9D%EC%84%A0%EA%B3%A0')    
    
"""list = []

count = 1

content = driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/article/div[3]/div[2]/div/div/div[6]')
class_name = driver.find_elements_by_class_name('wiki-list')
content_herf = driver.find_elements_by_class_name('a.wiki-link-external')

content_2 = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/article/div[3]/div[2]/div/div/div[6]')
depth_1_ul = content_2.find_element_by_class_name('wiki-list')
depth_2_div = depth_1_ul.find_element_by_class_name('wiki-paragraph')
depth_3_a = depth_2_div.find_element_by_class_name('wiki-link-external')
link = depth_3_a.get_attribute('herf')

time.sleep(1)


    
for item in content:
    print(item.text)


asd = driver.find_elements_by_css_selector(".wiki-link-external")

for i in asd :
   herf = i.get_attribute('herf')
   print(herf)

driver.quit()

"""


qwe = driver.find_elements_by_css_selector("div.wiki-heading-content")

content = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/article/div[3]/div[2]/div/div/div[6]')
dfg = content.find_elements_by_class_name("wiki-list")

xxvc = dfg.find_elements_by_css_selector("wiki-link-paragraph")
dfgs = xxvc.get_attribute('herf')

for i in dfg:
    print(i.text)
    
for i in dfgs :
    print(i.text)