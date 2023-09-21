season = input()
km_per_month = float(input())
price_per_km = 0

if season == 'Autumn' or season == 'Spring':
    if km_per_month <= 5000:
        price_per_km = 0.75
    elif km_per_month <= 10000:
        price_per_km = 0.95
    elif 10000 < km_per_month <= 20000:
        price_per_km = 1.45
elif season == 'Summer':
    if km_per_month <= 5000:
        price_per_km = 0.90
    elif km_per_month <= 10000:
        price_per_km = 1.10
    elif 10000 < km_per_month <= 20000:
        price_per_km = 1.45
elif season == 'Winter':
    if km_per_month <= 5000:
        price_per_km = 1.05
    elif km_per_month <= 10000:
        price_per_km = 1.25
    elif 10000 < km_per_month <= 20000:
        price_per_km = 1.45

salary = ((km_per_month * price_per_km) * 4)
salary *= 0.90
print(f'{salary:.2f}')