# Module 2 練習題：資料型態與基本運算
#
# 說明：
# 請依照每一題的要求完成程式。
# 本練習重點包含：
# - int、float、bool、str
# - list、tuple、set、dict
# - 算術運算子
# - 比較運算子
# - 邏輯運算子
# - in / not in
# - input() 與型別轉換


# 第 1 題：基本資料型態
#
# 請建立以下變數，並用 print() 印出每個變數的值與型態。
#
# 要求：
# 1. 建立一個整數變數 age。
# 2. 建立一個浮點數變數 height。
# 3. 建立一個布林變數 is_student。
# 4. 建立一個字串變數 name。
# 5. 使用 type() 印出每個變數的型態。
#
# 提示：
# - type(age) 可以取得 age 的資料型態。
# - print() 可以一次印出多個資料。

age = 25
height = 169.7
is_student = True
name = "Allen"
print(type(age), age)
print(type(height), height)
print(type(is_student), is_student)
print(type(name), name)


# 第 2 題：商品價格計算
#
# 請讓使用者輸入商品單價與購買數量，計算總金額。
#
# 要求：
# 1. 使用 input() 輸入商品單價。
# 2. 使用 input() 輸入購買數量。
# 3. 將輸入資料轉成數字。
# 4. 計算 total = price * quantity。
# 5. 印出總金額。
#
# 提示：
# - 商品單價可以使用 float。
# - 購買數量可以使用 int。
# - input() 取得的資料預設是 str。

price = int(input("輸入商品單價"))
number = int(input("輸入購買數量"))
total = price * number
print(f"總金額:{total}")

# 第 3 題：偶數或奇數
#
# 請讓使用者輸入一個整數，判斷它是偶數還是奇數。
#
# 要求：
# 1. 使用 input() 輸入整數。
# 2. 使用 % 運算子判斷是否能被 2 整除。
# 3. 如果是偶數，印出「偶數」。
# 4. 如果是奇數，印出「奇數」。
#
# 提示：
# - n % 2 == 0 代表 n 是偶數。
# - n % 2 != 0 代表 n 是奇數。

num = int(input("請輸入整數"))
if num %2 == 0:
    print("偶數")
else:
    print("奇數")


# 第 4 題：成績是否及格
#
# 請讓使用者輸入分數，判斷是否及格。
#
# 要求：
# 1. 使用 input() 輸入分數。
# 2. 分數大於或等於 60，印出「及格」。
# 3. 分數小於 60，印出「不及格」。
#
# 提示：
# - 會用到比較運算子 >=。
# - 輸入的分數要先轉成 int 或 float。

grade = int(input("請輸入分數"))
if grade >= 60:
    print("及格")
else:
    print("不及格")

# 第 5 題：簡易登入判斷
#
# 請設定正確帳號與密碼，並讓使用者輸入帳號與密碼。
#
# 要求：
# 1. 正確帳號為 "admin"。
# 2. 正確密碼為 "1234"。
# 3. 使用者輸入的帳號和密碼都正確時，印出「登入成功」。
# 4. 只要其中一個錯誤，印出「登入失敗」。
#
# 提示：
# - 會用到 == 比較字串。
# - 會用到 and 邏輯運算子。

account = "admin"
password = 1234
x = (input("請輸入帳號"))
y = (input("請輸入密碼"))
if x == account and y == password:
    print("登入成功")
else:
    print("登入失敗")

# 第 6 題：會員折扣判斷
#
# 請讓使用者輸入商品金額與是否為會員，計算折扣後金額。
#
# 規則：
# 1. 商品金額滿 2000 元，打 9 折。
# 2. 如果是會員，再打 95 折。
# 3. 如果兩個條件都符合，兩個折扣都要套用。
#
# 要求：
# 1. 使用 input() 輸入商品金額。
# 2. 使用 input() 輸入是否為會員，輸入 y 代表會員，n 代表非會員。
# 3. 印出原價、會員狀態、折扣後金額。
#
# 提示：
# - 可以先建立 final_price = price。
# - 如果 price >= 2000，讓 final_price *= 0.9。
# - 如果 member == "y"，讓 final_price *= 0.95。

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


# 第 7 題：list 基本操作
#
# 請建立一個 list 存放三個喜歡的水果。
#
# 要求：
# 1. 建立 fruits list。
# 2. 印出整個 list。
# 3. 印出第一個水果。
# 4. 使用 append() 新增一個水果。
# 5. 判斷 "apple" 是否在 fruits 裡。
#
# 提示：
# - 第一個元素的索引是 0。
# - 可以用 "apple" in fruits 判斷是否存在。

fruit_list = ['apple', 'banana', 'guava']
print(fruit_list)
print(fruit_list[0])
fruit_list.append('grape')
if 'apple' in fruit_list:
    print("在裡面")
else:
    print("不在裡面")

# 第 8 題：tuple 與 list 比較
#
# 請建立一個 tuple 存放座標，例如 (10, 20)。
#
# 要求：
# 1. 建立 point = (10, 20)。
# 2. 印出 x 座標與 y 座標。
# 3. 試著說明 tuple 和 list 最大的不同。
#
# 提示：
# - point[0] 是第一個值。
# - point[1] 是第二個值。
# - tuple 建立後不能直接修改內容。

point = (10, 20)
print(point)


# 第 9 題：set 去除重複資料
#
# 請使用 set 去除 list 中重複的數字。
#
# 範例資料：
# nums = [1, 2, 2, 3, 4, 4, 5]
#
# 要求：
# 1. 建立 nums list。
# 2. 將 nums 轉成 set。
# 3. 印出不重複的結果。
#
# 提示：
# - set(nums) 可以去除重複資料。
# - set 沒有固定順序。

nums = [1, 2, 2, 3, 4, 4, 5]
nums = set(nums)
print(nums)

# 第 10 題：dict 學生資料
#
# 請使用 dict 儲存一位學生的資料。
#
# 要求：
# 1. 建立 student dict。
# 2. 內容包含 name、age、score。
# 3. 印出學生姓名。
# 4. 印出學生分數。
# 5. 判斷 score 是否大於等於 60，並印出是否及格。
#
# 提示：
# - dict 使用 key 取得 value，例如 student["name"]。
# - 可以使用 student["score"] >= 60 判斷是否及格。

student_dict = {
    "name": "Allen",
    "age": 25,
    "score" : 60
}
print(student_dict["name"])
print(student_dict["score"])
if student_dict["score"] >= 60:
    print("及格")
else:
    print("不及格") 

# 第 11 題：綜合練習 - 簡易收銀機
#
# 請寫一個簡易收銀機程式。
#
# 要求：
# 1. 讓使用者輸入商品名稱。
# 2. 讓使用者輸入商品單價。
# 3. 讓使用者輸入購買數量。
# 4. 計算總金額。
# 5. 如果總金額滿 1000，折扣 100 元。
# 6. 印出商品名稱、單價、數量、原始總金額、最後金額。
#
# 提示：
# - 商品名稱是 str。
# - 單價可以轉成 int 或 float。
# - 數量可以轉成 int。
# - 可以用 if 判斷 total >= 1000。

name = str(input("請輸入商品名稱"))
price = int(input("請輸入商品單價"))
number = int(input("請輸入購買數量"))
total = price*number

if total >= 1000:
    final_price = total - 100
else:
    final_price = total
print(f"{name}的價格是{price}，總共買了{number}個，原本總共{total}元，折扣完是{final_price}元")