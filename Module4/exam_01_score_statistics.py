# 題目 1：成績統計器
#
# 給定一個成績列表，請計算成績統計資料。
#
# 範例資料：
# scores = [80, 95, 72, 60, 45, 88, 100]
#
# 要求：
# 1. 印出平均分數。
# 2. 印出最高分。
# 3. 印出最低分。
# 4. 印出及格人數。
# 5. 印出不及格人數。
#
# 提示：
# - 平均分數可以用 sum(scores) / len(scores)。
# - 最高分可以用 max(scores)。
# - 最低分可以用 min(scores)。
# - 60 分以上算及格。
# - 可以用 for 迴圈逐一判斷每個分數是否及格。

scores = [80, 95, 72, 60, 45, 88, 100]
x = sum(scores) / len(scores)
print(x)
y = max(scores)
print(f"最高分是{y}")
z = min(scores)
print(f"最低分是{z}")
num = 0
for i in scores:
    if i >= 60:
        num +=1
print(f"及格人數為{num}")
f = 0
for i in scores:
    if i < 60:
        f +=1
print(f"不及格人數{f}")