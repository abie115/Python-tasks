#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Napisz funkcję sum_from_one_to_n zwracającą sume liczb od 1 do n.
Jeśli podany argument jest mniejszy od 1 powinna być zwracana wartość 0.
"""


def sum_from_one_to_n(n):
    suma = 0
    if n < 1:
        return suma
    else:
        for i in range(n + 1):
            suma += i
    return suma


input = 999
output = 499500

print(sum_from_one_to_n(input))
