row, col = [int(x) for x in input().split(', ')]

total = 0
matrix = []

for i in range(row):
    data = [int(x) for x in input().split(', ')]
    total += sum(data)
    matrix.append(data)

print(total)
print(matrix)