size = int(input())

gambler_pos = []
matrix = []
money = 100
game_over = False

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    data = list(input())

    matrix.append(data)

    if 'G' in data:
        col = data.index('G')
        gambler_pos = [row,col]

while True:

    command = input()
    if command == 'end':
        break

    current_row,current_col = gambler_pos

    row = current_row + directions[command][0]
    col = current_col + directions[command][1]

    if not (0 <= row < size and 0 <= col < size):
        game_over = True
        print("Game over! You lost everything!")
        break

    symbol = matrix[row][col]
    matrix[current_row][current_col] = '-'
    matrix[row][col] = 'G'

    if symbol == 'W':
        money += 100

    elif symbol == 'P':
        money -= 200
        if money <= 0:
            print("Game over! You lost everything!")
            game_over = True
            break

    elif symbol == 'J':
        money += 100000
        print(f"You win the Jackpot!\nEnd of the game. Total amount: {money}$")
        break

    gambler_pos = [row,col]

if command == 'end':
    print(f'End of the game. Total amount: {money}$')

if not game_over:
    [print(''.join(row)) for row in matrix]