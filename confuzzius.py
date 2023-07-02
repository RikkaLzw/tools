import os

# 写一个python程序：打开C:\Users\33519\Desktop\result\de路径下的所有“result.log”，包括子文件夹下的“result.log”，并输出文件的个数，打开
# 每一个“result.log”，读取其中"swc-id": ""的，例如："swc-id": "104" 我需要读取所有包含“104”的文件个数。一个文件只算做一个个数
def count_swc_id(path, target_file, swc_id):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file == target_file:
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                    if f'SWC-ID:   {swc_id}' in content:  # confuzzius
                        count += 1
    return count
def find_files(path, file_name):
    files_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file == file_name:
                files_list.append(os.path.join(root, file))
    return files_list

def main():
    path = "C:\\Users\\33519\Desktop\\Experiments_result\\compare\\confuzzius\\tp"
    target_file = "result.log"
    files = find_files(path, target_file)
    print(f"Number of {target_file} files found: {len(files)}")
    swc_id = "101"

    count = count_swc_id(path, target_file, swc_id)
    print("Count of files containing swc-id {}: {}".format(swc_id, count))

if __name__ == "__main__":
    main()


# SWC-101	Integer Overflow and Underflow
# SWC-107	Reentrancy
# SWC-112	Delegatecall to Untrusted Callee
# SWC-104	Unchecked Call Return Value
# SWC-116	Block values as a proxy for time? tp


