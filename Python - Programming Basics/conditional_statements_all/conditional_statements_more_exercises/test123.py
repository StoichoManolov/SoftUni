from math import ceil


def validate_input(value, min_value, max_value):
    if value < min_value or value > max_value:
        exit()


series_name = input()
episode_duration = int(input())
rest_duration = int(input())

validate_input(episode_duration, 10, 90)
validate_input(rest_duration, 10, 120)

lunch_time = (rest_duration / 8)
rest_time = (rest_duration / 4)
total_time = rest_duration - lunch_time - rest_time

if total_time >= episode_duration:
    remaining_time = total_time - episode_duration
    print(f"You have enough time to watch {series_name} and left with {ceil(remaining_time)} minutes free time.")
else:
    necessary_time = episode_duration - total_time
    print(f"You don't have enough time to watch {series_name}, you need {ceil(necessary_time)} more minutes.")