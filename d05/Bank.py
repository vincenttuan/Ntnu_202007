class Account:
    actName = ''  # 戶名
    balnce = 0    # 餘額

    def save(self, money):  # 存款方法
        self.balnce += money

    def withdraw(self, money):  # 提款方法
        self.balnce -= money

    def printAct(self):  # 查詢餘額
        print("%s 帳戶餘額: %d" % (self.actName, self.balnce))
