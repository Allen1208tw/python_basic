# 題目 3：單字出現次數統計
#
# 請統計一段文字中，每個單字出現的次數。
#
# 範例資料：
# text = "apple banana apple orange banana apple"
#
# 預期結果：
# {"apple": 3, "banana": 2, "orange": 1}
#
# 要求：
# 1. 將文字切成單字 list。
# 2. 使用 dict 儲存每個單字出現的次數。
# 3. 最後印出統計結果。
#
# 提示：
# - 可以用 split() 將文字切開。
# - 可以用 for 迴圈逐一處理每個單字。
# - 可以用 if word in result 判斷單字是否已經存在。
# - 也可以研究 dict.get(word, 0) 的用法。

text = "apple banana apple orange banana apple"
list = text.split(" ")
print(list)
x = {}
for i in list:
    x[i] = list.count(i)
print(x)