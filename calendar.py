
class Calendar():

    def is_leapyear(self, year):
        
        if year % 4 == 0 and year % 400 == 0:
            if year % 100 == 0:
                return False
            else:
                return True

