'''
Created on Jan 10, 2017

@author: jfinn
'''
from _functools import reduce
import operator

# Storing the lengths instead of the strings here would save us a bunch of memory, but this might be useful later on

ones = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
teens = {0: "ten", 1: "eleven", 2: "twelve", 3: "thirteen", 4: "fourteen", 5: "fifteen", 6: "sixteen", 7: "seventeen", 8: "eighteen", 9: "nineteen"}
tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

def spell_out(num):
    spelling = ""
    digits = list(map(int, list(str(num))))
    digits.reverse()
    if num > 999:
        spelling += ones[digits[3]] + "thousand"
    if num > 99 and digits[2] > 0:
        spelling += ones[digits[2]] + "hundred"
        if digits[1] > 0 or digits[0] > 0:
            spelling += "and"
    if num > 9 and digits[1] == 1:
        spelling += teens[digits[0]]
    else:
        if num > 9 and digits[1] > 0:
            spelling += tens[digits[1]]
        if digits[0] > 0:
            spelling += ones[digits[0]]
    return spelling 
        
total_length = reduce(operator.add, map(len, map(spell_out, range(1,1001))))
print(total_length)
