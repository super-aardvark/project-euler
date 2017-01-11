'''
Created on Jan 10, 2017

@author: jfinn
'''
from _functools import reduce
import operator

num = 2**1000
digits = list(str(num))
sum = reduce(lambda x, y: int(x) + int(y), digits)
print(sum)