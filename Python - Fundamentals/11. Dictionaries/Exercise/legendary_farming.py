# legendary = {}
#
# valanyr_ = False
# shadowmourne = False
# dragonwrath = False
#
# legendary['shards'] = 0
# legendary['fragments'] = 0
# legendary['motes'] = 0
# while True:
#
#     material = input().split()
#
#     for i in range(0, len(material), 2):
#         value = int(material[i])
#         key = material[i + 1].lower()
#
#         if key not in legendary:
#             legendary[key] = value
#         else:
#             legendary[key] += value
#
#         if legendary.get("shards") >= 250:
#             legendary['shards'] += -250
#             print(f'Shadowmourne obtained!')
#             shadowmourne = True
#             break
#         elif legendary.get("fragments") >= 250:
#             legendary['fragments'] += -250
#             print(f'Valanyr obtained!')
#             valanyr_ = True
#             break
#         elif legendary.get("motes") >= 250:
#             legendary['motes'] += -250
#             print(f'Dragonwrath obtained!')
#             dragonwrath = True
#             break
#     if shadowmourne or valanyr_ or dragonwrath:
#         break
#
#
# mourne = legendary.pop('shards')
# valanyr = legendary.pop('fragments')
# dragon = legendary.pop('motes')
#
# print(f'shards: {mourne}')
# print(f'fragments: {valanyr}')
# print(f'motes: {dragon}')
#
# for item, value in legendary.items():
#     print(f'{item}: {value}')

legendary = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False

while not obtained:

    material = input().split()

    for i in range(0, len(material), 2):
        value = int(material[i])
        key = material[i + 1].lower()

        if key not in legendary:
            legendary[key] = 0
        legendary[key] += value

        if legendary["shards"] >= 250:
            legendary['shards'] += -250
            print(f'Shadowmourne obtained!')
            obtained = True
        elif legendary["fragments"] >= 250:
            legendary['fragments'] += -250
            print(f'Valanyr obtained!')
            obtained = True
        elif legendary["motes"] >= 250:
            legendary['motes'] += -250
            print(f'Dragonwrath obtained!')
            obtained = True

        if obtained:
            break

for item, value in legendary.items():
    print(f'{item}: {value}')

