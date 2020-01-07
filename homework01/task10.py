#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Napisz funkcję common_chars(string1, string2), która zwraca alfabetycznie
uporządkowaną listę wspólnych liter z lańcuchów string1 i string2.
Oba napisy będą składać się wyłacznie z małych liter.
"""


def common_chars(string1, string2):
    str1 = string1.replace(" ","")
    str2 = string2.replace(" ","")
    return sorted(set(str2).intersection(str1))
    

input1 = "this is a string"
input2 = "ala ma kota"
output = ['a', 't']

print(common_chars(input1,input2))