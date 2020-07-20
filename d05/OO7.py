class Human:
    name = ''
    age = 0
    sex = ''
    def __str__(self) -> str:
        return "%s age:%d sex=%s" % (self.name, self.age, self.sex)

class Student(Human):
    number = 0
    grade = ''
    def __str__(self) -> str:
        return super().__str__() + " number=%d grade=%s" % (self.number, self.grade)

if __name__ == '__main__':
    student = Student()
    student.name = 'Vincent'
    student.age = 18
    student.sex = '男'
    student.number = 1
    student.grade = '一年級'
    print(student)