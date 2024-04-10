# 判断一个字符串是否是回文
m = input("请输入字符串：")
if m == m[::-1]:
    print("是回文")
else:
    print("不是回文")
