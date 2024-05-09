dl = {"k1":"v1", "k2":"v2", "k3":"v3"}
dl["k4"] = "v4"
dl.pop("k1")

k = input("请输入键值: ")
if k in dl:
    print(dl[k])
else:
    print("键不存在！")

print("dl的所有键值对：")
for k,v in dl.items():
    print(k,v)
