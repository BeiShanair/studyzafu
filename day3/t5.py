money = input("请输入金额：")
money_type = money[0:3]
if money_type == "RMB":
    money = eval(money[3:])
    print("USD", money / 6.78)
elif money_type == "USD":
    money = eval(money[3:])
    print("RMB", money * 6.78)
else:
    print("输入格式有误")
