#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 06:02:53 2019

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
        ''' This method outputs the available actions for a given state'''             
        available_actions = np.full((1,4), False, dtype=bool)
        
        self.s_n = s + self.num_cols
        self.s_e = s + 1
        self.s_s = s - self.num_cols
        self.s_w = s - 1
        
        if self.s_n < self.num_fields:
            available_actions[0,0] = True
        if self.s_e % self.num_cols > 0:
            available_actions[0,1] = True
        if self.s_s >= 0:
            available_actions[0,2] = True
        if self.s_w % self.num_cols < self.num_cols - 1:
            available_actions[0,3] = True
               
        return available_actions
        
    def OneStepLookAhead(self, s, possible_actions, gamma=1, e=0.2):
        ''' This method calculates the value of neighbouring states for a given state
            putting e=0 (deterministic) yeilds the same result as excercise 1
        '''        
        if not possible_actions[0,0]:
            self.s_n = s            
        if not possible_actions[0,1]:
            self.s_e = s            
        if not possible_actions[0,2]:
            self.s_s = s            
        if not possible_actions[0,3]:
            self.s_w = s
       
        NESW_Cells = np.zeros(4)
        
        all_actions = np.array([self.s_n, self.s_e, self.s_s, self.s_w])
        
        for i in range(len(all_actions)):           
            NESW_Cells[i] = self.rewards[all_actions[i]] + gamma*((1-e)*self.V[all_actions[i]]+0.25*e*(self.V[self.s_n] + self.V[self.s_e] + self.V[self.s_s] + self.V[self.s_w])) 

        return NESW_Cells 
    
    def GetPolicy(self, value):
        ''' This method finds the optimal policy based on a converged value function'''
        policy_init = np.zeros(25, dtype=str)
        max_vals = np.zeros(25)
        arg_vals = np.zeros(25)
        for j in range(len(value)):
            pos_actions = self.GetAvailableActions(j)
            max_vals = self.OneStepLookAhead(j, pos_actions)
            arg_vals[j] = np.argmax(max_vals)
            
            if arg_vals[j] == 0:
                policy_init[j]='n'
            elif arg_vals[j] == 1:
                policy_init[j] = 'e'
            elif arg_vals[j] == 2:
                policy_init[j] = 's'
            elif arg_vals[j] == 3:
                policy_init[j] = 'w'
            
        return policy_init
        
grid = Gridworld()
theta = 1e-10
delta=np.zeros(grid.num_fields)
counter =0


while 1:
    
    for state in range(grid.num_fields):
        if state in grid.terminal_states:
            continue
        v = grid.V[state]
        available_actions = grid.GetAvailableActions(state)
        bellman_value_old = grid.OneStepLookAhead(state, available_actions)
        grid.V[state] = np.max(bellman_value_old)
        delta[state] = abs(v - grid.V[state])

    d = np.amax(delta)
    counter += 1
    if d < theta:
        break

v = grid.V
v_disp = grid.V.reshape(5,5)
print(np.flip(v_disp,0))
policy = grid.GetPolicy(v)
pol_disp = policy.reshape(5,5)
print(np.flip(pol_disp,0))