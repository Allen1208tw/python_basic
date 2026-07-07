# 題目 1：安全除法 safe_divide
#
# 請寫一個 safe_divide(a, b) 函式，安全地執行除法。
#
# 要求：
# 1. 如果可以正常相除，回傳計算結果。
# 2. 如果 b 是 0，回傳 "不能除以 0"。
# 3. 如果輸入資料型態錯誤，回傳 "輸入格式錯誤"。
# 4. 測試至少三種情況：
#    - 正常除法
#    - 除以 0
#    - 非數字資料
#
# 提示：
# - 除以 0 會產生 ZeroDivisionError。
# - 型態錯誤可能會產生 TypeError。
# - 可以使用 try-except 處理例外。

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "除數不能為0" 
    except TypeError:
        return "非數字資料" 
print(safe_divide(10,2))