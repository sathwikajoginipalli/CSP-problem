import time
import random

class Map():
    
    def __init__(self, vertices):
     ## function to initialize the adjacency matrix with 0's

        self.V = vertices

        self.map = []
        
        self.counter = 0
        
        for i in range(self.V):
            
            temp = []
            
            for j in range(self.V):
                
                temp.append("0")
                
            self.map.append(temp)
    

        
    def is_safe(self, v, color, c):
    ## checks whether the color assigned to state is safe or not
    ## returns true if safe

        for i in range(self.V):

            if self.map[v][i] == 1 and color[i] == c:

                self.counter+=1

                return False

        return True

    def get_neighbors(self,v):
    ## returns the neighbors of state

        neighbors_list = []

        for i in range(self.V):

            if self.map[v][i]==1:

                neighbors_list.append(i)
                
        return neighbors_list

    def MapColor(self, m, color, v):
    ## solves the map coloring problem by selecting one state at a time and assigning color if safe
    ## removes the values from domain of neighbors and adds back if color is not safe

        if v == self.V:

            return True
            
        if len(state_domain[v+1])==0:
                
            return False

        for c in state_domain[v+1]:

            if self.is_safe(v, color, c) == True:

                color[v] = c 

                neighbors = self.get_neighbors(v)

                for neighbor in neighbors:## removes the domain variables from neighbors

                    if c in state_domain[neighbor+1]:

                        state_domain[neighbor+1].remove(c)
                        
                if self.MapColor(m, color, v+1) == True:

                    return True

                for neighbor in neighbors:

                    a = neighbor+1

                    if c not in state_domain[a]:## reverts back the domain variables

                        state_domain[a].append(c) 

                        state_domain[a].sort()

                color[v] = 0
                        
    def MapColouring(self, m):
     ## function which takes the chromatic number and fills the states with colors & prints them 
        for o in range(0,4):
            
            value = ['red','blue','green']

            key = ['1','2','3']

            random.shuffle(value)

            colors = dict(zip(key,value))
        
            color = [0]* self.V
            
            for k, v in enumerate(states):
    
                val = list(range(1,4))

                state_domain[k+1] = val

            if self.MapColor(m, color, 0) == False:

                return False

            print("Number of backtrackings",self.counter)

            self.counter = 0

            i_val = [[i, val] for i, val in enumerate(color)]

            random.shuffle(i_val)

            for i,val in i_val:
            ## prints the states with colors
                print("{} ==> {}".format(states[i],colors[str(val)]))
            
        return True

state_domain = {}
## state domain dictionary - states, domain variables
states = ['V','T','NSW','Q','WA','SA','NT']

for k, v in enumerate(states):
    
    val = list(range(1,4))

    state_domain[k+1] = val

g = Map(7)
## adjacency matrix
g.map =  [[0,0,1,0,0,1,0],

          [0,0,0,0,0,0,0],

          [1,0,0,1,0,1,0],

          [0,0,1,0,0,1,1],

          [0,0,0,0,0,1,1],

          [1,0,1,1,1,0,1],

          [0,0,0,1,1,1,0]]
## m - chromatic number
m = 3  
start_time = time.time()
g.MapColouring(m)
end_time= time.time()
timetaken = start_time - end_time
##prints the time taken to run
print("Execution time-",timetaken)


