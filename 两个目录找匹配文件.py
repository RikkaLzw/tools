import os
"""写一个Python程序，要求：根据文件名查找对应的文件，目录1：C:\Users\33519\Desktop\no_dataset\re。目录2：C:\Users\33519\Desktop\no_vul\re 
 目录集合：目录1和目录2中的文件是匹配的，目录2的文件名称为：no_*graph.dot,则在目录1中查找名为*.sol的文件。例如：如果目录2中有：no_6graph.dot则在目录集合中查找6.sol,若果未找到则打印文件名称"""
def find_matching_files(directory1, directory2, collection):
    # 获取目录2中以"no_"开头、以".dot"结尾的文件名列表
    file_names = [file for file in os.listdir(directory2) if file.startswith("no_") and file.endswith(".dot")]

    # 遍历文件名列表
    for file_name in file_names:
        # 获取文件名中的数字
        number = file_name[3:-9]

        # 构建对应的.sol文件名
        sol_file_name = number + ".sol"

        # 在目录集合中查找对应的.sol文件
        if sol_file_name in collection:
            # 构建目录1中的文件路径
            file_path = os.path.join(directory1, sol_file_name)

            # 判断文件路径是否存在
            if os.path.exists(file_path) == False:
                print(f"找到匹配的文件，但在目录1中未找到：{sol_file_name}")
        else:
            print(f"未找到匹配的文件：{sol_file_name}")

# 目录1
directory1 = r"C:\Users\33519\Desktop\no_dataset\re"
# 目录2
directory2 = r"C:\Users\33519\Desktop\no_vul\re"
# 目录集合
collection = set(os.listdir(directory1)) | set(os.listdir(directory2))

# 调用函数查找匹配的文件
find_matching_files(directory1, directory2, collection)
