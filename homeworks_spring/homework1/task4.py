n = int(input())
f = list(input().split(' '))
f.reverse()
i = int(input())

d = {}
out = []

for j in range(1, i + 1):
    g = list(input().split(' '))
    if g[0] in d:
        d[g[0]][g[1]] = g[2]
    else:
        d[g[0]] = {g[1]: g[2]}

e = input()

for j in range(0, n):
    if e in d[f[j]].keys():
        if d[f[j]][e] != '_':
            e = d[f[j]][e]
        elif d[f[j]][e] == '_':
            for i in range(j, n):
                out.append(f[i])
            out.reverse()
            for i in out:
                print(i, end = ' ')
            break
