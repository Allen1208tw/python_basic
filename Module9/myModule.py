# 計算幾次方
def pow(x, y):
    print(f"{x}的{y}次方: {x**y}")



def discount(total, discount=200):
    if total >= 2000:
        cnt = total // 2000
        total -= discount * cnt
    return total

# print(f"MyModule.py的__name__:{__name__}")
if __name__ == "__main__":


    # 測試模組
    pow(2, 4)
    result = discount(5000)
    print(f"折扣後金額:{result}元")
