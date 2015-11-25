import re
import sys

data = sys.stdin.read()

results = re.findall("you", data)
print(len(results))
