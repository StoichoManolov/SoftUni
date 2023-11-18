products = {}

while True:

    command = input()

    if command == 'statistics':
        break

    command_split = command.split(': ')

    key = command_split[0]
    value = int(command_split[1])

    if key not in products:
        products[key] = value
    else:
        products[key] += value

print(f'Products in stock:')
for (product, quantity) in products.items():
    print(f'- {product}: {quantity}')
print(f'Total Products: {len(products.keys())}')
print(f'Total Quantity: {sum(products.values())}')





