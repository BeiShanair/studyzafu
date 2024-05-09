a = int(input("请输入一个整数a："))
b = int(input("请输入一个整数b："))
set1 = set()
set2 = set()
set3 = set()
for i in range(a, b + 1):
    if i % 3 == 0:
        set1.add(i)
    if i % 5 == 0:
        set2.add(i)
    if i % 7 == 0:
        set3.add(i)

set4 = set1 & set2 & set3
print(set4)
print(len(set4), "个")
