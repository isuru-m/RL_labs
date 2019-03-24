#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 23:25:21 2019

@author: Isuru
"""
import numpy as np
import itertools 
import matplotlib.pyplot as plt
import time
#%matplotlib inline

#from itertools import *
#tic-tac-toe random agents 

start = time.time()
win = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
episodes = 10000
    
class RandomAgent1:
        
    def choose_action(self,h,grid):
        if h==0:                
            action = np.random.choice(9)
        else:
            available = np.where(grid==0)[0]
            try:
                action = np.random.choice(available)
            except:
                action = []
        grid[action] = 1
        #return action
 
class AgentQ:
    def __init__(self, epsilon=0.05, alpha=0.1, gamma=1):
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        #self.Q_table = {}
                
    def choose_action(self, h,grid, Q_table):
        old_state = tuple(grid)             
        #choose randomly within zero positions
        if not old_state in Q_table: 
            Q_table[old_state] = np.zeros(9)
                    
        try:
            available = np.where(grid==0)
            Q_values = Q_table[old_state]
            available_Q_values = Q_values[available]
            max_available_Q_value = np.random.choice(np.flatnonzero(Q_table[old_state] == available_Q_values.max()))
            
            action = max_available_Q_value               
        except:
            print('AgentQ skipped')
            action = []
        
                
        #grid[action] = 2        
        return action, old_state
    
    def take_action(self, action, grid, Q_table):
        grid[action] = 2
        new_state = tuple(grid)
        return new_state
    
    def update_q(self, action, Q_table, new_state, old_state, reward_O):
        
       #print( action)
        #print( Q_table)
       #print( new_state)
       #print( old_state)
       #print( reward_O)
                                        
        
        
        if not new_state in Q_table:
            Q_table[new_state] = np.zeros(9)
                            
        old_q_arr = Q_table[(old_state)]
       #print('old_q_arr=', old_q_arr)
        old_q_value = old_q_arr[action] 
       #print('old_q_value=', old_q_value)           
        max_q_new_state = np.max(Q_table[new_state]) 
       #print('max_q_new_state', max_q_new_state)
                    
        Q_table[old_state][action] = (1-self.alpha)*old_q_value + self.alpha*(reward_O + self.gamma*max_q_new_state)
        #print('Q(s,a)=',Q_table[old_state][action])
            
        
def check_terminal(h):
    global reward_X, reward_O, X_wins, O_wins
    if h==1 or h==2 or h==3 or h==4:
        return False
    
    elif h==5 or h==6:
        checkX = np.where(grid==1)[0]
        checkX_tup = tuple(checkX)
        checkO = np.where(grid==2)[0]
        checkO_tup = tuple(checkO)        
        
        X_winner = checkX_tup in win
        O_winner = checkO_tup in win
        
        if X_winner:
            print("X won")
            X_wins += 1
            reward_X += 1
            reward_O -= 1
            return True
        
        if O_winner:
            print("O won")
            O_wins += 1
            reward_O += 1
            reward_X -= 1
            return True
    
    elif h==7 or h==8 or h==9:
        checkX = np.where(grid==1)[0]        
        for L in range(3, len(checkX)):
            for subsetX in itertools.combinations(checkX, L):
                if subsetX in win:
                    print("X won")
                    X_wins += 1
                    reward_X += 1 
                    reward_O -= 1
                    return True

        checkO = np.where(grid==2)[0]        
        for M in range(3, len(checkO)):
            for subsetO in itertools.combinations(checkO, M):
                if subsetO in win:
                    print("O won")
                    O_wins += 1
                    reward_O += 1
                    reward_X -= 1
                    return True
    elif h>=9:
        print('Draw!!')
        reward_O += 0
        reward_X -= 0        
        return True
        
       
agent1 = RandomAgent1()
agent2 = AgentQ()
#print(help(agent2))
#print(grid.reshape(3,3))  

f=0
return_x = np.zeros(shape=episodes)
return_o = np.zeros(shape=episodes)
X_wins = 0
O_wins = 0
Q_table = {}

for ep in range(episodes):
    i=0
    h=0
    grid = np.zeros(9, dtype=int)
    print(grid.reshape(3,3))
    reward_X = 0
    reward_O = 0
    player_1 = np.random.randint(2)

    while 1:
            
        if player_1 == 0:            
            agent1.choose_action(h,grid)
            #grid[action] = 1
            print(grid.reshape(3,3)) 
            h += 1
            
            if h==9 or check_terminal(h):
                break
                   
            action, old_state = agent2.choose_action(h,grid,Q_table)
            new_state = agent2.take_action(action,grid,Q_table)
            
            #grid[action] = 2    
            print(grid.reshape(3,3))
            h += 1
            
            if check_terminal(h):
                break
        else:
            action, old_state = agent2.choose_action(h,grid,Q_table)
            new_state = agent2.take_action(action,grid,Q_table)
            #grid[action] = 2    
            print(grid.reshape(3,3))
            h += 1
            
            if h==9 or check_terminal(h):
                break
            
            agent1.choose_action(h,grid)
            #grid[action] = 1
            print(grid.reshape(3,3)) 
            h += 1
            
            if check_terminal(h):
                break
            
        i += 1
    #update the Q table     
    agent2.update_q(action, Q_table, new_state, old_state, reward_O)    
    f += 1
    return_x[ep] = reward_X + return_x[ep-1]
    return_o[ep] = reward_O + return_o[ep-1]
      
plt.plot(return_x,'r',return_o,'g')      

end = time.time()
print(end-start)  
    
    
    
    
    
    

