day = int(input("请输入天数："))
num = 1
if day < 0:
    print("输入有误")
else:
    for i in range(1, day + 1):
        num = (num + 1) * 2
    print("第一天摘的桃子数量为：", num, "个")
