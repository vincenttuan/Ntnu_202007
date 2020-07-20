# 覆寫 override
class Bird:
    def move(self):
        print("我會飛")

class Ostrich(Bird):
    def move(self):
        #super().move()
        print("不會飛但會跑")


if __name__ == '__main__':
    o = Ostrich()
    o.move()