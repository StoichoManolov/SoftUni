day_of_the_week = input().lower()

working_days = 'monday', 'tuesday', 'wednesday', 'thursday', 'friday'
weekend_days = 'saturday', 'sunday'

if day_of_the_week in working_days:
    print('Working day')
elif day_of_the_week in weekend_days:
    print('Weekend')
else:
    print('Error')