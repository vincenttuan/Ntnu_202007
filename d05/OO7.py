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

class Teacher(Human):
    salary = 0
    def __str__(self) -> str:
        return super().__str__() + " salary=%d " % (self.salary)

if __name__ == '__main__':
    student = Student()
    student.name = 'Vincent'
    student.age = 18
    student.sex = '男'
    student.number = 1
    student.grade = '一年級'
    print(student)
    teacher = Teacher()
    teacher.name = 'Anita'
    teacher.age = 40
    teacher.sex = '女'
    teacher.salary = 120000
    print(teacher)