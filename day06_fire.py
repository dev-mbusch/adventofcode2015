"""
https://adventofcode.com/2015/day/6
"""


import re
from pprint import pprint as pp

# Grid Initilization
def grid_initialization(size: int, value: int):
    gridsize = size
    init_grid = [[value for _i in range(gridsize)] for _j in range(gridsize)]
    return init_grid


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

    for row in range(x1, x2 + 1):
        for col in range(y1, y2 + 1):
            if action == 'toggle':
                end_grid[row][col] = (end_grid[row][col] + 1) % 2
            elif action == 'turn_on':
                end_grid[row][col] = 1
            elif action == 'turn_off':
                end_grid[row][col] = 0
            else:
                raise ValueError(f'The provided action ´{action}´ is not a valid operation.')

    return end_grid

def compute_lights_on(grid):
    counter_lights_on = 0

    for row in grid:
        counter_lights_on += row.count(1)

    return counter_lights_on

def set_brightness(start_grid, start_point, end_point, action):
    end_grid = start_grid
    x1, y1 = start_point
    x2, y2 = end_point

    for row in range(x1, x2 + 1):
        for col in range(y1, y2 + 1):
            if action == 'toggle':
                end_grid[row][col] += 2
            elif action == 'turn_on':
                end_grid[row][col] += 1
            elif action == 'turn_off':
                end_grid[row][col] -= 1
            else:
                raise ValueError(f'The provided action ´{action}´ is not a valid operation.')
            if end_grid[row][col] < 0:
                end_grid[row][col] = 0

    return end_grid

def compute_brightness_value(grid):

    brightness_value = 0

    for row in grid:
        brightness_value += sum(row)

    return brightness_value

if __name__ == '__main__':

    # MB
    with open('day06_input_mb.txt', 'r') as fh:
        grid_1 = grid_initialization(1000, 0)

        for line in fh.readlines():
            start, end = parse_coordinates(line)
            action = parse_action(line)
            grid_1 = set_switch_plan(grid_1, start, end, action)

        print(f'MB - Number of lights switched on: {compute_lights_on(grid_1)}.')

    with open('day06_input_mb.txt', 'r') as fh:
        grid_2 = grid_initialization(1000, 0)

        for line in fh.readlines():
            start, end = parse_coordinates(line)
            action = parse_action(line)
            grid_2 = set_brightness(grid_2, start, end, action)

        print(f'MB - Brightness value: {compute_brightness_value(grid_2)}.')

    # MP

    with open('day06_input_mp.txt', 'r') as fh:
        grid_1 = grid_initialization(1000, 0)

        for line in fh.readlines():
            start, end = parse_coordinates(line)
            action = parse_action(line)
            grid_1 = set_switch_plan(grid_1, start, end, action)

        print(f'MP - Number of lights switched on: {compute_lights_on(grid_1)}.')

    with open('day06_input_mp.txt', 'r') as fh:
        grid_2 = grid_initialization(1000, 0)

        for line in fh.readlines():
            start, end = parse_coordinates(line)
            action = parse_action(line)
            grid_2 = set_brightness(grid_2, start, end, action)

        print(f'MP - Brightness value: {compute_brightness_value(grid_2)}.')