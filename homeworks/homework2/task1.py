s = input().split(" ")
n = int(s[0])
k = int(s[1])


def fac(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


def combinations(n, k):
    if k > n:
        return 0
    elif k == n or k == 0:
        return 1
    else:
        return (fac(n) // (fac(k) * fac(n - k)))

print(combinations(n, k))
