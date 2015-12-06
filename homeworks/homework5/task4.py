import re
import sys

data = sys.stdin.read()
data = data.split('\n')

count = 1
r = []

for i in data:
    if re.match(' *([#]+)', i) != None:
        count += 1
    else:
        r = re.findall(' *([\w,. ]+) = ', i)
        if len(r) > 0:
            if len(re.findall(",", i)) > 0:
                l = r[0].split(' = ')
                l = l[0].replace(',', '')
                print(str(count) + " " + l)
            else:
                l = r[0].split(' = ')
                print(str(count) + " " + l[0])
        count += 1
