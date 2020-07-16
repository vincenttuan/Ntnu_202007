items = [10, 20, 30, 40, 50]  # 數組(陣列)
print(items[0])
print(items[4])

for item in items:
    print(item)

for (i, item) in enumerate(items):
    print(i, item)

# 計算總和
sum = 0
for item in items:
    sum += item  # 累加, 相當於 sum = sum + item
print(sum)
