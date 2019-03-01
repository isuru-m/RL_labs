#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 09:07:42 2019

@author: Isuru
"""
import numpy as np

class Gridworld:
    
    def __init__(self):
        self.num_rows = 5
        self.num_cols = 5
        self.num_fields = self.num_cols * self.num_rows
        self.gold_reward = 10
        self.bomb_reward = -10
        self.gold_positions = np.array([23])
        self.bomb_positions = np.array([18])
        self.terminal_states = np.concatenate((self.gold_positions, self.bomb_positions))
        
        
        self.V = np.zeros(shape=self.num_fields)
        
        
        self.rewards = np.ones(shape=self.num_fields) * (-1)
        self.rewards[self.bomb_positions] = self.rewards[self.bomb_positions] + self.bomb_reward
        self.rewards[self.gold_positions] = self.rewards[self.gold_positions] + self.gold_reward
        
    def GetAvailableActions(self,s):
        available_actions = np.full((1,4), False, dtype=bool)
        
        self.s_n = s + 5
        self.s_e = s + 1
        self.s_s = s - 5
        self.s_w = s - 1
        
        if self.s_n < 25:
            available_actions[0,0] = True
        if self.s_e % 5 > 0:
            available_actions[0,1] = True
        if self.s_s >= 0:
            available_actions[0,2] = True
        if self.s_w % 5 < 4:
            available_actions[0,3] = True
               
        return available_actions
        

    def OneStepLookAhead(self, s, possible_actions, gamma=1, e=0.2):
        
        if not possible_actions[0,0]:
            self.s_n = s
            
        if not possible_actions[0,1]:
            self.s_e = s
            
        if not possible_actions[0,2]:
            self.s_s = s
            
        if not possible_actions[0,3]:
            self.s_w = s
        
        NESW_Cells = np.zeros(4)
        '''
        all_actions = np.array([self.s_n, self.s_e, self.s_s, self.s_w])
        
        
        for i in range(len(all_actions)):
            NESW_Cells[i] = gamma*self.V[all_actions[i]] + self.rewards[i]
        '''    
        NESW_Cells[0] = gamma*self.V[self.s_n] + self.rewards[self.s_n]  
        NESW_Cells[1] = gamma*self.V[self.s_e] + self.rewards[self.s_e]
        NESW_Cells[2] = gamma*self.V[self.s_s] + self.rewards[self.s_s]
        NESW_Cells[3] = gamma*self.V[self.s_w] + self.rewards[self.s_w]                  
        
        return NESW_Cells 
        
    
grid = Gridworld()
theta = 1e-10
c_while =0

while 1:
    delta=np.zeros(grid.num_fields)
    for state in range(grid.num_fields):              
        if state in grid.terminal_states:
            continue       
        v = grid.V[state]
        available_actions = grid.GetAvailableActions(state)
        bellman_value_old = grid.OneStepLookAhead(state, available_actions)
        grid.V[state] = np.max(bellman_value_old)
        delta[state] = abs(v - grid.V[state])        
    d = np.amax(delta)
    c_while+=1
    if d < theta:
        break
    
v = grid.V
v_disp = grid.V.reshape(5,5)
print("done")
print(np.flip(v_disp,0))
ac = grid.GetAvailableActions
print(ac)