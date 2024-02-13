SIZE = 6

matrix = []
position = []
iteration = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(SIZE):
    data = input().split()

    matrix.append(data)

tuples = input()

for tup in tuples.split('),('):
    tup = tup.replace(')','').replace('(','')
    t_split = tup.split(',')
    for i in t_split:
        position.append(int(i))

while True:
    current_row,current_col = position

    command = input()

    if command == 'Stop':
        break

    commands = command.split(', ')

    act = commands[0]
    direction = commands.pop(1)

    row = int(current_row) + directions[direction][0]
    col = int(current_col) + directions[direction][1]

    if act == 'Create':
        value = commands[1]

        if matrix[row][col] == '.':
            matrix[row][col] = value

    elif act == 'Update':
        value = commands[1]
        if matrix[row][col] != '.':
            matrix[row][col] = value
    elif act == 'Delete':
        if not matrix[row][col] == '.':
            matrix[row][col] = '.'
    elif act == 'Read':
        if matrix[row][col] != '.':
            symbol = matrix[row][col]
            print(symbol)

    position = [row,col]

[print(' '.join(row)) for row in matrix]