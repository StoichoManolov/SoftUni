product = input().lower()
city = input().lower()
amount = float(input())

if city == 'sofia':
    if product == 'coffee':
        price = 0.5
    elif product == 'water':
        price = 0.8
    elif product == 'beer':
        price = 1.20
    elif product == 'sweets':
        price = 1.45
    elif product == 'peanuts':
        price = 1.60

if city == 'plovdiv':
    if product == 'coffee':
        price = 0.4
    elif product == 'water':
        price = 0.7
    elif product == 'beer':
        price = 1.15
    elif product == 'sweets':
        price = 1.30
    elif product == 'peanuts':
        price = 1.50

if city == 'varna':
    if product == 'coffee':
        price = 0.45
    elif product == 'water':
        price = 0.7
    elif product == 'beer':
        price = 1.10
    elif product == 'sweets':
        price = 1.35
    elif product == 'peanuts':
        price = 1.55

total_cost = amount * price
print(total_cost)