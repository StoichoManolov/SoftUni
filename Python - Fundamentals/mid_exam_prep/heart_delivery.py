string = [int(x) for x in input().split('@')]
failed_jump = 0
jump_index = 0

while True:
    command = input()
    if command == 'Love!':
        break
    command_split = command.split()
    jump = int(command_split[1])
    jump_index += jump

    if not 0 <= jump_index < len(string):
        jump_index = 0

    if string[jump_index] > 0:
        string[jump_index] -= 2
        if string[jump_index] <= 0:
            print(f"Place {jump_index} has Valentine's day.")
    else:
        print(f"Place {jump_index} already had Valentine's day.")


print(f"Cupid's last position was {jump_index}.")

for x in string:
    if not x == 0:
        failed_jump += 1

if failed_jump == 0:
    print(f'Mission was successful.')
else:
    print(f'Cupid has failed {failed_jump} places.')



