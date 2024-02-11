from collections import deque

fuel = [int(x) for x in input().split()]
consumption_index = deque(int(x) for x in input().split())
fuel_quantity = deque(int(x) for x in input().split())
altitudes = []
altitude = 1

while fuel:

    current_fuel = fuel.pop()
    current_consumption = consumption_index.popleft()

    result = current_fuel - current_consumption

    quantity_needed = fuel_quantity.popleft()

    if result >= quantity_needed:
        print(f'John has reached: Altitude {altitude}')
        altitudes.append(f'Altitude {altitude}')
        altitude += 1
    else:
        print(f'John did not reach: Altitude {altitude}')
        break

if 2 <= altitude <= 4:
    print('John failed to reach the top.')
    print('Reached altitudes: ', end='',)
    print(', '.join(altitudes))

elif altitude == 1:
    print(f"John failed to reach the top. \nJohn didn't reach any altitude.")
else:
    print(f'John has reached all the altitudes and managed to reach the top!')



