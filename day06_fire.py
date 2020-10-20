"""
https://adventofcode.com/2015/day/6
"""

# TODO: 1. BITWISE OPERATION --> Je nach INSTRUCTION das jeweilige Element setzen
# TODO: 2. ZÄHLEN VON EINSEN IMPLEMENTIEREN

import re
from pprint import pprint as pp

# Grid Initilization
gridsize = 10
init_grid = [[0 for _i in range(gridsize)] for _j in range(gridsize)]


def parse_action(instructions: str) -> str:
    action = ""

    if instructions.find("turn on") > -1:
        action = "turn_on"
    elif instructions.find("turn off") > -1:
        action = "turn_off"
    else:
        action = "toggle"

    return action

def parse_coordinates(instructions: str):

    coordinates = re.findall("\d+",instructions)
    start = (int(coordinates[0]), int(coordinates[1]))
    end = (int(coordinates[2]), int(coordinates[3]))

    return start, end

def set_switch_plan(start_grid, start_point, end_point, action):
    end_grid = start_grid
    x1, y1 = start_point
    x2, y2 = end_point
    offset_x = x1
    offset_y = y1

    for i, row in enumerate(end_grid[x1:x2+1]):

        for j, column in enumerate(row[y1:y2+1]):
            if action == 'toggle':
                end_grid[j + offset_x][i + offset_y] = int(not end_grid[j][i])
            elif action == 'turn_on':
                end_grid[j + offset_x][i + offset_y] = 1
            elif action == 'turn_off':
                end_grid[j + offset_x][i + offset_y] = 0
            else:
                raise ValueError(f'The provided action ´{action}´ is not a valid operation.')

    return end_grid

def compute_lights_on(grid):
    counter_lights_on = 0

    for row in grid:
        counter_lights_on += row.count(1)

    return counter_lights_on

# Tests Part One 10x10 Grid
test_grid = []

assert compute_lights_on(set_switch_plan(init_grid, (0,0), (9,9), 'turn_on')) == 100 # Works fine
test_grid = set_switch_plan(init_grid, (0,0), (9,9), 'turn_on')

print('\n', '#' * 40, '\n')
pp(test_grid)
print('\n', '#' * 40, '\n')

assert compute_lights_on(set_switch_plan(test_grid, (0,0), (9,0), 'toggle')) == 90 # Works fine
test_grid = set_switch_plan(test_grid, (0,0), (9,0), 'toggle')
print(compute_lights_on(test_grid))

print('\n', '#' * 40, '\n')
pp(test_grid)
print('\n', '#' * 40, '\n')

# assert compute_lights_on(set_switch_plan(test_grid, (4,4), (5,5), 'turn_off')) == 86 # Works fine
# test_grid = set_switch_plan(test_grid, (4,4), (5,5), 'turn_off')

# print('\n', '#' * 40, '\n')
# pp(test_grid)
# print('\n', '#' * 40, '\n')

# assert compute_lights_on(set_switch_plan(test_grid, (0,0), (999,0), 'turn_on')) == 1_000

# WRONG ANSWER: 535162 --> "TOO LOW"

# if __name__ == '__main__':
#     with open('day06_input_mb.txt', 'r') as fh:
#     # with open('day06_input_test_smallgrid.txt', 'r') as fh:
#         grid = []
#         # print('Empty grid:')
#         # print('\n', '#' * 40, '\n')
#         # pp(grid)
#         # print('\n', '#' * 40, '\n')
#         # print('Initialized Grid:')
#         # print('\n', '#' * 40, '\n')
#         # pp(init_grid)
#         # print('\n', '#' * 40, '\n')

#         for line in fh.readlines():
#             start, end = parse_coordinates(line)
#             action = parse_action(line)
#             # print(f'Start Point: {start}, \t End Point: {end}, \t Action: {action}')
#             grid = set_switch_plan(init_grid, start, end, action)
#             # print('\n', '#' * 40, '\n')
#             # pp(grid)
#             # print('\n', '#' * 40, '\n')
#         print(f'Number of lights switched on: {compute_lights_on(grid)}.')
