number_of_students = int(input())

student_grades = {}

for _ in range(number_of_students):
    name, grade_as_str = input().split()
    grade = float(grade_as_str)

    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(grade)

for name,grade in student_grades.items():
    avg = sum(grade) / len(grade)
    format_of_avg = f"{' '.join([f'{g:.2f}' for g in grade])}"
    print(f'{name} -> {format_of_avg:} (avg: {avg:.2f})')
