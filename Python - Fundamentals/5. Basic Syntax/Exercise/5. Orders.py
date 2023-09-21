orders = int(input())
total = 0

for num in range(orders):
    price = 0
    capsule_price = float(input())
    days = int(input())
    capsules_a_day = int(input())
    if capsule_price < 0.01 or capsule_price > 100.00:
        continue
    elif days <= 0 or days > 31:
        continue
    elif capsules_a_day < 1 or capsules_a_day > 2000:
        continue
    price = (days * capsules_a_day) * capsule_price
    total += price
    print(f'The price for the coffee is: ${price:.2f}')
else:
    print(f'Total: ${total:.2f}')