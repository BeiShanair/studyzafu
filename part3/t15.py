for i in range(1, 10):
    for j in range(1, i+1):
        s = "{0}*{1}={2}".format(j, i, i*j)
        print("{:<10}".format(s), end="")
    print()
