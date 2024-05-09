result_dict = {"+": "x+y", "-": "x-y", "*": "x*y", "/": "x/y"}
x = input("请输入x：")
y = input("请输入y：")
op = input("请输入操作符：")
if op == "/" and y == "0":
    print("divided by zero!")
elif op not in result_dict:
    print("input operator error!")
else:
    print(eval(result_dict[op]))
