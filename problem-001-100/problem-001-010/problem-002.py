'''
Created on Jan 8, 2017

@author: jfinn
'''

def cycle(pair):
     even = pair[0] + pair[1]
     pair[0] = even + pair[1]
     pair[1] = pair[0] + even
     return even

last_two = [1,1]
sum = 0
while last_two[0] + last_two[1] < 4000000:
    sum += cycle(last_two)
     
print(sum)