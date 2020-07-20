class Pen:
    name = '鉛筆'
    price = 10
    subtotal = 0

    def __mul__(self, n):
        self.subtotal = self.price * n

if __name__ == '__main__':
    pen = Pen()
    pen * 20
    print(pen.subtotal)