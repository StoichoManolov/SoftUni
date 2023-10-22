dungeon_rooms = input().split('|')

health = 100
bitcoins = 0
rooms = 0
is_dead = False

for room in dungeon_rooms:
    rooms += 1
    room_split = room.split()
    command, number = room_split[0], int(room_split[1])

    if command == 'potion':
        health += number
        if health > 100:
            number = 100 - (health - number)
            health = 100
        print(f'You healed for {number} hp.')
        print(f'Current health: {health} hp.')
    elif command == 'chest':
        bitcoins += number
        print(f'You found {number} bitcoins.')
    else:
        health -= number
        if not health <= 0:
            print(f'You slayed {command}.')
        else:
            print(f'You died! Killed by {command}.')
            print(f'Best room: {rooms}')
            is_dead = True
            break

if not is_dead:
    print(f"You've made it!")
    print(f'Bitcoins: {bitcoins}')
    print(f'Health: {health}')
