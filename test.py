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

print(weekCalc(2022,12,15))"""
import calendar
a = calendar.weekday(2022, 12, 14)
print(a)
print(type(a))