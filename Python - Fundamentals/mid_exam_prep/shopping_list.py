groceries = input().split('!')

while True:
    command = input()
    if command == 'Go Shopping!':
        break

    command_split = command.split()
    order = command_split[0]
    item_one = command_split[1]

    if order == 'Urgent':
        if item_one not in groceries:
            groceries.insert(0, item_one)

    elif order == 'Unnecessary':
        if item_one in groceries:
            groceries.remove(item_one)

    elif order == 'Correct':
        new_item = command_split[2]
        if item_one in groceries:
            item = groceries.index(item_one)
            groceries.insert(item, new_item)
            groceries.remove(item_one)

    elif order == 'Rearrange':
        if item_one in groceries:
            groceries.append(item_one)
            groceries.remove(item_one)

print(', '.join(groceries))