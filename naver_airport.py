import travel
import calendar
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

today = input("Enter today date(ex:2022.12.25): ")
destination = input("Enter your destination: ")

travelPlan = travel.Travel(today, destination)
travelPlan.todayCalc()

print("\nChoose your travel date.\n")

for i in range(13):
    if travelPlan.nowMonth > 12:
        travelPlan.nowYear += 1
        travelPlan.nowMonth = travelPlan.nowMonth - 12
    
    calendar.prmonth(travelPlan.nowYear, travelPlan.nowMonth)
    print("\n", end = "")
    travelPlan.nowMonth += 1

##############################################################################
while True:

    departureDate = input("Enter your departure date(ex;2023.01.01): ")
    travel.Departure.depDateCalc(travelPlan, departureDate)

    if travelPlan.depYear < travelPlan.todayYear:
        print("Enter date after today.")

    elif travelPlan.depYear > travelPlan.todayYear:

        if travelPlan.depYear - travelPlan.todayYear >= 2:
            print("Enter the date within a year from today.")

        else:
            if travelPlan.depMonth > travelPlan.todayMonth:
                print("Enter the date within a year from today.")

            elif travelPlan.depMonth == travelPlan.todayMonth:

                if travelPlan.depDay > travelPlan.todayDay:
                    print("Enter the date within a year from today.")

                else:
                    break
            
            else:
                break

    else:

        if travelPlan.depMonth < travelPlan.todayMonth:
            print("Enter date after today.")

        elif travelPlan.depMonth > travelPlan.todayMonth:
            break

        else:
 
            if travelPlan.depDay <= travelPlan.todayDay:
                print("Enter date after today.")

            else:
                break

while True:

    arriveDate = input("Enter your come back date(ex:2023.01.07): ")
    travel.Arrival.arrDateCalc(travelPlan, arriveDate)

    if travelPlan.arrYear < travelPlan.depYear:
        print("Enter date after departure.")

    else: 

        if travelPlan.arrYear - travelPlan.todayYear >= 2:
            print("Enter the date within a year from today.")
        
        else:

            if travelPlan.arrYear == travelPlan.depYear:

                if travelPlan.arrMonth < travelPlan.depMonth:
                    print("Enter date after departure.")
                
                elif travelPlan.arrMonth > travelPlan.depMonth:
                    break

                else: 
                    if travelPlan.arrDay < travelPlan.depDay:
                        print("Enter date after departure.")
                    else:
                        break
            
            else:
                break
##############################################################################

travelPlan.letsGo(departureDate, arriveDate)

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://flight.naver.com/"
browser.get(url)

browser.find_elements(By.CLASS_NAME, 'select_name__1L61v')[1].click()
    
browser.find_element(By.CLASS_NAME, 'autocomplete_input__1vVkF').send_keys('{}'.format(travelPlan.destination))
time.sleep(1)
tmp = browser.find_elements(By.PARTIAL_LINK_TEXT, '{}'.format(travelPlan.destination))
tmp[0].click()

date = browser.find_elements(By.CLASS_NAME, 'tabContent_option__2y4c6')

depart = date[0]
depart.click()
time.sleep(1)

xpathAddress = '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[{}]/table/tbody/tr[{}]/td[{}]/button/b'

xpath_depart = xpathAddress.format(travelPlan.depMonthCode, travelPlan.depWeek, travelPlan.depDayofWeek)
browser.find_element(By.XPATH, xpath_depart).click()

arrive = date[1]
arrive.click()
time.sleep(1)

xpath_arrive = xpathAddress.format(travelPlan.arrMonthCode, travelPlan.arrWeek, travelPlan.arrDayofWeek)
browser.find_element(By.XPATH, xpath_arrive).click()

browser.find_element(By.CLASS_NAME, 'searchBox_search__2KFn3').click()
time.sleep(10)

waitCondition = WebDriverWait(browser, 90).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loadingProgress_loadingProgress__1LRJo'))) #로딩창이 없어질 때까지

result = browser.find_element(By.CLASS_NAME, 'concurrent_ConcurrentItemContainer__2lQVG')

print(result.text)
browser.close()