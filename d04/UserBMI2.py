# 讀取檔案
file = open('user.txt', 'r')
list = file.readlines()
for data in list:
    # 切割字串
    str = data.strip("\n") # '170, 60'
    rows = str.split(",")  # ['170', '60']
    h = rows[0]  # '170'
    w = rows[1]  # '60'
    h = float(h)
    w = float(w)
    bmi = w / ((h/100)**2)
    print("身高: %.1f 體重: %.1f BMI: %.2f" % (h, w, bmi))
