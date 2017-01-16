'''
Created on Jan 15, 2017

@author: jfinn
'''

# We can always use 1p coins to fill any missing value to make 2 pounds
# So, just find all permutations of the other coins that sum to less than that
# We can also ignore the 200p coin and add 1 to the number of other permutations

coins = [0,0,0,0,0,0] # 2p, 5p, 10p, 20p, 50p, 1q

def get_value(coins):
    return coins[0] * 2 + coins[1] * 5 + coins[2] * 10 + coins[3] * 20 + coins[4] * 50 + coins[5] * 100

def next_permutation(coins):
    coins[0] += 1
    i = 0
    while get_value(coins) > 200:
        coins[i] = 0
        i += 1
        if i == len(coins):
            return False
        else:
            coins[i] += 1
    return True

num = 2 # one for 1px200 and one for 200px1
while next_permutation(coins):
#     print(coins)
    num += 1
    
print(num)