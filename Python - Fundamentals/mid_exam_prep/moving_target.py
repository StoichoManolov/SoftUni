targets = [int(x) for x in input().split()]

while True:
    command = input()
    valid_index = True
    if command == 'End':
        break

    command_split = command.split()
    act = command_split[0]
    index = int(command_split[1])
    value = int(command_split[2])

    if not 0 <= index < len(targets):
        valid_index = False

    if act == 'Shoot':
        if valid_index:
            targets[index] -= value
            if targets[index] <= 0:
                del targets[index]

    elif act == 'Add':
        if valid_index:
            targets.insert(index, value)
        else:
            print(f'Invalid placement!')

    elif act == 'Strike':
        start_index = index - value
        end_index = index + value + 1
        if 0 <= start_index < len(targets) and 0 <= end_index < len(targets):
            del targets[start_index:end_index]
        else:
            print(f'Strike missed!')


print(*targets, sep="|")