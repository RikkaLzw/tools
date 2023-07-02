import os
import shutil
import glob
"""写一个Python程序，要求：根据文件名查找对应的文件，并保存至目录1：C:\\Users\\33519\Desktop\\no_dataset\\de。目录2：C:\Users\\33519
\Desktop\\no_vul\de  目录集合：F:\Python\python_test\source_code\overflow(OF)、F:\Python\python_test\source_code\\reentrancy(RE)、
F:\Python\python_test\source_code\\timestamp_dependency(TP)、F:\Python\python_test\source_code\unchecked_external(UC)、
F:\Python\python_test\source_code\delegatecall(DE)。目录2和目录集合中的文件是匹配的，目录2的文件名称为：no_*graph.dot,则在目录集合中查找名为*.sol的文件，并保存至目录1。

最后输出匹配成功的文件数量.例如：如果目录2中有：no_6graph.dot则在目录集合中查找6.sol，则将6.sol保存至目录1"""
# 目录1和目录2的路径
dir1 = r"C:\Users\33519\Desktop\no_dataset\re"
dir2 = r"C:\Users\33519\Desktop\no_vul\re"

# 目录集合
directories = [
    r"F:\Python\python_test\source_code\overflow(OF)",
    # r"F:\Python\python_test\source_code\reentrancy(RE)",
    r"F:\Python\python_test\source_code\timestamp_dependency(TP)",
    r"F:\Python\python_test\source_code\unchecked_external(UC)",
    r"F:\Python\python_test\source_code\delegatecall(DE)"
]

# 获取目录2中的文件名
files_in_dir2 = os.listdir(dir2)

# 匹配成功的文件数量
matched_files_count = 0

# 遍历目录2中的文件
for file_name in files_in_dir2:
    if file_name.startswith("no_") and file_name.endswith(".dot"):
        # 提取数字部分
        number = file_name[3:-9]

        # 在目录集合中查找对应的.sol文件
        for directory in directories:
            sol_files = glob.glob(os.path.join(directory, f"{number}.sol"))
            if sol_files:
                # 找到匹配的.sol文件，将其复制到目录1
                shutil.copy(sol_files[0], dir1)
                matched_files_count += 1
                break

print(f"匹配成功的文件数量：{matched_files_count}")
