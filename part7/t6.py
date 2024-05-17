import csv
with open('D:\\file\\score_raw.txt', 'r', encoding='utf-8') as file:
    score_list = []
    for line in file.readlines():
        # 去除末尾换行符
        line = line.strip("\n")
        # 按逗号分割字符串
        score_list.append(line.split(","))

# gbk编码，保证中文不乱码
with open('D:\\file\\score.csv', 'w', newline='', encoding='gbk') as file:
    writer = csv.writer(file)
    writer.writerows(score_list)

# 计算总分
en_sum = math_sum = pc_sum = 0
for i in range(1, len(score_list)):
    sum_score = eval(score_list[i][1]) + eval(score_list[i][2]) + eval(score_list[i][3])
    score_list[i].append(str(sum_score))
    en_sum += eval(score_list[i][1])
    math_sum += eval(score_list[i][2])
    pc_sum += eval(score_list[i][3])


score_list[0].append('总分')

en_avg = en_sum / (len(score_list) - 1)
math_avg = math_sum / (len(score_list) - 1)
pc_avg = pc_sum / (len(score_list) - 1)
score_list.append(['各科平均分', str(en_avg), str(math_avg), str(pc_avg)])

with open('D:\\file\\score1.csv', 'w', newline='', encoding='gbk') as file:
    writer = csv.writer(file)
    writer.writerows(score_list)
