# 物件的比較
import math
class Line:
    d = 0
    def __init__(self, x1, y1, x2, y2) -> None:
        self.d = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2));

    def __gt__(self, line):
        return self.d > line.d

if __name__ == '__main__':
    l1 = Line(0, 0, 5, 5)
    l2 = Line(0, 0, 3, 3)
    print(l1 > l2)