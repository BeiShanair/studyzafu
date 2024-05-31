with open("D:\\file\\score1.txt", "r") as f:
    score_list = []
    for line in f.readlines():
        # 去除末尾换行符
        line = line.strip("\n")
        # 按逗号分割字符串
        score_list.append(line.split(","))

for i in range(len(score_list)):
    sum_score = eval(score_list[i][1]) * 0.4 + eval(score_list[i][2]) * 0.6
    s = round(sum_score)
    score_list[i].append(str(s))

score_list.sort(key=lambda x: eval(x[3]), reverse=True)

with open("D:\\file\\scorel1.txt", "w") as f:
    f.write("学号,平时成绩,期末成绩,总评成绩\n")
    for i in score_list:
        f.write(",".join(i) + "\n")
