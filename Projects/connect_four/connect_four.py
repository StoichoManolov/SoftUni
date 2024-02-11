class FullColumnError(Exception):
    pass


class InvalidColumnChoice(Exception):
    pass


ROWS = 6
COLS = 7

DIRECTION_MAPPER = {
    'left': (0, -1),
    'up': (-1, 0),
    'main_diagonal': (-1, -1),
    'other_diagonal': (-1, 1),
}


def travel_direction(coordinates,current_row,current_col,element ,board):
    count = 0
    for i in range(1, 4):
        row_direction, col_direction = coordinates
        next_element_row_idx = current_row + row_direction * i
        next_element_col_idx = current_col + col_direction * i
        try:
            if board[next_element_row_idx][next_element_col_idx] == element:
                count += 1
            else:
                return count
        except IndexError:
            return count


def travel_opposite_direction(coordinates,current_row,current_col,element ,board):
    count = 0
    for i in range(1, 4):
        row_direction, col_direction = coordinates
        next_element_row_idx = current_row - row_direction * i
        next_element_col_idx = current_col - col_direction * i
        try:
            if board[next_element_row_idx][next_element_col_idx] == element:
                count += 1
            else:
                return count
        except IndexError:
            return count
    return count


def is_winner(row,col,board):

    for direction, coords in DIRECTION_MAPPER.items():
        searched_element = board[row][col]
        travel_direction_count = travel_direction(coords, row, col, searched_element, board)
        travel_opposite_direction_count = travel_opposite_direction(coords, row, col, searched_element, board)

        if travel_direction_count + travel_opposite_direction_count + 1 >= 4:
            return True
    else:
        return False


def is_board_full(board):
    available_spots = [el for el in board[0] if el == 0]
    if not available_spots:
        return True
    return False


def validate_col(col):

    if 1 <= col <= COLS:
        return True
    raise InvalidColumnChoice


def print_board(board):

    for row in board:
        print(row)


def player_choice(col_index, board):

    for row_idx in range(ROWS - 1, -1, -1):
        if board[row_idx][col_index] == 0:
            return row_idx
        else:
            raise FullColumnError('This column is full, please select another one.')


board = []

for _ in range(ROWS):
    board.append([0 for _ in range(COLS)])

turns = 1
while True:
    player = 2 if turns % 2 == 0 else 1

    try:
        column = int(input(f'Player {player}, please choose a column: '))
        validate_col(column)
        column_idx = int(column) - 1
        row = player_choice(column_idx,board)
        board[row][column_idx] = player
        if is_winner(row, column_idx, board):
            break
        if is_board_full(board):
            print('Board is full, nobody wins.')
            exit()
    except FullColumnError:
        print('This column is already full, please select another one.')
        continue
    except (InvalidColumnChoice, ValueError):
        print(f'This column is invalid, please select a number between 1 and {COLS}')
        continue

    print_board(board)
    turns += 1

print_board(board)
print(f'Winners is {player}')


