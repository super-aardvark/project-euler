'''
Created on Jan 11, 2017

@author: jfinn
'''
from _functools import reduce
import operator
import math
from helpers import get_proper_divisors

def d(num):
    return reduce(operator.add, get_proper_divisors(num))

amicable = []
for num in range(3,10000):
    if num in amicable:
        continue
    d_num = d(num)
    if d_num != num and d(d_num) == num:
        amicable.append(num)
        amicable.append(d_num)
        
print(amicable)
print(reduce(operator.add, amicable))