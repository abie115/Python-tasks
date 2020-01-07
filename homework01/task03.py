#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Zad 4. Napisz funkcje oov(text, vocab), która zwraca listę wyrazów
(bez duplikatów), które występują w tekście text i nie występują w liście
znanych wyrazów vocab. Argumenty funkcji text i vocab to odpowiednio łańcuch
znakowy i lista łańuchów znakowych (oov = out of vocabulary)
"""


def oov(text, vocab):
    words = []
    splits=sorted(set(text.split()))
    for w in splits: 
            if w not in vocab:
                words.append(w)
    return words

input = "this is a string , which i will use for string testing"
vocab = [',', 'this', 'is', 'a', 'which', 'for', 'will', 'i']
output = ['string', 'testing', 'use']
print(oov(input,vocab))
