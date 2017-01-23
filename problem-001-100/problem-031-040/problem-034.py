'''
Created on Jan 22, 2017

@author: jfinn
'''
from _functools import reduce
import operator
import math

nums = []
sum = 0
for num in range(3, 2540160): # upper bound: 9!*7 < 9999999
    digits = map(int, str(num))
    fact_sum = reduce(operator.add, map(math.factorial, digits))
    if fact_sum == num:
        nums.append(num)
        sum += num

print(nums)
print(sum)