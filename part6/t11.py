dicTXL = {"小新": {"手机": "13913000001", "QQ": "18191220001"},
          "小亮": {"手机": "13913000002", "QQ": "13913000002"},
          "小刚": {"手机": "13913000003", "QQ": "18191220003"}}

dicOther = {"大刘": {"手机": "13914000001", "QQ": "18191230001"},
            "大王": {"手机": "13914000002", "QQ": "18191230002"},
            "大张": {"手机": "13914000003", "QQ": "18191230003"}}

dicTXL.update(dicOther)
for key in dicTXL:
    print(key, dicTXL[key])

dicWX = {"小新": {"微信": "Xx9907"},
         "小刚": {"微信": "Gang1004"},
         "大王": {"微信": "Jack_w"},
         "大刘": {"微信": "Liu666"}}

for key in dicTXL:
    if key in dicWX:
        dicTXL[key].update(dicWX[key])
    else:
        dicTXL[key]["微信"] = dicTXL[key]["手机"]

for key in dicTXL:
    print(key, dicTXL[key])

print("大王原来的通信方式：\n", dicTXL["大王"])
dicTXL["大王"]["手机"] = "13914000004"
print("大王更改后的通信方式：\n", dicTXL["大王"])

a = input("请输入要查询的学生姓名：")
if a in dicTXL:
    print(a, dicTXL[a])
else:
    print("查无此人！")
