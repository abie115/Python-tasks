#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Napisz funkcję leet_speak, która podmienia w podanym napisie niektóre litery
na podobnie wyglądające cyfry: 'e' na '3', 'l' na '1', 'o' na '0', 't' na '7'.
Np. leet('leet') powinno zwrócić '1337'.
"""


def leet_speak(text):
    replacements = (
        ('e', '3'), ('l', '1'), ('o', '0'), ('t', '7'), ('s', '5'), ('a', '4'), ('b', '8'), ('g', '6'), ('i', '1'),
        ('p', '9'), ('z', '2')
    )
    new_speak = text
    for old, new in replacements:
        new_speak = new_speak.replace(old, new)
    return new_speak


input = 'leet'
output = '1337'

print(leet_speak(input))
