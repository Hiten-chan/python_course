import re
import sys

data = sys.stdin.read()
phones = data.split('\n')

h = [0,1,2,3,4,5,6,7,8,9]

for i in phones:
    for j in h:
        if len(re.findall(str(j)+'{3}', i)) != 0:
            print(i)
            break
