name = input()
points = 0
player2 = 0
name_player = ''

while name != "Stop":
    points = 0
    for _, digit in enumerate(name):
        number = int(input())

        if number == ord(digit):
            points += 10
        else:
            points += 2
    if player2 <= points:
        player2 = points
        name_player = name
    name = input()


diff = abs(player2 - points)

if points == player2:
    print(f'The winner is {name_player} with {player2} points!')
elif points > player2:
    print(f'The winner is {name_player} with {player2} points!')
else:
    print(f'The winner is {name_player} with {player2} points!')

