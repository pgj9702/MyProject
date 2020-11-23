import time

import document as document
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyautogui
from bs4 import BeautifulSoup
from datetime import datetime

try:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('window-size=1920x1080')
    chrome_options.add_argument('disable-gpu')
    chrome_options.add_argument('lang=ko_KR')

    driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)

    driver.get('https://map.naver.com/v5/search/강남역%20맛집?c=14140183.7974172,4508743.2143150,15,0,0,0,dh')
    delay = 3
    driver.implicitly_wait(delay)
    driver.get_screenshot_as_file('s0.png')

    # print(driver.page_source)   # html 소스 보기

    # #document 경로를 찾고 switch_to.frame 으로 상호 목록 html 을 전환함
    scroll_frame_xpath = driver.find_element_by_xpath('//*[@id="searchIframe"]')
    driver.switch_to.frame(scroll_frame_xpath)
    driver.implicitly_wait(delay)

    # scroll container 의 xpath 를 찾음
    scroll_container_xpath = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]')
    driver.implicitly_wait(delay)

    # 맛집 목록의 스크롤을 내림
    for _ in range(7):
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_container_xpath)
        time.sleep(1)

    # test 하기 위해 스크롤을 전부 내린 후 스샷으로 저장
    driver.get_screenshot_as_file('s3.png')

    # [@class="Tx7az" "_36o75 _3jJcF"]
    # 식당 클릭
    # scroll container 안의 모든 식당들을 클릭하기
    elements = driver.find_elements(By.XPATH, '//*[@class="Tx7az"]')

    for i, idx in zip(elements, range(len(elements))):
        i.click()   # element, 상호명으로 된 버튼을 클릭함
        # 클릭하면 새로운 html 이 생성됨, 그것에 접속하고 그 html 을 beautiful soup 에 넣어 html 을 크롤링해야함
        time.sleep(1)
        driver.switch_to.default_content()   # 상위 프레임으로 전환 (root frame)
        
        # 가게 정보 html 로 전환
        store_info_xpath = driver.find_element_by_xpath('//*[@id="entryIframe"]')

        # 크롤링 소스 ~~


        # 크롤링 소스

        # 상위 프레임으로 전환 (root frame)
        driver.switch_to.default_content()
        driver.switch_to.frame(scroll_frame_xpath)

        # test 하기 위해 상호를 클릭할 때마다 스샷을 찍어 저장함
        driver.get_screenshot_as_file(str(idx) + '.png')
        # ******** 여기서 부터 html

    driver.quit()


    # time.sleep(delay)
    #
    # driver.get_screenshot_as_file('s3.png')


except:
    print("오류")
