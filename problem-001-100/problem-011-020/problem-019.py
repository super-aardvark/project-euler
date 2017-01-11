'''
Created on Jan 10, 2017

@author: jfinn
'''

# No sense reinventing the wheel
import calendar

sum = 0
for year in range(1901, 2001):
    for month in range(12):
       if calendar.weekday(year, month + 1, 1) == 6:
           sum += 1

print(sum) 