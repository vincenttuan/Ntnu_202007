import sys
'''
使用者可選擇是否要輸入身高,體重等資訊
使用者可以離開系統
系統可以重複使用
'''
# 系統目錄
def menu():
    print("BMI 計算系統")
    print("--------------")
    print("1. 輸入資料")
    print("2. Exit")
    print("--------------")
    choice()

# 系統運作流程
def choice():
    id = int(input('請輸入選項:'))
    if id == 1:
        h = float(input('請輸入身高:'))
        w = float(input('請輸入體重:'))
        bmi = getBMI(h, w)
        print("%.2f" % bmi)
        print('按下任意鍵繼續...')
        sys.stdin.read(1)
        menu()
    elif id == 2:
        print("謝謝使用")
    else:
        print("輸入錯誤請重新輸入")
        menu()

# 系統商業邏輯運算
def getBMI(h, w):
    bmi = w / ((h / 100) ** 2)
    return bmi

# 主程式
if __name__ == '__main__':
    menu()
