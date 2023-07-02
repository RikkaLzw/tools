ture = 269
false = 269
# TP表示模型正确地将正类样本预测为正类样本的数量
TP = 75
# TN表示模型正确地将负类样本预测为负类样本的数量
TN = false - 0
# FP表示模型错误地将负类样本预测为正类样本的数量
FP = false - TN
# FN表示模型错误地将正类样本预测为负类样本的数量
FN = ture - TP

# 准确率（Accuracy）
accuracy = (TP + TN) / (TP + TN + FP + FN)
print("Accuracy:", accuracy)

# 召回率（Recall）
recall = TP / (TP + FN)
print("Recall:", recall)

# 精确率（Precision）
precision = TP / (TP + FP)
print("Precision:", precision)

# F1值（F1-Score）
f1_score = 2 * precision * recall / (precision + recall)
print("F1-Score:", f1_score)

# 假阳性率（FPR）
false_positive_rate = FP / (FP + TN)
print("FPR:", false_positive_rate)
