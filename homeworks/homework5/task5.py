import re
import sys

data = sys.stdin.read()

print(re.sub('(\W)+', " ", data))
