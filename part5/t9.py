season = ["春季", "夏季", "秋季", "冬季"]
i = int(input("请输入月份："))
if i < 1 or i > 12:
    print("输入有误")
else:
    if i in [3, 4, 5]:
        print("这个月份是：", season[0])
    elif i in [6, 7, 8]:
        print("这个月份是：", season[1])
    elif i in [9, 10, 11]:
        print("这个月份是：", season[2])
    else:
        print("这个月份是：", season[3])
        