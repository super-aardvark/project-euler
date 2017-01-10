'''
Created on Jan 9, 2017

@author: jfinn
'''

def is_palindrome(string):
    for n in range(int(len(string) / 2)):
        if string[n] != string[len(string) - 1 - n]:
            return False
    return True

max = 0
for i in range(100,999):
    for j in range(100,999):
        num = i*j
        if is_palindrome(str(num)) and num > max:
            max = num
            factors = (i,j)

print(factors)
print(max)