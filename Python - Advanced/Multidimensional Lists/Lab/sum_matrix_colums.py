rows,columns = [int(x) for x in input().split(', ')]

matrix = []

for i in range(rows):
    row_date = [int(x) for x in input().split()]
    matrix.append(row_date)

for cow_idx in range(columns):
    col_total = 0
    for row_idx in range(rows):
        col_total += matrix[row_idx][cow_idx]
    print(col_total)
