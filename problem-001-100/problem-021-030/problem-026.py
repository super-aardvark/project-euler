'''
Created on Jan 15, 2017

@author: jfinn
'''
from decimal import *

print(range(1,2))
precision = 100
getcontext().prec = precision
one = Decimal(1)
max_length = 0
answer = 0
for d in range(2,1000):
    num = one / Decimal(d)
    decimal_places = str(num)[2:-1]
    if len(decimal_places) < (precision - 3):
        # no cycle
        continue
    cycle_found = False
    while len(decimal_places) > 3 and not cycle_found:
        max_detectable_length = len(decimal_places)//2
        for i in range(1, max_detectable_length):
            cycle = decimal_places[:i]
            num_cycles = len(decimal_places)//i
            match = True
            for j in range(1, num_cycles):
                if cycle != decimal_places[i*j:i*j+i]:
                    match = False
                    break
            if match:
                cycle_found = True
                if len(cycle) > max_length:
                    max_length = len(cycle)
                    answer = d
#                     print("new max length:", max_length,"for denominator",d)
                    if max_length > precision // 3:
                        precision *= 4
                        getcontext().prec = precision
#                         print("Precision increased to", precision)
                break
        # Maybe there's a non-repeating prefix...
        decimal_places = decimal_places[1:]
print("Max cycle length of",max_length,"was found for denominator",answer)