#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 23:25:21 2019

@author: Isuru
"""
import numpy as np
import itertools 
import matplotlib.pyplot as plt
#%matplotlib inline

#from itertools import *
#tic-tac-toe random agents 

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
        return action
 
class AgentQ:
    def __init__(self, epsilon=0.05, alpha=0.1, gamma=1):
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.Q_table = {}
                
    def choose_action(self, h,grid):
        #self.grid_state = grid
        old_state = tuple(grid) 
        '''
        if h==0:   
            self.Q_table[old_state] = np.zeros(9, dtype=int)             
            #randomly choose a position
            action = np.random
        else:
        '''
            
        #choose randomly within zero positions
        if not old_state in self.Q_table:           
            self.Q_table[old_state] = np.zeros(9, dtype=int)
            print(self.Q_table)
            available = np.where(grid==0)[0]
            Q_values = self.Q_table[old_state]
            available_Q_values = Q_values[available]
            max_available_Q_value = np.random.choice(np.flatnonzero(self.Q_table[old_state] == available_Q_values.max()))
            try:
                action = max_available_Q_value               
            except:
                action = []
        else:
            available = np.where(grid==0)[0]
            Q_values = self.Q_table[old_state]
            available_Q_values = Q_values[available]
            self.max_available_Q_value = np.random.choice(np.flatnonzero(self.Q_table[old_state] == available_Q_values.max()))             
            try:
                action = max_available_Q_value               
            except:
                action = []
                
        #grid[action] = 2        
        return action, old_state
    
    def take_action(self, action, grid):
        grid[action] = 2
        new_state = tuple(grid)
        
        self.Q_table[new_state] = np.zeros(9, dtype=int)
              
        old_q_arr = self.Q_table[(old_state)]
        old_q_value = old_q_arr[action]
        
        max_q_new_state = np.max(self.Q_table[new_state]) 
        
        
        self.Q_table[old_state][action] = (1-self.alpha)*old_q_value + self.alpha*(reward_O + self.gamma*max_q_new_state)
        return new_state
            
        
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
    elif h>9:
        print('Draw!!')
        reward_O += 0
        reward_X -= 0        
        return True
        
q_table = {}
       
agent1 = RandomAgent1()
agent2 = AgentQ()
#print(help(agent2))
#print(grid.reshape(3,3))  

f=0
return_x = np.zeros(shape=episodes)
return_o = np.zeros(shape=episodes)
X_wins = 0
O_wins = 0

for ep in range(episodes):
    i=0
    h=0
    grid = np.zeros(9, dtype=int)
    reward_X = 0
    reward_O = 0
    player_1 = np.random.randint(2)

    while 1:
            
        if player_1 == 0:            
            agent1.choose_action(h,grid)
            #grid[action] = 1
            #print(grid.reshape(3,3)) 
            h += 1
            
            if check_terminal(h):
                break
                   
            action, old_state = agent2.choose_action(h,grid)
            new_state = agent2.take_action(action,grid)
            
            #grid[action] = 2    
            #print(grid.reshape(3,3))
            h += 1
            
            if check_terminal(h):
                break
        else:
            action, old_state = agent2.choose_action(h,grid)
            new_state = agent2.take_action(action,grid)
            #grid[action] = 2    
            #print(grid.reshape(3,3))
            h += 1
            
            if check_terminal(h):
                break
            
            agent1.choose_action(h,grid)
            #grid[action] = 1
            #print(grid.reshape(3,3)) 
            h += 1
            
            if check_terminal(h):
                break
                    
        i += 1
        
    f += 1
    return_x[ep] = reward_X + return_x[ep-1]
    return_o[ep] = reward_O + return_o[ep-1]
      
plt.plot(return_x,'r',return_o,'g')      
   
    
    
    
    
    
    

