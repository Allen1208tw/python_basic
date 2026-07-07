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
        
