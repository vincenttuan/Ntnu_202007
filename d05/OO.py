class Human:  # Record class
    name = ''
    age = 0
    sex = ''

if __name__ == '__main__':
    h = Human() # 建立一個 Human 的物件
    h.name = 'Vincent';h.age = 20;h.sex='男'
    h2 = Human()  # 建立一個 Human 的物件
    h2.name = 'Anita';h2.age = 17;h2.sex = '女'

    list = [h, h2]
    print(list)
    for h in list:
        print(h.name, h.age, h.sex, type(h))




