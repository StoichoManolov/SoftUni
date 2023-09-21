capacity = int(input())
cost = 0
tickets_in = 0
is_time = False
is_full = False
while True:
    command = input()

    if command == 'Movie time!':
        is_time = True
        break

    tickets = int(command)
    tickets_in += tickets

    if tickets_in > capacity:
        is_full = True
        break

    if tickets % 3 == 0:
        cost += (tickets * 5) - 5
    else:
        cost += tickets * 5

diff = abs(tickets_in - capacity)

if is_time:
    print(f'There are {diff} seats left in the cinema.')
elif is_full:
    print(f'The cinema is full.')

print(f'Cinema income - {cost} lv.')


