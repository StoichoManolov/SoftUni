size = int(input())

matrix = []
pos = []
killed_planes = 0
armor = 300

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    data = list(input())

    if 'J' in data:
        col = data.index('J')
        pos = [row,col]

    matrix.append(data)

while True:

    direction = input()

    current_row,current_col = pos

    row = current_row + directions[direction][0]
    col = current_col + directions[direction][1]

    symbol = matrix[row][col]
    matrix[current_row][current_col] = '-'
    matrix[row][col] = 'J'

    if symbol == 'E':
        armor -= 100
        killed_planes += 1
        if killed_planes == 4:
            print("Mission accomplished, you neutralized the aerial threat!")
            break
        if armor == 0:
            print(f"Mission failed, your jetfighter was shot down! Last coordinates [{row}, {col}]!")
            break
    elif symbol == 'R':
        armor = 300

    pos = [row,col]

[print(''.join(row)) for row in matrix]
