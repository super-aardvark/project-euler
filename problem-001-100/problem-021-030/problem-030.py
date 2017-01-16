'''
Created on Jan 15, 2017

@author: jfinn
'''
from _functools import reduce
import operator

def is_sum_of_digit_fifth_powers(num):
    return num == reduce(operator.add, [int(x)**5 for x in str(num)])

# 7*9**5 < 1000000, so these numbers can have at most 6 digits
all_sums = [x for x in range(2,1000000) if is_sum_of_digit_fifth_powers(x)]
print(all_sums)
print(reduce(operator.add, all_sums))