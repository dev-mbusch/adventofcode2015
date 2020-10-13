"""
https://adventofcode.com/2015/day/5
"""

import re


def check_three_vowels(input_str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    counter = 0

    for char in input_str:
        if char in vowels:
            counter += 1
        else:
            continue
    if counter >= 3:
        return True
    else:
        return False


def check_double_letter(input_str):
    precessor = ''

    for char in input_str:
        if char == precessor:
            return True
            break
        else:
            precessor = char

    return False


def check_not_forbidden_strings(input_str):
    pattern = re.compile("ab|cd|pq|xy")

    match = re.search(pattern, input_str)

    if match:
        return False
    else:
        return True


def check_string(input_str):
    if check_three_vowels(input_str) == True and check_double_letter(input_str) == True and check_not_forbidden_strings(input_str) == True:
        return 'nice'
    else:
        return 'naughty'

# Part Two functions

def indices(lst, element):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)

def check_for_pairs(input_str):
    valid_pair_counter = 0
    n = 2
    liste = [input_str[i:i+n] for i in range(0, len(input_str)-1, n-1)]
    for i in range(0, len(liste)-1):
        #match_indices = [j for j, e in enumerate(liste) if e == liste[i]]
        match_indices = indices(liste, liste[i])
        
        if liste.count(liste[i]) > 2:
            print(match_indices)
            valid_pair_counter += 1
        elif liste.count(liste[i]) == 2 and match_indices[1] - match_indices[0] > 1:
            print(match_indices)
            valid_pair_counter += 1
        else:
            continue
    
    if valid_pair_counter >= 1:
        print(liste)
        return True
    else: 
        return False


    # for pair in liste:
    #     if liste.count(pair) > 1:
    #         pairs.append(pair)

    # return pairs

def check_for_overlap(input_str):
    pair = check_for_pairs(input_str)
    char = pair[0][:1]
    if char * 3 in input_str:
        return False
    else:
        return True

def check_for_palindrom(input_str):
    preprecessor = ''
    precessor = ''

    for char in input_str:
        if char == preprecessor:
            return True
            break
        else:
            preprecessor = precessor
            precessor = char

    return False

# def check_string_2(input_str):
#     if len(check_for_pairs(input_str)) > 1 and check_for_overlap(input_str) and check_for_palindrom(input_str):
#         return 'nice'
#     else:
#         return 'naughty'

def check_string_2(input_str):
    if check_for_pairs(input_str) and check_for_palindrom(input_str):
        return 'nice'
    else:
        return 'naughty'

# Test Cases Part One
assert check_string('ugknbfddgicrmopn') == 'nice'
assert check_string('aaa') == 'nice'
assert check_string('jchzalrnumimnmhp') == 'naughty'
assert check_string('haegwjzuvuyypxyu') == 'naughty'
assert check_string('dvszwmarrgswjxmb') == 'naughty'

# Test Cases Part Two
assert check_string_2('qjhvhtzxzqqjkmpb') == 'nice'
assert check_string_2('xxyxx') == 'nice'
assert check_string_2('uurcxstgmygtbstg') == 'naughty'
assert check_string_2('ieodomkazucvgmuy') == 'naughty'

# TODO
# THINK ABOUT WHAT'S AN ACTUAL OVERLAP --> jhghdfjdaaa YES/NO?

if __name__ == '__main__':
    counter_mp = 0
    counter_mp_2 = 0

    with open('./day05_input_mp.txt', 'r') as fh:
        lines_mp = fh.readlines()

    for line in lines_mp:
        if check_string(line) == 'nice':
            counter_mp +=1

    print(f'MP Count: {counter_mp}')


    with open('./day05_input_mp_2.txt', 'r') as fh:
        lines_mp = fh.readlines()

    for line in lines_mp:
        if check_string_2(line) == 'nice':
            counter_mp_2 +=1

    print(f'MP Count 2: {counter_mp_2}')

    # counter_mb = 0
    # counter_mb_2 = 0

    # with open('./day05_input_mb.txt', 'r') as fh:
    #     lines_mb = fh.readlines()

    # for line in lines_mb:
    #     if check_string(line) == 'nice':
    #         counter_mb +=1

    # for line in lines_mb:
    #     if check_string_2(line) == 'nice':
    #         counter_mb_2 +=1

    # print(f'MB Count: {counter_mb}')
    # print(f'MB Count 2: {counter_mb_2}')


