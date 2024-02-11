# row = int(input())
#
# matrix = []
#
# for i in range(row):
#     matrix.append([int(x) for x in input().split()])
#
# total_sum = 0
#
# for row_idx in range(row):
#     for col_idx in range(row):
#         if row_idx == col_idx:
#             total_sum += matrix[row_idx][col_idx]
#
# print(total_sum)

row = int(input())

matrix = []

for i in range(row):
    matrix.append([int(x) for x in input().split()])

total_sum = 0
for row_idx in range(row):
    total_sum += matrix[row_idx][row_idx]

print(total_sum)

