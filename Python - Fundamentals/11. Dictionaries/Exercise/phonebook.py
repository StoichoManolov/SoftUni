phonebook = {}

while True:

    contact = input()
    if '-' not in contact:
        search = int(contact)

        for i in range(search):
            name = input()

            if name in phonebook:
                print(f'{name} -> {phonebook[name]}')
            else:
                print(f'Contact {name} does not exist.')
        else:
            break

    contact_split = contact.split("-")

    name = contact_split[0]
    number = contact_split[1]

    phonebook[name] = number





