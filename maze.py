import numpy as np
import random

EMPTY=0
WALL=1
START=2
GOAL=3
PATH=4
OPEN=5
CLOSED=6

#Random maze generator
def create_maze(rows=10,cols=10,wall_density=0.25):
    maze=np.zeros((rows,cols))
    #Add random walls
    for i in range(rows):
        for j in range(cols):
            if random.random()<wall_density:
                maze[i][j]=WALL
            
    #Random start and goal
    while True:
        start=(random.randint(0,rows-1),random.randint(0,cols-1))
        if maze[start] != WALL:
            maze[start] = START
            break
    while True:
        goal=(random.randint(0,rows-1),random.randint(0,cols-1))
        if maze[goal] != WALL and goal != start:
            maze[goal] = GOAL
            break

    return maze
    