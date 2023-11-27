string = input()

while True:

    command = input()
    if command == 'Reveal':
        break

    command_split = command.split(':|:')

    act = command_split[0]

    if act == 'InsertSpace':
        index = int(command_split[1])
        string = string[:index] + ' ' + string[index:]
        print(string)
    elif act == 'Reverse':
        substring = command_split[1]
        if substring in string:
            string = string.replace(substring, "", 1) + substring[::-1]
            print(string)
        else:
            print(f'error')
    elif act == 'ChangeAll':
        substring = command_split[1]
        new_string = command_split[2]
        string = string.replace(substring, new_string)
        print(string)


print(f'You have a new text message: {string}')
