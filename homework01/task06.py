#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Napisz funkcję big_no zwracającej tzw. "Big 'NO!'"
(zob. http://tvtropes.org/pmwiki/pmwiki.php/Main/BigNo)
dla zadanej liczby tj. napis typu "NOOOOOOOOOOOOO!", gdzie liczba 'O' ma być
równa podanemu argumentem, przy czym jeśli argument jest mniejszy niż 5,
ma być zwracany napis "It's not a Big 'No!'".
"""


def big_no(n):
    if n < 5:
        sentence="It's not a Big 'No!"
    else:
        sentence="Big 'N" + "O" * n + "!'"
    return sentence

input = 2
output = "It's not a Big 'No!'"
print(big_no(input))

input2 = 10
print(big_no(input2))
