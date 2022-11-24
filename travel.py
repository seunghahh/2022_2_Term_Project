import calendar
from datetime import datetime

class Travel:

    def __init__(self, nowYear, nowMonth, destination):
        
        self.nowYear = nowYear
        self.nowMonth = nowMonth
        self.destination = destination
        self.week = {}
"""
    def depDateCalc(self, depDate):
        self.depYear = int(depDate[:4])
        self.depMonth = int(depDate[5:7])
        self.depDay = int(depDate[8:])

    def arrDateCalc(self, arrDate):
        self.arrYear = int(arrDate[:4])
        self.arrMonth = int(arrDate[5:7])
        self.arrDay = int(arrDate[8:])

    def depWeekCalc(self, year, month, day):

        inputDate = f'{year:04d}-{month:02d}-{day:02d}'
        inputDate = datetime.strptime(inputDate, '%Y-%m-%d')

        lastDay = calendar.monthrange(year, month)[1]

        weekNo = 1
        tmpList = []

        for i in range(1, lastDay):

            dayofWeek = inputDate.replace(day = i).weekday()
            tmpList.append(i)

            if dayofWeek == 5:
                self.week[weekNo] = tmpList
                weekNo += 1
                tmpList = []
                continue

        for weekKey in self.week:

            weekValue = self.week.get(weekKey)

            for i in range(len(weekValue)):

                if weekValue[i] == day:
                    self.depWeek = str(weekKey)
                else:
                    continue

    def arrWeekCalc(self, year, month, day):

        inputDate = f'{year:04d}-{month:02d}-{day:02d}'
        inputDate = datetime.strptime(inputDate, '%Y-%m-%d')

        lastDay = calendar.monthrange(year, month)[1]

        weekNo = 1
        tmpList = []

        for i in range(1, lastDay):

            dayofWeek = inputDate.replace(day = i).weekday()
            tmpList.append(i)

            if dayofWeek == 5:
                self.week[weekNo] = tmpList
                weekNo += 1
                tmpList = []
                continue

        for weekKey in self.week:

            weekValue = self.week.get(weekKey)

            for i in range(len(weekValue)):

                if weekValue[i] == day:
                    self.arrWeek = str(weekKey)
                else:
                    continue

    def depMonthCalc(self):

        tmpValue = self.depMonth - self.nowMonth

        if tmpValue < 0:
            tmpValue = tmpValue + 12

        self.depMonthCode = str(tmpValue + 2)

    def arrMonthCalc(self):

        tmpValue = self.arrMonth - self.nowMonth

        if tmpValue < 0:
            tmpValue = tmpValue + 12

        self.arrMonthCode = str(tmpValue + 2)

    def depDayofWeekCalc(self):
        tmpDay = calendar.weekday(self.depYear, self.depMonth, self.depDay)
        if tmpDay == 6:
            self.depDayofWeek = '1'
        else:
            self.depDayofWeek = str(tmpDay + 2)

    def arrDayofWeekCalc(self):
        tmpDay = calendar.weekday(self.arrYear, self.arrMonth, self.arrDay)
        if tmpDay == 6:
            self.arrDayofWeek = '1'
        else:
            self.arrDayofWeek = str(tmpDay + 2)"""

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

        for i in range(1, lastDay):

            dayofWeek = inputDate.replace(day = i).weekday()
            tmpList.append(i)

            if dayofWeek == 5:
                self.week[weekNo] = tmpList
                weekNo += 1
                tmpList = []
                continue

        for weekKey in self.week:

            weekValue = self.week.get(weekKey)

            for i in range(len(weekValue)):

                if weekValue[i] == day:
                    self.depWeek = str(weekKey)
                else:
                    continue

    def depMonthCalc(self):

        tmpValue = self.depMonth - self.nowMonth

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

        for i in range(1, lastDay):

            dayofWeek = inputDate.replace(day = i).weekday()
            tmpList.append(i)

            if dayofWeek == 5:
                self.week[weekNo] = tmpList
                weekNo += 1
                tmpList = []
                continue

        for weekKey in self.week:

            weekValue = self.week.get(weekKey)

            for i in range(len(weekValue)):

                if weekValue[i] == day:
                    self.arrWeek = str(weekKey)
                else:
                    continue

    def arrMonthCalc(self):

        tmpValue = self.arrMonth - self.nowMonth

        if tmpValue < 0:
            tmpValue = tmpValue + 12

        self.arrMonthCode = str(tmpValue + 2)                 

    def arrDayofWeekCalc(self):

        tmpDay = calendar.weekday(self.arrYear, self.arrMonth, self.arrDay)

        if tmpDay == 6:
            self.arrDayofWeek = '1'
        else:
            self.arrDayofWeek = str(tmpDay + 2)