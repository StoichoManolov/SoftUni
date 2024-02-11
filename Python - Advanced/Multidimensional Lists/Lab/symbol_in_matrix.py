n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(input()))

searched_element = input()
is_found = False

for row_idx in range(n):
    if is_found:
        break
    for col_idx in range(len(matrix[row_idx])):
        if matrix[row_idx][col_idx] == searched_element:
            print(f'({row_idx}, {col_idx})')
            is_found = True
            break

if not is_found:
    print(f'{searched_element} does not occur in the matrix')



