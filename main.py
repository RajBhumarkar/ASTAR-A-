import numpy as np
import math
import sys
X_end,Y_end = 9,9
x_start,y_start = 5,5
cost = 1
'''                 10x10 GRID


            [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
            [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
            [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
            [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
            [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
            [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
            [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
            [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
            [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
            [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 

'''
class Node:
    # whenever the node is defined tell me its x and y position
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.parent = tuple # it will be a int or a tupple (will decide later)
        self.local_goal = sys.maxsize
        self.global_goal = sys.maxsize
        self.is_start = False
    def get_pos(self):
        return self.x,self.y
    def heuristic(self):
        h = math.sqrt(
            (self.x-X_end)**2 + (self.y-Y_end)**2


        )
        # print(f'H for x: {self.x},y : {self.y}')
        # print(h)
        return h 
    def get_neighbour(self):
        
        neighbour_list = list()

        if self.x-1>=0:
            neighbour_list.append([self.x-1,self.y])
        if self.x+1<=9:
            neighbour_list.append([self.x+1,self.y])
        if self.y-1>=0:
            neighbour_list.append([self.x,self.y-1])
        if self.y+1<=9:
            neighbour_list.append([self.x,self.y+1])
        return neighbour_list

    def set_start(self):
        if self.is_start == True:
            self.local_goal = 0
            self.global_goal = self.local_goal + self.heuristic()
            self.parent = (self.x,self.y)
grid = np.empty((10,10),dtype=object)

for row in range(10):
    for  col in range(10):
        grid[row][col] = Node(row,col)

# setting this to starting node 
grid[x_start][y_start].is_start = True
grid[x_start][y_start].set_start()

current_x,current_y = x_start,y_start
# zipped_list = list()

p = 0
while True:
    if current_x == X_end and current_y == Y_end:
        print('goal_reached')
        break
    node = list()
    node_global = list()
    for neighbour in grid[current_x][current_y].get_neighbour():
        x,y = neighbour
        print(neighbour)
        if grid[current_x][current_y].local_goal + cost < grid[x][y].local_goal:
            # this is basically an update function
            grid[x][y].local_goal = grid[current_x][current_y].local_goal+cost
            grid[x][y].global_goal = grid[x][y].heuristic()+grid[x][y].local_goal
            grid[x][y].parent = (current_x,current_y)
            node.append(grid[x][y])
            node_global.append(grid[x][y].global_goal)
            
    zipped_list = list(zip(node,node_global))

    zipped_list = sorted(zipped_list,key=lambda x:x[1])
    # print(zipped_list)
    current_x,current_y = zipped_list[0][0].x,zipped_list[0][0].y
    print(current_x,current_y)
    