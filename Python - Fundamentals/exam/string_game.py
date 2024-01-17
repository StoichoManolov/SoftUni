string = input()

while True:

    command = input()
    if command == 'Done':
        break

    command_split = command.split()

    act = command_split[0]

    if act == 'Change':
        char = command_split[1]
        replacement = command_split[2]
        string = string.replace(char,replacement)
        print(string)
    elif act == 'Includes':
        substring = command_split[1]
        if substring in string:
            print('True')
        else:
            print('False')
    elif act == 'End':
        substring = command_split[1]
        if string.endswith(substring):
            print('True')
        else:
            print(f'False')
    elif act == 'Uppercase':
        string = string.upper()
        print(string)
    elif act == 'FindIndex':
        char = command_split[1]
        index = string.index(char)
        print(index)
    elif act == 'Cut':
        index = int(command_split[1])
        count = int(command_split[2])
        cut = string[index:index + count]
        print(cut)