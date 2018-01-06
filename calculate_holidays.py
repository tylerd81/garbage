"""Federal Holidays:
    1/1 New Year's Day
    MLK Day - 3rd Monday in January
    Presidents Day - 3rd Monday in February
    Memorial Day - Last Monday in May
    Independence Day - July 4
    Labor Day - First Monday in September
    Columbus Day - Second Monday in October
    Veterans Day - November 11
    Thanksgiving - Fourth Thursday in November
    Christmas - December 25
"""

import datetime

def calc_mlk_day(year):

    # MLK Day is 3rd Monday in January

    jan = datetime.date(year, 1, 1)
    next_day = datetime.timedelta(days=1)

    #find the first Monday
    while jan.weekday() != 0: # 0 is Monday
        jan = jan + next_day

    #jan.weekday() == 1st Monday of January
    #add 14 more days to get the third Monday
    mlk_day = jan + datetime.timedelta(days=14)
    return mlk_day    
    
def calc_presidents_day(year):
    
    #Presidents day is the third monday in February
    feb = datetime.date(year, 2, 1)
    next_day = datetime.timedelta(days=1)

    #find the first Monday
    while feb.weekday() != 0: # 0 is Monday
        feb = feb + next_day

    #jan.weekday() == 1st Monday of January
    #add 14 more days to get the third Monday
    pres_day = feb + datetime.timedelta(days=14)    
    return pres_day

def calc_memorial_day(year):
    
    #last Monday in May
    memorial_day = datetime.date(year, 5, 1)

    #find the first Monday
    while memorial_day.weekday() != 0:
        memorial_day = memorial_day + datetime.timedelta(days=1)
    
    done = False

    while not done:
        next_mon = memorial_day + datetime.timedelta(days=7)

        if next_mon.month == 5:
            #still in may, check next monday
            memorial_day = next_mon
        else:
            done = True

    #memorial_day will always be pointing to the last Monday we checked
    return memorial_day

def calc_labor_day(year):
    #Labor Day is the first Monday in September

    labor_day = datetime.date(year, 9, 1)

    while labor_day.weekday() != 0:
        labor_day = labor_day + datetime.timedelta(days=1)

    print('Labor Day is: {}/{}/{}'.format(
        labor_day.month,
        labor_day.day,
        labor_day.year
    ))

    return labor_day

def calc_columbus_day(year):
    
    #Columbus day is the second Monday in October

    #Days go from 0 - 6
    #Day 0 is Monday
    #0 + 7 will loop back to 0 which is Monday
    # if the day is day 2 we are already 2 days ahead in the week
    # so we need to move 5 more days to get back to Monday
    # 7 - 2 = 5
    # add 7 more to get to the Monday after that

    columbus_day = datetime.date(year,10,1)
    if columbus_day.weekday() != 0:
        num_days = (7 - columbus_day.weekday()) + 7
    else:
        #first day of October is a Monday, so just go to the next Monday
        num_days = 7

    columbus_day = columbus_day + datetime.timedelta(days=num_days)
    return columbus_day

def calc_thanksgiving(year):
    #4th Thursday of November

    thanks = datetime.date(year, 11, 1)

    weekday = thanks.weekday()
    
    while thanks.weekday() != 3:
        thanks = thanks  + datetime.timedelta(days=1)

    thanks = thanks + datetime.timedelta(days=21) # 21 days == jumps 3 Thurs. ahead
   
    print('Thanksgiving is {}/{}/{}'.format(
        thanks.month,
        thanks.day,
        thanks.year
    ))

    return thanks

if __name__ == '__main__':
    year = 2018
    calc_mlk_day(year)
    calc_presidents_day(year)
    calc_memorial_day(year)
    calc_labor_day(year)
    calc_columbus_day(year)
    calc_thanksgiving(year)