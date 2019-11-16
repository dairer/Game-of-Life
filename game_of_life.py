import pygame
import numpy as np
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (220,220,220)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [750, 750]
screen = pygame.display.set_mode(WINDOW_SIZE)

cell_size = 2
cell_count = int(WINDOW_SIZE[0]/cell_size)

# Create a 2 dimensional array. A two dimensional
grid = [[0 for x in range(cell_count)] for y in range(cell_count)]

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = cell_size
HEIGHT = cell_size

# This sets the margin between each cell
MARGIN = 0





# Initialize pygame
pygame.init()

# Set title of screen
pygame.display.set_caption("~ game of life ~")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# generate random population
for k in range(cell_count):
    for b in range(cell_count):
        grid[k][b] = np.random.choice([0,1])



'''
grid[10][10] = 1
grid[10][11] = 1
grid[10][9] = 1
'''


def check_cell_status(row, col, grid):
    alive_count = 0
    if row>0 and column>0 and row<cell_count-1 and column<cell_count-1:
        # cells with less than two neighbours die
            #itterate through neighbours and count how many are alive
            neighbours = [grid[row-1][column],
                          grid[row+1][column],
                          grid[row][column-1],
                          grid[row][column+1],
                          grid[row+1][column+1],
                          grid[row-1][column-1],
                          grid[row+1][column-1],
                          grid[row-1][column+1]]
            for neighbour in neighbours:
                if neighbour == 1:
                    alive_count+=1

    if grid[row][column] == 1 and alive_count<2:
        return 0
    elif grid[row][column] == 1 and alive_count==2 or alive_count==3:
        return 1
    elif grid[row][column] == 0 and alive_count==3:
        return 1
    elif grid[row][column] == 1 and alive_count>3:
        return 0



def draw_life():
    for row in range(cell_count):
        for column in range(cell_count):
            color = WHITE
            if grid[row][column] == 1:
                color = BLACK
            pygame.draw.rect(screen, color,[(MARGIN + WIDTH) * column + MARGIN,
                            (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])




# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop



    '''
                    rules

    - 1 Any live cell with two or three neighbors survives.
    - 2 Any dead cell with three live neighbors becomes a live cell.
    - 3 All other live cells die in the next generation.
        Similarly, all other dead cells stay dead.
    '''
    draw_life()
    #
    # check status of every cell

    next_generation = [[0 for x in range(cell_count)] for y in range(cell_count)]
    for row in range(cell_count):
        for column in range(cell_count):
            next_generation[row][column] = check_cell_status(row, column, grid)

    grid = next_generation
    # Draw the grid

    clock.tick(5) # frames per second



    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
