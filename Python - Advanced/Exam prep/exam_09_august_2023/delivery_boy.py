rows, cols = [int(x) for x in input().split()]

matrix = []
boy_pos = []
boy_starting = []


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(rows):
    data = list(input())

    matrix.append(data)
    if 'B' in data:
        col = data.index('B')
        boy_pos = [row, col]
        boy_starting = [row, col]


while True:
    current_row, current_col = boy_pos

    command = input()

    row = current_row + directions[command][0]
    col = current_col + directions[command][1]

    if not (0 <= row < rows and 0 <= col < cols):
        print("The delivery is late. Order is canceled.")
        row, col = boy_starting
        matrix[row][col] = ' '
        break

    symbol = matrix[row][col]

    if symbol == '*':
        continue

    boy_pos = [row, col]

    if symbol == 'P':
        matrix[row][col] = 'R'
        print("Pizza is collected. 10 minutes for delivery.")

    elif symbol == 'A':
        matrix[row][col] = 'P'
        print(f"Pizza is delivered on time! Next order...")
        break

    elif symbol == '-':
        matrix[row][col] = '.'


[print(''.join(row)) for row in matrix]


