gifts = input().split()

command = input()

while not command == 'No Money':
    command = command.split()
    command_one = command[0]
    gift_name = command[1]

    if command_one == 'OutOfStock':
        for items in gifts:
            if items == gift_name:
                ind = gifts.index(items)
                gifts[ind] = 'None'
    elif command_one == 'Required':
        gift_index = command[2]
        if 0 <= int(gift_index) <= int(len(gifts)-1):
            gifts[int(gift_index)] = gift_name
    elif command_one == 'JustInCase':
        gifts[-1] = gift_name   # replacing the last item by index in a list

    command = input()

for exception in gifts:
    if exception != 'None':
        print(f'{exception}', end=' ')



