def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)

list_a = []
num = int(input("请输入一个数："))
for i in range(1, num+1):
    list_a.append(f(i))
print(list_a)