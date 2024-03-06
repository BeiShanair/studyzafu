# 输入一个文件路径
file_path = input("请输入文件路径：")

# 从文件路径中提取文件名、主文件名、拓展名、文件路径
file_name = file_path.split("\\")[-1]
file_main_name = file_name.split(".")[0]

file_type = file_name.split(".")[-1]

file_path2 = file_path.replace("\\" + file_name, "")

# 输出结果
print("文件：", file_name)
print("主文件名：", file_main_name)
print("拓展名：", file_type)
print("文件路径：", file_path2)
