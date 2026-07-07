# 題目 1：函式版 BMI 計算器
#
# 請使用函式完成 BMI 計算與狀態判斷。
#
# 要求：
# 1. 建立 calculate_bmi(height, weight) 函式，回傳 BMI。
# 2. 建立 get_bmi_status(bmi) 函式，回傳 BMI 狀態。
# 3. 讓使用者輸入身高與體重。
# 4. 印出 BMI 數值與狀態。
#
# BMI 狀態規則：
# - BMI < 18.5：過輕
# - 18.5 <= BMI < 24：正常
# - BMI >= 24：過重
#
# 提示：
# - BMI 公式是 weight / height ** 2。
# - 函式結果要用 return 回傳。
# - 可以用 if-elif-else 判斷狀態。
# - 可以用 f"{bmi:.2f}" 顯示小數點後 2 位。

def calculate_bmi(height, weight):
    result = weight / (height ** 2)
    return result
def get_bmi_status(bmi):
    if bmi < 18.5:
        return"過輕"
    elif 18.5 <= bmi < 24:
        return"正常"
    else:
        return"過重"
try:
    x = float(input("請輸入身高(公尺)"))
    y = int(input("請輸入體重"))
    bmi = calculate_bmi(x,y)
    print(f"{bmi:.2f}")
    print(get_bmi_status(bmi))
except ValueError:
    print("請輸入數字")
    
