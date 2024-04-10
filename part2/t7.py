# 输入身份证号码
id_card_number = input("请输入身份证号码：")

# 截取身份证号码中的出生年月日
year_number = id_card_number[6:10]
month_number = id_card_number[10:12]
day_number = id_card_number[12:14]

# 输出出生年月日
print("出生年月日为", year_number, "年", month_number, "月", day_number, "日")

# 判断性别
sex_number = eval(id_card_number[16:17]) % 2
if sex_number == 0:
    print("性别:女")
else:
    print("性别:男")

# 加密身份证号码
encrypted_id_card_number = id_card_number[:6] + "*" * 8 + id_card_number[14:]
print("加密后的身份证号码为", encrypted_id_card_number)
