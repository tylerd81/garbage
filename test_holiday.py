import holiday_list

def run():
    hol_list = holiday_list.HolidayList()

    hol_list.add_holiday(4,21)
    hol_list.dump_holidays()

    day = hol_list.is_holiday(4,21)

    print(day)
    print('done')

if __name__ == '__main__':
    run()