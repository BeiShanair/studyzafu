import random

count = 0
r_num = random.randint(1, 100)
while True:
    num = int(input("请输入一个1-100的整数："))
    if num > r_num:
        print("您猜的数大了！请重猜！")
        count += 1
    elif num < r_num:
        print("您猜的数小了！请重猜！")
        count += 1
    else:
        print("恭喜您！猜对了！")
        count += 1
        break

print("一共猜了{}次".format(count))
