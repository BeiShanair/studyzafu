import random
num = random.randint(1, 100)
i = int(input("请输入一个1-100之间的整数："))
count = 0
while i != num:
    if i < num:
        print("猜小了")
    else:
        print("猜大了")
    i = int(input("请再次输入："))
    count += 1
print("猜对了", "共猜了", count, "次")
