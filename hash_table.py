# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 22:54:52 2019

@author: rasim
"""

import random

def create_hash(n):
    # n must be prime
    table = []
    
    for i in range(n):
        table.append(0)
    
    return table
    
def my_hash(size, number_to_be_inserted):
    
    return number_to_be_inserted % size

def insert(table, number_to_be_inserted):
    
    is_collision = False
    index = my_hash(len(table), number_to_be_inserted)
    
    if(table[index] == 1):
        is_collision = True
    
    else:
        table[index] = 1
    
    return is_collision

def test(size = 13, number_to_be_inserted = 10):
    
    my_hash_1 = create_hash(size)
    c = 0
    
    for s in range(number_to_be_inserted):
        number = random.randint(0, 1000)
        
        if(insert(my_hash_1, number) == True):
            c += 1
            
    return c

test_1 = test(203, 50)
print(test_1)