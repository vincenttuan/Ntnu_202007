# 判斷 bmi
def verifyBMI(bmi):
    if bmi > 23:
        return "過重"
    elif bmi < 18:
        return "過輕"
    else:
        return "正常"

# 取得 bmi
def getBMI(h, w):
    bmi = w / ((h/100)**2)
    resultText = verifyBMI(bmi)
    return bmi, resultText

bmi, resultText = getBMI(170, 60)
print("%.2f %s" % (bmi, resultText))