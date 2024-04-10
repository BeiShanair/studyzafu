def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)


n = int(input("请输入一个整数："))
s = []
for i in range(1, n + 1):
    s.append(f(i))
print(s)
