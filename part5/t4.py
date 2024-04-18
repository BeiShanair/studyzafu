import random
a = []
for i in range(20):
    a.append(random.randint(1000, 5000))

print("生成的列表：", a)
su_shu = (2, 3, 5, 7)
print("不能被10以内的素数整除的元素：", end="")
for i in a:
    for j in su_shu:
        if i % j == 0:
            break
    else:
        print(i, end=" ")