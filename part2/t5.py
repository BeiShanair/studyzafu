# 输入一个表示星期的数字（1~7），输出对应的星期字符串名称
m = eval(input("请输入一个表示星期的数字（1~7）: "))
list1 = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
print(list1[m-1])