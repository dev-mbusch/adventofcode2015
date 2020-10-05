"""
https://adventofcode.com/2015/day/4
"""

import hashlib

secret_mb = 'iwrupvqb'
secret_mp = 'ckczppom'
secret_test = 'abcdef'

# Test Case Part One
assert hashlib.md5(b'abcdef609043').hexdigest()[0:5].startswith('00000')

def find_hash(secret, digits):
    target_hash = '0' * digits
    counter = 0
    try_hash = ''

    while try_hash != target_hash:
        counter += 1
        try_hash = hashlib.md5(bytes(secret + str(counter), encoding='utf-8')).hexdigest()[0:digits]
    return counter

# Results Part One
print(find_hash(secret_mb, 5))
print(find_hash(secret_mp, 5))

# Results Part Two
print(find_hash(secret_mb, 6))
print(find_hash(secret_mp, 6))
