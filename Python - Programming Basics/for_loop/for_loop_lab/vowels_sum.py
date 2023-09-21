word = input()

total_points = 0

for char in word:
    if char == 'a':
        total_points += 1
    elif char == 'e':
        total_points += 2
    elif char == 'i':
        total_points += 3
    elif char == 'o':
        total_points += 4
    elif char == 'u':
        total_points += 5
print(total_points)