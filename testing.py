# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 10:47:23 2019

@author: Allan
"""
import numpy as np

class Site:
    def __init__(self):
        self.rowCount = 5
        self.colCount = 5
        self.totalPosCount = self.rowCount * self.colCount
        self.goldPos=np.array([23])
        self.bombPos=np.array([18])
        
        self.rewards = np.full((self.totalPosCount),-1)
        self.goldReward = 10
        self.rewards[self.goldPos] = self.goldReward + self.rewards[self.goldPos] 
        self.bombReward = 10
        self.rewards[self.bombPos] = self.bombReward + self.rewards[self.bombPos] 
        
        self.Values = self.delta = np.zeros(shape=self.totalPosCount)
                
    def bellman(self, state, gamma=1, e=0):
        
        X = np.zeros(4)
        
        if state+5 in self.Values:
            self.s_n = state + 5
        else:
            self.s_n = state
        
        if not(state%5==0):
            self.s_w = state - 1 
        else:
            self.s_w = state
        
        if state-5 in self.Values:
            self.s_s = state - 5
        else:
            self.s_s = state
        
        if not(state%5==4):
            self.s_e = state + 1
        else:
            self.s_e = state
        
        stateAction = np.array([self.s_n, self.s_w, self.s_s, self.s_e])
        
        for i in range(len(stateAction)):
            X[i] = self.rewards[stateAction[i]] + gamma * ( (1-e) * self.Values[stateAction[i]] + 0.25*e*(self.Values[self.s_n] + self.Values[self.s_e] + self.Values[self.s_s] + self.Values[self.s_w]))
        
        Val = np.max(X)
        return Val
    
    def findPol(self,value):
        direction=np.zeros(4)        
        policy = np.array(["F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F"])
        policy_raw= np.empty(len(value))
        l = range(len(value))
        
        for p in l:
                    
            if p+5 in self.bomb_positions and p+5 in l:
                direction[0] = -1000
            elif p+5 in self.gold_positions and p+5 in l:
                direction[0] = 1000
            elif p+5 in l:
                direction[0] = value[p+5]
            else:
                direction[0] =-1000
                
            if p-1 in self.bomb_positions and p%5!=0:
                direction[1] = -1000
            elif p-1 in self.gold_positions and p%5!=0:
                direction[1] = 1000
            elif p%5!=0:
                direction[1] = value[p-1]
            else:
                direction[1] =-10000
                
            if p-5 in self.bomb_positions  and p-5 in l:
                direction[2] = -1000
            elif p-5 in self.gold_positions and p-5 in l:
                direction[2] = 1000
            elif p-5 in l:
                direction[2] = value[p-5]
            else:
                direction[2] =-10000    
               
            if p+1 in self.bomb_positions and p%5!=4:
                direction[3] = -1000
            elif p+1 in self.gold_positions and p%5!=4:
                direction[3] = 1000
            elif p%5!=4:
                direction[3] = value[p+1]
            else:
                direction[3] =-1000    

            policy_raw[p] = np.argmax(direction)                        
            if   policy_raw[p] == 0:
                policy[p]="n"
            elif policy_raw[p] == 1:
                policy[p]="w"
            elif policy_raw[p] == 2:
                policy[p]="s"
            elif policy_raw[p] == 3:
                policy[p]="e"

        return policy
    
            
c_while =0          
env = Site()
theta = 1e-10
while 1:
    for state in range(env.totalPosCount):
        if state in env.goldPos or state in env.bombPos:
            continue
        
        temp = env.Values[state]
        env.Values[state] = env.bellman(state)
        env.delta[state] = abs(temp - env.Values[state])
        print(env.delta[state])    
        d = np.amax(env.delta)
        print(d)
        c_while+=1
        
        if d < theta:
           # print(c_while)
            break
        
value = env.Values       
policy=findPol(value)

print(value)
print(policy)

        
        
        
        
        