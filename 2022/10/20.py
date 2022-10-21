#!/usr/bin/env python3


# Given a list of numbers and a number `k`, return whether any two numbers from the list add up to `k`.
# Bonus: Do it in one line.

def read_input(filename):
    with open(filename) as f:
        values = [int(line) for line in f.readlines()]
    return values


def check_addition(lst: list, k: int) -> list:
    for i in range(len(lst)):
        for j in range(len(lst)):
            if (not i >= j) and lst[i] + lst[j] == k:
                return [lst[i], lst[j]]

if __name__ == '__main__':
    k = 17
    values = read_input('inputs/20.txt')
    print(check_addition(values, k))

# Bonus:
# result = [(lst[i], lst[j]) for i in range(len(lst)) for j in range(len(lst)) if ((not i >= j) and (lst[i] + lst[j] == k))]
