class BMI:
    h = 0
    w = 0
    def getBMI(self):
        return self.w / ((self.h/100)**2)

if __name__ == '__main__':
    b1 = BMI()
    b1.h = 170;b1.w=60
    b2 = BMI()
    b2.h = 180;b2.w = 80
    list = [b1, b2]
    for b in list:
        print(b.getBMI())