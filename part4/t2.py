def fa(n):
    if n == 0:
        return 1
    return n * fa(n - 1)


a = int(input("请输入一个整数："))
print(a, "的阶乘是", fa(a))
