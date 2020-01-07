#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Napisz funkcję euclidean_distance obliczającą odległość między
dwoma punktami przestrzeni trójwymiarowej. Punkty są dane jako
trzyelementowe listy liczb zmiennoprzecinkowych.
np. odległość pomiędzy punktami (0, 0, 0) i (3, 4, 0) jest równa 5.
"""

import math


def euclidean_distance(x, y):
    return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 + (x[2] - y[2]) ** 2)


input = [[2.3, 4.3, -7.5], [2.3, 8.5, -7.5]]
output = 4.2
print(euclidean_distance(input[0], input[1]))
