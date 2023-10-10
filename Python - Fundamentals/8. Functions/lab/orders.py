product = input()
quantity = int(input())

def order(item, count):
    price = 0
    if item == 'coffee':
        price = 1.50
    elif item == 'water':
        price = 1.00
    elif item == 'coke':
        price = 1.40
    elif item == 'snacks':
        price = 2.00
    result = count * price
    return result

print(f'{order(product, quantity):.2f}')