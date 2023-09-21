hour_from_the_day = int(input())
day_from_the_week = input().lower()
# work time 10-18h

work_days = 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'

if day_from_the_week in work_days and 10 <= hour_from_the_day <= 18:
    print('open')
else:
    print('closed')
