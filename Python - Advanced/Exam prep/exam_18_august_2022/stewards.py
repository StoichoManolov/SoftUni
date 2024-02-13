from collections import deque

seats = input().split(', ')

seat_matches = []
rotations = 0
seats_found = 0

queues = deque(int(x) for x in input().split(', '))
stack = [int(x) for x in input().split(', ')]


while True:

    current_q = queues.popleft()
    current_stack = stack.pop()

    result = current_stack + current_q

    ascii_symbol = chr(result)

    current_stack_str = str(current_q) + ascii_symbol
    current_q_str = str(current_stack) + ascii_symbol

    if current_q_str in seats:
        seats_found += 1
        seats.remove(current_q_str)
        seat_matches.append(current_q_str)

    elif current_stack_str in seats:
        seats_found += 1
        seats.remove(current_stack_str)
        seat_matches.append(current_stack_str)

    else:
        queues.append(current_q)
        stack.insert(0,current_stack)

    rotations += 1

    if rotations == 10:
        break
    elif seats_found == 3:
        break

print(f'Seat matches: {", ".join(seat_matches)}')
print(f'Rotations count: {rotations}')

