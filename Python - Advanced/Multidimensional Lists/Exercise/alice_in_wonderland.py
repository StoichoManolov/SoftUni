size = int(input())

collected_bags = 0
alice_pos = []
matrix = []

directions = {  # създаваме променлива, в която да пазим посоките
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    matrix.append(input().split())

    if 'A' in matrix[row]:
        alice_pos = [row,matrix[row].index('A')]
        matrix[row][alice_pos[1]] = '*'

while collected_bags < 10:
    direction = input()

    row = alice_pos[0] + directions[direction][0]
    col = alice_pos[1] + directions[direction][1]

    if not (0 <= row < size and 0 <= col < size):
        break

    alice_pos = [row,col]
    position = matrix[row][col]
    matrix[row][col] = '*'

    if position == 'R':
        break

    if position.isdigit():
        collected_bags += int(position)

if collected_bags < 10:  # проверяваме дали Алиса е събрала нужния брой пакетчета, в случая 10
    print("Alice didn't make it to the tea party.")  # принтираме, че Алиса не е успяла да отиде на партито
else:
    print("She did it! She went to the party.")  # принтираме, че Алиса е успяла да отиде на партито

print(*[' '.join(row) for row in matrix], sep='\n')  # принтираме матрицата
