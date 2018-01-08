import datetime
import holiday_list
import calculate_holidays as ch
import calendar

NUMBER_OF_DISTRICTS = 5

"""
create_schedule() creates a Garbage Pickup Schedule.

The variable schedule is returned which is a list of lists. Each list item
contains the dates throughout the year that garbage will be picked up. It is a list
of dict objects of the form {month, year}

So it is [ [district_0], [district_1], [district_2], ...]

Each district element is a list of dict items.

The scheduler tries to schedule each district for pickup once every seven days. It
takes into account all holidays and weekends. There is no garbage pickup on weekends.
There is no garbage pickup on holidays. When there is a holiday the entire schedule is
shifted ahead one day.
"""

def create_schedule(year):
       
    schedule = [None] * 5

    current_date = datetime.date(year, 1,1)
    next_day = datetime.timedelta(days=1)
    current_district = 0

    #just add the correct holidays
    holidays = holiday_list.HolidayList()
    calculate_holidays(year, holidays)

    # skip sat and sun

    while current_date.year == year :
    
        #make sure it's not saturday, sunday, or a holiday       
        if ( current_date.weekday() != 5 and current_date.weekday() != 6 and
             not holidays.is_holiday(current_date.month, current_date.day)):

            # the dict is the form {district, month, day}
            if schedule[current_district] == None:
                schedule[current_district] = []
            schedule[current_district].append({'month' : current_date.month, 'day' : current_date.day})

            # schedule.append({'district':current_district, 'month' : current_date.month, 'day' : current_date.day})

            #switch to the next district
            if(current_district == NUMBER_OF_DISTRICTS - 1):
                current_district = 0
            else:
                current_district += 1
        
        # goto the next day
        current_date = current_date + next_day

    return schedule
    # use the district key to filter dates for a specific district
    # for date in districts:
    #     if date['district'] == 2:
    #         print(date)

def write_schedule(schedule, filename):
    district_num = 1

    with open(filename, 'w') as file:
        for district in schedule:    
            #write the header
            file.write('District {}'.format(district_num).center(30) + '\n')    

            for pickup_day in district:
                file.write('{}/{}\n'.format(pickup_day['month'], pickup_day['day']))            
            district_num += 1
            
# def display_garbage_schedule(schedule, district_number):
def display_garbage_schedule(schedule, district_number):
    
    print('Garbage Schedule For District {}'.format(district_number))

    for day in schedule:        
        print('{}/{}'.format(day['month'], day['day']))


def calculate_holidays(year, holidays):
    
    #easy ones
    holidays.add_holiday({'month' : 1,'day': 1}) # New Years
    holidays.add_holiday({'month': 7, 'day': 4}) # Fourth of July
    holidays.add_holiday({'month' : 12, 'day': 25}) # X-mas

    holidays.add_holiday(ch.to_cal_format(ch.calc_mlk_day(year)))
    holidays.add_holiday(ch.to_cal_format(ch.calc_presidents_day(year)))
    holidays.add_holiday(ch.to_cal_format(ch.calc_memorial_day(year)))
    holidays.add_holiday(ch.to_cal_format(ch.calc_labor_day(year)))
    holidays.add_holiday(ch.to_cal_format(ch.calc_columbus_day(year)))

    #thanksgiving day and the day after
    thanks = ch.calc_thanksgiving(year)
    thanks_day_after = thanks + datetime.timedelta(days=1)

    holidays.add_holiday(ch.to_cal_format(thanks))
    holidays.add_holiday(ch.to_cal_format(thanks_day_after))

    holidays.add_holiday(ch.to_cal_format(ch.calc_election_day(year)))
    holidays.add_holiday(ch.to_cal_format(ch.calc_veterans_day(year)))


if __name__ == "__main__":
    schedule = create_schedule(2018)
    filename = 'schedule.txt'

    print('Writing {}...'.format(filename))

    write_schedule(schedule, filename)

    print('Done.')
    # display_garbage_schedule(schedule[2], 3)


