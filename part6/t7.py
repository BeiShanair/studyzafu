dic_count = {"a": 0, "b": 0, "c": 0}
a = input("请输入字符串：")
for i in a:
    if i in dic_count:
        dic_count[i] += 1
for k, v in dic_count.items():
    print("字符", k, "出现", v, "次！")
