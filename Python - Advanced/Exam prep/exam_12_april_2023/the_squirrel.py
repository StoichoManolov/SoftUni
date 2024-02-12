rows = int(input())
direction = input().split(', ')

matrix = []
squirrel = []
hazelnuts = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(rows):
    data = list(input())

    matrix.append(data)

    if 's' in data:
        col = data.index('s')
        squirrel = [row,col]
        matrix[row][col] = '*'

for way in direction:

    current_row,current_col = squirrel
    row = current_row + directions[way][0]
    col = current_col + directions[way][1]

    if not (0 <= row < rows and 0 <= col < rows):
        print("The squirrel is out of the field.")
        break

    symbol = matrix[row][col]
    matrix[current_row][current_col] = '*'

    if symbol == 'h':
        hazelnuts += 1
        if hazelnuts == 3:
            print("Good job! You have collected all hazelnuts!")
            break
    elif symbol == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        break

    squirrel = [row,col]
else:
    print(f"There are more hazelnuts to collect.")

print(f'Hazelnuts collected: {hazelnuts}')

