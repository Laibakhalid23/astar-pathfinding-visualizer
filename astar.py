import heapq
from maze import WALL

def get_neighbors(node,maze):
    neighbors=[]
    rows,cols=maze.shape
    directions=[(-1,0),(1,0),(0,-1),(0,1)]
    for dx, dy in directions:
        x=node[0]+dx
        y=node[1]+dy
        if 0<=x<rows and 0<=y<cols:
            if maze[x][y]!=WALL:
                neighbors.append((x,y))
    return neighbors

def reconstruct_path(came_from,current):
    path=[current]
    while current in came_from:
        current=came_from[current]
        path.append(current)
    path.reverse()
    return path

def astar(maze,start,goal,heuristic_func):
    open_set=[]
    heapq.heappush(open_set, (heuristic_func(start, goal), heuristic_func(start, goal), start))
    came_from={}
    g_cost={start:0}
    f_cost={start:heuristic_func(start,goal)}
    open_nodes=set([start])
    closed_nodes=set()
    history=[]
    while open_set:
        f, h, current = heapq.heappop(open_set)
        open_nodes.discard(current)
        closed_nodes.add(current)
        history.append((set(open_nodes),set(closed_nodes),current))
        if current==goal:
            path=reconstruct_path(came_from,current)
            return path,history
        
        for neighbor in get_neighbors(current,maze):
            tentative_g=g_cost[current]+1
            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                came_from[neighbor]=current
                g_cost[neighbor]=tentative_g
                f_cost[neighbor]=tentative_g + heuristic_func(neighbor,goal)

                if neighbor not in closed_nodes:
                    heapq.heappush(open_set,(f, heuristic_func(neighbor, goal), neighbor))
                    open_nodes.add(neighbor)
    return None,history

