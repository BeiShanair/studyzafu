num = input("数字字符串：")
zh_list = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
if num.isdigit():
    for i in num:
        print(zh_list[int(i)], end="")
else:
    print("输入有误")