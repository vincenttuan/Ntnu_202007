import random as r
import sys

balance = 100  # 本金
bet = 10  # 下注金額

def getSum():
    d1 = [1, 2, 3, 4, 5, 6]
    d2 = [1, 2, 3, 4, 5, 6]
    d3 = [1, 2, 3, 4, 5, 6]
    pc_sum   = d1[r.randint(0, 5)] + d2[r.randint(0, 5)] + d3[r.randint(0, 5)]
    user_sum = d1[r.randint(0, 5)] + d2[r.randint(0, 5)] + d3[r.randint(0, 5)]
    return pc_sum, user_sum

def menu():
    print("骰子比大小")
    print("-------------")
    print("1.設定下注金額")
    print("2.比大")
    print("3.比小")
    print("4.查詢餘額")
    print("5.Exit")
    print("-------------")
    id = int(input('請選擇'))
    play(id)

def play(id):
    global bet
    global balance
    if(id == 1):     # 設定下注金額
        print("修改前下注金額:", bet)
        money = int(input('請設定金額:'))
        bet = money
        print("修改後下注金額:", bet)
    elif(id == 2):   # 比大
        pc_sum, user_sum = getSum()
        if(user_sum > pc_sum):
            print("比大 You Win", pc_sum, user_sum)
            balance += bet
        elif(user_sum < pc_sum):
            print("比大 You Lose", pc_sum, user_sum)
            balance -= bet
        else:
            print("平手", pc_sum, user_sum)
    elif (id == 3):  # 比小
        pc_sum, user_sum = getSum()
        if (user_sum < pc_sum):
            print("比小 You Win", pc_sum, user_sum)
            balance += bet
        elif (user_sum > pc_sum):
            print("比小 You Lose", pc_sum, user_sum)
            balance -= bet
        else:
            print("平手", pc_sum, user_sum)
    elif (id == 4):  # 查詢餘額
        print("餘額:", balance)

    elif (id == 5):  # Exit
        return

    print("按下 Enter 鍵繼續")
    sys.stdin.read(1)
    menu()

if __name__ == '__main__':
    menu()