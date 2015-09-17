lst = input().split(" ")
numbers = 0
n = 0

for i in lst:
    numbers += int(i)
    n += 1

print(numbers/n)
