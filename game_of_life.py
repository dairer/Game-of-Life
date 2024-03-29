import pygame
import numpy as np
import time

<<<<<<< HEAD
#black gradient

colours = [(0, 0, 0),
           (64,64,64),
           (128,128,128),
           (160,160,160),
           (192,192,192),
           (224,224,224),
           (255,255,255)]


'''
#green gradient
colours = [(0, 51, 25),
           (0,102,51),
           (0,153,76),
           (0,204,102),
           (0,255,128),
           (153,224,204),
           (204,255,229),
           (255,255,255)]
'''


# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [700, 700]
=======
BLACK = (0, 0, 0)
WHITE = (220,220,220)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WINDOW_SIZE = [750, 750]
>>>>>>> 9aadff892dfcff480e9d5d5b048c1de068144c0d
screen = pygame.display.set_mode(WINDOW_SIZE)

cell_size = 6
cell_count = int(WINDOW_SIZE[0]/cell_size)

grid = [[0 for x in range(cell_count)] for y in range(cell_count)]

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = cell_size
HEIGHT = cell_size

# This sets the margin between each cell
MARGIN = 0


colour_of_cells = [[colours[-1] for x in range(cell_count)] for y in range(cell_count)]

pygame.init()

# Set title of screen
pygame.display.set_caption("~ game of life ~")

done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# generate random population
for k in range(cell_count):
    for b in range(cell_count):
        grid[k][b] = np.random.choice([0,1], p=[0.9, 0.1])



'''
grid[10][10] = 1
grid[10][11] = 1
grid[10][9] = 1
'''


def check_cell_status(row, col, grid):

    # 1 indicates alive
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
            color = colours[-1]
            if grid[row][column] == 1:
                colour_of_cells[row][column] = colours[0]
            else:
                if colours.index(colour_of_cells[row][column]) != len(colours)-1:
                    colour_of_cells[row][column] = colours[colours.index(colour_of_cells[row][column])+1]
            pygame.draw.rect(screen, colour_of_cells[row][column],[(MARGIN + WIDTH) * column + MARGIN,
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
    
    # check status of every cell

    next_generation = [[0 for x in range(cell_count)] for y in range(cell_count)]
    for row in range(cell_count):
        for column in range(cell_count):
            next_generation[row][column] = check_cell_status(row, column, grid)

    grid = next_generation

    clock.tick(5) # frames per second



    pygame.display.flip()


pygame.quit()
