from math import ceil

guests = int(input())
budget = int(input())

bread = ceil(guests / 3)
eggs = guests * 2
bread_price = bread * 4
eggs_price = eggs * 0.45

total = eggs_price + bread_price

diff = abs(total - budget)

if budget >= total:
    print(f'Lyubo bought {bread} Easter bread and {eggs} eggs.')
    print(f'He has {diff:.2f} lv. left.')
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {diff:.2f} lv. more.")

