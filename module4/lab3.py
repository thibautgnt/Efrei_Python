def isYearLeap(year):
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

def daysInMonth(year, month):
    if month == 2:
        if isYearLeap(year):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def dayOfYear(year, month, day):
    if not isYearLeap(year) and month == 2 and day == 29:
        return None
    elif month < 1 or month > 12 or day < 1 or day > daysInMonth(year, month):
        return None
    else:
        total_days = 0
        for m in range(1, month):
            total_days += daysInMonth(year, m)
        total_days += day
        return total_days

print(dayOfYear(2000, 12, 31))