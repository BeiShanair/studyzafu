import random
n = int(input("请输入一个数（小于1000）："))
a = []
for i in range(n):
    a.append(random.randint(1, 1000))
print(a)

b = []
for i in a:
    if i not in b:
        b.append(i)
b.sort()
print(b)
