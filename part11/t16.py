with open("D:\\file\\data.txt", "r") as f:
    data = f.readline().split(" ")
    for i in range(len(data)):
        data[i] = eval(data[i])

sum_data = sum(data)
with open("D:\\file\\out.txt", "w") as f:
    f.write(str(sum_data))
