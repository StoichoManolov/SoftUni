chrysanthemums_bought = int(input())
roses_bought = int(input())
tulips_bought = int(input())
season = input()
holiday_or_not = input()
chrysanthemums_price = 0
roses_price = 0
tulips_price = 0
total_flower = roses_bought + chrysanthemums_bought + tulips_bought

if season == 'Spring' or season == 'Summer':
    chrysanthemums_price = 2
    roses_price = 4.10
    tulips_price = 2.50
elif season == 'Winter' or season == 'Autumn':
    chrysanthemums_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15

if holiday_or_not == 'Y':
    chrysanthemums_price *= 1.15
    roses_price *= 1.15
    tulips_price *= 1.15

cost = chrysanthemums_bought * chrysanthemums_price + tulips_bought * tulips_price + roses_bought * roses_price

if season == 'Spring' and tulips_bought > 7:
    cost *= 0.95
elif season == 'Winter' and roses_bought >= 10:
    cost *= 0.90

if total_flower > 20:
    cost *= 0.80

cost = cost + 2
print(f'{cost:.2f}')


