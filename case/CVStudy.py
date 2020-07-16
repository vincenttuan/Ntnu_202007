import case.Utility as util
# http://estat.ncku.edu.tw/topic/desc_stat/base/CV.html
'''
一.
調查五位學生之身高及體重如下，試比較其分散程度 (求 C.V 值)。
身高：172、168、164、170、176(公分)
體重：62、57、58、64、64(公斤)
'''
height = [172, 168, 164, 170, 176]
weight = [62, 57, 58, 64, 64]
cv_height = util.getCV(height)
cv_weight = util.getCV(weight)
print(cv_height, cv_weight)
'''
二.
某公司有18位員工，其中10位在去年投資股票，一年的獲
利率如下(單位：%)：
    7.6 3.9 15.6 28.3 1.2 10.8 35.3 45.6 10.2 0.5
另外8位員工投資買公債一年內獲利率如下(單位：%)
    6.8 7.2 6.8 7.5 6.9 7.9 7.9 7.1 7.2
試分別求此公司的員工投資股票與公債的獲利率變異係數。
'''