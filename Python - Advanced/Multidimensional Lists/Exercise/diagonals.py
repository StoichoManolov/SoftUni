# n = int(input())
#
# matrix = [[int(el) for el in input().split(", ")] for _ in range(n)]
# primary = [matrix[r][r] for r in range(n)]
# second = [matrix[r][n - r - 1] for r in range(n)]
#
# print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
# print(f"Secondary diagonal: {', '.join(str(x) for x in second)}. Sum: {sum(second)}")
#
# rows = int(input())
#
# nested_list = [[int(x) for x in input().split(", ")] for _ in range(rows)]
#
#
# def diagonal_sums(matrix, rows):
#     diagonals = {
#         "primary sum": [],
#         "secondary sum": []
#     }
#
#     for i in range(rows):
#         diagonals["primary sum"].append(matrix[i][i])
#         diagonals["secondary sum"].append(matrix[i][rows - i - 1])
#
#     print(
#         f"Primary diagonal: {', '.join(str(x) for x in diagonals['primary sum'])}. Sum: {sum(diagonals['primary sum'])}")
#     print(
#         f"Secondary diagonal: {', '.join(map(str, diagonals['secondary sum']))}. Sum: {sum(diagonals['secondary sum'])}")
#
#
# diagonal_sums(nested_list, rows)

#
# [1,2,3]
# [4,5,6]
# [7,8,9]

n = int(input())

matrix = [[int(el) for el in input().split(', ')]for _ in range(n)]

primary = []
secondary = []

for r_idx in range(n):
    primary.append(matrix[r_idx][r_idx])
    secondary.append(matrix[r_idx][n - r_idx - 1])

print(primary)
print(secondary)