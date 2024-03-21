# 假设一年开头是星期一

advance = 1
for day in range(1, 366):
    if day % 7 in [6, 0]:
        advance *= 0.999
    else:
        advance *= 1.01
print("一年365天积累进步的力量是：{:.2f}".format(advance - 1))
