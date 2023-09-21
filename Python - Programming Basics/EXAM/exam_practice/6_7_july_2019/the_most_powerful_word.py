from math import floor

word = input()
points = 0
vocal = 'a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'
name = ''

while not word == 'End of words':
    current_points = 0
    for letter, symbol in enumerate(word):
        current_points += ord(symbol)

    if word[0] in vocal:
        current_points *= len(word)
    else:
        current_points = floor(current_points / len(word))

    if current_points > points:
        points = current_points
        name = word

    word = input()

print(f'The most powerful word is {name} - {points}')




