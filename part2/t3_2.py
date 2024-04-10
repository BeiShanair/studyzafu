# 判断输入的字符串是否以.py结尾
m = input("请输入字符串：")
judge = m.endswith(".py")
if judge:
    print("yes!")
else:
    print("no!")