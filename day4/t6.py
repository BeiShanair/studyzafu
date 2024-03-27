def f(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    else:
        return f(n - 1) + f(n - 2) + f(n - 3)


for i in range(1, 21):
    print(f(i), end=" ")
