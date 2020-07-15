import random
symbol = '2330.TW'
name = '台積電'
price = 363.5  # 現在價格
cost = 350.5  # 成本價
shares = 3000  # 股數

print("2330.TW 台積電 成本: 350.5 張數: 3 張 成交價: 363.5")
print("%s %s 成本: %.1f 張數: %d 張 成交價: %.1f"
      % (symbol, name, cost, shares//1000, price))
