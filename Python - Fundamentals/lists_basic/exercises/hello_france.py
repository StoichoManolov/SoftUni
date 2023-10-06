items_price = input().split("|")
budget = float(input())


items_float = []
total_cost = 0
profit = 0
ticket = 150


for items in items_price:

    current_item = items.split('->')
    item_name = current_item[0]
    item_prices = float(current_item[1])

    if item_prices <= budget:
        if item_name == 'Clothes':
            if item_prices > 50.00:
                continue
            else:
                total_cost += item_prices
                budget -= item_prices
                items_float.append(item_prices)
        elif item_name == 'Shoes':
            if item_prices > 35.00:
                continue
            else:
                total_cost += item_prices
                budget -= item_prices
                items_float.append(item_prices)
        elif item_name == 'Accessories':
            if item_prices > 20.50:
                continue
            else:
                total_cost += item_prices
                budget -= item_prices
                items_float.append(item_prices)
        else:
            continue

for ind, item in enumerate(items_float):
    items_float[ind] = item * 1.40
    profit += item * 1.40

profit_total = profit - total_cost
new_budget = budget + profit

for item in items_float:
    print(f'{item:.2f}', end=' ')
else:
    print()
print(f'Profit: {profit_total:.2f}')
if new_budget >= 150:
    print(f'Hello, France!')
else:
    print(f'Not enough money.')










