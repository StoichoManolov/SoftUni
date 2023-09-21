number = int(input())

for num in range(number):
    current_number = int(input())
    if current_number == 88:
        print(f'Hello')
    elif current_number == 86:
        print(f'How are you?')
    elif current_number < 88:
        print(f'GREAT!')
    else:
        print(f'Bye.')