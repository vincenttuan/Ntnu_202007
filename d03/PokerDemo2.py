import random as r
poker = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4
r.shuffle(poker)
print(poker)
n1 = poker.pop(0)
n2 = poker.pop(0)
print(n1, n2)
print(poker)
