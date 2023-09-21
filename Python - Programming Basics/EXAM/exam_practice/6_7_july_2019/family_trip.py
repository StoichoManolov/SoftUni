budget = float(input())
sleeping = int(input())
price_per_night = float(input())
percent_bonus_tax = int(input())

if sleeping > 7:
    price_per_night *= 0.95

bonus_tax = budget * (percent_bonus_tax / 100)

total = bonus_tax + (sleeping * price_per_night)
diff = abs(total - budget)
if total <= budget:
    print(f'Ivanovi will be left with {diff:.2f} leva after vacation.')
else:
    print(f'{diff:.2f} leva needed.')
