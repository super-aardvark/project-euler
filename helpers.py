'''
Created on Jan 9, 2017

@author: jfinn
'''
import math

def get_prime_factors(num, primes=[2]):
    factors = []
    max_factor = int(math.sqrt(num))
    for div in primes:
        if num == 1 or div > max_factor: 
            break
        while num % div == 0:
            factors.append(div)
            num = num / div
    largest_prime = primes[-1]
    if num != 1 and largest_prime < max_factor:
            for div in range(largest_prime + 1, max_factor + 1):
                if num == 1: 
                    break
                while num % div == 0:
                    factors.append(div)
                    num = num / div
    return factors

def is_prime(num, primes=[2]):
    if len(get_prime_factors(num, primes)) == 0:
        return True
    else:
        return False

