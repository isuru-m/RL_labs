# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 16:40:27 2019

@author: Isuru
"""
import numpy as np
import itertools 
import matplotlib.pyplot as plt
#%matplotlib inline

#from itertools import *
#tic-tac-toe random agents 

win = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
episodes = 250
    
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
        
        
agent1 = RandomAgent1
agent2 = RandomAgent2
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

    while 1:
    
        if i==0:
            ini=True
        else:
            ini=False
                    
        action = agent1.choose_action(grid,ini)
        grid[action] = 1 
        #print(grid.reshape(3,3)) 
        h += 1
        
        if check_terminal(h):
            break
               
        action = agent2.choose_action(grid,ini=False)
        grid[action] = 2    
        #print(grid.reshape(3,3))
        h += 1
        
        if check_terminal(h):
            break
        
        i += 1
        
    f += 1
    return_x[ep] = reward_X + return_x[ep-1]
    return_o[ep] = reward_O + return_o[ep-1]
      
plt.plot(return_x,'r',return_o,'g')      
   
    
    
    
    
    
    

