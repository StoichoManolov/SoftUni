def course_in_or_not():

    if course not in courses.keys():
        courses[course] = []

    courses[course].append(student)


courses = {}

while True:

    students = input()

    if students == 'end':
        break

    course, student = students.split(' : ')

    course_in_or_not()


for item in courses:
    print(f'{item}: {len(courses[item])}')
    for x in courses[item]:
        print(f'-- {x}')





