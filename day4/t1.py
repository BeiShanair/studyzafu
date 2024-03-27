def check(i):
    if i[::-1] == i:
        return True
    else:
        return False


a = input("请输入一个字符串：")
if check(a):
    print("True")
else:
    print("False")
