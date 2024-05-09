set1 = {"李雷", "张玉", "王晓刚", "陈红静", "方向", "司马清"}
set2 = {"施然", "李芳芳", "刘潇", "方向", "孙一航", "黄煌"}
set3 = {"陈红静", "方向", "刘培良", "张玉", "施小冉", "司马清"}

class_num = 25
set4 = set1 | set2 | set3
set5 = set1 & set2 & set3
set6 = ((set1 & set2) | (set1 & set3) | (set2 & set3)) - set5

print("没有选修课程的同学：", class_num - len(set4), "人")

print("选修了1门课程的同学：", len(set4) - len(set5) - len(set6), "人")
print("名单如下：", end="")
for i in set4 - set5 - set6:
    print(i, end=" ")
print()

print("选修了2门课程的同学：", len(set6), "人")
print("名单如下：", end="")
for i in set6:
    print(i, end=" ")
print()

print("选修了3门课程的同学：", len(set5), "人")
print("名单如下：", end="")
for i in set5:
    print(i, end=" ")
print()
