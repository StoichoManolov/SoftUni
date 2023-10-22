targets = [int(x) for x in input().split()]
shoots = 0
while True:
    command = input()

    if command == 'End':
        break

    index = int(command)
    current_index = 0
    if 0 <= index < len(targets):
        copy = targets[index]
        targets[index] = -1
        for x in targets:
            if x == -1:
                current_index += 1
                continue
            else:
                if x > copy:
                    targets[current_index] -= copy
                else:
                    targets[current_index] += copy
            current_index += 1


for x in targets:
    if x == -1:
        shoots +=1

targets = [str(x) for x in targets]

print(f'Shot targets: {shoots} ->',*targets)





