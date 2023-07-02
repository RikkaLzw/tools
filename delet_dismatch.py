import os

def main():
    folder_path = "C:\\Users\\33519\\Desktop\\code"

    # 获取文件夹内所有文件名，并将文件名放入一个列表中
    filenames = os.listdir(folder_path)

    # 使用字典存储每个文件（名字不带扩展名）及其扩展名，如{"1": [".sol", ".txt"]}
    file_dict = {}
    for name in filenames:
        file_name, file_ext = os.path.splitext(name)
        if file_name not in file_dict:
            file_dict[file_name] = [file_ext]
        else:
            file_dict[file_name].append(file_ext)

    # 找出不符合规则的文件并删除
    for file_name, file_exts in file_dict.items():
        if len(file_exts) < 2 or ".sol" not in file_exts or ".txt" not in file_exts:
            for file_ext in file_exts:
                incorrect_file = "{}\\{}{}".format(folder_path, file_name, file_ext)
                print("删除不符合规则的文件：{}".format(incorrect_file))
                os.remove(incorrect_file)

if __name__ == "__main__":
    main()
