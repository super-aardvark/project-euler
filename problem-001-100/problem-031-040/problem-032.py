'''
Created on Jan 15, 2017

@author: jfinn
'''
from itertools import permutations
from _functools import reduce
import operator

pandigitcal_products = []
for factor_digits in permutations(range(1,10), 5):
    multiplicand = factor_digits[0] * 10 + factor_digits[1]
    multiplier = factor_digits[2] * 100 + factor_digits[3] * 10 + factor_digits[4]
    product = multiplicand * multiplier
    product_digits = tuple(map(int, str(product)))
    digits = factor_digits + product_digits
    if (0 not in digits and len(digits) == 9 and len(set(digits)) == 9):
#             or (len(digits) == 10 and len(set(digits)) == 10):
        print(multiplicand, " * ", multiplier, " = ", product)
        pandigitcal_products.append(product)
        
    multiplicand = factor_digits[0]
    multiplier = factor_digits[1] * 1000 + factor_digits[2] * 100 + factor_digits[3] * 10 + factor_digits[4]
    product = multiplicand * multiplier
    product_digits = tuple(map(int, str(product)))
    digits = factor_digits + product_digits
    if (0 not in digits and len(digits) == 9 and len(set(digits)) == 9):
#             or (len(digits) == 10 and len(set(digits)) == 10):
        print(multiplicand, " * ", multiplier, " = ", product)
        pandigitcal_products.append(product)

print(pandigitcal_products)
unique_pd_products = set(pandigitcal_products)
print(unique_pd_products)
print(reduce(operator.add, unique_pd_products))
