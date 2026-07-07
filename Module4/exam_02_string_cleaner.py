# 題目 2：字串整理工具
#
# 請寫一個程式整理字串。
#
# 範例資料：
# text = "  Python,is,Fun  "
#
# 要求：
# 1. 去掉字串前後空白。
# 2. 將字串全部轉成小寫。
# 3. 使用逗號 "," 將字串切成 list。
# 4. 使用空白 " " 將 list 接回一個新的字串。
# 5. 印出每一步處理後的結果。
#
# 提示：
# - 去空白可以用 strip()。
# - 轉小寫可以用 lower()。
# - 分割字串可以用 split(",")。
# - 合併 list 可以用 " ".join(words)。

text = "  Python,is,Fun  "
x = text.strip(" ")
print(x)
y = x.lower()
print(y)
z = y.split(",")
print(z)
w = " ".join(z)
print(w)