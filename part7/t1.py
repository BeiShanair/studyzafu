import os

file_name = "sourcel.txt"

if not os.path.exists("C:\\chfile"):
    os.makedirs("C:\\chfile")
with open("C:\\chfile\\" + file_name, "w") as f:
    f.writelines("hello world\n")
    f.writelines("hello python\n")
    f.writelines("hello China\n")
    f.writelines("hello ZAFU\n")
    f.writelines("hello 2024\n")



