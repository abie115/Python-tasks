#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Napisz funkcję sum_div35(n), która zwraca sumę wszystkich liczb podzielnych
przez 3 lub 5 mniejszych niż n.
"""


def sum_div35(n):
    n_div_35 = []
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            n_div_35.append(i)
    return sum(n_div_35)


input = 100
output = 2318

print(sum_div35(input))
