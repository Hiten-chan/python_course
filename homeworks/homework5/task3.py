import re
import sys

data = sys.stdin.read()
data = data.split('\n')

count = 1
r = []

for i in data:
    r = re.findall("\w+ = ", i)
    if len(r) > 0:
        l = r[0].split(' ')
        print(str(count) + " " + l[0])
    count += 1
