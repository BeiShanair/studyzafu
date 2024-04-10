# 输入三门课的成绩
chinese = eval(input("请输入语文成绩: "))
math = eval(input("请输入数学成绩: "))
english = eval(input("请输入英语成绩: "))

# 计算总分和平均分
total = chinese + math + english
average = total / 3

# 计算最高分和最低分
min_score = min(chinese, math, english)
max_score = max(chinese, math, english)

# 计算最终总评成绩
final_score = chinese * 0.5 + math * 0.3 + english * 0.2

# 输出结果
print("总分为", total)
print("平均分为", average)
print("最高分为", max_score)
print("最低分为", min_score)
print("最终总评成绩为", final_score)
