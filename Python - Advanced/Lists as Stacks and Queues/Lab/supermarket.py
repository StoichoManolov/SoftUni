from collections import deque

customers = deque()

while True:

    command = input()

    if command == 'End':
        break
    elif command == 'Paid':
        for i in customers:
            print(i)
        customers.clear()
    else:
        customers.append(command)

print(f'{len(customers)} people remaining.')
