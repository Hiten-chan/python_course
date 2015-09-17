word = input()
number = int(input())

if word == "óòşã":
    if number % 10 == 1 and number != 11 and number % 100 != 11:
        print(number, word)
    elif (
                    number % 10 == 2 or number % 10 == 3 or number % 10 == 4) and number % 100 != 12 and number % 100 != 13 and number % 100 != 14:
        print(number, word + "à")
    else:
        print(number, word + "îâ")
elif word == "ëîæêà":
    if number % 10 == 1 and number != 11 and number % 100 != 11:
        print(number, word)
    elif (
                    number % 10 == 2 or number % 10 == 3 or number % 10 == 4) and number % 100 != 12 and number % 100 != 13 and number % 100 != 14:
        print(number, word[0:4] + "è")
    else:
        print(number, word[0:3] + "åê")
