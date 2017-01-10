'''
Created on Jan 9, 2017

@author: jfinn
'''

def next_collatz_sequence(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1

max_length = 0
max_start = 0
for start in range(1,1000000):
    if start % 10000 == 0:
        print("Longest chain below",start,"is",max_length,"starting at",max_start)
    num = start
    n = 0
    chain = [start]
    while num > 1:
        num = next_collatz_sequence(num)
        n += 1
        chain.append(num)
    if n > max_length:
        max_length = n
        max_start = start

print("Longest chain below 1,000,000 is",max_length,"starting at",max_start)


# I started to work on a memoization scheme to speed this up, 
# but it finished running as-is before I finished writing it.  
# Here's the WIP:

# max_length = 0
# max_start = 0
# graph = {1:(None, 1)}
# for start in range(1,1000000):
#     if start % 10000 == 0:
#         print("Longest chain below",start,"is",max_length,"starting at",max_start)
#     num = start
#     n = 0
#     chain = [start]
#     while num > 1:
#         num = next_collatz_sequence(num)
#         n += 1
#         if num in graph:
#             
#         else:
#             chain.append(num)
#     if n > max_length:
#         max_length = n
#         max_start = start