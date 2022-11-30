"""
import calendar
import datetime
from datetime import date

nowYear = input("What Year now?: ")
nowMonth = input("What Month now?: ")

print("\nChoose your travel date.\n")
year = int(nowYear)
month = int(nowMonth)

for i in range(13):
    if month > 12:
        year += 1
        month = month - 12
    
    calendar.prmonth(year, month)
    print("\n", end = "")
    month += 1

travelDate = input("Enter your travel date(ex:2023.01.01): ")

depYear = travelDate[:4]
depMonth = travelDate[5:7]
depDay = travelDate[8:]

print(depYear, depMonth, depDay)"""
"""
import calendar
from datetime import datetime

def ymd_to_datetime(y, m, d): # 3

    s = f'{y:04d}-{m:02d}-{d:02d}'
    return datetime.strptime(s, '%Y-%m-%d')

week = {}

def weekCalc(y, m, d):

    target_day = f'{y:04d}-{m:02d}-{d:02d}'
    target_day = datetime.strptime(target_day, '%Y-%m-%d')

    lastDay = calendar.monthrange(y, m)[1]

    weekNo = 1
    tmpList = []

    for i in range(1, lastDay):

        dayofWeek = target_day.replace(day = i).weekday()
        tmpList.append(i)

        if dayofWeek == 5:
            week[weekNo] = tmpList
            weekNo += 1
            tmpList = []
            continue
    
    for weekKey in week:

        weekValue = week.get(weekKey)

        for i in range(len(weekValue)):

            if weekValue[i] == d:
                return weekKey
            else:
                continue

print(weekCalc(2022,12,15))
import calendar
a = calendar.weekday(2022, 12, 14)
print(a)
print(type(a))

import travel

travelPlan = travel.Travel("2022.11.28", "JFK")
travelPlan.todayCalc()

while True:

    departureDate = input()
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
print(departureDate)

while True:


    arriveDate = input()
    travel.Arrival.arrDateCalc(travelPlan, arriveDate)


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

print(arriveDate, "ok")"""

import matplotlib.pyplot as plt

plt.plot([1,2,3,4],[1,3,2,5])
plt.show()
