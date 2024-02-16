from collections import deque

elf_energy = deque(int(x) for x in input().split())
materials_in_a_box = [int(x) for x in input().split()]

toys = 0
elf_taken = 1
energy = 0

while elf_energy and materials_in_a_box:

    current_elf = elf_energy.popleft()
    current_box = materials_in_a_box.pop()

    if current_elf < 5:
        materials_in_a_box.append(current_box)
        continue

    if elf_taken % 5 == 0 and elf_taken % 3 == 0:
        if current_box*2 <= current_elf:
            energy += current_box * 2
            elf_taken += 1
            result = current_elf - (current_box * 2)
            elf_energy.append(result)
        else:
            elf_taken += 1
            elf_energy.append(current_elf*2)
            materials_in_a_box.append(current_box)

    elif elf_taken % 5 == 0:
        if current_box <= current_elf:
            energy += current_box
            elf_taken += 1
            result = current_elf - current_box
            elf_energy.append(result)
        else:
            elf_taken += 1
            elf_energy.append(current_elf*2)
            materials_in_a_box.append(current_box)

    elif elf_taken % 3 == 0:
        if current_box * 2 <= current_elf:
            energy += current_box * 2
            toys += 2
            result = (current_elf - (current_box * 2)) + 1
            elf_energy.append(result)
            elf_taken += 1
        else:
            elf_taken += 1
            elf_energy.append(current_elf*2)
            materials_in_a_box.append(current_box)

    elif current_elf >= current_box:
        elf_taken += 1
        toys += 1
        energy += current_box
        result = (current_elf - current_box) + 1
        elf_energy.append(result)
    else:
        elf_taken +=1
        materials_in_a_box.append(current_box)
        elf_energy.append(current_elf*2)


print(f'Toys: {toys}')
print(f'Energy: {energy}')

if elf_energy:
    print(f'Elves left: {", ".join(str(x) for x in elf_energy)}')

if materials_in_a_box:
    print(f'Boxes left: {", ".join(str(x) for x in materials_in_a_box)}')
