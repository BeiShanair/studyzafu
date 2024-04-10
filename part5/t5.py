sign_up_list = [["姓名", "性别", "100米", "3000米", "跳远", "跳高"],
                ["王平", "男", 1, 1, 0, 0],
                ["李丽", "女", 0, 1, 0, 1],
                ["陈晓梅", "女", 0, 0, 1, 0],
                ["孙洪涛", "男", 0, 1, 1, 1],
                ["方亮", "男", 1, 0, 1, 0]]

s = 0

for i in range(1, len(sign_up_list)):
    if sum(sign_up_list[i][2:]) >= 2:
        s += 1
print("报名超过两项（包括两项）的学生人数：", s)
print("女生的报名情况：")
for i in range(1, len(sign_up_list)):
    if sign_up_list[i][1] == "女":
        print(sign_up_list[i])

print("报名3000米学生的姓名和性别：")
for i in range(1, len(sign_up_list)):
    if sign_up_list[i][3] == 1:
        print(sign_up_list[i][0], sign_up_list[i][1])
