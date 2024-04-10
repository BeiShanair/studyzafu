# 输入一个三位整数
m = eval(input("请输入一个三位整数: "))
a = m // 100
b = m % 100 // 10
c = m % 10

# 求各位数字之和
sum_num = a + b + c
print("各位数字之和为", sum_num)
