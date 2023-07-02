import os

# 写一段python代码，比较目录1：C:\Users\33519\Desktop\code2\of与目录2：C:\Users\33519\Desktop\datasets\OF下的文件，正确的情况下目
# 录1有的文件目录2也应该有，但两个目录下的文件格式不同，目录1为：*.sol,目录2 的文件为：*graph.dot,例如目录1中有6.sol，则目录2中应有6graph.dot,
# 找出目录1存在，而目录2不存在的文件，并打印输出


dir1 = r"C:\Users\33519\Desktop\code2\uc"
dir2 = r"C:\Users\33519\Desktop\datasets\UC"

# 获取目录1中的所有文件
files1 = [f for f in os.listdir(dir1) if os.path.isfile(os.path.join(dir1, f))]

# 获取目录2中的所有文件
files2 = [f for f in os.listdir(dir2) if os.path.isfile(os.path.join(dir2, f))]

# 找出目录1存在而目录2不存在的文件
missing_files = [f for f in files1 if f.replace(".sol", "graph.dot") not in files2]

# 打印输出缺失的文件
for file in missing_files:
    print(file)
