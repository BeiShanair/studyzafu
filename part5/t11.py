import random
even = []
odd = []
for i in range(16):
    a = random.randint(10, 100)
    if a % 2 == 0:
        even.append(a)
    else:
        odd.append(a)

max_even = max(even)
min_even = min(even)

max_odd = max(odd)
min_odd = min(odd)

sum_even = sum(even)
sum_odd = sum(odd)

print("偶数：", even)
print("奇数：", odd)

print("最大偶数：", max_even)
print("最小偶数：", min_even)

print("最大奇数：", max_odd)
print("最小奇数：", min_odd)

print("偶数和：", sum_even)
print("奇数和：", sum_odd)
