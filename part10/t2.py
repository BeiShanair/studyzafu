import random

list_a = [random.randint(1, 100) for i in range(20)]
print("排序前：", list_a)

list_b = sorted(list_a[::2], reverse=True)

for i in range(0, len(list_a), 2):
    list_b.insert(i, list_a[i + 1])

print("排序后：", list_b)
