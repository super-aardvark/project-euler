'''
Created on Jan 22, 2017

@author: jfinn
'''
import math

def is_palindrome(word):
    for i in range(len(word)):
        if word[i] != word[-(i+1)]:
            return False
    return True

sum = 0
for num in range(1,1000000):
    if is_palindrome(str(num)) and is_palindrome(format(num, 'b')):
        sum += num

print(sum)