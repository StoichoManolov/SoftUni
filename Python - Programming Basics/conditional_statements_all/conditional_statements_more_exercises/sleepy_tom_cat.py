holidays = int(input())
overtime_played = 0
hours_played = 0
minutes_played = 0
time_played = 0

minutes_played_during_break = holidays * 127
minutes_played_during_work_days = (365 - holidays) * 63

total_minutes_played = minutes_played_during_break + minutes_played_during_work_days

if total_minutes_played > 30000:
    overtime_played = total_minutes_played - 30000
    hours_played = overtime_played // 60
    minutes_played = overtime_played % 60
    print(f'Tom will run away')
    print(f"{hours_played} hours and {minutes_played} minutes more for play")
else:
    time_played = 30000 - total_minutes_played
    hours_played = time_played // 60
    minutes_played = time_played % 60
    print('Tom sleeps well')
    print(f'{hours_played} hours and {minutes_played} minutes less for play')
