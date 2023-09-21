drink = input()
sugar = input()
amount = int(input())
price = 0

if drink == "Espresso":
    if sugar == 'Without':
        price = 0.90
    elif sugar == 'Normal':
        price = 1
    else:
        price = 1.20
elif drink == "Cappuccino":
    if sugar == 'Without':
        price = 1
    elif sugar == 'Normal':
        price = 1.20
    else:
        price = 1.60
elif drink == "Tea":
    if sugar == 'Without':
        price = 0.50
    elif sugar == 'Normal':
        price = 0.60
    else:
        price = 0.7

total_price = price * amount

if sugar == 'Without':
    total_price *= 0.65

if drink == "Espresso" and amount >= 5:
    total_price *= 0.75
if total_price > 15:
    total_price *= 0.80

print(f"You bought {amount} cups of {drink} for {total_price:.2f} lv.")
