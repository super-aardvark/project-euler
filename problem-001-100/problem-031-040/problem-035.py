'''
Created on Jan 22, 2017

@author: jfinn
'''
from helpers import is_prime

primes = [2]
for num in range(3,1000000):
    if is_prime(num):
        primes.append(num)

primes = set(primes) # faster lookup

circ_primes = []
num_circ = 0
for prime in primes:
    is_circ_prime = True
    num_digits = len(str(prime))
    num = prime
    for i in range(num_digits):
        if num not in primes:
            is_circ_prime = False
            break
        ones = num % 10
        num = (num // 10) + (ones * 10**(num_digits - 1))
    if is_circ_prime:
        num_circ += 1
        circ_primes.append(prime)

print(circ_primes)
print(num_circ)