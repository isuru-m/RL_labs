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
        print(self.terminal_states)
        print("TestPoint")
        
        self.V_old = np.zeros(shape=self.num_fields)
        self.V_new = np.zeros(shape=self.num_fields)
        
        self.rewards = np.ones(shape=self.num_fields) * (-1)
        self.rewards[self.bomb_positions] = self.rewards[self.bomb_positions]+self.bomb_reward
        self.rewards[self.gold_positions] = self.rewards[self.gold_positions]+self.gold_reward
        

    def OneStepLookAhead(self,s):

            s_n = s + self.num_cols
            s_e = s + 1
            s_s = s - self.num_cols
            s_w = s - 1

            NESW_Cells = np.zeros(4)

            if s_n >= self.num_fields: #condition for top bound
                NESW_Cells[0] = self.V_old[s] + self.rewards[s]
            else:
                NESW_Cells[0] = self.V_old[s_n] + self.rewards[s_n]

            if s_e % self.num_cols == 0: #condition for right corner 
                NESW_Cells[1] = self.V_old[s] + self.rewards[s]
            else:
                NESW_Cells[1] = self.V_old[s_e] + self.rewards[s_e]

            if s_s < 0: #condition for bottom bound
                NESW_Cells[2] = self.V_old[s] + self.rewards[s]
            else:
                NESW_Cells[2] = self.V_old[s_s] + self.rewards[s_s]

            if s_w % self.num_cols == self.num_cols - 1: #condition for left corner 
                NESW_Cells[3] = self.V_old[s] + self.rewards[s]
            else:
                NESW_Cells[3] = self.V_old[s_w] + self.rewards[s_w]
            #else:
                #raise ValueError('ya dun goofed it boi!')

            return NESW_Cells
        
    def find_policy(self,value):
        direction=np.zeros(5)        
        print(value)
        policy = np.array(["F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F"])
        #policy= np.empty(len(value))
        policy_raw= np.empty(len(value))
        l = range(len(value))
        for p in l:
            print(p)
            
            if p in self.terminal_states:
                direction[4] = 10000
            else:
                direction[4] = -1
            
            if p+5 in self.bomb_positions and p+5 in l:
                direction[0] = -1000
            elif p+5 in self.gold_positions and p+5 in l:
                direction[0] = 1000
            elif p+5 in l:
                direction[0] = value[p+5]
            else:
                direction[0] =-1
                
            if p-1 in self.bomb_positions and p%5!=0:
                direction[1] = -1000
            elif p-1 in self.gold_positions and p%5!=0:
                direction[1] = 1000
            elif p%5!=0:
                direction[1] = value[p-1]
            else:
                direction[1] =-1
                
            if p-5 in self.bomb_positions  and p-5 in l:
                direction[2] = -1000
            elif p-5 in self.gold_positions and p-5 in l:
                direction[2] = 1000
            elif p-5 in l:
                direction[2] = value[p-5]
            else:
                direction[2] =-1    
               
            if p+1 in self.bomb_positions and p%5!=4:
                direction[3] = -1000
            elif p+1 in self.gold_positions and p%5!=4:
                direction[3] = 1000
            elif p%5!=4:
                direction[3] = value[p+1]
            else:
                direction[3] =-1    
                            
            print(direction)
            print(np.argmax(direction))
            policy_raw[p] = np.argmax(direction)
                        
            if policy_raw[p] == 0:
                policy[p]="n"
            elif policy_raw[p] == 1:
                policy[p]="w"
            elif policy_raw[p] == 2:
                policy[p]="s"
            elif policy_raw[p] == 3:
                policy[p]="e"
            elif policy_raw[p] == 4:
                policy[p]=""

        print(policy)
        print(value)
        return policy

grid = Gridworld()
theta = 1e-10

delta=np.zeros(grid.num_fields)
#print(grid.rewards)
c_while =0
while 1:
#for i in range(8):
    
    for state in range(grid.num_fields):
        #print(state)
        
        if state == 18 or state == 23:
            #print("terminal state")
            continue
        v = grid.V_new[state]
        bellman_value_old = grid.OneStepLookAhead(state)
        grid.V_new[state] = np.max(bellman_value_old)
        
        #print(bellman_value_old)
        
        delta[state] = abs(v - grid.V_new[state])

        #print(grid.V_new)
        #print(delta)
        
    grid.V_old = grid.V_new     
    #print(bellman_value_old)
    d = np.amax(delta)
    c_while+=1
    #print(c_while)
    if d < theta:
        Fvalues=grid.V_new
        policy=grid.find_policy(grid.V_new)
        break
        


print("done")