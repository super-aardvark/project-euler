'''
Created on Jan 9, 2017

@author: jfinn
'''
import math

def get_all_factors(num):
    factors = []
    max_factor = int(math.sqrt(num))
    for div in range(1, max_factor):
        if num % div == 0:
            factors.append(div)
            factors.append(num // div)
    if max_factor**2 == num:
        factors.append(max_factor)
    return factors

num = 0
i = 1
while True:
    num += i
    i += 1
    factors = get_all_factors(num)
    if len(factors) > 500:
        print(factors)
        print(num)
        break
        
