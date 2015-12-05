import requests
import re
from urllib.parse import urlencode

f = open('links.txt', 'r')

l = f.read().split('\n')
f.close()

out = []

for i in l:
    html = requests.get(i).text
    result = re.findall("[\w\.]+@[\w\.]+", html)
    if len(result) > 0: 
        for j in result:
            if j not in out:
                out.append(j)            

f2 = open('email_addresses.txt', 'w' )
for item in out:
    f2.write(item)
    f2.write("\n")
f2.close()
