rows,cols = [int(x) for x in input().split()]

matrix = []
position = []
players = 0
moves = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(rows):
    data = input().split()

    matrix.append(data)

    if 'B' in data:
        col = data.index('B')
        position = [row,col]
        matrix[row][col] = '-'

while True:
    direction = input()

    if direction == 'Finish':
        break

    current_row,current_col = position

    row = current_row + directions[direction][0]
    col = current_col + directions[direction][1]

    if not (0 <= row < rows and 0 <= col < cols):
        continue

    symbol = matrix[row][col]

    if symbol == 'O':
        continue

    position = [row,col]

    if symbol == '-':
        moves += 1
    elif symbol == 'P':
        players += 1
        moves += 1
        matrix[row][col] = '-'
        if players == 3:
            break

print('Game over!')

print(f'Touched opponents: {players} Moves made: {moves}')
