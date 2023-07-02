import os
# 写一个python程序：打开C:\Users\33519\Desktop\oyente\de路径下的所有“result.log”，包括子文件夹下的“result.log”，并输出文件的个数，打开每一个“result.log”，读取其中
# "Integer Overflow:"
# "Timestamp Dependency: "
# "Re-Entrancy Vulnerability: "
# 后面的值是否为ture，最后打印true的个数
def search_logs_in_path(path):
    count_files = 0
    count_true = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file == "result.log":
                count_files += 1
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                    for keyword in ["Timestamp Dependency: "]:
                        line_start = content.find(keyword)
                        if line_start != -1:
                            value_start = line_start + len(keyword)
                            value = content[value_start:].split("\n")[0].strip()
                            if value.lower() == "true":
                                count_true += 1
    return count_files, count_true

path = "C:\\Users\\33519\Desktop\\Experiments_result\\compare\\oyente\\uc"
# path = "C:\\Users\\33519\\Desktop\\Experiments_result\\smarbugs_result\\oyente\\of"
count_files, count_true = search_logs_in_path(path)

print(f"文件个数: {count_files}")
print(f"True 的个数: {count_true}")
