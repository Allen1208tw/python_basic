# 題目 1：簡易購物折扣
#
# 請寫一個程式，讓使用者輸入商品價格與是否為會員，並計算最後應付金額。
#
# 要求：
# 1. 使用 input() 輸入商品價格。
# 2. 使用 input() 輸入是否為會員，例如輸入 y 或 n。
# 3. 商品價格滿 2000 元，先打 9 折。
# 4. 如果是會員，再打 95 折。
# 5. 最後輸出：
#    - 原價
#    - 是否為會員
#    - 折扣後金額
#
# 提示：
# - input() 取得的資料是字串，價格要轉成 int 或 float。
# - 可以用 if 判斷價格是否 >= 2000。
# - 可以用 if 判斷會員輸入是否為 "y"。
# - 可以用 f-string 格式化輸出結果。
user_member = input("是否為會員? 是/否")
price = int(input("請輸入商品價格:"))
final_price = price
if price >= 2000:
    discount = price * 0.9
    final_price = discount
    if user_member == "是":
        final_price= discount * 0.95
else:
    if user_member == "是":
        final_price = price * 0.95

print(f"原價是:{price} \n 是否有會員資格{user_member} \n 折扣完金額:{final_price}")

