def softuni_students(*args,**kwargs):
    invalid_students = []
    valid_students = {}

    for id,name in args:
        if id in kwargs.keys():
            valid_students[name] = kwargs[id]
        else:
            invalid_students.append(name)

    result = ''

    if valid_students:
        for name_student, name_courses in sorted(valid_students.items()):
            result += f"*** A student with the username {name_student} has successfully finished the course {name_courses}!\n"
    if invalid_students:
        result += f"!!! Invalid course students: {', '.join(sorted(invalid_students))}"

    return result




print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))
