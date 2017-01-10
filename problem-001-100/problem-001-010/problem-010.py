'''
Created on Jan 9, 2017

@author: jfinn
'''
from helpers import is_prime
from _functools import reduce
import operator

primes = [2]
for n in range(3,2000000):
    if is_prime(n, primes):
        primes.append(n)

print("Found", len(primes), "primes below 2,000,000")
print(reduce(operator.add, primes))