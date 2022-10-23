#!/usr/bin/env python3


# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.


def get_lowest_positive_int(lst: list) -> int:
    lst.sort()
    for i in range(1, lst[-1:][0] + 2):
        if i not in lst:
            return i

if __name__ == '__main__':
    lst = [3, 4, -1, 1]
    print(get_lowest_positive_int(lst))
