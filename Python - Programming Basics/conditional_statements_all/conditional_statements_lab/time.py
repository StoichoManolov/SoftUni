current_hours = int(input())
current_minutes = int(input())

current_time_in_minutes = current_hours * 60 + current_minutes + 15
current_time_as_hours = current_time_in_minutes // 60
current_time_as_minutes = current_time_in_minutes % 60

if current_time_as_hours == 24:
    current_time_as_hours = 0

print(f'{current_time_as_hours}:{current_time_as_minutes:02d}')