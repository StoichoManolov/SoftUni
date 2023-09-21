decorations = int(input())
days = int(input())

total_cost = 0
total_spirit = 0

for num in range(1, days + 1):
    if num % 11 == 0:
        decorations += 2

    if num % 2 == 0:
        total_cost += decorations * 2
        total_spirit += 5
    if num % 3 == 0 and num % 5 == 0:
        total_cost += decorations * 3 + decorations * 15 + decorations * 5
        total_spirit += 60
    elif num % 3 == 0:
        total_cost += decorations * 3 + decorations * 5
        total_spirit += 13
    elif num % 5 == 0:
        total_cost += decorations * 15
        total_spirit += 17

    if num % 10 == 0:
        total_spirit -= 20
        total_cost += 23

    if num == days and days % 10 == 0:
        total_spirit -= 30


print(f'Total cost: {total_cost}')
print(f'Total spirit: {total_spirit}')
