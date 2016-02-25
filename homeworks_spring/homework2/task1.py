l = [A, B, C]
out = []
for i in l:
    if issubclass(D, i) == True:
        out.append(str(i)[-3])
out.sort()
print(" ".join(out))
