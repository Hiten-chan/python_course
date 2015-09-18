lst = input().split(" ")
ev = []
od = []
n = 0
m = 0

for i in range(0, len(lst), 2):
    od.insert(n, int(lst[i]))
    n += 1

for i in range(1, len(lst), 2):
    ev.insert(m, int(lst[i]))
    m += 1

od.sort()
ev.sort()
ev.reverse()

for i in range (0, int(len(lst)/2)):
    print(od[i], ev[i], end=' ')