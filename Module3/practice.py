# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# 告訴使用者需要輸入的數字範圍 input()
# 超出範圍要顯示「超出範圍請重新輸入」
# 數字太大 要提示「請輸入更小的數字」
# 數字太小 要提示「請輸入更大的數字」
# 使用者猜對要回傳「恭喜中獎」

import random
answer = random.randint(1,100)
num = 1
while True:
    user_input = int(input("輸入1-100之間的數\n" ))
    if user_input >100 or user_input < 1:
        print("超出範圍")
    elif user_input < answer:
        print("太小了")
        num +=1
    elif user_input > answer:
        print("太大了")
        num +=1
    else:
        print("答對!，總共猜了:", num, "次")









