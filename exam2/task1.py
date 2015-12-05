import re

f = open('hp5.txt', 'r')

l = f.read().split('\n')
f.close()

dic = {}
m = 0
n = 0
k = 0

for i in l:
    
    o = re.findall('whispered [A-Z][a-z]+ [A-Z][a-z]+|whispered [A-Z][a-z]+|[A-Z][a-z]+ [A-Z][a-z]+ whispered|[A-Z][a-z]+ whispered', i)
    if len(o) > 0:
        r = o[0].split(' ')
        if r[0] == 'whispered' and len(r) == 3:
            if r[1]+' '+r[2] in dic:
                dic[r[1]+' '+r[2]] += 1
            else:
                dic[r[1]+' '+r[2]] = 1
        elif r[0] == 'whispered' and len(r) == 2:
            if r[1] in dic:
                dic[r[1]] += 1
            else:
                dic[r[1]] = 1
        elif r[1] == 'whispered':
            if r[0] in dic:
                dic[r[0]] += 1
            else:
                dic[r[0]] = 1
        elif r[2] == 'whispered':
            if r[0]+' '+r[1] in dic:
                dic[r[0]+' '+r[1]] += 1
            else:
                dic[r[0]+' '+r[1]] = 1
                
for key in dic.keys():
    if dic[key] > n:
        k = key
        n = dic[key]
        
print(n, k)
