pool_volume_in_litres = int(input())
pipe_one_per_hour = int(input())
pipe_two_per_hour = int(input())
hours_worker_is_away = float(input())

pipe_one_volume = pipe_one_per_hour * hours_worker_is_away
pipe_two_volume = pipe_two_per_hour * hours_worker_is_away

total_both_pipes = pipe_two_volume + pipe_one_volume

volume_poured = pool_volume_in_litres - total_both_pipes
volume_poured_in_percent = volume_poured / pool_volume_in_litres * 100
volume_filled = 100 - volume_poured_in_percent

first_pipe_percent = pipe_one_volume / total_both_pipes * 100
second_pipe_percent = pipe_two_volume / total_both_pipes * 100

if total_both_pipes > pool_volume_in_litres:
    overflow = total_both_pipes - pool_volume_in_litres
    print(f"For {hours_worker_is_away} hours the pool overflows with {overflow} liters.")
else:
    print(f"The pool is {volume_filled}% full. Pipe 1: {first_pipe_percent:.2f}%. Pipe 2: {second_pipe_percent:.2f}%.")
