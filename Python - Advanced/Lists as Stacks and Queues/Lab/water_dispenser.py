from collections import deque

quantity_of_water = int(input())

people = deque()

while True:
    name = input()
    if name == 'Start':
        break
    people.append(name)


while True:
    command = input()
    if command == 'End':
        break
    elif 'refill' in command:
        act, quantity = command.split()
        quantity_of_water += int(quantity)
        continue
    water = int(command)
    person = people.popleft()
    if quantity_of_water >= water:
        quantity_of_water -= water
        print(f'{person} got water')
    else:
        print(f'{person} must wait')

print(f'{quantity_of_water} liters left')

