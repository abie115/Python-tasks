#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Napisz funkcję char_sum, która dla zadanego łańcucha zwraca
sumę kodów ASCII znaków. Wykorzystaj funkcję ord()
"""

def char_sum(text):
    suma=0
    for znak in text:
        suma+=ord(znak)
    return suma

input = "this is a string"
output = 1516

print(char_sum(input))

