
list_lq = [[2006, 0.57], [2007, 0.56], [2008, 0.57], [2009, 0.62], [2010, 0.69], [2011, 0.72], [2012, 0.75],
           [2013, 0.76], [2014, 0.74], [2015, 0.74]]
sum_lq = 0
max_lq = 0
index_lq = 0
for i in list_lq:
    sum_lq += i[1]
    if i[1] > max_lq:
        max_lq = i[1]
        index_lq = i[0]

average_lq = sum_lq / len(list_lq)
print("十年平均录取率为：{}".format(average_lq))
print("录取率最高的年份为：{}".format(index_lq))
