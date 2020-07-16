import math
def getSum(scores):
    sum = 0
    for score in scores:
        sum += score
    return sum

def getAvg(scores):
    avg = getSum(scores) / len(scores)
    return avg

def getSD(scores):
    sum = 0
    avg = getAvg(scores)
    for score in scores:
        sum += math.pow(score - avg, 2)
    sd = math.sqrt(sum / len(scores))
    return sd

scores1 = [40, 70, 100]
scores2 = [10, 15, 20]

print(getSD(scores1), getSD(scores2))
