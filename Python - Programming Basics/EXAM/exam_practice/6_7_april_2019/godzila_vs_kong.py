budget = float(input())
statists = int(input())
clothes = float(input())
discount = 0
decor = budget * 0.10

if statists > 150:
    discount = 0.10

clothes_price = (clothes * statists) * (1 - discount)

total = clothes_price + decor

diff = abs(total - budget)

if total > budget:
    print(f'Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')
else:
    print(f'Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')
