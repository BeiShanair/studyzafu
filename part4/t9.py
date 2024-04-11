def peach(n):
    if n == 1:
        return 1
    return 2 * (peach(n - 1) + 1)


print(peach(10))
