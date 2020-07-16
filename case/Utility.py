import math
'''
工具資源提供說明:
1.getSum(items)  取得總和
2.getAvg(items)  取得平均
3.getSD(items)   取得標準差
4.getCV(items) 取得變異係數
'''
def getSum(items):
    sum = 0
    for item in items:
        sum += item
    return sum


def getAvg(items):
    avg = getSum(items) / len(items)
    return avg


def getSD(items):
    sum = 0
    avg = getAvg(items)
    for item in items:
        sum += math.pow(item - avg, 2)
    sd = math.sqrt(sum / len(items))
    return sd


def getCV(items):
    avg = getAvg(items)
    sd = getSD(items)
    return sd / avg