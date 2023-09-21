budget = float(input())
season = input().lower()
car_cost = 0
car_type = ''
if budget <= 100:
    print('Economy class')
    if season == 'summer':
        car_cost = 0.35
        car_type = 'Cabrio'
    elif season == 'winter':
        car_type = 'Jeep'
        car_cost = 0.65
elif 100 < budget <= 500:
    print('Compact class')
    if season == 'summer':
        car_type = 'Cabrio'
        car_cost = 0.45
    elif season == 'winter':
        car_type = 'Jeep'
        car_cost = 0.80
elif budget > 500:
    print('Luxury class')
    car_type = 'Jeep'
    car_cost = 0.90

total_cost = budget * car_cost

print(f'{car_type} - {total_cost:.2f}')





