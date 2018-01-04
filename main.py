import sys
import calendar

def main(year):
    cal = calendar.Calendar(year)
    cal.mark_days(1, [13,21])
    cal.mark_days(2, [1,28])
    cal.set_month(1)
    cal.display_calendar()

    cal.set_month(2)
    cal.display_calendar()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        year = int(sys.argv[1])
    else:
        year = 2018

    main(year)

