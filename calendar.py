#TODO: add a way to mark days with different symbols

import datetime

class Calendar():

    """Constructor"""
    def __init__(self, year):

        self.year = year
        self.current_date = datetime.date(self.year, 1, 1)
        self.marked_days = [None] * 12

        #number of days per month
        self.days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        #check if a leap year
        if self.is_leapyear(year):
            self.days_per_month[1] += 1

    """Testing method"""
    def dump(self):
        print('The year is: ' + str(self.year))

        for month in range(0,12):
            current_date = datetime.date(self.year, month + 1, 1)

            print(current_date.strftime('%B: ' + str(self.days_per_month[month])))

    """Calculate if the year is a leap year.
    Returns true if it is, false if not
    """
    def is_leapyear(self, year):        
        if (year % 4 == 0 or year % 400 == 0) and (year % 100 != 0):     
            return True
        else:
            return False

    def display_header(self):
        print(self.current_date.strftime('%B'.center(13)))
        print('S  M  T  W  T  F  S')

    def display_calendar(self):
        
        starting_day = self.current_date.weekday()       
        
        current_marked_days = self.marked_days[self.current_date.month - 1]
        marked_days_index = 0

        self.display_header()

        #print the correct number of spaces to start the day on the correct day
        num_spaces = 3
        
        if starting_day != 6: #6 is sunday
            for i in range(0, starting_day + 1):
                print(' ' * num_spaces, end='')

        num_days = self.days_per_month[self.current_date.month - 1]

        #Days go from 0 - 6 with monday == 0 and sunday == 6
        #So getting the days to line up as Sunday - Saturday like a regular calendar
        #takes some checking.

        for current_day in range(1, num_days + 1):
            
            if (current_marked_days != None and 
                marked_days_index < len(current_marked_days) and
                current_marked_days[marked_days_index] == current_day):
                print('*  ', end='')
                marked_days_index += 1
            else:
                print('%-2d ' % current_day, end='')

            starting_day += 1

            if starting_day == 6:
                print('')                
            elif starting_day > 6:
                starting_day = 0

        print('\n')

    """set_month() sets the month to val, 1 - 12
    It creates a new date object and sets it to self.current_date
    The month will default to 1 if an invalid number is passed
    """
    def set_month(self, val):
        if val < 1 or val > 12:
            val = 1

        self.current_date = self.current_date.replace(month=val)


    """mark_days() adds to the list of marked days on the calendar.
    marked_days is a list of list items like this:
    
    [[13,23], [12,29]]
    
    Each index is a month and then the list will be the days to mark
    The list should be sorted

    The months will be from 1 - 12 since that is what datetime works with but the
    list index will be from 0 - 11

    Any days that are already marked for the month will be overwritten
    days_to_mark is a list of days
    """

    #maybe make a new class to hold the holidays...
    
    def mark_days(self, month, days_to_mark):
        
        if month < 1 or month > 12:
            return
        
        self.marked_days.insert(month - 1, days_to_mark) 
        
