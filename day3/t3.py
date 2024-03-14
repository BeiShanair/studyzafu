score = int(input("请输入成绩："))
if score < 0 or score > 100:
    print("成绩不在范围内，请重新输入")
else:
    if score < 60:
        print("成绩等级为F")
    elif score < 85:
        print("成绩等级为P")
    else:
        print("成绩等级为A")
        