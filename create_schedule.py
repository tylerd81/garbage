import datetime
import holiday_list

NUMBER_OF_DISTRICTS = 5

def create_schedule():
    
    year = 2018
    districts = []
    current_date = datetime.date(year, 1,1)
    next_day = datetime.timedelta(days=1)
    current_district = 0

    #just add the correct holidays
    holidays = holiday_list.HolidayList()
    holidays.add_holiday(1,15)
    holidays.add_holiday(1,1)

    # skip sat and sun

    while current_date.month < 4 :
        #make sure it's not saturday, sunday, or a holiday       
        if ( current_date.weekday() != 5 and current_date.weekday() != 6 and
             not holidays.is_holiday(current_date.month, current_date.day)):

            # the dict is the form {district, month, day}
            districts.append({'district':current_district, 'month' : current_date.month, 'day' : current_date.day})

            #switch to the next district
            if(current_district == NUMBER_OF_DISTRICTS - 1):
                current_district = 0
            else:
                current_district += 1
        
        # goto the next day
        current_date = current_date + next_day


    # use the district key to filter dates for a specific district
    for date in districts:
        if date['district'] == 1:
            print(date)


if __name__ == "__main__":
    create_schedule()

