def movie_organizer(*args):
    movies = {}
    result = ''

    for movie,genre in args:
        if genre not in movies:
            movies[genre] = []
        movies[genre].append(movie)

    movies_sorted = sorted(movies.items(), key=lambda x: (-len(x[1]), x[0]))

    for genre,movie in movies_sorted:
        result += f'{genre} - {len(movies[genre])}\n'

        movies_in_genre_sorted = sorted(movie)
        for mov in movies_in_genre_sorted:
            result += f'* {mov}\n'

    return result


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))

