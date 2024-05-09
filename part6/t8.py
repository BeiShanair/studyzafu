sentence = input("请输入一句英文句子（假设没有标点，单词之间用空格分隔）wish you a fascinating future just like the beautiful fireworks：")
words = sentence.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
for k, v in word_count.items():
    print("单词", k, "出现", v, "次！")