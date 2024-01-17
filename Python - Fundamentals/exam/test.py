number = int(input())

for num in range(number, 0, -1):
    row = num
    numbers = row
    for n in range(row,0,-1):
        print(f'{numbers}', end='')
        numbers += 1
    row -= 1
    print()


