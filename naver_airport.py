# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

destination = input("Enter your destination: ")
nowMonth = input("What month now?: ")
depMonth = input("What month do you want to leave?: ")
depWeek = input("What week do you want to leave?: ")
depDay = input("What day of the week do you want to leave?: ")
arriveMonth = input("What month do you want to come back?: ")
arriveWeek = input("What week do you want to come back?: ")
arriveDay = input("What day of the week do you want to come back?: ")

depMonth = str(int(depMonth) - int(nowMonth) + 2)
def dayCalc(day):
    week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    for i in range(len(week)):
        if week[i] == day:
            return i+1
        else:
            continue

depDay = str(dayCalc(depDay))
arriveMonth = str(int(arriveMonth) - int(nowMonth) + 2)
arriveDay = str(dayCalc(arriveDay))

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://flight.naver.com/"
browser.get(url)

browser.find_elements(By.CLASS_NAME, 'select_name__1L61v')[1].click()
    
browser.find_element(By.CLASS_NAME, 'autocomplete_input__1vVkF').send_keys('{}'.format(destination))
time.sleep(1)
tmp = browser.find_elements(By.PARTIAL_LINK_TEXT, '{}'.format(destination))
tmp[0].click()

date = browser.find_elements(By.CLASS_NAME, 'tabContent_option__2y4c6')

depart = date[0]
depart.click()
time.sleep(1)

xpath_depart = '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[{}]/table/tbody/tr[{}]/td[{}]/button/b'.format(depMonth,depWeek,depDay)
browser.find_element(By.XPATH, xpath_depart).click()

arrive = date[1]
arrive.click()
time.sleep(1)

xpath_arrive = '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[{}]/table/tbody/tr[{}]/td[{}]/button/b'.format(arriveMonth, arriveWeek, arriveDay)
browser.find_element(By.XPATH, xpath_arrive).click()

browser.find_element(By.CLASS_NAME, 'searchBox_search__2KFn3').click()
time.sleep(5)

waitCondition = WebDriverWait(browser, 90).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loadingProgress_loadingProgress__1LRJo'))) #로딩창이 없어질 때까지

result = browser.find_element(By.CLASS_NAME, 'concurrent_ConcurrentItemContainer__2lQVG')

print(result.text)