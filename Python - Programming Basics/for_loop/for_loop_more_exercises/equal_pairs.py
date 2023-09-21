number = int(input())
previous_duo = 0
max_diff = 0
equal = True


for duos in range(number):
    num1 = int(input())
    num2 = int(input())
    total = num1 + num2

    if duos != 0 and total != previous_duo:
        equal = False
        diff = abs(total - previous_duo)
        max_diff = diff

    previous_duo = total

if equal:
    print (f'Yes, value={previous_duo}')
else:
    print(f'No, maxdiff={max_diff}')


