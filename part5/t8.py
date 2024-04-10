a = input("输入：")
b = a.split()
average = sum([int(i) for i in b]) / len(b)
for i in b:
    if i > str(average):
        print(i,end=" ")
