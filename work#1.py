class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'ФИО: {self.fullname} | Возраст: {self.age} | Статус брака: {self.is_married}')


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average_marks(self):
        total = sum(self.marks.values())
        average = total / len(self.marks)
        return average


class Teacher(Person):
    salary = 10000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def get_salary(self):
        if self.experience > 3:
            bonus = ((self.salary / 100) * (self.experience - 3))
            return self.salary + bonus
        else:
            return self.salary


def creat_students():
    student_1 = Student('Samat', 18, False, {"Math": 5, "History": 5, "English": 5})
    student_2 = Student('Esen', 17, False, {"Math": 5, "History": 4, "English": 4})
    student_3 = Student('Eldyar', 16, False, {"Math": 5, "History": 4, "English": 5})
    students = [student_1, student_2, student_3]

    for student in students:
        student.introduce_myself()
        print(f'Среднее арифметическое оценок: {round(student.average_marks(),3)}')


persons = Person('Doflamingo', 21, False)
persons.introduce_myself()
creat_students()
teachers = Teacher('Kate', 21, True, 5)
teachers.introduce_myself()
print(f'Зарплата: {teachers.get_salary()}')
