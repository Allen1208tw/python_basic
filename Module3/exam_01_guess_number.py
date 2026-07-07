# 題目 1：猜數字遊戲
#
# 請寫一個猜數字遊戲，讓電腦隨機產生 1 到 100 的整數，
# 玩家重複輸入數字，直到猜中為止。
#
# 要求：
# 1. 使用 random.randint(1, 100) 產生答案。
# 2. 使用 while 迴圈讓玩家可以一直猜。
# 3. 如果玩家猜太大，印出「太大」。
# 4. 如果玩家猜太小，印出「太小」。
# 5. 如果玩家猜對，印出猜了幾次，並結束遊戲。
# 6. 如果玩家輸入的不是數字，提示「請輸入數字」，並重新輸入。
#
# 提示：
# - 記得 import random。
# - 可以用 while True 建立無限迴圈。
# - 猜對時可以用 break 結束迴圈。
# - 可以用 try-except ValueError 處理非數字輸入。

import random
num = 1
answer = random.randint(1,100)
while True:
    try:
        user_input = int(input("輸入1-100之間的數\n" ))
    except ValueError:
        print("請輸入數字")
        continue
    if user_input == answer:
        print(f"恭喜中獎 總共猜了{num}次")
        if input("是否再玩一次? y/n") == "y":
            answer = random.randint(1,100)
            num = 1
            continue
        else:
            print("結束程式")
            break
    elif user_input > 100 or user_input < 1:
        print("超出範圍")
    elif num ==3:
        print("猜錯三次 遊戲結束")
        break
    elif user_input > answer:
        print("太大了")
        num += 1
    elif user_input < answer:
        print("太小了")
        num += 1
        
