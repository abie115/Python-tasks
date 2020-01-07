#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Napisz funkcję days_in_year zwracającą liczbę dni w roku (365 albo 366).
"""

def days_in_year(year):
    if (year % 4 == 0 and year % 100 != 0 ) or  year % 400==0:
        num=366
    else:
        num=365
    return num


input = 2019
output = 365

print(days_in_year(input))