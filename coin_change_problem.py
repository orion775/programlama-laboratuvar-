#!/usr/bin/env python
# coding: utf-8

# In[1]:


#greedy method
coins = [1, 5, 10, 25, 50]
n = len(coins)
 
def findMin(V):
    ans = []
    i = n-1	
    while (i>=0):
        while (V >= coins[i]):
           V = V - coins[i]
           ans.append(coins[i])
        i -= 1
    for coin in ans:
        print(coin)
V = 65
findMin(V)


# In[15]:


#recursive method
def rec_coin(coins, change, known_result):
    min_coins = change
    if change in coins:
        known_result[change] = 1
        return 1
    elif known_result[change] > 0:
        return known_result[change]
    
    else:
        for i in [c for c in coins if c <= change]:
            num_coins = 1 + rec_coin(coins, change - i, known_result)
            if num_coins < min_coins:
                min_coins = num_coins
                known_result[change] = min_coins
    return min_coins

result = rec_coin([1,5,10,25], 40, [0] * (40+1))
print(result)


# In[7]:


#expressions
list = [i for i in range(10) if i%2 == 0]
list

