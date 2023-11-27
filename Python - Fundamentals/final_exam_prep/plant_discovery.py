def rate(plant, rating):
    if plant in plants:
        plants[plant]['rating'].append(rating)


def update(plant,new_rarity):

    plants[plant]['rarity'] = new_rarity


def reset(plant):

    plants[plant]['rating'] = []


number = int(input())
plants = {}

for i in range(number):

    plant = input().split('<->')
    name = plant[0]
    rarity = int(plant[1])

    if name not in plants:
        plants[name] = {'rarity': 0, 'rating': []}
    plants[name]['rarity'] = rarity

while True:
    command = input()
    if command == 'Exhibition':
        break

    command_split = command.split(' - ')
    plant_name_and_command = command_split[0]
    act, plant = plant_name_and_command.split(': ')

    if plant not in plants.keys():
        print(f'error')
        continue

    if 'Rate' in command:
        rating = command_split[1]
        rate(plant,rating)
    elif 'Update' in command:
        new_rarity = command_split[1]
        update(plant, new_rarity)
    elif 'Reset' in command:
        reset(plant)


print(f'Plants for the exhibition:')

for item, value in plants.items():
    average = 0
    count = 0
    for avg in value['rating']:
        average += int(avg)
        count += 1
    if count == 0:
        average = 0
    else:
        average /= count

    print(f'- {item}; Rarity: {value["rarity"]}; Rating: {average:.2f}')






