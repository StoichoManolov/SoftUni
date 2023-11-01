list_of_cards = input().split(', ')
number_of_commands = int(input())

for n in range(number_of_commands):

    command = input()
    command_split = command.split(', ')
    act = command_split[0]

    if act == 'Add':
        card_name = command_split[1]
        if card_name not in list_of_cards:
            list_of_cards.append(card_name)
            print(f'Card successfully added')
        else:
            print(f'Card is already in the deck')

    elif act == 'Remove':
        card_name = command_split[1]
        if card_name in list_of_cards:
            list_of_cards.remove(card_name)
            print(f'Card successfully removed')
        else:
            print(f'Card not found')

    elif act == 'Remove At':
        index = int(command_split[1])
        if 0 <= index < len(list_of_cards):
            list_of_cards.pop(index)
            print(f'Card successfully removed')
        else:
            print(f'Index out of range')

    elif act == 'Insert':
        index = int(command_split[1])
        card_name = command_split[2]

        if 0 <= index < len(list_of_cards):
            if card_name not in list_of_cards:
                list_of_cards.insert(index, card_name)
                print(f'Card successfully added')
            else:
                print(f'Card is already added')
        else:
            print(f'Index out of range')

print(', '.join(list_of_cards))


