class Account:
    actName = ''  # 戶名
    balnce = 0    # 餘額

    def save(self, money):  # 存款方法
        self.balnce += money

    def withdraw(self, money):  # 提款方法
        self.balnce -= money

    def printAct(self):  # 查詢餘額
        print("%s 帳戶餘額: %d" % (self.actName, self.balnce))

def menu(act):
    print("-----------")
    print("1.存款")
    print("2.提款")
    print("3.查詢")
    print("9.離開")
    print("-----------")
    id = int(input('請選擇:'))
    if id == 1:
        money = int(input('請輸入存款金額:'))
        act.save(money)
    elif id == 2:
        money = int(input('請輸入提款金額:'))
        act.withdraw(money)
    elif id == 3:
        act.printAct()
    elif id == 9:
        return
    menu(act)

if __name__ == '__main__':
    actName = input('請輸入戶名:')
    act = Account()
    act.actName = actName
    menu(act)

