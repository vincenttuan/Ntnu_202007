class BMI :
    name = '' # 公有屬性
    __h = 0   # 私有屬性
    __w = 0   # 私有屬性

    # 建構式
    def __init__(self, name, h, w) -> None:
        self.name = name
        self.__h = h
        self.__w = w

    # 封裝(設定 __h 與 __w 的值)
    def setHW(self, h, w):
        if 0 < h < 300:
            self.__h = h
        if 0 < w < 1000:
            self.__w = w

    def getBMI(self) -> float:
        h = self.__h
        w = self.__w
        return w / ((h/100)**2)

    def __str__(self) -> str:
        return '%s 身高:%.1f 體重:%.1f BMI:%.2f' % (self.name, self.__h, self.__w, self.getBMI())


if __name__ == '__main__':
    bmi = BMI('Anita', 165, 48)
    print(bmi.getBMI())
    print(bmi)