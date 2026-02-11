import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.widgets import Button
from maze import *
import numpy as np

def visualize(maze, path, history, start, goal):
    cmap = colors.ListedColormap([
        'white',    # EMPTY
        'black',    # WALL
        'green',    # START
        'red',      # GOAL
        'yellow',   # PATH
        'cyan',     # OPEN
        'blue'      # CLOSED
    ])

    # Convert to integer type
    grid = maze.copy().astype(int)
    start = (int(start[0]), int(start[1]))
    goal = (int(goal[0]), int(goal[1]))

    fig, ax = plt.subplots(figsize=(6,6))
    plt.subplots_adjust(bottom=0.2)

    def draw_animation():
        """Animate the A* search process"""
        for i, (open_nodes, closed_nodes, current) in enumerate(history):
            display_grid = grid.copy().astype(int)
            
            # Mark open nodes
            for node in open_nodes:
                r, c = int(node[0]), int(node[1])
                if (r, c) not in (start, goal) and display_grid[r, c] != WALL:
                    display_grid[r, c] = OPEN
            
            # Mark closed nodes
            for node in closed_nodes:
                r, c = int(node[0]), int(node[1])
                if (r, c) not in (start, goal) and display_grid[r, c] != WALL:
                    display_grid[r, c] = CLOSED

            display_grid[start] = START
            display_grid[goal] = GOAL

            ax.clear()
            ax.imshow(display_grid, cmap=cmap, origin='upper', vmin=0, vmax=6)
            ax.set_title(f"A* Search Animation - Step {i+1}/{len(history)}")
            plt.pause(0.05)

        # Draw final path
        if path:
            final_grid = grid.copy().astype(int)
            for node in path:
                r, c = int(node[0]), int(node[1])
                if (r, c) not in (start, goal):
                    final_grid[r, c] = PATH

            final_grid[start] = START
            final_grid[goal] = GOAL

            ax.clear()
            ax.imshow(final_grid, cmap=cmap, origin='upper', vmin=0, vmax=6)
            ax.set_title(f"Final Path - {len(path)} steps")
        else:
            ax.clear()
            ax.imshow(grid, cmap=cmap, origin='upper', vmin=0, vmax=6)
            ax.set_title("No Path Found")
        
        plt.draw()

    def play_again(event):
        """Reset and replay animation"""
        ax.clear()
        draw_animation()

    # Initial animation
    draw_animation()

    # Add button
    ax_button = plt.axes([0.4, 0.05, 0.2, 0.075])
    button = Button(ax_button, 'Play Again')
    button.on_clicked(play_again)

    plt.show()