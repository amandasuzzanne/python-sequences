#!/usr/bin/env python3

def print_fibonacci(length):
    ls = []
    if length > 0:
        ls.append(0)
    if length >= 2:
        ls.append(1)
        for i in range(2, length):
            ls.append(ls[-1] + ls[-2])
    print(ls)
    return
    