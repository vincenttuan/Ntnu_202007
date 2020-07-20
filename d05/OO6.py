class Human:
    name = ''
    age = 0
    sex = ''

    def __str__(self) -> str:
        return 'name=%s age=%d sex=%s' % (self.name, self.age, self.sex)


if __name__ == '__main__':
    h = Human()
    h.name = 'Vincent'
    h.age = 18
    h.sex = '男'
    h2 = Human()
    h2.name = 'Anita'
    h2.age = 19
    h2.sex = '女'
    print(h)
    print(h2)
    list = [h, h2]
    for h in list:
        print(h)