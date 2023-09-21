fruit = input().lower()
day_from_the_week = input().lower()
amount = float(input())
fruits = 'banana', 'apple', 'orange', 'grapefruit', 'kiwi', 'pineapple', 'grapes'
working_days = 'monday', 'tuesday', 'wednesday', 'thursday', 'friday'
price = 0
if day_from_the_week in working_days:
    if fruit == 'banana':
        price = 2.50
    elif fruit == 'apple':
        price = 1.20
    elif fruit == 'orange':
        price = 0.85
    elif fruit == 'grapefruit':
        price = 1.45
    elif fruit == 'kiwi':
        price = 2.70
    elif fruit == 'pineapple':
        price = 5.50
    elif fruit == 'grapes':
        price = 3.85

elif day_from_the_week == 'sunday' or day_from_the_week == 'saturday':
    if fruit == 'banana':
        price = 2.70
    elif fruit == 'apple':
        price = 1.25
    elif fruit == 'orange':
        price = 0.90
    elif fruit == 'grapefruit':
        price = 1.60
    elif fruit == 'kiwi':
        price = 3.00
    elif fruit == 'pineapple':
        price = 5.60
    elif fruit == 'grapes':
        price = 4.20

if day_from_the_week not in working_days and day_from_the_week != 'sunday' and day_from_the_week != 'saturday':
    print('error')
elif fruit not in fruits:
    print('error')
else:
    total_cost = amount * price
    print(f'{total_cost:.2f}')

