row = int(input())

matrix = []
for i in range(row):
    row_data = [int(x) for x in input().split(', ')]
    matrix.extend(row_data)

print(matrix)