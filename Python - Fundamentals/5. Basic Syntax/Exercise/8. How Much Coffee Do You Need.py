command = input()
coffees = 0

lower_case = 'coding', 'dog', 'cat', 'movie'
upper_case = 'CODING', 'DOG', 'CAT', 'MOVIE'

while command != 'END':
    if command in lower_case:
        coffees += 1
    elif command in upper_case:
        coffees += 2

    command = input()

if coffees > 5:
    print(f'You need extra sleep')
else:
    print(f'{coffees}')


