"""
https://adventofcode.com/2015/day/7

https://wiki.python.org/moin/BitwiseOperators

Hypothesis #1
1. All cables are set to 0 because no cable has yet received a signal.

2. When there are more than one operand per side on a logic gate we presume the logic works as follows:
i.e.: kg OR kf -> kh

Truth Table
a b      OR
0 0      0
0 1      1
1 0      1
1 1      1

k        k
    OR
g        f


That means if our hypothesis is right the given example results in the following:

If any of these four are 1 then k and h are set to 1.

Hypothesis #2
1. Wires are not initialized. If they don't have a signal they aren't relevant in the step.

2. Each line has a maximum of two operands on the left side.

3. Converting decimal to binary is easy like that:
a = 16
b = 16
print(bin(a+b))

a = bin(16)
print(a)
print(int(a, base=2))

4. Pseudocode

Go through the whole list of instructions and take the right side and use it as keys in a dictionary.
Initializing every key with None.

Outer While loop that checks if `a` is not None (or maybe for part two if there is any key left with None as value).

Inner loop: Go through left side and look for instructions a la `44430 -> b`.



"""

import re
from os import kill

# def read_instructions(filename):
#     operation_pattern = '[A-Z]+'

#     with open(filename, 'r') as fh:
#         for line in fh.readlines():
#             instructions = line.strip('\n').split(' -> ')
#             left_side = instructions[0].split()
#             right_side = instructions[1]

#             if 'NOT' in left_side:


#             print(left_side, right_side)
#             # operation = re.findall(operation_pattern, left_side)[0]
#             # print(instructions, left_side, right_side, operation)

# read_instructions(r'day07_input_mb.txt')
