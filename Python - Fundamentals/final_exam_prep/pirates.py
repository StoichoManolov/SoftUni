def plunder(town,people,gold):

    targets[town][0] -= people
    targets[town][1] -= gold

    print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
    if targets[town][0] == 0 or targets[town][1] == 0:
        print(f'{town} has been wiped off the map!')
        del targets[town]


def prosper(town, gold):
    if 0 < gold:
        targets[town][1] += gold
        return f"{gold} gold added to the city treasury. {town} now has {targets[town][1]} gold."
    return f"Gold added cannot be a negative number!"


targets = {}

while True:
    command = input()
    if command == 'Sail':
        break

    command_split = command.split('||')
    city = command_split[0]
    population = int(command_split[1])
    gold = int(command_split[2])

    if city in targets.keys():
        targets[city][0] += population
        targets[city][1] += gold
    elif city not in targets.keys():
        targets[city] = []
        targets[city].append(population)
        targets[city].append(gold)


while True:
    command = input()
    if command == 'End':
        break

    command_split = command.split('=>')
    act = command_split[0]
    town = command_split[1]

    if act == 'Plunder':
        people = int(command_split[2])
        gold = int(command_split[3])
        plunder(town,people,gold)

    elif act == 'Prosper':
        gold = int(command_split[2])
        print(prosper(town,gold))


if len(targets) == 0:
    print(f'Ahoy, Captain! All targets have been plundered and destroyed!')
else:
    print(f'Ahoy, Captain! There are {len(targets)} wealthy settlements to go to:')
    for item in targets:
        print(f'{item} -> Population: {targets[item][0]} citizens, Gold: {targets[item][1]} kg')

