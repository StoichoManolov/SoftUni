from collections import deque

milligrams_of_caffeine = [int(x) for x in input().split(', ')]
energy_drinks = deque(int(x) for x in input().split(', '))

MAX_CAFFEINE = 300
total_caffeine = 0

while milligrams_of_caffeine and energy_drinks:

    current_caffeine = milligrams_of_caffeine.pop()
    current_drink = energy_drinks.popleft()

    result = current_drink * current_caffeine

    if result + total_caffeine <= 300:
        total_caffeine += result
    else:
        energy_drinks.append(current_drink)
        total_caffeine -= 30
        if total_caffeine < 0:
            total_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks) }")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
