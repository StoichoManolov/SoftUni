age = float(input())
gender = input().lower()\

if age >= 16:
    if gender == 'm':
        print('Mr.')
    else:
        print('Ms.')
elif age < 16:
    if gender == 'm':
        print('Master')
    else:
        print('Miss')