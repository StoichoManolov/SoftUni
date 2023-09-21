from math import floor
record_in_seconds = float(input())
distance_in_meters = float(input())
time_per_meter_in_seconds = float(input())

setback = floor((distance_in_meters // 50) * 30)

climbing = distance_in_meters * time_per_meter_in_seconds + setback

if climbing >= record_in_seconds:
    print(f'No,{climbing - record_in_seconds:.2f} slower')
else:
    print(f'yes{climbing:.2f}fast')
