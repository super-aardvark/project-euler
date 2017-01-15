'''
Created on Jan 14, 2017

@author: jfinn
'''

from helpers import is_abundant, get_proper_divisors
from _functools import reduce
import operator

max_theoretical = 28123
abundant_numbers = list(filter(is_abundant, range(12,max_theoretical)))
print(len(abundant_numbers), "abundant numbers below", max_theoretical)

# I tried this first... too slow.
def is_not_sum_of_two_abundant_numbers(num):
    if num % 1000 == 0:
        print("Checking", num)
    for i in range(len(abundant_numbers)):
        n1 = abundant_numbers[i]
        if n1 > num/2:
            return True
        for j in range(i, len(abundant_numbers)):
            n2 = abundant_numbers[j]
            if n1 + n2 > num:
                break
            if n1 + n2 == num:
                return False
    return True

# Much faster
all_abundant_sums = set([x + y for x in abundant_numbers for y in abundant_numbers if x + y <= max_theoretical])
print(len(all_abundant_sums), "abundant sums below threshold")

non_abundant_sums = [x for x in range(1,max_theoretical+1) if x not in all_abundant_sums]
print(len(non_abundant_sums), "non-abundant sums")
print(non_abundant_sums)
print(reduce(operator.add, non_abundant_sums))



