budget = float(input())
season = input().lower()
location = ''
type_of_shelter = ''
price = 0

if budget <= 1000:
    type_of_shelter = 'Camp'
    if season == 'summer':
        price = 0.65
    elif season == 'winter':
        price = 0.45
elif 1000 < budget <= 3000:
    type_of_shelter = 'Hut'
    if season == 'summer':
        price = 0.80
    elif season == 'winter':
        price = 0.60
elif budget > 3000:
    type_of_shelter = 'Hotel'
    if season == 'summer':
        price = 0.90
    elif season == 'winter':
        price = 0.90

if season == 'summer':
    location = 'Alaska'
elif season == 'winter':
    location = 'Morocco'

total_cost = budget * price
print(f'{location} - {type_of_shelter} - {total_cost:.2f}')

