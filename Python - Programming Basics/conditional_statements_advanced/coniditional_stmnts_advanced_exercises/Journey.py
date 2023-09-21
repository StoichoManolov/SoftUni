budget = float(input())
season = input()
price = 0
type_of_holiday = ''
place = ''

if budget <= 100:  # Bulgaria
    place = 'Bulgaria'
    if season == 'summer':
        type_of_holiday = 'Camp'
        price = 0.3
    elif season == 'winter':
        type_of_holiday = 'Hotel'
        price = 0.70
elif budget <= 1000:  # Balkans
    place = 'Balkans'
    type_of_holiday = 'Camp'
    if season == 'summer':
        price = 0.40
    elif season == 'winter':
        type_of_holiday = 'Hotel'
        price = 0.80
elif budget > 1000:  # Europe
    place = 'Europe'
    type_of_holiday = 'Hotel'
    price = 0.9

total_cost = budget * price
print(f'Somewhere in {place}')
print(f'{type_of_holiday} - {total_cost:.2f}')

