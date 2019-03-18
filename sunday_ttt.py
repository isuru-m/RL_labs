# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 16:40:27 2019

@author: Isuru
"""
import numpy as np
import itertools 
#from itertools import *
#tic-tac-toe random agents 
grid = np.zeros(9, dtype=int)
win = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    
class RandomAgent1:
        
    def choose_action(self, ini=True):
        if ini:                
            action = np.random.choice(9)
        else:
            available = np.where(grid==0)[0]
            try:
                action = np.random.choice(available)
            except:
                action = []
        return action
 
class RandomAgent2:
        
    def choose_action(self, ini=True):
        if ini:                
            #randomly choose a position
            action = np.random.choice(9)
        else:
            #choose randomly within zero positions
            available = np.where(grid==0)[0]
            try:
                action = np.random.choice(available)
            except:
                action = []
        return action
        
def check_terminal(h):
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
            return True
        
        if O_winner:
            print("O won")
            return True
    
    elif h==7 or h==8 or h==9:
        checkX = np.where(grid==1)[0]        
        for L in range(3, len(checkX)):
            for subsetX in itertools.combinations(checkX, L):
                if subsetX in win:
                    print("iter worked for X")
                    return True

        checkO = np.where(grid==2)[0]        
        for M in range(3, len(checkO)):
            for subsetO in itertools.combinations(checkO, M):
                if subsetO in win:
                    print("iter worked for O")
                    return True
        
    
#env = tick.grid
agent1 = RandomAgent1
agent2 = RandomAgent2
#print(help(agent2))
print(grid.reshape(3,3))  
i=0
h=0
while 1:

    if i==0:
        ini=True
    else:
        ini=False
                
    action = agent1.choose_action(grid,ini)
    grid[action] = 1 
    print(grid.reshape(3,3)) 
    h += 1
    
    if check_terminal(h):
        break
           
    action = agent2.choose_action(grid,ini=False)
    grid[action] = 2    
    print(grid.reshape(3,3))
    h += 1
    
    if check_terminal(h):
        break
    
    i += 1
    
    if h>=9:
        print("Game Draw!!")
        break 
      
        
    
    
    
    
    
    
    