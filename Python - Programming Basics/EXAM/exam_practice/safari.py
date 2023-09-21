budget = float(input())
fuel_needed = float(input())
day_of_the_week = input()
discount = 0

fuel_price = fuel_needed * 2.10

if day_of_the_week == 'Saturday':
    discount = 0.10
elif day_of_the_week == 'Sunday':
    discount = 0.20

total_cost = (fuel_price + 100) * (1 - discount)
if total_cost <= budget:
    print(f'Safari time! Money left: {budget - total_cost:.2f} lv')
else:
    print(f'Not enough money! Money needed {abs(budget - total_cost):.2f}')

print(discount)
