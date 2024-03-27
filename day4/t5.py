def f(n):
    sum = 0
    for i in n:
        sum += int(i)**2
    return sum


a = input("请输入一个整数：")
print(f(a))