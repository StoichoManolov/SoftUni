row,col = [int(x) for x in input().split()]

equal_sq = 0
matrix = [[el for el in input().split()]for x in range(row)]

for row_idx in range(row - 1):
    for col_idx in range(col - 1):
        current_element = matrix[row_idx][col_idx]
        below_element = matrix[row_idx + 1][col_idx]
        right_element = matrix[row_idx][col_idx + 1]
        right_below_element = matrix[row_idx + 1][col_idx + 1]

        if current_element == right_element and current_element == below_element and current_element == \
                right_below_element:
            equal_sq += 1


print(equal_sq)