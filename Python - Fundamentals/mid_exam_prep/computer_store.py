cost = 0

while True:
    command = input()

    if command == 'special' or command == 'regular':
        break
    price = float(command)

    if price <= 0:
        print(f'Invalid price!')
        continue

    cost += price

tax = cost * 0.20


if not cost == 0:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {cost:.2f}$")
    print(f'Taxes: {tax:.2f}$')
    print(f'-----------')
    if command == 'special':
        special_discount = (tax + cost) - ((tax + cost) * 0.1)
        print(f'Total price: {special_discount:.2f}$')
    else:
        print(f'Total price: {tax + cost:.2f}$')
else:
    print(f'Invalid order!')