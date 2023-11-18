orders = {}

while True:
    order = input()

    if order == 'buy':
        break
    order = order.split()

    product = order[0]
    price = float(order[1])
    quantity = int(order[2])

    if product not in orders:
        orders[product] = [price, quantity]
    elif product in orders:
        orders[product][0] = price
        orders[product][1] += quantity

for order in orders:
    price = orders[order][0]
    value = orders[order][1]
    result = price * value
    print(f'{order} -> {result:.2f}')