#!/usr/bin/env python3

import math


# Given an array of integers, return a new array such that each element at index `i` of the new array is the product of all the numbers in the original array except the one at `i`.
# Follow-up: What if you can't use division?

def product(lst: list) -> list:
    result = []
    for i in range(len(lst)):
        aux = lst.copy()
        aux.pop(i)
        result.append(math.prod(aux))
    return result

if __name__ == '__main__':
    values = [1, 2, 3, 4, 5]
    print(product(values))
