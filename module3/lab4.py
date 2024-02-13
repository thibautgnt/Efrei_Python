"""
Due to astronomical reasons, years may be leap (366 days) or common (365 days). Since the introduction of the Gregorian calendar (in 1582), the following rules is used to determine the kind of year:

Leap year is every year that is evenly divisible by 4

except every it is evenly divisible by 100
unless the year is also evenly divisible by 400
The code reads a year number, and needs to be completed to output one of the 3 messages :
Leap year | Common year | Not within the Gregorian calendar

Hint : use the != and % operators.
"""

year = int(input("Enter a year: "))
if year < 1582:
    print("Not within the Gregorian calendar")
else:
    if year % 4 != 0:
        print("Common year")
    elif year % 100 != 0:
        print("Leap year")
    elif year % 400 != 0:
        print("Common year")
    else:
        print("Leap year")
    