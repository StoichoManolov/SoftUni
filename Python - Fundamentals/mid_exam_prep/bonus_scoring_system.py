students = int(input())
lectures = int(input())
bonus = int(input())

max_bonus = 0
student_attendance = 0

for i in range(students):
    attendance = int(input())

    total_bonus = round((attendance / lectures) * (5 + bonus))

    if total_bonus >= max_bonus:
        max_bonus = total_bonus
        student_attendance = attendance

print(f'Max Bonus: {max_bonus}.')
print(f'The student has attended {student_attendance} lectures.')


