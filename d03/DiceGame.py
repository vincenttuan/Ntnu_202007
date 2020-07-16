import random as r

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

if __name__ == '__main__':
    menu()