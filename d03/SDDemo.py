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

sd1 = getSD(scores1)
sd2 = getSD(scores2)
print(sd1, sd2)
print("scores1" if sd1<sd2 else "scores2", "集中度高")
