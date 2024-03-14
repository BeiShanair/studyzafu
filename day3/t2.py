id_card_num = input("请输入身份证号码：")
if len(id_card_num) != 18:
    print("身份证号码有误")

sex_num = eval(id_card_num[16:17])
if sex_num % 2 == 0:
    print("性别：女")
else:
    print("性别：男")