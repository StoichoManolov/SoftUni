size = int(input())

matrix = [list(input()) for _ in range(size)]

positions = (  # създаваме тюпъл с всички посоки на коня
    (-2, -1),  # горе 2 и ляво 1
    (-2, 1),  # горе 2 и дясно 1
    (-1, -2),  # горе 1 и ляво 2
    (-1, 2),  # горе 1 и дясно 2
    (2, 1),  # долу 2 и дясно 1
    (2, -1),  # долу 2 и ляво 1
    (1, 2),  # долу  1 и дясно 2
    (1, -2)  # долу 1 и ляво 2
)

removed_knights = 0

while True:
    max_attacks = 0
    knight_with_most_attacks_pos = []

    for row in range(size):
        for col in range(size):

            if matrix[row][col] == 'K':
                attacks = 0

                for pos in positions:
                    pos_row = row + pos[0]
                    col_row = col + pos[1]

                    if 0 <= pos_row < size and 0 <= col_row < size:
                        if matrix[pos_row][col_row] == 'K':
                            attacks += 1

                if attacks > max_attacks:
                    max_attacks = attacks
                    knight_with_most_attacks_pos = [row, col]

    if knight_with_most_attacks_pos:  # проверяваме дали имаме кон за махане
        r, c = knight_with_most_attacks_pos  # взимаме позицията на коня
        matrix[r][c] = "0"  # заменяме коня с 0
        removed_knights += 1  # увеличаваме броя на махнатите коне
    else:  # в противен случай, прекратяваме цикъла
        break

print(removed_knights)