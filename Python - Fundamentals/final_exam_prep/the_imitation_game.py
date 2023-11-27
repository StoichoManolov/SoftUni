encrypted_message = input()
new_string = ''
while True:
    strings = input()

    if strings == 'Decode':
        break

    message_split = strings.split('|')

    command = message_split[0]

    if command == 'Move':
        number_of_moves = int(message_split[1])
        moving = encrypted_message[0:number_of_moves]
        new_string = ''
        new_string += encrypted_message[number_of_moves:] + moving
        encrypted_message = new_string
    elif command == 'Insert':
        index = int(message_split[1])
        index = int(message_split[1])
        value = message_split[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif command == 'ChangeAll':
        substring = message_split[1]
        replacement = message_split[2]

        encrypted_message = encrypted_message.replace(substring, replacement)

print(f'The decrypted message is: {encrypted_message}')





