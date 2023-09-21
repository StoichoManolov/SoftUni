month = input().lower()
days_rented = int(input())
price = 0
discount = 0

if month == 'may' or month == 'october':
    if 7 < days_rented <= 13:
        price = 50 * 0.95
    elif days_rented > 14:
        price = 50 * 0.70
    else:
        price = 50
elif month == 'june' or month == 'september':
    if days_rented > 14:
        price = 75.20 * 0.80
    else:
        price = 75.20
elif month == 'july' or month == 'august':
    price = 76

studio_price = days_rented * price

if month == 'may' or month == 'october':
    price = 65
elif month == 'june' or month == 'september':
    price = 68.70
elif month == 'july' or month == 'august':
    price = 77

if days_rented > 14:
    discount = 0.10

price_discount = price * (1 - discount)
apartment_price = days_rented * price_discount

print(f'Apartment: {apartment_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')

