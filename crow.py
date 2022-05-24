from xml.dom.minidom import Element
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import time
from pytest import Item
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pdb
from pymongo import MongoClient
import psycopg2
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from urllib.request import urlretrieve



def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver
driver = set_chrome_driver()



#soup =



def PageUrl(pageNum):
  url_1 = 'https://www.musinsa.com/app/codimap/lists?style_type=&tag_no=&brand=&display_cnt=60&list_kind=big&sort=date&page='
  url = url_1+str(pageNum)
  return url
pageurl = PageUrl(1)
driver.get(pageurl)
totalPageNum = driver.find_element_by_css_selector(".totalPagingNum").text
print("Total Page" , str(totalPageNum))

for i in range(int(totalPageNum)):
    
    time.sleep(1)
    pageurl = PageUrl(i+1)
    driver.get(pageurl)
    last_height = driver.execute_script("return document.body.scrollHeight")
    before_location = driver.execute_script("return window.pageYOffset") 

    while True: 
        driver.execute_script("window.scrollTo(200,{})".format(before_location + 300)) 
        time.sleep(1) #이동 후 스크롤 위치 
        after_location = driver.execute_script("return window.pageYOffset") 
        #이동후 위치와 이동 후 위치가 같으면(더 이상 스크롤이 늘어나지 않으면) 종료 
        if before_location == after_location: break 
        #같지 않으면 다음 조건 실행 
        else: 
        # #이동여부 판단 기준이 되는 이전 위치 값 수정 
            before_location = driver.execute_script("return window.pageYOffset")


    item_infos = driver.find_elements_by_css_selector('body > div.wrap > div.right_area > form > div.right_contents.hover_box > div > ul > li')
    img = driver.find_elements_by_css_selector('img.style-list-thumbnail__img')
    #searchList > li:nth-child(1) > div.li_inner > div.list_img > a > img

    for i in range(len(item_infos)):
            time.sleep(0.5)
            cody = item_infos[i].find_element_by_class_name('style-list-information__text').text
            title = item_infos[i].find_element_by_class_name('style-list-information__title').text
            img_url = img[i].get_attribute("src")
    
            urllib.request.urlretrieve(img_url, "/Users/jeong-gihun/Desktop/style/" + cody+'-'+title+".jpg")

driver.close()