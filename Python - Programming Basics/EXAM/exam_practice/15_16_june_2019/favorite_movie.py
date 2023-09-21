films = 0
max_points = 0
name = ''
is_full = False

film_name = input()

while film_name != 'STOP':

    current_points = 0

    for idx, letter in enumerate(film_name):
        points = ord(letter)
        if letter.isupper():
            points -= len(film_name)
        elif letter.islower():
            points -= 2*(len(film_name))

        current_points += points

    if current_points > max_points:
        max_points = current_points
        name = film_name

    films += 1

    if films >= 7:
        is_full = True
        break

    film_name = input()

if is_full:
    print(f'The limit is reached.')

print(f'The best movie for you is {name} with {max_points} ASCII sum.')







