word = input()

while word != 'End':
    copies = ''
    if word == 'SoftUni':
        word = input()
        continue
    for index,digit in enumerate(word):
        copies += digit
        copies += digit
    else:
        print(copies)
    word = input()