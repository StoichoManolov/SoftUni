from math import floor
record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_one_meter = float(input())

swimming_needed = distance_in_meters * time_in_seconds_for_one_meter
water_resistance = floor(distance_in_meters / 15) * 12.5
total_time = swimming_needed + water_resistance

if total_time < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - record_in_seconds:.2f} seconds slower.")