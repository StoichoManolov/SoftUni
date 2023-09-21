budget = int(input())
total = 0
product = input()
current_product = int(product)

while product != 'End':
    current_product = int(product)
    total += current_product
    if budget < total:
        print(f'You went in overdraft!')
        break
    product = input()
else:
    print(f'You bought everything needed.')
