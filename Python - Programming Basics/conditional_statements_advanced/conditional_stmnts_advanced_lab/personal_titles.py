age = float(input())
gender = input().lower()

if age >= 16 and gender == 'm':
    print('Mr.')
elif age < 16 and gender == 'm':
    print('Master')
elif age >= 16 and gender == 'f':
    print('Ms.')
else:
    print('Miss')