def my_sorted(raw_list, flag=False):
    # 默认降序
    if not flag:
        for i in range(len(raw_list)):
            for j in range(i, len(raw_list)):
                if raw_list[i] > raw_list[j]:
                    raw_list[i], raw_list[j] = raw_list[j], raw_list[i]
        return raw_list
    else:
        for i in range(len(raw_list)):
            for j in range(i, len(raw_list)):
                if raw_list[i] < raw_list[j]:
                    raw_list[i], raw_list[j] = raw_list[j], raw_list[i]
        return raw_list


lst = [1, 3, 2, 4, 5]
print(my_sorted(lst))
