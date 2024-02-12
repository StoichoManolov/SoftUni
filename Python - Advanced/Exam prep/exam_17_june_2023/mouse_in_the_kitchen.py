rows,cols = [int(x) for x in input().split(',')]

matrix = []
mouse_pos = []
cheese = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(rows):
    data = list(input())

    matrix.append(data)

    if 'M' in data:
        col = data.index('M')
        mouse_pos = [row,col]

    if 'C' in data:
        cheese_count = data.count('C')
        cheese += cheese_count


while True:

    current_row, current_col = mouse_pos

    direction = input()
    if direction == 'danger':
        print('Mouse will come back later!')
        break

    row = current_row + directions[direction][0]
    col = current_col + directions[direction][1]

    if not (0 <= row < rows and 0 <= col < cols):
        print('No more cheese for tonight!')
        break

    symbol = matrix[row][col]

    if symbol == '@':
        continue

    matrix[current_row][current_col] = '*'
    matrix[row][col] = 'M'

    mouse_pos = [row, col]

    if symbol == 'T':
        print('Mouse is trapped!')
        break
    elif symbol == 'C':
        cheese -= 1
        if cheese <= 0:
            print('Happy mouse! All the cheese is eaten, good night!')
            break


[print("".join(row)) for row in matrix]



