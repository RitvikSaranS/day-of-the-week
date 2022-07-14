def century_code(year):
    century_part = int(year/100)
    match century_part%4:
        case 0:
            return 6
        case 1:
            return 4
        case 2:
            return 2
        case 3:
            return 0
        case _:
            return 6

def is_leap(year):
    leap = False
    if year%400 == 0:
        leap = True
    elif not(year%100 == 0) and year%4 == 0:
        leap = True
    return leap

def month_code(month, year):
    match month:
        case "january" | "october":
            if is_leap(year) and month == "january":
                return 6
            else:
                return 0
        case "may":
            return 1
        case "august":
            return 2
        case "february" | "march" | "november":
            if is_leap(year) and month == "february":
                return 2
            else:
                return 3
        case "june":
            return 4
        case "september" | "december":
            return 5
        case "april" | "july":
            return 6

def year_code(year):
    year_part = year%100
    return (year_part + int(year_part/4))%7

def test_date(year, month, day):
    is_valid = False
    if int(day) == day and int(year) == year and str(month) == month:
        if month in ["april", "june", "september", "november"] and day<=30:
            is_valid = True
        elif month in ["january", "march", "may", "july", "august", "october", "december"] and day<=31:
            is_valid = True
        elif month == "february" and (((is_leap(year) and day<=29)) or day<=28):
            is_valid = True
    return is_valid

year = int(input("Enter the year : "))
month = (input("Enter the month : ")).lower()
day = int(input("Enter the day : "))

if test_date(year, month, day):
    day_code = (century_code(year) + year_code(year) + month_code(month, year) + day)%7
    match day_code:
        case 0:                                                       
            print("Sunday")
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
else:
    print("The date does not exists")

