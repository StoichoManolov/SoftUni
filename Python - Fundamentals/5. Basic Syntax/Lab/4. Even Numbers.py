num = int(input())
is_even = True

for n in range(num):
    number = int(input())
    if number % 2 != 0:
        print(f'{number} is odd!')
        is_even = False
        break
if is_even:
    print(f'All numbers are even.')
