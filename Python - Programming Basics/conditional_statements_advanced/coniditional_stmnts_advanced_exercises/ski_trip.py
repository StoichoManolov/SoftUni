days_stay = int(input()) - 1
type_of_room = input()
grade = input()
room_price = 0
discount = 0
total_cost = 0

if type_of_room == 'room for one person':
    room_price = 18
elif type_of_room == 'apartment':
    room_price = 25
    if days_stay < 10:
        discount = 0.30
    elif 10 < days_stay <= 15:
        discount = 0.35
    elif days_stay > 15:
        discount = 0.50
else:
    room_price = 35
    if days_stay < 10:
        discount = 0.10
    elif 10 < days_stay <= 15:
        discount = 0.15
    elif days_stay > 15:
        discount = 0.20

cost_of_room = (days_stay * room_price) * (1 - discount)

if grade == 'positive':
    grade_discount = 0.25
    total_cost = cost_of_room * grade_discount + cost_of_room
elif grade == 'negative':
    grade_discount = 0.10
    total_cost = cost_of_room - (cost_of_room * grade_discount)

print(f'{total_cost:.2f}')



