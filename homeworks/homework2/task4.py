lst = input().split(" ")
a = int(lst[0])


def euclid(x, y):
    y = int(y)
    if y == 0:
        return x
    elif x % y == 0:
        return y
    else:
        return euclid(y, x % y)


def rpfilter(a, *args):
    numbers = []
    s = list(args[0])
    i = 1
    print(s)
    while i < len(s):
        if euclid(a, int(s[i])) == True:
            numbers.append(int(s[i]))
            i += 1
        else:
            i += 1
    return numbers

n = rpfilter(a, lst)

if len(n) > 0:
    for k in n:
        print(k, end=' ')
else:
    print("None")