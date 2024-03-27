def t(a):
    b = a.split(" ")
    s = ""
    for i in b:
        s += i[0].upper()
    return s


a = input("请输入短语：")
print(t(a))
