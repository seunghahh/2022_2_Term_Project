import calendar

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

print(depYear, depMonth, depDay)