score_table = {"丁一": "95", "金二": "78", "张三": "47", "李四": "67", "王五": "64", "赵六": "52"}
max_score = 0
name = ""
for key in score_table:
    if int(score_table[key]) > max_score:
        max_score = int(score_table[key])
        name = key

print("{}最高：{}".format(name, max_score))
print("不及格的有：")
for key in score_table:
    if int(score_table[key]) < 60:
        print(key, score_table[key])
