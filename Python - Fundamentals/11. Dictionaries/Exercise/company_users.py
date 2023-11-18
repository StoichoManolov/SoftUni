company_users = {}

while True:

    command = input()

    if command == 'End':
        break

    company, ID = command.split(' -> ')

    if company not in company_users:
        company_users[company] = []

    if ID not in company_users[company]:
        company_users[company].append(ID)


for item in company_users:
    print(f'{item}')
    for value in company_users[item]:
        print(f'-- {value}')
