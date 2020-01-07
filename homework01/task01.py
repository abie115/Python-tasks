#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Zad 2. Napisz funkcję even_elements zwracającą listę,
która zawiera tylko elementy z list o parzystych indeksach.
"""


def even_elements(lista):
    even_list = []
    for i in range(len(lista)):
        if (i % 2) == 0:
           even_list.append(lista[i])
    return even_list

input = [1, 2, 3, 4, 5, 6]
output = [1, 3, 5]
print(even_elements(input))