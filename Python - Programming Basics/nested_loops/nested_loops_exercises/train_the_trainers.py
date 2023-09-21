total_avg = 0
total_grades = 0

jury = int(input())
presentation = input()

while presentation != "Finish":

    avg = 0

    for n in range(jury):
        grade = float(input())
        avg += grade
        total_avg += grade
        total_grades += 1

    avg /= jury

    print(f'{presentation} - {avg:.2f}.')

    presentation = input()

total_avg /= total_grades
print(f"Student's final assessment is {total_avg:.2f}.")