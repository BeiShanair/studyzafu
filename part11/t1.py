id_num = input("请输入18位的身份证号码：")
date = id_num[6:14]
year = id_num[6:10]
month = id_num[10:12]
day = id_num[12:14]

print("此人出生于{}年{}月{}日".format(year, month, day))
sex = id_num[16]
if int(sex) % 2 == 0:
    print("性别：女")
else:
    print("性别：男")

j_num = id_num.replace(date,"********")
print("加密后的身份证号码为：", j_num)
