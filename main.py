import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome('C:/Users/user/Desktop/학교/4학년 1학기/소웨실/크롤링/chromedriver.exe')
url = 'https://gall.dcinside.com/board/lists/?id=dcbest'
driver.get(url)

# class 이름에 공백이 있으면 .으로 연결해줘야함
# 댓글 저장 리스트
review = []
i = 2

while True:
    if len(review) >= 3000:
        break
    # 쿼리 선택 게시글 리스트에서 글을 선택하여 들어간다.
    qurey = '//*[@id="container"]/section[1]/article[2]/div[2]/table/tbody/tr['+str(i+1)+']/td[2]/a[1]'
    i += 1
    elemnt = driver.find_element_by_xpath(qurey)
    elemnt.click()
    # 페이지 타임 걸기
    time.sleep(15)
    # 댓글 모으기
    re = driver.find_elements_by_class_name('clear.cmt_txtbox.btn_reply_write_all')
    for e in re:
        review.append(e.text)
    # 바깥페이지로 이동
    el = driver.find_element_by_xpath('//*[@id="container"]/section/article[2]/div[4]/div[1]/button[1]')
    el.click()


with open('reply.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(review)