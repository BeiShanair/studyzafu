num = int(input("请输入一个正整数："))
# 判断素数
if num < 2:
    print("输入有误")
else:
    for i in range(2, num):
        if num % i == 0:
            print("不是素数")
            break
    else:
        print("是素数")
