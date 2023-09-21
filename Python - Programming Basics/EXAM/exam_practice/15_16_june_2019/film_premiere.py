film = input()
food = input()
tickets = int(input())
price = 0

if food == 'Drink':
    if film == 'John Wick':
        price = 12
    elif film == 'Star Wars':
        price = 18
    else:
        price = 9
elif food == 'Popcorn':
    if film == 'John Wick':
        price = 15
    elif film == 'Star Wars':
        price = 25
    else:
        price = 11
elif food == 'Menu':
    if film == 'John Wick':
        price = 19
    elif film == 'Star Wars':
        price = 30
    else:
        price = 14

total = price * tickets

if film == 'Star Wars' and tickets >= 4:
    total *= 0.7
elif film == 'Jumanji' and tickets == 2:
    total *= 0.85

print(f'Your bill is {total:.2f} leva.')