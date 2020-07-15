import keyword
# Python 保留字
print(keyword.kwlist)

# 刪除變數
r = 10
pi = 3.14
area = r**2 * pi
print(r, pi, area)
del area  # 刪除 area 變數
# print(r, pi, area) # 不可使用 area 變數
