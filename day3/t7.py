num = input("请输入一个正整数：")
for i in range(1, int(num) + 1):
    if int(i) % 7 != 0:
        if "7" not in str(i):
            print(i, end=" ")
            