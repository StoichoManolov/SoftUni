from sys import maxsize

films = int(input())
max_rating = - maxsize
lowest_rating = maxsize
average = 0
max_rating_movie = ''
lowest_rating_movie = ''

for _ in range(films):
    film_name = input()
    film_score = float(input())
    average += film_score
    if max_rating < film_score:
        max_rating = film_score
        max_rating_movie = film_name
    if lowest_rating > film_score:
        lowest_rating = film_score
        lowest_rating_movie = film_name

average /= films

print(f'{max_rating_movie} is with highest rating: {max_rating:.1f}')
print(f'{lowest_rating_movie} is with lowest rating: {lowest_rating:.1f}')
print(f'Average rating: {average:.1f}')

