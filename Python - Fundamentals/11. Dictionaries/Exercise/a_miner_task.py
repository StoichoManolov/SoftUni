items = {}

while True:

    strings = input()
    if strings == 'stop':
        break

    quantity = int(input())

    if strings not in items:
        items[strings] = quantity
    else:
        items[strings] += quantity


for item,value in items.items():
    print(f'{item} -> {value}')

