# Vulnerability: Reentrancy
# Vulnerability: Integer Overflow
# Vulnerability: Time Manipulation
# Vulnerability: Unchecked Low Level Call
# Vulnerability: Arithmetic
import os

def find_files(path, file_name):
    files_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file == file_name:
                files_list.append(os.path.join(root, file))
    return files_list

def count_vulnerabilities(file_path):
    with open(file_path, 'r', errors='ignore') as file:
        content = file.read()
    vulnerabilities = [
        # "Vulnerability: Reentrancy", # re
        "Vulnerability: Integer Overflow",  # of
        # "Vulnerability: Time Manipulation",  # tp
        # "Vulnerability: Unchecked Low Level Call",  # uc
    ]
    count = 0
    for vulnerability in vulnerabilities:
        if vulnerability in content:
            count += 1
    return count

if __name__ == "__main__":
    path = "C:\\Users\\33519\Desktop\\Experiments_result\\compare\\conkas\\conkas\\uc"
    file_name = "result.log"
    files = find_files(path, file_name)
    print(f"Number of {file_name} files found: {len(files)}")

    total_vulnerabilities = 0
    for file in files:
        vulnerabilities = count_vulnerabilities(file)
        total_vulnerabilities += vulnerabilities
        # print(f"{file}: {vulnerabilities} vulnerabilities")

    print(f"Total vulnerabilities: {total_vulnerabilities}")
