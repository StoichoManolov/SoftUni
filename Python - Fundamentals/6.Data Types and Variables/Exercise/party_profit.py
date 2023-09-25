group_size = int(input())
days_spend = int(input())

coins = 0


for num in range(1, days_spend + 1):
    if num % 10 == 0:
        group_size -= 2
    if num % 15 == 0:
        group_size += 5
    coins += 50
    coins -= group_size * 2

    if num % 3 == 0 and num % 5 == 0:
        coins += group_size * 20
        coins -= group_size * 5
    elif num % 3 == 0:
        coins -= group_size * 3
    elif num % 5 == 0:
        coins += group_size * 20

coins_left = int(coins / group_size)

print(f'{group_size} companions received {int(coins_left)} coins each.')


