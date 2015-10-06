#Checks if the year is valid
#Params: year, The year to check
#Returns: True if year is greater than 0, False otherwise
def isYearValid(year):
    return (year >= 1)

#Checks if a month is valid
#Params: month, The month to check
#Returns: True if the month is between 1 and 12 inclusive
def isMonthValid(month):
    return (month >= 1) and (month <= 12)

#Checks if a year is a leap year
#Params: year, The year to check
#Returns: True if the year is a leap year, False otherwise
def isLeapYear(year):
    #Check if year is divisible by 4
    if (year % 4 == 0):
        #Check if the year is divisible by 4 and 100
        if (year % 100 == 0):
            #Check if the year is divisible by 4 and 100 and 400
            return (year % 400 == 0)
        else:
            #Return True if the year is divisible by 4 and 100
            return True
    else:
        #Return false if the year is not divisible by 4
        return False

#Checks if a date has or ever will exist
#Params: day, The day of the date
#        month, The month of the date
#        year, The year of the date
#Returns: True if the date is valid, False otherwise
def validate_date(day, month, year):
    if isYearValid(year) and isMonthValid(month):
        #Apr, Jun, Sep, Nov all have 30 days
        months_with_30_days = [4, 6, 9, 11]

        #Jan, Mar, May, Jul, Aug, Oct, Dec all have 31 days
        months_with_31_days = [1, 3, 5, 7, 8, 10, 12]

        #Check of the month has 30 or 31 days or neither
        if (month in months_with_30_days):
            #Month has 30 days
            #Check if the day is between 1 and 30, inclusive
            return (day > 0) and (day <= 30)
        elif (month in months_with_31_days):
            #Month has 31 days
            #Check if the day is between 1 and 30, inclusive
            return (day > 0) and (day <= 31)
        else:
            #Must be february, check if it's a leap year
            if isLeapYear(year):
                #Check if the day is between 1 and 29, inclusive
                return (day > 0) and (day <= 29)
            else:
                #Check if the day is between 1 and 28, inclusive
                return (day > 0) and (day <= 28)
    else:
        #Return False because the year or month is not valid
        return False



def main():
    print("1996, leap year:", isLeapYear(1996))
    print("400, leap year:", isLeapYear(400))
    print("100, leap year:", isLeapYear(100))
    print("4, leap year:", isLeapYear(4))
    print()
    print("29, 2, -1:", validate_date(29, 2, -1))
    print("29, 13, 1:", validate_date(29, 13, 1))
    print("29, -1, 1:", validate_date(29, -1, 1))
    print("29, 6, 1:", validate_date(29, 6, 1))
    print("31, 5, 2015:", validate_date(31, 5, 2015))
    print("28, 2, 2015:", validate_date(28, 2, 2015))
    print("29, 2, 2015:", validate_date(29, 2, 2015))
    print("29, 2, 1996", validate_date(29, 2, 1996))
    print("29, 2, 4:", validate_date(29, 2, 4))
    print("29, 2, 100:", validate_date(29, 2, 100))
    print("29, 2, 400:", validate_date(29, 2, 400))

main()
