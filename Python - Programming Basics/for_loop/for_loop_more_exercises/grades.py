students_exam = int(input())
average_grade = 0
number_of_students = 0

between_two_and_two_ninety_nine = 0
between_three_and_three_ninety_nine = 0
between_four_and_four_ninety_nine = 0
above_five = 0

for number in range(1, students_exam + 1):
    student_grade = float(input())
    number_of_students += 1
    average_grade += student_grade
    if student_grade <= 2.99:
        between_two_and_two_ninety_nine += 1
    elif student_grade <= 3.99:
        between_three_and_three_ninety_nine += 1
    elif student_grade <= 4.99:
        between_four_and_four_ninety_nine += 1
    elif student_grade >= 5.00:
        above_five += 1

average_grade = average_grade / students_exam

print(f'Top students: {above_five / number_of_students * 100:.2f}%')
print(f'Between 4.00 and 4.99: {between_four_and_four_ninety_nine / number_of_students * 100:.2f}%')
print(f'Between 3.00 and 3.99: {between_three_and_three_ninety_nine / number_of_students * 100:.2f}%')
print(f'Fail: {between_two_and_two_ninety_nine /number_of_students * 100:.2f}%')
print(f'Average: {average_grade:.2f}')