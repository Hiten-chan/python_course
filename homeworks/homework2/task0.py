# -*- coding: utf8 -*-
word = str(input())
n = int(input())

def plural(number, words):
    if number % 10 == 1 and number != 11 and number % 100 != 11:
        return words[0]
    elif number % 10 in [2, 3, 4] and number % 100 not in [12, 13, 14]:
        return words[1]
    else:
        return words[2]

if word == "ложка":
    w = ["ложка", "ложки", "ложек"]
    cor_word = plural(n, w)
elif word == "утюг":
    w = ["утюг", "утюга", "утюгов"]
    cor_word = plural(n, w)
elif word == "гармошка":
    w = ["гармошка", "гармошки", "гармошек"]
    cor_word = plural(n, w)
elif word == "чайник":
    w = ["чайник", "чайника", "чайников"]
    cor_word = plural(n, w)

print(n, cor_word)
