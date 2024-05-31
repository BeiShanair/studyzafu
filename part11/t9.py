user = {"admin": "123", "usera": "111", "userb": "456"}
count = 0
while count < 3:
    user_name = input("请输入用户名：")
    password = input("请输入密码：")

    if user_name not in user:
        print("用户不存在！请重新登陆！")
        count += 1
    else:
        if user[user_name] == password:
            print("登陆成功！")
            break
        else:
            print("密码错误！请重新登陆！")
            count += 1

else:
    print("登陆超过三次，请稍后再试！")
