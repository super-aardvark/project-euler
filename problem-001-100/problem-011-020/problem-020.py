'''
Created on Jan 10, 2017

@author: jfinn
'''
from math import factorial
from _functools import reduce
import operator

print(reduce(operator.add, map(int, list(str(factorial(100))))))
# Boy, Python sure makes this stuff easy_install
# ....though my IDE might be a little overzealous about code completion
