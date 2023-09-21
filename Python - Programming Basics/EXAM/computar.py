month = input()
hours_spent = int(input())
group_size = int(input())
time_of_day = input()

price = 0

if month == 'march' or month == 'april' or month == 'may':
    if time_of_day == 'day':
        price = 10.50
    elif time_of_day == 'night':
        price = 8.40
elif month == 'june' or month == 'july' or month == 'august':
    if time_of_day == 'day':
        price = 12.60
    elif time_of_day == 'night':
        price = 10.20

if group_size >= 4:
    price *= 0.90

if hours_spent >= 5:
    price *= 0.50

total = price * group_size * hours_spent


print(f'Price per person for one hour: {price:.2f}')
print(f'Total cost of the visit: {total:.2f}')