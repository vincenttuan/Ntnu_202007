# 互動式 BMI 計算機
h = float(input('請輸入身高(cm):')) # str -> float
w = float(input('請輸入體重(kg):')) # str -> float
print(h, w)
print(type(h), type(w))
# 請問 BMI = ?
h = h / 100
bmi = w / h**2
print(bmi)
