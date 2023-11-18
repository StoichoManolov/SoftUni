number = int(input())

students = {}

for _ in range(number):

    name = input()
    grade = float(input())

    if name not in students.keys():
        students[name] = []

    students[name].append(grade)


for student in students:
    grades = 0
    avg = 1
    for grade in students[student]:
        avg = len(students[student])
        grades += grade
    grades /= avg
    if grades >= 4.50:
        print(f'{student} -> {grades:.2f}')


