import os

def find_files(path, file_name):
    files_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file == file_name:
                files_list.append(os.path.join(root, file))
    return files_list

def count_files_with_swc_id(directory, swc_id):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == "result.log":
                filepath = os.path.join(root, file)
                with open(filepath, 'r') as f:
                    content = f.read()
                    if '"swc-id": "{}"'.format(swc_id) in content:
                        count += 1
    return count

directory = r"C:\Users\33519\Desktop\Experiments_result\compare\mythril\tp"
swc_id = "112"

file_name = "result.log"
files = find_files(directory, file_name)
print(f"Number of {file_name} files found: {len(files)}")

file_count = count_files_with_swc_id(directory, swc_id)
print("文件个数：", file_count)
# SWC-101	Integer Overflow and Underflow
# SWC-107	Reentrancy
# SWC-112	Delegatecall to Untrusted Callee
# SWC-104	Unchecked Call Return Value
# SWC-116	Block values as a proxy for time? tp