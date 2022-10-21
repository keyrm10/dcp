#!/usr/bin/env python3


# Given a list of numbers and a number `k`, return whether any two numbers from the list add up to `k`.
# Bonus: Do it in one line.


## Solution 1

def check_addition(lst: list, k: int) -> bool:
    for i in lst:
        if k - i in lst:
            return True
    return False

# result = any(k - i in lst for i in lst)

if __name__ == '__main__':
    values = [10, 15, 3, 7]
    k = 17
    print(check_addition(values, k))


## Solution 2

# def check_addition(lst: list, k: int) -> list:
#     for i in range(len(lst)):
#         for j in range(len(lst)):
#             if (not i >= j) and lst[i] + lst[j] == k:
#                 return [lst[i], lst[j]]

# result = [(lst[i], lst[j]) for i in range(len(lst)) for j in range(len(lst)) if ((not i >= j) and (lst[i] + lst[j] == k))]
