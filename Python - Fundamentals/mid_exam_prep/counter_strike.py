initial_energy = int(input())
battles_won = 0
is_out_of_energy = False

while True:
    command = input()

    if command == 'End of battle':
        break
    if initial_energy >= int(command):
        initial_energy -= int(command)
    else:
        is_out_of_energy = True
        print(f'Not enough energy! Game ends with {battles_won} won battles and {initial_energy} energy')
        break
    battles_won += 1
    if battles_won % 3 == 0:
        initial_energy += battles_won


if not is_out_of_energy:
    print(f'Won battles: {battles_won}. Energy left: {initial_energy}')