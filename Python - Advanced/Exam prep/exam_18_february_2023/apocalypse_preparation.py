from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = [int(x) for x in input().split()]

equipment = {
    "MedKit": 0,
    "Bandage": 0,
    "Patch": 0,
}

while textiles and medicaments:

    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()

    result = current_medicament + current_textile

    if result == 30:
        equipment['Patch'] += 1
    elif result == 40:
        equipment['Bandage'] += 1
    elif result == 100:
        equipment['MedKit'] += 1
    elif result > 100:
        equipment['MedKit'] += 1
        diff = result - 100
        medicaments[-1] += diff
    else:
        current_medicament += 10
        medicaments.append(current_medicament)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print(f'Textiles are empty.')
elif not medicaments:
    print('Medicaments are empty.')


sorted_items = sorted(equipment.items(), key=lambda x: (-x[1], x[0]))
for name, count in sorted_items:
    if count > 0:
        print(f"{name} - {count}")

if medicaments:
    medicaments.reverse()
    print(f'Medicaments left: {", ".join(str(x) for x in medicaments)}')
if textiles:
    print(f'Textiles left: {", ".join(str(x) for x in textiles)}')
