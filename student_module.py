students = [
    {'name': 'zainab', 'course': 'NCP', 'grade': 'A'},
    {'name': 'sade', 'course': 'DCP', 'grade': 'A'}
]
def find_student(name):
     for student in students:
         if student['name'] == name:
              return student
