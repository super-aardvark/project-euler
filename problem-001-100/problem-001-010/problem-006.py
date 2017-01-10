'''
Created on Jan 9, 2017

@author: jfinn
'''
from _functools import reduce
import operator

def sum_of_squares(list):
    return reduce(operator.add, map(lambda x: x**2, list))

def square_of_sum(list):
    return reduce(operator.add, list)**2

list = range(1,101)
difference = square_of_sum(list) - sum_of_squares(list)
print(difference)