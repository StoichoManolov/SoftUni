budget = float(input())
series_amount = int(input())
cost = 0

for _ in range(series_amount):
    series_name = input()
    series_price = float(input())
    if series_name == 'Thrones':
        series_price *= 0.50
    elif series_name == 'Lucifer':
        series_price *= 0.60
    elif series_name == 'Protector':
        series_price *= 0.70
    elif series_name == 'TotalDrama':
        series_price *= 0.80
    elif series_name == 'Area':
        series_price *= 0.90
    cost += series_price

diff = abs(budget - cost)

if budget >= cost:
    print(f'You bought all the series and left with {diff:.2f} lv.')
else:
    print(f'You need {diff:.2f} lv. more to buy the series!')


