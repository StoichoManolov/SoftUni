n = int(input())

matrix = [[int(el) for el in input().split()]for _ in range(n)]

primary = 0
secondary = 0

for r_idx in range(n):
    primary += matrix[r_idx][r_idx]
    secondary += matrix[r_idx][n - r_idx - 1]

print(abs(primary - secondary))