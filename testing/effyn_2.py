"""
Published under the  MIT license.
Copyright (c) 2019 Effyn
"""


import math


def is_vampire_number(number):
    # largest n such that 10^n < number
    n = int(math.log10(number))
    # if n is odd, the number of digits is even
    if n % 2:
        sorted_number = sorted(f"{number}")
        start = 10 ** (n // 2)
        # for every n/2-digit number (possible fangs)
        for x in range(start, start * 10):
            # if x divides evenly into number and all digits in x and y are also in number
            if not number % x and sorted(f"{x}{number // x}") == sorted_number:
                # the number is a vampire
                return True
    return False
