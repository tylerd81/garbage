import create_schedule
import datetime

def next_pickup_day(district):

    year = 2018   

    schedule = create_schedule.create_schedule(year)[district]

    today = datetime.date.today()
    
    #find the date closest to today
    
    schedule_index = 0
    found = False

    garbage_day = None

    while not found and schedule_index < len(schedule):
        pickup_day = schedule[schedule_index]
        month = pickup_day['month']
        day = pickup_day['day']    

        if month == today.month:
            if day >= today.day:
                garbage_day = pickup_day
                found = True
            else:
                #check if we are at the end of the month and garbage day is
                #next month
                #check if the next day is next month
                next_day = schedule[schedule_index + 1]
                if next_day['month'] == month + 1:
                    garbage_day = next_day
                    found = True

        schedule_index += 1

    #TODO: Account for the pickup day rolling over into the next year.

    if garbage_day:
        if today.day == garbage_day['day'] and today.month == garbage_day['month']:
            print('Your garbage pickup is TODAY!')
        else:
            print('Your next garbage pickup is: {}/{}'.format(
                garbage_day['month'],
                garbage_day['day']
            ))
    else:
        print('There is no garbage pickup.')

def prompt():
    menu = [
        'Woodlawn - Central Park',
        'Mont Pleasant - Hamilton Hill',
        'Mont Pleasant - Bellevue',
        'Downtown - Central Schenectady',
        'North Schenectady - Upper Union St.'
    ]

    option = 1
    for menu_item in menu:
        print('{}: {}'.format(option, menu_item))
        option += 1
    
    done = False

    while not done:
        try:
            c = int(input('> '))
            if c >= 1 and c <= len(menu):
                done = True
            else:
                print('Please enter a value from the menu')
        except:
            print('Please enter a value from the menu.')
    
    return c

if __name__ == '__main__':
    next_pickup_day(prompt() - 1)