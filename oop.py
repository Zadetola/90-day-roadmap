class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show_grade(self):
        print(self.name , 'grade is', self.grade)
s1 = Student('zainab', 'A')
s1.show_grade()