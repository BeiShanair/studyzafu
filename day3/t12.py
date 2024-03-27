import random
num = random.randint(1, 100)
i = int(input("请输入一个1-100之间的整数："))
count = 0
while i != num:
    if i < num:
        print("您猜的数小了！请重猜！")
    else:
        print("您猜的数大了！请重猜！")
    i = int(input("请再次输入："))
    count += 1
print("恭喜你！猜对了！", "共猜了", count, "次")
