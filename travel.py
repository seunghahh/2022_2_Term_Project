class Travel:

    def __init__(self, nowYear, nowMonth, destination):
        
        self.nowYear = nowYear
        self.nowMonth = nowMonth
        self.destination = destination

        """self.destination = destination
        self.depMonth = depMonth
        self.depWeek = depWeek
        self.depDay = depDay
        self.arrMonth = arrMonth
        self.arrWeek = arrWeek
        self.arrDay = arrDay"""

    """
    def inputTravel(self):
        self.destination = input("Enter your destination: ")
        self.nowMonth = input("What month now?: ")
        self.depMonth = input("What month do you want to leave?: ")
        self.depWeek = input("What week do you want to leave?: ")
        self.depDay = input("What day of the week do you want to leave?: ")
        self.arriveMonth = input("What month do you want to come back?: ")
        self.arriveWeek = input("What week do you want to come back?: ")
        self.arriveDay = input("What day of the week do you want to come back?: ")"""


    def depDateCalc(self, depDate):
        self.depYear = depDate[:4]
        self.depMonth = depDate[5:7]
        self.depDay = depDate[8:]

    def arrDateCalc(self, arrDate):
        self.arrMonth = 1
        self.arrWeek = 1
        self.arrDay = 1

    def monthCalc(self):

        tmpValue = int(self.depMonth) - int(self.nowMonth)

        if tmpValue < 0:
            tmpValue = tmpValue + 12

        return str(tmpValue + 2)

    def dayCalc(self):
        dayOfWeek = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
        for i in range(len(dayOfWeek)):
            if dayOfWeek[i] == self.depDay:
                return i+1
            else:
                continue

    


#str(int(depMonth) - int(nowMonth) + 2)


"""destination = input("Enter your destination: ")
nowMonth = input("What month now?: ")
depMonth = input("What month do you want to leave?: ")
depWeek = input("What week do you want to leave?: ")
depDay = input("What day of the week do you want to leave?: ")
arriveMonth = input("What month do you want to come back?: ")
arriveWeek = input("What week do you want to come back?: ")
arriveDay = input("What day of the week do you want to come back?: ")"""