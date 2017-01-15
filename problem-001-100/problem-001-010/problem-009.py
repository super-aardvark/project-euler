'''
Created on Jan 9, 2017

@author: jfinn
'''

sum = 1000
for a in range(1, int(sum/3)):
    for b in range(a+1, int((sum-a)/2)+1):
        c = sum - a - b
        if a**2 + b**2 == c**2:
            print(sum, (a,b,c))
            print("product: ", a*b*c)
           