courses = input().split(', ')
rank = 1
while True:
    command = input()

    if command == 'course start':
        break

    command_split = command.split(':')
    courses = input().split(', ')
    rank = 1
    while True:
        command = input()

        if command == 'course start':
            break

        command_split = command.split(':')
        command_modify = command_split[0]
        lesson_name = command_split[1]

        if command_modify == 'Add':
            if lesson_name not in courses:
                courses.append(lesson_name)
        elif command_modify == 'Insert':
            index = int(command_split[2])
            if lesson_name in courses:
                continue
            courses.insert(index, lesson_name)
        elif command_modify == 'Remove':
            if lesson_name in courses:
                courses.remove(lesson_name)
            if f'{lesson_name}-Exercise' in courses:
                courses.remove(f'{lesson_name}-Exercise')
        elif command_modify == 'Swap':
            lesson_two = command_split[2]
            if lesson_two in courses and lesson_name in courses:
                ind_one = courses.index(lesson_name)
                ind_two = courses.index(lesson_two)
                courses[ind_one], courses[ind_two] = courses[ind_two], courses[ind_one]
            else:
                continue
            if f'{lesson_name}-Exercise' in courses:
                courses.remove(f'{lesson_name}-Exercise')
                index = courses.index(lesson_name)
                courses.insert(index + 1, f'{lesson_name}-Exercise')
            if f'{lesson_two}-Exercise' in courses:
                courses.remove(f'{lesson_two}-Exercise')
                index = courses.index(lesson_two)
                courses.insert(index + 1, f'{lesson_two}-Exercise')
        elif command_modify == 'Exercise':
            if lesson_name not in courses and f'{lesson_name}-Exercise' not in courses:
                courses.append(lesson_name)
                courses.append(f'{lesson_name}-Exercise')
            elif lesson_name in courses and f'{lesson_name}-Exercise' not in courses:
                index = courses.index(lesson_name)
                courses.insert(index + 1, f'{lesson_name}-Exercise')

    for classes in courses:
        print(f'{rank}.{classes}')
        rank += 1
