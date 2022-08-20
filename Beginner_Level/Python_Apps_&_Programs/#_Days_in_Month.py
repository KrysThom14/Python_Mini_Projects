# This program will take a year and a month as inputs. It will use this
# information to work out the number of days in the month, then return that as
# the output. The list month_days contains the number of days in a month from
# January to December for a non-leap year. A leap year has 29 days in February.

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    if month > 12 or month < 1:
        return 'Invalid input.'
    regular_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    type_of_year = is_leap(year)
    if type_of_year == True:
        num_days = leap_year[month-1]
        return num_days
    elif type_of_year == False:
        num_days = regular_year[month-1]
        return num_days

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
