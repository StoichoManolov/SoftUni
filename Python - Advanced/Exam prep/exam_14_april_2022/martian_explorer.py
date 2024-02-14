SIZE = 6

position = []
matrix = []

water = 0
metal = 0
concrete = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(SIZE):
    data = input().split()

    if 'E' in data:
        col = data.index('E')
        position = [row,col]
    matrix.append(data)

direction = input().split(', ')

for ways in direction:

    current_row,current_col = position

    row = current_row + directions[ways][0]
    col = current_col + directions[ways][1]

    if not (0 <= row < SIZE and 0 <= col < SIZE):

        if row < 0:
            row = len(matrix) - 1
        elif row >= len(matrix):
            row = 0

        if col < 0:
            col = len(matrix) - 1
        elif col >= len(matrix):
            col = 0

    symbol = matrix[row][col]
    matrix[row][col] = 'E'
    matrix[current_row][current_col] = '-'

    if symbol == 'W':
        print(f'Water deposit found at ({row}, {col})')
        water += 1
    elif symbol == 'M':
        print(f'Metal deposit found at ({row}, {col})')
        metal += 1
    elif symbol == 'C':
        print(f'Concrete deposit found at ({row}, {col})')
        concrete += 1
    elif symbol == 'R':
        print(f'Rover got broken at ({row}, {col})')
        break

    position = [row,col]


if metal and concrete and water:
    print('Area suitable to start the colony.')
else:
    print("Area not suitable to start the colony.")







