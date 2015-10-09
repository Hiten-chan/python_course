s = input().split(" ")
a = int(s[0])
b = int(s[1])


def euclid(a, b):
    if b == 0:
        return a
    elif a % b == 0:
        return b
    else:
        return euclid(b, a % b)

print(euclid(a, b))
