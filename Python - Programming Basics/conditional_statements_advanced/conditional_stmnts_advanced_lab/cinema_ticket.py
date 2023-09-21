day_of_the_week = input().lower()

if day_of_the_week == 'monday' or day_of_the_week == 'tuesday' or day_of_the_week == 'friday':
    price = 12
elif day_of_the_week == 'wednesday' or day_of_the_week == 'thursday':
    price = 14
else:
    price = 16

print(price)
