"""
https://adventofcode.com/2015/day/1
"""

def find_floor(instructions: str) -> int:
    """
    Just counts all occurences of '(' and ')'
    and subtracts them from another.
    """
    go_up = instructions.count('(')
    go_down = instructions.count(')')
    return go_up - go_down

def find_floor_2(instructions: str) -> int:
    """
    Finds the position where Santa enters the basement.
    """
    floor = 0
    position = 0

    for i, instruction in enumerate(instructions):
        if instruction == '(':
            floor += 1
        elif instruction == ')':
            floor -= 1
        if floor == -1:
            position = i + 1
            break

    return position

# Given Test Cases Part One
assert find_floor('(())') == 0
assert find_floor('()()') == 0
assert find_floor('(((') == 3
assert find_floor('))(((((') == 3
assert find_floor('())') == -1
assert find_floor(')))') == -3
assert find_floor(')())())') == -3

# Given Test Cases Part Two
assert find_floor_2(')') == 1
assert find_floor_2('()())') == 5
assert find_floor_2('())()') == 3

if __name__ == '__main__':
    with open(r'day01_input.txt', 'r') as f:
        INPUT_TEXT = f.read()
        part1_target_floor = find_floor(INPUT_TEXT)
        print(f'Part One - Target floor is: {part1_target_floor}')
        part2_target_floor = find_floor_2(INPUT_TEXT)
        print(f'Part Two - Position to enter basement: {part2_target_floor}')

