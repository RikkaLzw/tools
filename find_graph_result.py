import re

with open(r"C:\Users\33519\Desktop\实验结果\未优化_result\未优化\RE\smartcheck_3.log", "r", encoding="utf-8") as f:
    content = f.read()

fn_pattern = r"fn_list\(predict == 0 & label == 1\): \[([0-9, ]*)\]"
fp_pattern = r"fp_list\(predict == 1 & label == 0\): \[([0-9, ]*)\]"

fn_contents = re.findall(fn_pattern, content)
fp_contents = re.findall(fp_pattern, content)

fn_list = []
for fn_content in fn_contents:
    fn_list += [int(x) for x in fn_content.split(', ') if x]

fp_list = []
for fp_content in fp_contents:
    fp_list += [int(x) for x in fp_content.split(', ') if x]

print("predict == 0 & label == 1:", *fn_list, "\n", "predict == 1 & label == 0:", *fp_list)
print(len(fn_list), len(fp_list))
