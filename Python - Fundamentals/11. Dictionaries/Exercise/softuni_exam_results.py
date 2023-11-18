results = {'Submissions': {}}

while True:

    command = input()
    if command == 'exam finished':
        break

    if 'banned' not in command:
        username, language, points = [int(x) if x.isdigit() else x for x in command.split("-")]
        if username not in results:
            results[username] = []
            results[username].append(language)
        if language not in results['Submissions']:
            results['Submissions'][language] = 0
        results['Submissions'][language] += 1
        results[username].append(points)

    else:
        username, banned = command.split('-')

        del results[username]


print(f'Results:')
for i in results:
    if i != "Submissions":
        grade = 0
        for values in results[i]:
            if isinstance(values, int):
                if values > grade:
                    grade = values
        print(f'{i} | {grade}')

print(f'Submissions:')
for items,values in results['Submissions'].items():
    print(f'{items} - {values}')



