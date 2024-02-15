from collections import deque

size = 8
matrix = []
white = []
black = []
start = ord('a')
players = deque(['white', 'black'])

for row in range(size):
    data = input().split()

    if 'w' in data:
        col = data.index('w')
        white = [row,col]

    if 'b' in data:
        col = data.index('b')
        black = [row,col]
    matrix.append(data)


while True:

    player = players[0]

    if player == 'white':
        row,col = white
        matrix[row][col] = '-'

        if 0 <= row - 1 < size and 0 <= col - 1 < size:
            if matrix[row - 1][col - 1] == 'b':
                start += col - 1
                letter = chr(start)
                print(f'Game over! White win, capture on {letter}{abs(row-9)}.')
                break

        if 0 <= row - 1 < size and 0 <= col + 1 < size:
            if matrix[row - 1][col + 1] == 'b':
                start += col + 1
                letter = chr(start)
                print(f'Game over! White win, capture on {letter}{abs(row-9)}.')
                break
        row -= 1

        matrix[row][col] = 'w'
        white = [row,col]
        if row == 0:
            start += col
            letter = chr(start)
            print(f'Game over! White pawn is promoted to a queen at {letter}{len(matrix)}.')
            break

    elif player == 'black':
        row,col = black
        matrix[row][col] = '-'

        if 0 <= row+1 < size and 0 <= col-1 < size:
            if matrix[row + 1][col-1] == 'w':
                start += col - 1
                letter = chr(start)
                print(f'Game over! Black win, capture on {letter}{abs(row+1-8)}.')
                break

        if 0 <= row+1 < size and 0 <= col + 1 < size:
            if matrix[row+1][col+1] == 'w':
                start += col + 1
                letter = chr(start)
                print(f'Game over! Black win, capture on {letter}{abs(row+1-8)}.')
                break

        row += 1
        matrix[row][col] = 'b'
        black = [row,col]

        if row == len(matrix) - 1:
            start += col
            letter = chr(start)
            print(f'Game over! Black pawn is promoted to a queen at {letter}{1}.')
            break

    players.rotate()

# matrix = []
# b_row, b_col, w_col, w_row = 0, 0, 0, 0
#
# for row in range(8):
#     matrix.append(input().split())
#     if "w" in matrix[row]:
#         w_row, w_col = row, matrix[row].index("w")
#     elif "b" in matrix[row]:
#         b_row, b_col = row, matrix[row].index("b")
#
# while True:
#
#     if (w_row - 1, w_col - 1) == (b_row, b_col) or (w_row - 1, w_col + 1) == (b_row, b_col):
#         print(f"Game over! White win, capture on {chr(97 + b_col)}{abs(b_row - 8)}.")
#         break
#     w_row -= 1
#     if w_row == -1:
#         print(f"Game over! White pawn is promoted to a queen at {chr(97 + w_col)}8.")
#         break
#
#     if (b_row + 1, b_col - 1) == (w_row, w_col) or (b_row + 1, b_col + 1) == (w_row, w_col):
#         print(f"Game over! Black win, capture on {chr(97 + w_col)}{abs(w_row - 8)}.")
#         break
#     b_row += 1
#     if b_row == 8:
#         print(f"Game over! Black pawn is promoted to a queen at {chr(97 + b_col)}1.")
#         break
