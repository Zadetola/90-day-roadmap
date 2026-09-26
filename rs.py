students = [
    {'name': 'zainab', 'course': 'NCP', 'grade': 'A'},
    {'name': 'sade', 'course': 'DCP', 'grade': 'A'}
]
print(students[1]['grade'])
def find_student(name):
     for student in students:
         if student['name'] == name:
              return student

result = find_student ('sade')
print(result)