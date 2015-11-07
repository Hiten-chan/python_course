f1 = open("yazkora.txt", 'r')
l = f1.read().replace("\n", "").split(".")
f1.close()

out = []

for i in l:
    p = i.split(" ")
    out.append([word for word in p if word.endswith('yo')])

f2 = open('answer.txt', 'w' )

for item in out:
    for j in item:
        f2.write(j + " ")
    f2.write("\n")

f2.close()
