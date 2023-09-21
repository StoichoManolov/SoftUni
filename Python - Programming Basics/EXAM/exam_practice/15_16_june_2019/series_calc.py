serial = input()
seasons = int(input())
episodes = int(input())
episode_duration = float(input())

ads = episode_duration * 1.20
extra_episodes = seasons * 10

total_time = extra_episodes + (ads * seasons * episodes)

print(f'Total time needed to watch the {serial} series is {int(total_time)} minutes.')

