n = int(input())
lst = []
i = 1
l = 1

while i <= n:
    i += 1
    lst.append(int(input()))

def prime(k):
    d = 2
    while k % d != 0:
        d += 1
    return d == k

while l <= n:
    w = prime(int(lst[l-1]))
    l += 1
    print(w)
