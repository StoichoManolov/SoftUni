heroes = {}

while True:

    command = input()
    if command == 'End':
        break

    command_split = command.split()

    act = command_split[0]
    hero_name = command_split[1]

    if act == 'Enroll':
        if hero_name not in heroes:
            heroes[hero_name] = {}
        else:
            print(f'{hero_name} is already enrolled.')
    elif act == 'Learn':
        spell = command_split[2]
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        else:
            if spell in heroes[hero_name]:
                print(f"{hero_name} has already learnt {spell}.")
            else:
                heroes[hero_name] = spell

    elif act == 'Unlearn':
        spell = command_split[2]
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        else:
            if spell not in heroes[hero_name]:
                print(f"{hero_name} doesn't know {spell}.")
            else:
                heroes.pop(spell, hero_name)

print(f'Heroes:')
for key,value in heroes.items():
    values = heroes[key]
    if len(values) == 0:
        values = ''
    print(f'{key}: {values}')

