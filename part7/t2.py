with open("D:\\file\\score.txt", "r") as f:
    score_list = f.readline().split(" ")
    for i in range(len(score_list)):
        score_list[i] = eval(score_list[i])


score_list.remove(max(score_list))
score_list.remove(min(score_list))

sum_score = 0
for i in score_list:
    sum_score += i

average_score = sum_score / len(score_list)
with open("D:\\file\\score.txt", "a") as f:
    f.write("\n选手得分：{}".format(average_score))
