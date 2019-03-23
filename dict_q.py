#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:54:37 2019

@author: Isuru
"""

import numpy as np

A = np.array([5, 3, 5, 2, 4, 1, 2, 4, 5])
B = np.array([7, 4, 2, 4, 7, 6, 8, 2, 3])
C = np.array([9, 5, 7, 1, 3, 4, 7, 3, 4])

d = {(0,0,9): A,(1, 1, 1): B,(2, 2, 2) : C}
t = (0,0,9)

new_state = (5,5,5)

available = [0 ,5, 8]
q = d[t]
available_q_values = q[available]
max_available_q_values = np.random.choice(np.flatnonzero(d[t] == available_q_values.max()))

q[max_available_q_values] = update

d[new_state] = np.zeros(9)




x = np.argmax(d[(t)])
y = np.random.choice(np.flatnonzero(d[(t)] == d[(t)].max()))   #randomly choose within maximum Q-values 



grid = np.array([0,1,2,2,1,0,1,1,0])
available = np.where(grid==0)[0]



'''

def terminal_t(i):
    global reward
    reward += 1 
    if i>=3:
        return True, reward
    
reward = 0   
for i in range(5):
    print(i)
    if terminal_t(i):
        bool1, reward_return= terminal_t(i)
        print(reward_return)
        print('loop break')
        break
'''    

