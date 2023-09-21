from math import ceil,floor

MAGNOLIAS_PRICE = 3.25   # •	Магнолии – 3.25 лева
HYACINTHS_PRICE = 4  # Зюмбюли – 4 лева
ROSES_PRICE = 3.50  # Рози – 3.50 лева
CACTUS_PRICE = 8   # Кактуси – 8 лева

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cactus = int(input())
gift_price = float(input())

magnolias_cost = magnolias * MAGNOLIAS_PRICE
hyacinths_cost = hyacinths * HYACINTHS_PRICE
roses_cost = roses * ROSES_PRICE
cactus_cost = cactus * CACTUS_PRICE

total_cost = magnolias_cost + hyacinths_cost + roses_cost + cactus_cost
cost_with_taxes = total_cost - (total_cost * 0.05)

if cost_with_taxes >= gift_price:
    money_left = cost_with_taxes - gift_price
    print(f'She is left with {floor(money_left)} leva.')
else:
    money_needed = gift_price - cost_with_taxes
    print(f'She will have to borrow {ceil(money_needed)} leva.')

