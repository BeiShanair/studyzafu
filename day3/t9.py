original = input("请输入明文：")
change = ""
for i in original:
    if i.isalpha():
        if i.islower():
            change += chr((ord(i) - 97 + 3) % 26 + 97)
        else:
            change += chr((ord(i) - 65 + 3) % 26 + 65)
    else:
        change += i
print("密文：", change)
