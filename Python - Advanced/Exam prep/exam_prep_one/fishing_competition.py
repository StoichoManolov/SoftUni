size = int(input())

game_over = False
matrix = []
fisher_pos = []
fish = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row_idx in range(size):

    data = list(input())
    matrix.append(data)

    if 'S' in data:
        col = data.index('S')
        fisher_pos = [row_idx,col]


while True:

    current_row,current_col = fisher_pos

    direction = input()

    if direction == 'collect the nets':
        break

    row = current_row + directions[direction][0]
    col = current_col + directions[direction][1]

    if not (0 <= row < size and 0 <= col < size):

        if row < 0:
            row = len(matrix) - 1
        elif row >= len(matrix):
            row = 0

        if col < 0:
            col = len(matrix) - 1
        elif col >= len(matrix):
            col = 0

    matrix[current_row][current_col] = '-'
    symbol = matrix[row][col]
    matrix[row][col] = 'S'

    if symbol == 'W':
        print("You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the "
              "ship: "
              f"[{row},{col}]")
        game_over = True
        break
    elif symbol.isdigit():
        fish += int(symbol)

    fisher_pos = [row,col]

if game_over:
    pass
elif fish >= 20:
    print(f'Success! You managed to reach the quota!')

elif 20 > fish:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - fish} tons of fish more.")

if not game_over:
    if fish > 0:
        print(f'Amount of fish caught: {fish} tons.')
    [print(''.join(row)) for row in matrix]





