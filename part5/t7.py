def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)


a = int(input("请输入一个整数："))
s = []
for i in range(1, a + 1):
    s.append(f(i))
print(s)
