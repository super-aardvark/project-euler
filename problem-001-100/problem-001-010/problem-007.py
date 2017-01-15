'''
Created on Jan 9, 2017

@author: jfinn
'''

import helpers


n = 1
primes = [2]
num = 2
while n < 10001:
    num += 1
    if helpers.is_prime(num, primes):
        primes.append(num)
        n += 1

print(len(primes))
print(num)
