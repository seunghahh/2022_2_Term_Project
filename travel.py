import calendar
from datetime import datetime

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