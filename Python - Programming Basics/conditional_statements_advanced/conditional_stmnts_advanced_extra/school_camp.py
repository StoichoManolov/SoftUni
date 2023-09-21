season = input()
type_of_group = input()
number_of_students = int(input())
overnight_stays = int(input())
price_per_night = 0
discount = 0
sport = ''

if season == 'Winter':
    if type_of_group == 'girls':
        sport = 'Gymnastics'
        price_per_night = 9.60
    elif type_of_group == 'boys':
        sport = 'Judo'
        price_per_night = 9.60
    elif type_of_group == 'mixed':
        sport = 'Ski'
        price_per_night = 10
elif season == 'Spring':
    if type_of_group == 'girls':
        sport = 'Athletics'
        price_per_night = 7.20
    elif type_of_group == 'boys':
        sport = 'Tennis'
        price_per_night = 7.20
    elif type_of_group == 'mixed':
        sport = 'Cycling'
        price_per_night = 9.50
elif season == 'Summer':
    if type_of_group == 'girls':
        sport = 'Volleyball'
        price_per_night = 15
    elif type_of_group == 'boys':
        sport = 'Football'
        price_per_night = 15
    elif type_of_group == 'mixed':
        sport = 'Swimming'
        price_per_night = 20

if number_of_students >= 50:
    discount = 0.50
elif number_of_students >= 20:
    discount = 0.15
elif number_of_students >= 10:
    discount = 0.05

total_cost = price_per_night * overnight_stays * number_of_students * (1-discount)
print(f'{sport} {total_cost:.2f} lv.')

