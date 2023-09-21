from math import ceil

series_name = str(input())
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
relaxing = break_duration * 0.25

break_left = (break_duration - (lunch_time + relaxing))

if break_left >= episode_duration:
    print(f'You have enough time to watch {series_name} and left with {ceil(break_left - episode_duration)} minutes free time.')
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(episode_duration - break_left)} more minutes.")