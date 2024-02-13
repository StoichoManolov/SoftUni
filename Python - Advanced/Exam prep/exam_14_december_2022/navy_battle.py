size = int(input())

matrix = []
submarine = []
mines_hit = 0
cruiser_ships = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    data = list(input())

    matrix.append(data)

    if 'S' in data:
        col = data.index('S')
        submarine = [row,col]

while True:

    direction = input()

    current_row,current_col = submarine

    row = current_row + directions[direction][0]
    col = current_col + directions[direction][1]

    symbol = matrix[row][col]
    matrix[row][col] = 'S'
    matrix[current_row][current_col] = '-'
    submarine = [row,col]

    if symbol == '-':
        continue
    elif symbol == '*':
        mines_hit += 1
        if mines_hit == 3:
            print(f'Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!')
            break
    elif symbol == 'C':
        cruiser_ships += 1
        if cruiser_ships == 3:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break


[print(''.join(row)) for row in matrix]