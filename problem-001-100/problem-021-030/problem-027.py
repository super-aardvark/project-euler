'''
Created on Jan 15, 2017

@author: jfinn
'''
from helpers import is_prime

# some memoization to speed things up later...
primes = [2]
for num in range(3,1000000):
    if is_prime(num, primes):
        primes.append(num)
        
print("stored", len(primes), "primes below 1,000,000")
        
max_primes = 0
answer = 0
for a in range(-999,1000):
#     print("a=",a)
    for b in range(-1000,1001):
        n = 0
        num = n*n + a*n + b
        while num > 1 and is_prime(num, primes):
            n += 1
            num = n*n + a*n + b
        num_primes = n
        if num_primes > max_primes:
            max_primes = num_primes
            answer = a*b
            print(num_primes, " primes for a=",a,", b=",b)

print(answer)