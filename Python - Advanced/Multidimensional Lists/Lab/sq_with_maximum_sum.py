row, col = [int(x) for x in input().split(', ')]

matrix = []
sub_matrix = []
max_sum = 0

for _ in range(row):
    matrix.append([int(x) for x in input().split(', ')])

for row_index in range(row - 1):
    for col_index in range(col - 1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        element_under = matrix[row_index + 1][col_index]
        diagonal_element = matrix[row_index + 1][col_index + 1]

        total_sum = current_element + next_element + element_under + diagonal_element
        if total_sum > max_sum:
            max_sum = total_sum
            sub_matrix =[[current_element,next_element],[element_under, diagonal_element]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)