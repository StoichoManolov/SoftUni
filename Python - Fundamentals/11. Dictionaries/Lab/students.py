student_grades = []

while True:

    student_info = input()
    if ':' not in student_info:
        break

    name, ID, course = student_info.split(':')

    student_grades.append({'name' : name, 'ID' : ID, 'course' : course})

for student in student_grades:
    if student_info.startswith(student['course'][0:5]):
        print(f'{student["name"]} - {student["ID"]}')

