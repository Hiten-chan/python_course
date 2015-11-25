import re
import sys

data = sys.stdin.read()

results = re.findall("(y|Y)ou", data)
print(len(results))
