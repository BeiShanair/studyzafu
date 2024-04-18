import random
list1 = []
a = 0
for i in range(50):
    list1.append(random.randint(0, 10))
    if a % 10 == 0 and a != 0:
        print()
    a += 1
    print("{:^5}".format(list1[i]), end=" ")

print()

for i in range(11):
    print(i, "出现的次数为：", list1.count(i))
