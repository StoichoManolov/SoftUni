budget = int(input())
destination = input()
season = input()
days = int(input())
price = 0

if season == 'Winter':
    if destination == 'Dubai':
        price = 45000
    elif destination == 'Sofia':
        price = 17000
    elif destination == 'London':
        price = 24000
elif season == 'Summer':
    if destination == 'Dubai':
        price = 40000
    elif destination == 'Sofia':
        price = 12500
    elif destination == 'London':
        price = 20250

total_price = days * price

if destination == 'Sofia':
    total_price *= 1.25
elif destination == 'Dubai':
    total_price *= 0.70
diff = abs(total_price - budget)

if total_price > budget:
    print(f"The director needs {diff:.2f} leva more!")
else:
    print(f'The budget for the movie is enough! We have {diff:.2f} leva left!')