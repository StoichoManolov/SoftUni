from collections import deque

SIZE = 6

matrix = []
tom = False
jerry = False

players = deque(input().split(', '))

for row in range(SIZE):
    data = input().split()

    matrix.append(data)

while True:

    row,col = [int(x) for x in input()[1:-1].split(", ")]

    player = players[0]

    if tom and player == 'Tom':
        tom = False
        players.rotate()
        continue
    elif jerry and player == 'Jerry':
        jerry = False
        players.rotate()
        continue

    symbol = matrix[row][col]

    if symbol == 'E':
        print(f"{player} found the Exit and wins the game!")
        break
    elif symbol == 'T':
        print(f"{player} is out of the game! The winner is {players[1]}." )
        break
    elif symbol == 'W':
        print(f"{player} hits a wall and needs to rest.")
        if player == 'Tom':
            tom = True
        elif player == 'Jerry':
            jerry = True

    players.rotate()