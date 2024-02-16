rows,cols = [int(x) for x in input().split(', ')]

matrix = []
pos = []

items_collected = 0
all_items = 0
collected = False

cookies = 0
gifts = 0
decorations = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(rows):
    data = input().split()

    if 'Y' in data:
        col = data.index('Y')
        pos = [row,col]

    if 'G' in data:
        amount = data.count('G')
        all_items += amount

    if 'D' in data:
        amount = data.count('D')
        all_items += amount
    if 'C' in data:
        amount = data.count('C')
        all_items += amount

    matrix.append(data)


while True:

    command = input()

    if command == 'End':
        break

    direction,steps = command.split('-')

    for _ in range(int(steps)):
        current_row,current_col = pos

        row = current_row + directions[direction][0]
        col = current_col + directions[direction][1]

        if not (0 <= row < rows and 0 <= col < cols):

            if row > rows - 1:
                row = 0
            elif row < 0:
                row = rows - 1

            if col > cols - 1:
                col = 0
            elif col < 0:
                col = cols - 1

        symbol = matrix[row][col]
        matrix[current_row][current_col] = 'x'
        matrix[row][col] = 'Y'

        if symbol == 'D':
            items_collected += 1
            decorations += 1
        elif symbol == 'G':
            gifts += 1
            items_collected +=1
        elif symbol == 'C':
            cookies += 1
            items_collected += 1

        pos = [row,col]

        if items_collected == all_items:
            collected = True
            print("Merry Christmas!")
            break

    if collected:
        break

print("You've collected:")
print(f'- {decorations} Christmas decorations')
print(f'- {gifts} Gifts')
print(f'- {cookies} Cookies')

[print(' '.join(row)) for row in matrix]