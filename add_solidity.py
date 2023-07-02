import os

files = ["no_dataset/tp/1009.sol",
    "no_dataset/tp/22629.sol",
    "no_dataset/tp/746.sol",
    "no_dataset/uc/1186.sol",
    "no_dataset/uc/14.sol",
    "no_dataset/uc/1419.sol",
    "no_dataset/uc/1424.sol",
    "no_dataset/uc/1515.sol",
    "no_dataset/uc/1576.sol",
    "no_dataset/uc/1627.sol",
    "no_dataset/uc/40.sol",
    "no_dataset/uc/of_de_2018-13722.sol",
    "no_dataset/uc/of_de_2018-13777.sol",
    "no_dataset/uc/of_de_2018-14001.sol",
    "no_dataset/uc/of_de_2018-14086.sol",
    "no_dataset/uc/of_de_2018-14576.sol"]

new_line = 'pragma solidity ^0.4.23;\n'
file_path = "C:\\Users\\33519\\Desktop\\"

for sol_file in files:
    # 以utf8打开
    with open(os.path.join(file_path, sol_file), 'r', encoding="utf-8") as file:
        content = file.read()

    with open(os.path.join(file_path, sol_file), 'w', encoding="utf-8") as file:
        file.write(new_line + content)

print("Inserted pragma statement in all files.")
