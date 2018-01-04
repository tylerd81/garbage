
import datetime

class Calendar():

    def __init__(self, year):

        self.year = year

        #number of days per month
        self.days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        #check if a leap year
        if self.is_leapyear(year):
            self.days_per_month[1] + 1

        for month in range(0,12):
            current_date = datetime.date(year,month + 1, 1)

            print(current_date.strftime("%B: " + str(self.days_per_month[month])))

    def is_leapyear(self, year):        
        if (year % 4 == 0 or year % 400 == 0) and (year % 100 != 0):     
            return True
        else:
            return False
    


