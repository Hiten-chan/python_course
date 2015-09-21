d = {}
for i in list(input()):
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for key in sorted(d):
    print(key, d[key])