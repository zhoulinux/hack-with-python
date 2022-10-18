'''
http://www.pythonchallenge.com/pc/return/cat.html

There's a burnt hole on the calendar, it must be year 1xx6.
That year's Jan 26 is a Monday.
It was a leap year, since Feb 29 is on the calendar.
<!-- he ain't the youngest, he is the second -->
Title: whom?
<!-- todo: buy flowers for tomorrow -->
1756-01-27 is the birthday of Mozart

http://www.pythonchallenge.com/pc/return/mozart.html
'''


import datetime
import calendar


count = 0
for year in range(1996, 996, -10):
    if calendar.isleap(year):
        day = datetime.date(year, 1, 26)
        if day.weekday() == 0:
            count += 1
            if count == 2:
                print(day)
                break
