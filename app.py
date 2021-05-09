from selenium import webdriver
import time, os
from dotenv import load_dotenv

load_dotenv(verbose=True)

i = os.getenv("ID")
p = os.getenv("PASSWORD")

print('id       : {id}'.format(id=i))
print('password : {password}'.format(password=p))

os.exit()

URL = "http://www.cretop.com/"

driver = webdriver.Chrome('./chromedriver')
driver.get(URL)

elem = driver.find_element_by_id("in_id")
elem.send_keys(i)

elem = driver.find_element_by_id("in_pw")
elem.send_keys(p)

elem = driver.find_element_by_id("loginBtn1")
elem.click()

time.sleep(2)


# 검색어 입력
search_keyword = "태광후지킨"
elem = driver.find_element_by_id("_srchNm")
elem.send_keys(search_keyword)

elem = driver.find_element_by_id("uniSrch")
elem.click()
time.sleep(3)

print('검색성공')

# 검색결과 리스트 클릭
searchs_dom = driver.find_element_by_id("srchListDiv")
first_row = searchs_dom.find_element_by_css_selector('.first a')

first_row.click() 

print('for CEO 페이지 접속 성공')
# 기본으로 전환되는 페이지 브리핑 for CEO
for_CEO_download_btn = driver.find_element_by_id('ENCOM01E0')
for_CEO_download_btn.click()
time.sleep(2)
print('for CEO 페이지 다운로드 완료')

first_row = driver.find_elements_by_css_selector("a[title='기업재무']")[-1]
first_row.click()

# 기업재무-개별재무제표
first_row = driver.find_elements_by_css_selector("a[data-menuid='0100000088']")[-1]
first_row.click()

time.sleep(2)
for_CEO_download_btn = driver.find_element_by_id('ENFNS01S0') # 다운로드
for_CEO_download_btn.click()
time.sleep(2)


# 기업재무-연결재무제표
first_row = driver.find_elements_by_css_selector("a[data-menuid='0100000092']")[-1]
first_row.click()
time.sleep(2)
for_CEO_download_btn = driver.find_element_by_id('ENFNS02S0') # 다운로드
for_CEO_download_btn.click()
time.sleep(2)

# 기업재무-재무분석
first_row = driver.find_elements_by_css_selector("a[data-menuid='0100000097']")[-1]
first_row.click()
time.sleep(2)
for_CEO_download_btn = driver.find_element_by_id('ENFNA02S0') # 다운로드
for_CEO_download_btn.click()
time.sleep(2)

# 기업재무-제무제표신뢰도
first_row = driver.find_elements_by_css_selector("a[data-menuid='0100000106']")[-1]
first_row.click()
time.sleep(2)
# for_CEO_download_btn = driver.find_element_by_id('ENFNS02S0') # 다운로드
# for_CEO_download_btn.click()
# time.sleep(2)