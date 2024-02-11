n = int(input())

matrix = [[int(y) for y in input().split()]for x in range(n)]

while True:
    command, *data = input().split()

    if command == 'END':
        break

    rows,cols,number = data

    if not (0 <= int(rows) < n and 0 <= int(cols) < n):
        print(f'Invalid coordinates')
        continue

    elif command == 'Add':
        matrix[int(rows)][int(cols)] += int(number)
    elif command == 'Subtract':
        matrix[int(rows)][int(cols)] -= int(number)

[print(*row) for row in matrix]