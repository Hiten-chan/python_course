def character(filename, s):
    filename = str(filename)
    s = str(s)
    f1 = open(filename, 'r')
    l = f1.read().replace("\n", " ").split(".")
    f1.close()

    out = []

    for i in l:
        p = i.split(" ")
        out.append([word for word in p if word.endswith(s)])

    f2 = open('answer.txt', 'w' )

    for item in out:
        for j in item:
            f2.write(j + " ")
        f2.write("\n")
    f2.close()
