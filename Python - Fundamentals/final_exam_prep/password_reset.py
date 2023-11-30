def takeodd():
    empty_string = ''
    count = 0
    for i in string:
        if count % 2 != 0:
            empty_string += i
        count += 1
    return empty_string

def cut(index,length):

    new = string[:index] + string[index + length:]
    return new


def substitute(substring,sub):
    new = string.replace(substring,sub)
    return new

string = input()

while True:
    command = input()
    if command == 'Done':
        break

    command_split = command.split()

    act = command_split[0]

    if act == 'TakeOdd':
        string = takeodd()
        print(string)
    elif act == 'Cut':
        index = int(command_split[1])
        length = int(command_split[2])
        string = cut(index,length)
        print(string)
    elif act == 'Substitute':
        substring = command_split[1]
        substitutes = command_split[2]
        if substring in string:
            string = substitute(substring,substitutes)
            print(string)
        else:
            print(f'Nothing to replace!')

print(f'Your password is: {string}')