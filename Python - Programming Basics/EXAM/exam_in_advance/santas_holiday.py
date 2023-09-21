days_spent = int(input()) - 1
type_of_room = input()
grade = input()

price = 0
discount = 0

if type_of_room == 'room for one person':
    price = 18
elif type_of_room == 'apartment':
    price = 25
    if days_spent < 10:
        discount = 0.30
    elif 10 <= days_spent <= 15:
        discount = 0.35
    else:
        discount = 0.50
elif type_of_room == 'president apartment':
    price = 35
    if days_spent < 10:
        discount = 0.10
    elif 10 <= days_spent <= 15:
        discount = 0.15
    else:
        discount = 0.20


total_cost = (price * days_spent) * (1 - discount)

if grade == 'positive':
    total_cost *= 1.25
else:
    total_cost *= 0.90

print(f'{total_cost:.2f}')
