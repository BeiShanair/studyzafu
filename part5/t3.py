sentence = input("请输入英文：")
words = sentence.split()
length = 0
for word in words:
    if len(word) > length:
        length = len(word)

print("最长的单词是：", length)
