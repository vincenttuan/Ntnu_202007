class Human:
    name = ''
    age = 0
    sex = ''

    def __init__(self, name, age, sex) -> None:
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self) -> str:
        return "%s age:%d sex=%s" % (self.name, self.age, self.sex)

class Student(Human):
    number = 0
    grade = ''

    def __init__(self, name, age, sex, number, grade) -> None:
        super().__init__(name, age, sex)
        self.number = number
        self.grade = grade

    def __str__(self) -> str:
        return super().__str__() + " number=%d grade=%s" % (self.number, self.grade)

class Teacher(Human):
    salary = 0

    def __init__(self, name, age, sex, salary) -> None:
        super().__init__(name, age, sex)
        self.salary = salary

    def __str__(self) -> str:
        return super().__str__() + " salary=%d " % (self.salary)

if __name__ == '__main__':
    student = Student('Vincent', 18, '男', 1, '一年級')
    print(student)
    teacher = Teacher('Anita', 40, '女', 120000)
    print(teacher)