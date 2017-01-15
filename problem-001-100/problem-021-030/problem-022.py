'''
Created on Jan 11, 2017

@author: jfinn
'''
from _functools import reduce
import operator


def word_value(word):
    return reduce(operator.add, map(lambda char: ord(char) - (ord('A') - 1), word))
 

names = []
file = open("p022_names.txt")
names = file.readline().split(",")
names = list(map(lambda qn: qn.strip('"'), names))
  
names.sort()
  
sum = 0
i = 0
for name in names:
    i += 1
    sum += i * word_value(name)
 
 
print(sum)