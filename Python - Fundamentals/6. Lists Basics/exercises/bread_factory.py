events = input().split('|')

ENERGY = 100
COINS = 100
factor_is_open = True

for event in events:
    event_values = event.split('-')
    event_type = event_values[0]
    event_value = int(event_values[1])

    if event_type == 'rest':
        current_energy = ENERGY
        ENERGY += event_value
        if ENERGY > 100:
            ENERGY = 100
        print(f'You gained {abs(current_energy - ENERGY)} energy.')
        print(f'Current energy: {ENERGY}.')
    elif event_type == 'order':
        if ENERGY >= 30:
            COINS += event_value
            print(f'You earned {event_value} coins.')
            ENERGY -= 30
        else:
            ENERGY += 50
            print(f'You had to rest!')
    else:
        if COINS >= event_value:
            COINS -= event_value
            print(f'You bought {event_type}.')
        else:
            print(f'Closed! Cannot afford {event_type}.')
            factor_is_open = False
            break

else:
    print(f'Day completed!')
    print(f'Coins: {COINS}')
    print(f'Energy: {ENERGY}')
