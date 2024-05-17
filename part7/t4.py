with open("D:\\file\\water.txt", "r") as f:
    data_list = []
    for line in f.readlines():
        # 去除末尾换行符
        line = line.strip("\n")
        # 按空格分割字符串
        data_list.append(line.split(" "))

for i in range(len(data_list)):
    sum_data = 0
    for j in range(1, len(data_list[i]) - 1):
        # 计算每个用户的用水量
        sum_data += eval(data_list[i][j + 1]) - eval(data_list[i][j])
    else:
        print("用户{0} = {1:.2f}元".format(data_list[i][0], sum_data*1.05))


