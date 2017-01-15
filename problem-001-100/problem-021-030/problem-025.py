'''
Created on Jan 14, 2017

@author: jfinn
'''
from math import log

first = 1
second = 1
i = 2
digits = 1
while True:
    new = first + second
    i += 1
    new_digits = int(log(new, 10)) + 1
    if new_digits > digits:
        digits = new_digits
        print("first {0}-digit Fibonacci number has index {1}".format(digits, i))
        if digits >= 1000:
            break
    first = second
    second = new
    