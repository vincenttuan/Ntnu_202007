def getSum(scores):
    sum = 0
    for score in scores:
        sum += score
    return sum

def getAvg(scores):
    avg = getSum(scores) / len(scores)
    return avg

def getSD():
    pass

scores1 = [40, 70, 100]
scores2 = [10, 15, 20]

