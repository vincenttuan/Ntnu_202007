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

def getCV(sd, avg):
    return sd / avg

scores1 = [40, 70, 100]
scores2 = [10, 15, 20]

sd1 = getSD(scores1)
sd2 = getSD(scores2)
print(sd1, sd2)
print("scores1" if sd1<sd2 else "scores2", "集中度高")

cv1 = getCV(sd1, getAvg(scores1))
cv2 = getCV(sd2, getAvg(scores2))
print("scores1" if cv1>cv2 else "scores2", "分散程度高")
