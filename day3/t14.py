# 百钱买百鸡
total = 100
for i in range(total + 1):
    for j in range(total + 1):
        k = total - i - j
        if i * 5 + j * 3 + k / 3 == total and i != 0 and j != 0 and k != 0:
            print(f"鸡翁：{i}只，鸡母：{j}只，鸡雏：{k}只")
