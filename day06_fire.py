"""
https://adventofcode.com/2015/day/6
"""

# TODO: 1. BITWISE OPERATION --> Je nach INSTRUCTION das jeweilige Element setzen
# TODO: 2. ZÄHLEN VON EINSEN IMPLEMENTIEREN

import re
from pprint import pprint as pp
from re import findall

# Grid Initilization
gridsize = 10
grid = [[0 for _i in range(gridsize)] for _j in range(gridsize)]


def find_action(instructions: str) -> str:
    action = ""

    if instructions.find("turn on") > -1:
        action = "turn_on"
    elif instructions.find("turn off") > -1:
        action = "turn_off"
    else:
        action = "toggle"

    return action
# turn on 458,710 through 688,847
# toggle 12,484 through 878,562
# turn off 241,964 through 799,983
#print(find_action("turn off 241,964 through 799,983"))

def find_coordinates(instructions: str):

    coordinates = re.findall("\d+",instructions)
    start = (int(coordinates[0]), int(coordinates[1]))
    end = (int(coordinates[2]), int(coordinates[3]))

    return start, end

def calculate_switch_plan(start_grid, start_point, end_point):
    end_grid = start_grid
    x1, y1 = start_point
    x2, y2 = end_point

    for i, row in enumerate(end_grid[x1:x2+1]):
        for j, column in enumerate(row[y1:y2+1]):
            end_grid[i][j] = 1

    return end_grid


start, end = find_coordinates("turn on 0,0 through 2,2")

pp(grid)

calculate_switch_plan(grid, start, end)
print('\n####################\n')
pp(grid)
