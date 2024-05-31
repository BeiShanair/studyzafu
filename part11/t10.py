mini_dic1 = {"红": "red", "黄": "yellow", "蓝": "blue", "绿": "green"}
mini_dic2 = {"黑": "black", "白": "white"}
new_dic = dict(mini_dic1, **mini_dic2)

print("所有条目：")
for k, v in new_dic.items():
    print(k, v)

color = input("请输入颜色：")
if color in new_dic:
    print(new_dic[color])
else:
    print("没有该中文对应的英文单词！")
