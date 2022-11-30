import calendar
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Travel:

    def __init__(self, today, destination):

        self.today = today
        self.destination = destination
        self.weekDict = {}

    def todayCalc(self):

        self.todayYear = int(self.today[:4])
        self.todayMonth = int(self.today[5:7])
        self.nowYear = self.todayYear
        self.nowMonth = self.todayMonth
        self.todayDay = int(self.today[8:])

    def letsGo(self, departureDate, arriveDate):

        Departure.depDateCalc(self, departureDate)
        Arrival.arrDateCalc(self, arriveDate)

        Departure.depWeekCalc(self, self.depYear, self.depMonth, self.depDay)
        Arrival.arrWeekCalc(self, self.arrYear, self.arrMonth, self.arrDay)

        Departure.depMonthCalc(self)
        Arrival.arrMonthCalc(self)

        Departure.depDayofWeekCalc(self)
        Arrival.arrDayofWeekCalc(self)


class Departure(Travel):

    def __init__(self, nowYear, nowMonth, destination):

        super().__init__(nowYear, nowMonth, destination)

    def depDateCalc(self, depDate):

        self.depYear = int(depDate[:4])
        self.depMonth = int(depDate[5:7])
        self.depDay = int(depDate[8:])

    def depWeekCalc(self, year, month, day):

        inputDate = f'{year:04d}-{month:02d}-{day:02d}'
        inputDate = datetime.strptime(inputDate, '%Y-%m-%d')

        lastDay = calendar.monthrange(year, month)[1]

        weekNo = 1
        tmpList = []

        for i in range(1, lastDay+1):
            dayofWeek = inputDate.replace(day = i).weekday()
            tmpList.append(i)

            if i == lastDay:
                self.weekDict[weekNo] = tmpList
                break

            if dayofWeek == 5:
                self.weekDict[weekNo] = tmpList
                weekNo += 1
                tmpList = []
                continue

        for weekKey in self.weekDict:
            weekValue = self.weekDict.get(weekKey)

            for i in range(len(weekValue)):

                if weekValue[i] == day:
                    self.depWeek = str(weekKey)
                    break

                else:
                    continue

    def depMonthCalc(self):

        tmpValue = self.depMonth - self.todayMonth

        if tmpValue < 0:
            tmpValue = tmpValue + 12

        self.depMonthCode = str(tmpValue + 2)   

    def depDayofWeekCalc(self):

        tmpDay = calendar.weekday(self.depYear, self.depMonth, self.depDay)
        
        if tmpDay == 6:
            self.depDayofWeek = '1'

        else:
            self.depDayofWeek = str(tmpDay + 2)

class Arrival(Travel):

    def __init__(self, nowYear, nowMonth, destination):

        super().__init__(nowYear, nowMonth, destination)

    def arrDateCalc(self, arrDate):

        self.arrYear = int(arrDate[:4])
        self.arrMonth = int(arrDate[5:7])
        self.arrDay = int(arrDate[8:])

    def arrWeekCalc(self, year, month, day):

        inputDate = f'{year:04d}-{month:02d}-{day:02d}'
        inputDate = datetime.strptime(inputDate, '%Y-%m-%d')

        lastDay = calendar.monthrange(year, month)[1]

        weekNo = 1
        tmpList = []

        for i in range(1, lastDay+1):
            dayofWeek = inputDate.replace(day = i).weekday()
            tmpList.append(i)

            if i == lastDay:
                self.weekDict[weekNo] = tmpList
                break

            if dayofWeek == 5:
                self.weekDict[weekNo] = tmpList
                weekNo += 1
                tmpList = []
                continue

        for weekKey in self.weekDict:
            weekValue = self.weekDict.get(weekKey)

            for i in range(len(weekValue)):

                if weekValue[i] == day:
                    self.arrWeek = str(weekKey)
                    break

                else:
                    continue

    def arrMonthCalc(self):

        tmpValue = self.arrMonth - self.todayMonth

        if tmpValue < 0:
            tmpValue = tmpValue + 12

        self.arrMonthCode = str(tmpValue + 2)                 

    def arrDayofWeekCalc(self):

        tmpDay = calendar.weekday(self.arrYear, self.arrMonth, self.arrDay)

        if tmpDay == 6:
            self.arrDayofWeek = '1'

        else:
            self.arrDayofWeek = str(tmpDay + 2)

today = input("Enter today date(ex:2022.12.25): ")
destination = input("Enter your destination(ex.New York->JFK): ")

travelPlan = Travel(today, destination)
travelPlan.todayCalc()

print("\nChoose your travel date.\n")

for i in range(13):
    if travelPlan.nowMonth > 12:
        travelPlan.nowYear += 1
        travelPlan.nowMonth = travelPlan.nowMonth - 12
    
    calendar.prmonth(travelPlan.nowYear, travelPlan.nowMonth)
    print("\n", end = "")
    travelPlan.nowMonth += 1

############################ 입력한 여행 날짜가 site에 입력 가능한 날짜인지 판별 ############################

while True:

    departureDate = input("Enter your departure date(ex:2023.01.01): ")
    Departure.depDateCalc(travelPlan, departureDate)

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


    arriveDate = input()
    Arrival.arrDateCalc(travelPlan, arriveDate)


    if travelPlan.arrYear < travelPlan.depYear:
        print("Enter date after departure.")

    else: #arrYear >= depYear

        if travelPlan.arrYear - travelPlan.todayYear >= 2:
            print("Enter the date within a year from today.")
        
        else: #arrYear - depYear = 1 or arrYear = depYear

            if travelPlan.arrYear == travelPlan.depYear:

                if travelPlan.depYear == travelPlan.todayYear:

                    if travelPlan.arrMonth < travelPlan.depMonth:
                        print("Enter date after departure.")
                    
                    elif travelPlan.arrMonth == travelPlan.depMonth:

                        if travelPlan.arrDay < travelPlan.depDay:
                            print("Enter date after departure.")
                        
                        else:
                            break

                    else:
                        break

                else: #depYear > todayYear
                    
                    if travelPlan.arrMonth > travelPlan.todayMonth:
                         print("Enter the date within a year from today.")

                    else:
                        if travelPlan.arrMonth < travelPlan.depMonth:
                            print("Enter date after departure.")

                        elif travelPlan.arrMonth == travelPlan.depMonth:

                            if travelPlan.arrDay < travelPlan.depDay:
                                print("Enter date after departure.")

                            else:
                                if travelPlan.arrDay > travelPlan.todayDay:
                                    print("Enter the date within a year from today.")
                                else:
                                    break

                        else: # arrMonth > depMonth
                            if travelPlan.arrDay > travelPlan.todayDay:
                                print("Enter the date within a year from today.")

                            else:
                                break

            else: # arrYear - depYear = 1
                if travelPlan.arrMonth > travelPlan.todayMonth:
                    print("Enter the date within a year from today.")

                elif travelPlan.arrMonth == travelPlan.todayMonth:
                    if travelPlan.arrDay > travelPlan.todayDay:
                        print("Enter the date within a year from today.")
                    
                    else:
                        break
                
                else:
                    break

##################################################################################################

print("\n")
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