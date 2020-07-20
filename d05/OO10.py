# 覆寫 override
class Bird:
    def move(self):
        print("我會飛")

class Ostrich(Bird):
    def move(self):
        #super().move()
        print("不會飛但會跑")

# 多型操作
def printMove(animal):
    animal.move()

if __name__ == '__main__':
    a = Bird()
    b = Ostrich()
    printMove(a)
    printMove(b)