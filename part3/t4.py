import math

num = eval(input("请输入一个实数："))
if num < -5:
    result = abs(num)
    print("y为：", result)
elif num <= 5:
    result = math.pow(num, 4)
    print("y为：", result)
elif num < 10:
    result = math.log(num, math.e)
    print("y为：", result)
else:
    result = math.sqrt(num)
    print("y为：", result)
