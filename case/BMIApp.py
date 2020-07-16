import case.BMISystem as bs
# 主程式
if __name__ == '__main__':
    h = 170
    w = 60
    bmi = bs.getBMI(h, w)
    print("%.2f" % bmi)