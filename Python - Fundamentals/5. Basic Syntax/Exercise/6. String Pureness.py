number = int(input())

for num in range(number):
    word = input()
    for index,digit in enumerate(word):
        if digit == '_' or digit == ',' or digit == '.':
            print(f'{word} is not pure!')
            break
    else:
        print(f'{word} is pure.')

