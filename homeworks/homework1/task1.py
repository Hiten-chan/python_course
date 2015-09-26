word = input()
number = int(input())

if word == "утюг":
    if number % 10 == 1 and number != 11 and number % 100 != 11:
        print(number, word)
    elif number % 10 == [2, 3, 4] and number % 100 != [12, 13, 14]:
        print(number, word + "2")
    else:
        print(number, word + "ов")
elif word == "ложка":
    if number % 10 == 1 and number != 11 and number % 100 != 11:
        print(number, word)
    elif number % 10 == [2, 3, 4] and number % 100 != [12, 13, 14]:
        print(number, word[0:4] + "и")
    else:
        print(number, word[0:3] + "ек")
