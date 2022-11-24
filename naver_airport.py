import travel
import calendar
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

today = input("Enter today date(ex:2022.12.25): ")
nowYear = int(input("What Year now?: "))
nowMonth = int(input("What Month now?: "))

destination = input("Enter your destination: ")

a = travel.Travel(nowYear, nowMonth, destination)
#travel.Travel.todayCalc(a)

print("\nChoose your travel date.\n")

for i in range(13):
    if nowMonth > 12:
        nowYear += 1
        nowMonth = nowMonth - 12
    
    calendar.prmonth(nowYear, nowMonth)
    print("\n", end = "")
    nowMonth += 1

departureDate = input("Enter your departure date(ex;2023.01.01): ")
arriveDate = input("Enter your come back date(ex:2023.01.07): ")

travel.Departure.depDateCalc(a, departureDate)
travel.Arrival.arrDateCalc(a, arriveDate)

travel.Departure.depWeekCalc(a, a.depYear, a.depMonth, a.depDay)
travel.Arrival.arrWeekCalc(a, a.arrYear, a.arrMonth, a.arrDay)

travel.Departure.depMonthCalc(a)
travel.Arrival.arrMonthCalc(a)

travel.Departure.depDayofWeekCalc(a)
travel.Arrival.arrDayofWeekCalc(a)

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://flight.naver.com/"
browser.get(url)

browser.find_elements(By.CLASS_NAME, 'select_name__1L61v')[1].click()
    
browser.find_element(By.CLASS_NAME, 'autocomplete_input__1vVkF').send_keys('{}'.format(a.destination))
time.sleep(1)
tmp = browser.find_elements(By.PARTIAL_LINK_TEXT, '{}'.format(a.destination))
tmp[0].click()

date = browser.find_elements(By.CLASS_NAME, 'tabContent_option__2y4c6')

depart = date[0]
depart.click()
time.sleep(1)

xpath_depart = '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[{}]/table/tbody/tr[{}]/td[{}]/button/b'.format(a.depMonthCode, a.depWeek, a.depDayofWeek)
browser.find_element(By.XPATH, xpath_depart).click()

arrive = date[1]
arrive.click()
time.sleep(1)

xpath_arrive = '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[{}]/table/tbody/tr[{}]/td[{}]/button/b'.format(a.arrMonthCode, a.arrWeek, a.arrDayofWeek)
browser.find_element(By.XPATH, xpath_arrive).click()

browser.find_element(By.CLASS_NAME, 'searchBox_search__2KFn3').click()
time.sleep(5)

waitCondition = WebDriverWait(browser, 90).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loadingProgress_loadingProgress__1LRJo'))) #로딩창이 없어질 때까지

result = browser.find_element(By.CLASS_NAME, 'concurrent_ConcurrentItemContainer__2lQVG')

print(result.text)