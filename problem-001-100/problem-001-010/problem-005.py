'''
Created on Jan 9, 2017

@author: jfinn
'''

# For 1-20, all we really need is a calculator.
# For the general case (1-n) I'd use the get_prime_factors function from problem 3, 
# and the same approach: include all the unique prime factors of all the numbers 1-n.

num = 1
num *= 2 
num *= 3 
num *= 2  # 4 = 2 * 2 
num *= 5 
          # 6 = 2 * 3
num *= 7 
num *= 2  # 8 = 4 * 2
num *= 3  # 9 = 3 * 3
num *= 11
          # 12 = 3 * 4
num *= 13
          # 14 = 2 * 7
          # 15 = 3 * 5
num *= 2  # 16 = 8 * 2
num *= 17 
          # 18 = 2 * 9
num *= 19
          # 20 = 4 * 5
    
print(num)