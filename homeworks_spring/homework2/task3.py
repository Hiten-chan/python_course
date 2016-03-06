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
            
m = int(input())
lst2 = []
for i in range(m):
    lst2.append(input().split(' '))

met = {}
for i in lst2:
    if i[1] not in met:
        met[i[1]] = []
        met[i[1]].append(i[0])
    else:
        met[i[1]].append(i[0])

method = input()
mt = method.split(' ')

def find_met(a, b):
    if [a, b] in lst2:
        return a
    if dic[a] != None:
        for i in dic[a]:
            if find_met(i, b) != None:
                return find_met(i, b)
        return
     
print(find_met(mt[0], mt[1])) 
