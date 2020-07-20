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
    print(h)