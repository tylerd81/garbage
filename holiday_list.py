class HolidayList():

    def __init__(self):        
        # the list of lists that will hold the holidays
        self.holidays = [None] * 12

    def add_holiday(self, holiday_dict, symbol='*'):               
        day = holiday_dict['day']
        month = holiday_dict['month']
        
        if month < 1 or month > 12:
            return  # invalid month

        #check if we already added something to this month
        #month index goes from 0 - 11

        month_index = month - 1

        if self.holidays[month_index] == None:
            self.holidays[month_index] = []

        self.holidays[month_index].append({'month' : month, 'day' : day, 'symbol':symbol})

    def is_holiday(self, month, day):        
        if month < 1 or month > 12:
            return None

        if self.holidays[month - 1]:            
            holiday_list = self.holidays[month - 1] # list of holidays for this month
                       
            for holiday_item in holiday_list:                               
                if holiday_item['day'] == day:
                    return True        

        return False # the day was not a holiday
        
    def get_symbol(self, month, day):
        if month < 1 or month > 12:
            return None

        if self.holidays[month - 1]:            
            holiday_list = self.holidays[month - 1] # list of holidays for this month
                       
            for holiday_item in holiday_list:                               
                if holiday_item['day'] == day:
                    return holiday_item['symbol']        

        return None # the day was not a holiday

    
    def dump_holidays(self):
        for month_list in self.holidays:
            if month_list:
                for holiday in month_list:
                    self.display_holiday(holiday)

    def display_holiday(self, holiday):
        print('Month: {}, Day: {}, Symbol: {}'.format(holiday['month'], holiday['day'], holiday['symbol']))
