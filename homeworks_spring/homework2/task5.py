n = int(input())
lst = []
for i in range(n):
    t = input().split(' ')
    if len(t) == 1:
        lst.append(t)
    else:
        t.pop(1)
        lst.append(t)

dic = {}
for i in lst:
    if len(i) == 1 and i[0] not in dic:
        dic[i[0]] = None
    elif i[0] not in dic:
        dic[i[0]] = i[1:]
    else:
        dic[i[0]].append(i[1:])
                        

def cheack(a, b):
    if a == b:
        return 'Yes'
    elif dic[a] != None and b in dic[a]:
        return 'Yes'
    elif dic[a] == None:
        return 'No'
    else: 
        for q in dic[a]:
            if cheack(q, b) == 'Yes':
                return 'Yes'
    return cheack(q, b)
            

c = int(input())
h = c
t = []
ans = []
for i in range(c):
    t.append(input())
 
c = []
p = []
for i in t:
    for j in p:
        if cheack(i, j) == 'Yes':
            if i not in c:
                c.append(i)
    p.append(i)

for i in c:
    print(i)
