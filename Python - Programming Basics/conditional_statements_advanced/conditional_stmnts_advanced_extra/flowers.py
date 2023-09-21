chrysanthemums_bought = int(input())
roses_bought = int(input())
tulips_bought = int(input())
season_bought_in = input().lower()
holiday_or_not = input().lower()
discount = 0
if season_bought_in == 'summer' or season_bought_in == 'spring':
    chrysanthemums_price = 2.00
    roses_price = 4.10
    tulips_price = 2.50
else:
    chrysanthemums_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15

total_flowers = chrysanthemums_bought + roses_bought + tulips_bought
flowers_cost = chrysanthemums_bought * chrysanthemums_price + tulips_bought * tulips_price + roses_bought * roses_price

if holiday_or_not == 'y':
    new_cost = flowers_cost * 0.15 + flowers_cost
else:
    new_cost = flowers_cost

if tulips_bought >= 7 and season_bought_in == 'spring':
    new_price = new_cost - (new_cost * 0.05)
else:
    new_price = new_cost

if roses_bought >= 10 and season_bought_in == 'winter':
    new_cost_two = new_price - (new_price * 0.10)
else:
    new_cost_two = new_price

if total_flowers >= 20:
    discount = 0.20

new_cost_final = new_cost_two - (new_cost_two * (1 - discount))
total_cost_zx = (new_cost_two - new_cost_final) + 2

print(f'{total_cost_zx:.2f}')
