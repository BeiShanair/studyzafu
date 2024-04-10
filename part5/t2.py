list_lq = [[2006, 0.57], [2007, 0.56], [2008, 0.57], [2009, 0.62], [2010, 0.69], [2011, 0.72], [2012, 0.75],
           [2013, 0.78], [2014, 0.74], [2015, 0.74]]
index_for_list = 0
sum_rate = 0
for i in list_lq:
    if i[1] > list_lq[index_for_list][1]:
        index_for_list = list_lq.index(i)
    sum_rate += i[1]

average_rate = sum_rate / len(list_lq)
print("录取率的平均值为：", average_rate)
print("录取率最高的年份为：", list_lq[index_for_list][0])


