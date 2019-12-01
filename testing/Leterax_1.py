"""
Published under the  MIT license.
Copyright (c) 2019 Leterax https://github.com/Leterax
"""


import math
from itertools import permutations

import numba as nb


def is_vampire_number_large(num):
    fang_minus_1, even = divmod(int(math.log10(num)), 2)
    if even:
        num_split = sorted(f"{num}")
        for x in range(10 ** fang_minus_1, 10 ** (fang_minus_1 + 1) - 1):
            b = num // x
            # if x >= b: continue
            if not num % x and sorted(f"{x}{b}") == num_split:
                return True
    return False


@nb.njit(fastmath=True, cache=True)
def convert(n):
    return [(n // (10 ** i)) % 10 for i in range(int(math.log10(n) + 1) - 1, -1, -1)]


def concatenate2x2(a, b):
    return a * 100 + b


def concatenate_xxx(n):
    return sum([x * 10 ** (len(n) - (i + 1)) for i, x in enumerate(n)])


def is_vampire_number(num):
    c = concatenate2x2
    digits = convert(num)
    if num < 1000:
        return False
    if num < 10000:
        perms = set(permutations(digits, 2))
        for a, b in perms:
            p = c(a, b)
            if p < 10: continue
            n = num // p
            if n in perms and not (p % 10 and n % 10): return True
        return False

    return is_vampire_number_large(num)


convert(12346789)
