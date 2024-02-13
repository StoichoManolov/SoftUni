size = int(input())
racing_number = input()

matrix = []
car = []
kilometers = 0
t_list = []


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    data = input().split()

    matrix.append(data)
    car = [0, 0]

    if 'T' in data:
        col = data.index('T')
        t_list.append([row,col])


while True:
    command = input()

    if command == 'End':
        print(f"Racing car {racing_number} DNF.")
        row,col = car
        break

    current_row,current_col = car

    row = current_row + directions[command][0]
    col = current_col + directions[command][1]

    symbol = matrix[row][col]
    matrix[row][col] = '.'
    car = [row,col]

    if symbol == '.':
        kilometers += 10

    elif symbol == 'T':
        kilometers += 30
        t_list.remove([row,col])
        row,col = t_list[0]
        matrix[row][col] = '.'
        car = [row,col]
    elif symbol == 'F':
        kilometers += 10
        print(f'Racing car {racing_number} finished the stage!')
        break

matrix[row][col] = 'C'

print(f'Distance covered {kilometers} km.')
[print("".join(row))for row in matrix]
