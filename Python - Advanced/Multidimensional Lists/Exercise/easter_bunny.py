size = int(input())

way = []
best_path = []
collected_eggs = float('-inf')
matrix = []

directions = {  # създаваме променлива, в която да пазим посоките
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    matrix.append(input().split())

    if 'B' in matrix[row]:
        bunny_pos = [row,matrix[row].index('B')]

for direction,position in directions.items():

    row = bunny_pos[0] + position[0]
    col = bunny_pos[1] + position[1]

    current_eggs = 0
    current_path = []

    while 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == 'X':
            break

        current_eggs += int(matrix[row][col])
        current_path.append([row,col])

        row += position[0]
        col += position[1]

        if current_eggs > collected_eggs:
            collected_eggs = current_eggs
            way = direction
            best_path = current_path

print(way)
print(*best_path, sep='\n')
print(collected_eggs)