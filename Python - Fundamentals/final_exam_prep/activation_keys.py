key = input()

while True:

    command = input()

    if command == 'Generate':
        break

    command_split = command.split('>>>')

    act = command_split[0]

    if act == 'Contains':
        substring = command_split[1]
        if substring in key:
            print(f'{key} contains {substring}')
        else:
            print(f'Substring not found!')
    elif act == 'Flip':
        upper_lower = command_split[1]
        start_index = int(command_split[2])
        end_index = int(command_split[3])
        sliced = key[start_index:end_index]
        if upper_lower == 'Lower':
            key = key[:start_index] + sliced.lower() + key[end_index:]
        elif upper_lower == 'Upper':
            key = key[:start_index] + sliced.upper() + key[end_index:]
        print(key)
    elif act == 'Slice':
        start_index = int(command_split[1])
        end_index = int(command_split[2])

        key = key[:start_index] + key[end_index:]
        print(key)


print(f'Your activation key is: {key}')