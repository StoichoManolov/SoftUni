# loot = input().split('|')
# stolen_loot = []
#
# while True:
#     command = input()
#
#     if command == 'Yohoho!':
#         break
#
#     command_split = command.split()
#     loot_command = command_split[0]
#     if loot_command == 'Loot':
#         for i in command_split:
#             if i == 'Loot':
#                 continue
#             elif i not in loot:
#                 loot.insert(0, i)
#     elif loot_command == 'Drop':
#         index = int(command_split[1])
#         if 0 >= len(loot) >= index:
#             loot.append(loot.pop(index))
#
#     elif loot_command == 'Steal':
#         index = int(command_split[1])
#         for i in loot[:]:
#             if index <= 0:
#                 break
#             index -= 1
#             stolen = loot[-1]
#             stolen_loot.insert(0, stolen)
#             loot.pop(-1)
#
#
# def avg_treasure():
#     avg_treasures = 0
#     for items in loot:
#         avg_treasures += len(items)
#     if len(loot) <= 0:
#         return f'Failed treasure hunt.'
#     else:
#         avg_treasures /= len(loot)
#         return f'Average treasure gain: {avg_treasures:.2f} pirate credits.'
#
#
# print(', '.join(stolen_loot))
# print(avg_treasure())
