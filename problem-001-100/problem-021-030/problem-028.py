'''
Created on Jan 15, 2017

@author: jfinn
'''

next_diag = 1
sum = 1
max_side = 1001
for side in [x*2+1 for x in range(1, max_side//2 + 1)]:
    for d in range(4):
        next_diag += side - 1
        sum += next_diag

print(sum)