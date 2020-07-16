import random as r
poker = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
print(poker)
# 反轉
poker.reverse()
print(poker)
# 排序
poker.sort()
print(poker)
# 洗牌(Shuffle)
def shuffle(poker):
    n1, n2 = r.randint(0, len(poker)-1), r.randint(0, len(poker)-1)
    p1 = poker[n1]
    poker[n1] = poker[n2]
    poker[n2] = p1
    return poker

for i in range(0, 10000):
    poker = shuffle(poker)

print(poker)