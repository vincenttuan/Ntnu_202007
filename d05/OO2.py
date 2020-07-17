class Stock:
    symbol=''
    cost=0
    shares=0
    def getTotal(self):
        return self.shares * self.cost

if __name__ == '__main__':
    stock = Stock()
    stock.symbol='2330.TW'
    stock.cost = 275.5
    stock.shares = 3000
    print(stock.getTotal())
