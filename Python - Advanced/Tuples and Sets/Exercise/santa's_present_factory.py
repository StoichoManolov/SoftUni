# from collections import deque
#
# materials = [int(x) for x in input().split()]
# magic = deque(int(x) for x in input().split())
#
# doll = 0
# bicycle = 0
# train = 0
# teddy_bear = 0
#
# while materials and magic:
#
#     box_materials = materials.pop()
#     magic_material = magic.popleft()
#
#     if box_materials == 0 and magic_material == 0:
#         continue
#     elif box_materials == 0:
#         if materials:
#             box_materials = materials.pop()
#         else:
#             magic.appendleft(magic_material)
#     elif magic_material == 0:
#         if magic:
#             magic_material = magic.popleft()
#         else:
#             materials.append(box_materials)
#
#     present = box_materials * magic_material
#
#     if present == 400:
#         bicycle += 1
#     elif present == 300:
#         teddy_bear += 1
#     elif present == 250:
#         train += 1
#     elif present == 150:
#         doll += 1
#     elif present < 0:
#         present = box_materials + magic_material
#         materials.append(present)
#     elif present > 0:
#         box_materials += 15
#         materials.append(box_materials)
#
# if teddy_bear >= 1 and bicycle >= 1:
#     print(f'The presents are crafted! Merry Christmas!')
# elif doll >= 1 and train >= 1:
#     print(f'The presents are crafted! Merry Christmas!')
# else:
#     print(f'No presents this Christmas!')
#
# materials.reverse()
# if materials:
#     print(f'Materials left: {", ".join(str(x) for x in materials)}')
# if magic:
#     print(f'Magic left: {", ".join(str(x) for x in magic)}')
#
# if bicycle >= 1:
#     print(f'Bicycle: {bicycle}')
# if doll >= 1:
#     print(f'Doll: {doll}')
# if teddy_bear >= 1:
#     print(f'Teddy bear: {teddy_bear}')
# if train >= 1:
#     print(f'Wooden train: {train}')

from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())

crafted = []
presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while materials and magic_levels:
    material = materials.pop() if magic_levels[0] or not materials[-1] else 0  # 0
    magic_level = magic_levels.popleft() if material or not magic_levels[0] else 0  # 0

    if not magic_level:
        continue

    product = material * magic_level

    if presents.get(product):
        crafted.append(presents[product])
    elif product < 0:
        materials.append(material + magic_level)
    elif product > 0:
        materials.append(material + 15)

if {"Doll", "Wooden train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")

if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

[print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]