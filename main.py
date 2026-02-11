from maze import create_maze, START, GOAL
from heuristics import manhattan
from astar import astar
from visualization import visualize
import numpy as np


# Create Random Maze
rows, cols = 10, 15       
wall_density = 0.25       
maze = create_maze(rows, cols, wall_density)

# Get coordinates of START and GOAL in maze
start_coords = np.argwhere(maze == START)
goal_coords = np.argwhere(maze == GOAL)

start = (int(start_coords[0][0]), int(start_coords[0][1]))
goal = (int(goal_coords[0][0]), int(goal_coords[0][1]))

print("Start:", start)
print("Goal:", goal)

# Run A* Algorithm
path, history = astar(maze, start, goal, manhattan)

if path:
    print("Path found! Steps:", len(path))
else:
    print("No path found.")

# Visualize
visualize(maze, path, history, start, goal)
