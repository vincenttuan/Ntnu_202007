import random as r
# 不重複串列(陣列, 數組)
# 樂透今彩539 (1~39之間取出5組且不可重複)
lotto = set()
while(len(lotto) < 5):
    n = r.randint(1, 39)
    lotto.add(n)
print(lotto)

