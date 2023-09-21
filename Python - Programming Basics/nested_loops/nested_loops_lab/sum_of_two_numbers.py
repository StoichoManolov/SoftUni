number = int(input())
end_number = int(input())
magic_number = int(input())
combination = 0
is_found = False

for x in range(number, end_number + 1):
    for y in range(number, end_number + 1):
        total = x + y
        combination += 1
        if total == magic_number:
            is_found = True
            break
    if is_found:
        break


if is_found:
    print(f'Combination N:{combination} ({x} + {y} = {magic_number})')
else:
    print(f'{combination} combinations - neither equals {magic_number}')