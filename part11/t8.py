score_table = {"丁一": "95", "金二": "78", "张三": "47", "李四": "67", "王五": "64", "赵六": "52"}
max_score = 0
name = ""
for k, v in score_table.items():
    if int(v) > max_score:
        max_score = int(v)
        name = k

print("{}最高，{}分".format(name, max_score))
print("不及格人员名单及其分数：")
for k, v in score_table.items():
    if int(v) < 60:
        print(k, v)
