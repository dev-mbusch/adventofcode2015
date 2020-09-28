"""
https://adventofcode.com/2015/day/2
"""

import math

TEST_INPUT = '2x3x4'

def calculate_squarefeet(package: str) -> int:
    l, w, h = package.split('x')

    package_surfaces = (2 * int(l) * int(w), 2 * int(w) * int(h), 2 * int(h) * int(l))
    total_package_surface = sum(package_surfaces)
    min_surface = min(package_surfaces) // 2
    return total_package_surface + min_surface

def calculate_length_ribbon(package_size: str) -> int:
    l, w, h = package_size.split('x')
    all_measurements = sorted((int(l), int(w), int(h)))
    min = all_measurements[0]
    snd_min = all_measurements[1]
    total_length = 2 * min + 2 * snd_min + math.prod(all_measurements)
    return total_length


# Test cases Part One:
assert calculate_squarefeet('2x3x4') == 58
assert calculate_squarefeet('1x1x10') == 43

# Test cases Part Two:
assert calculate_length_ribbon('2x3x4') == 34
assert calculate_length_ribbon('1x1x10') == 14

if __name__ == '__main__':
    total_squarefeet_wrapping = 0
    total_ribbon_feet = 0
    with open(r'day02_marten_input.txt', 'r') as f:
        for line in f.readlines():
            total_squarefeet_wrapping += calculate_squarefeet(line)
            total_ribbon_feet += calculate_length_ribbon(line)
        print(f'Martens Ergebnis: {total_squarefeet_wrapping}')
        print(f'Martens Ergebnis: {total_ribbon_feet}')

    total_squarefeet_wrapping = 0
    total_ribbon_feet = 0
    with open(r'day02_input.txt', 'r') as f:
        for line in f.readlines():
            total_squarefeet_wrapping += calculate_squarefeet(line)
            total_ribbon_feet += calculate_length_ribbon(line)
        print(f'MBs Ergebnis: {total_squarefeet_wrapping}')
        print(f'MBs Ergebnis: {total_ribbon_feet}')
