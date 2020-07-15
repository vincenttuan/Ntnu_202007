import math
# 二點間的距離
x1, y1 = 10, 20
x2, y2 = 40, 80
d = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))
print("%.2f" % d)