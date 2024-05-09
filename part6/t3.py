user = {"admin": "123", "usera": "111", "userb": "456"}

max_try = 3
count = 0
while count < max_try:
    user_name = input("请输入用户名：")
    if user_name in user:
        password = input("请输入密码：")
        if password == user[user_name]:
            print("登录成功！")
            break
        else:
            print("密码错误！")
    else:
        print("用户名不存在！请重新登录！")
    count += 1
else:
    print("登录超过3次，请稍后再试！")
