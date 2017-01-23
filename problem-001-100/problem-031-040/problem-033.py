'''
Created on Jan 22, 2017

@author: jfinn
'''

numerators = []
denomenators = []
for n in range(11,100):
    if n % 10 == 0:
        continue
    for d in range(n+1,100):
        if d % 10 == 0:
            continue
        if (d//10 == n%10 and (n//10) / (d%10) == n/d) or (d%10 == n//10 and (n%10) / (d//10) == n/d):
            numerators.append(n)
            denomenators.append(d)
            
print(numerators)
print(denomenators)
