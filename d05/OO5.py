class BMI :
    name = '' # 公有屬性
    __h = 0   # 私有屬性
    __w = 0   # 私有屬性

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

if __name__ == '__main__':
    bmi = BMI()
    bmi.name = 'Vincent'
    bmi.setHW(170, 60)
    print(bmi.getBMI())