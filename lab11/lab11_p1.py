import time
import copy

SIZE = 20  # size of the 2D cellular automaton


def printSep():
    '''Print a separator'''
    for ctr in range(0, SIZE + 2):
        print('-', end='')
    print('')


def Automation(world):
    """
    with given world,
    analyze which cells will die or live or revive
    then return next world
    """
    newWorld = copy.deepcopy(world) # prevent aliases

    # count alive neighbors
    for row in range(SIZE):
        for index in range(SIZE):
            neighbor = []
            if row == 0:  # row 0
                if index == 0:
                    neighbor.append(world[row][index + 1])
                    neighbor.append(world[row + 1][index + 1])
                    neighbor.append(world[row + 1][index])

                elif index == SIZE - 1:
                    neighbor.append(world[row][index - 1])
                    neighbor.append(world[row + 1][index - 1])
                    neighbor.append(world[row + 1][index])

                else:
                    neighbor.append(world[row][index - 1])
                    neighbor.append(world[row + 1][index - 1])
                    neighbor.append(world[row + 1][index])
                    neighbor.append(world[row + 1][index + 1])
                    neighbor.append(world[row][index + 1])

            elif row == SIZE - 1:  # last row
                if index == 0:
                    neighbor.append(world[row - 1][index])
                    neighbor.append(world[row - 1][index + 1])
                    neighbor.append(world[row][index + 1])

                elif index == SIZE - 1:
                    neighbor.append(world[row - 1][index])
                    neighbor.append(world[row - 1][index - 1])
                    neighbor.append(world[row][index - 1])

                else:
                    neighbor.append(world[row][index - 1])
                    neighbor.append(world[row - 1][index - 1])
                    neighbor.append(world[row - 1][index])
                    neighbor.append(world[row - 1][index + 1])
                    neighbor.append(world[row][index + 1])

            else:
                if index == 0:
                    neighbor.append(world[row - 1][index])
                    neighbor.append(world[row - 1][index + 1])
                    neighbor.append(world[row][index + 1])
                    neighbor.append(world[row + 1][index + 1])
                    neighbor.append(world[row + 1][index])

                elif index == SIZE - 1:
                    neighbor.append(world[row - 1][index])
                    neighbor.append(world[row - 1][index - 1])
                    neighbor.append(world[row][index - 1])
                    neighbor.append(world[row + 1][index - 1])
                    neighbor.append(world[row + 1][index])

                else:
                    neighbor.append(world[row - 1][index - 1])
                    neighbor.append(world[row - 1][index])
                    neighbor.append(world[row - 1][index + 1])
                    neighbor.append(world[row][index + 1])
                    neighbor.append(world[row + 1][index + 1])
                    neighbor.append(world[row + 1][index])
                    neighbor.append(world[row + 1][index - 1])
                    neighbor.append(world[row][index - 1])

            live_neighbor = neighbor.count(1)

            # alive cell
            if world[row][index] == 1:
                if (live_neighbor <= 1 or live_neighbor >= 4):  # die
                    newWorld[row][index] = 0
            # dead cell
            elif world[row][index] == 0:
                if live_neighbor == 3:
                    newWorld[row][index] = 1    # revive

    return newWorld


def printWorld(world):
    """ print each generation's world """

    printSep()  # separator
    for row in range(SIZE):
        print('|', end='')
        for index in range(SIZE):
            if world[row][index] == 1:  # alive cell -> 'x'
                print('x', end='')
            else:
                print(' ', end='')
        print('| row', row)
    printSep()


#----
# main

# get grid sidelength
try:
    input_size = int(input('Grid sidelength (default 20): '))
    if input_size >= 20:
        SIZE = input_size

except ValueError:
    SIZE = 20

# get generation number
while True:
    try:
        input_gen = int(input('Max generation: '))
        if input_gen > 0:
            break

    except ValueError:
        input_gen = input('Max generation: ')

# initialize
world = []
for i in range(SIZE):
    lst = []
    for j in range(SIZE):
        lst.append(0)
    world.append(lst)
    # list world became list of sublists of zero elements.

# initial alive cells
default = [[0, 1], [1, 1], [2, 1], [10, 10], [10, 11], [10, 12], [11, 10], [12, 10], [12, 11], [12, 12]]
for i in default:
    world[i[0]][i[1]] = 1


# Compute:
now = 0
while now <= input_gen:
    printWorld(world)
    world = Automation(world)
    now += 1
    time.sleep(1)
