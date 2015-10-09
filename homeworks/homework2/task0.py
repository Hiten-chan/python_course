# -*- coding: utf8 -*-
word = str(input())
n = int(input())

if word == "ложка":
    w = ["ложка", "ложки", "ложек"]
elif word == "утюг":
    w = ["утюг", "утюга", "утюгов"]
elif word == "гармошка":
    w = ["гармошка", "гармошки", "гармошек"]
elif word == "чайник":
    w = ["чайник", "чайника", "чайников"]

def plural(number, words = []):
    if number % 10 == 1 and number != 11 and number % 100 != 11:
        print(number, words[0])
    elif number % 10 in [2, 3, 4] and number % 100 not in [12, 13, 14]:
        print(number, words[1])
    else:
        print(number, words[2])

plural(n, w)
