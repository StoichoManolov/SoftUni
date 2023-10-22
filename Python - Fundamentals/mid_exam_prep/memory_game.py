elements = input().split()

number_of_moves = 0
game_over = False


while True:
    command = input()

    if command == 'end':
        if len(elements) == 0:
            game_over = True
        break

    number_of_moves += 1
    command_split = command.split()
    first_element = int(command_split[0])
    second_element = int(command_split[1])

    if first_element == second_element or not 0 <= first_element < len(elements) or not 0<= second_element<len(elements):
        print(f'Invalid input! Adding additional elements to the board')
        middle = int(len(elements) // 2)
        elements.insert(middle, str(-number_of_moves) + 'a')
        elements.insert(middle, str(-number_of_moves) + 'a')
    elif elements[first_element] == elements[second_element]:
        number = elements[first_element]
        print(f'Congrats! You have found matching elements - {number}!')
        elements.remove(number)
        elements.remove(number)

    elif elements[first_element] != elements[second_element]:
        print(f'Try again!')

    if len(elements) == 0:
        game_over = True
        break


if game_over:
    print(f'You have won in {number_of_moves} turns!')
else:
    print(f'Sorry you lose :(')
    print(*elements)

#  runtime error