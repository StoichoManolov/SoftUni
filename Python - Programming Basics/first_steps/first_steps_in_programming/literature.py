from math import floor

pages_in_book = int(input())
pages_per_hour = int(input())
days = int(input())

time_spent_reading = pages_in_book / pages_per_hour
hours_needed = time_spent_reading / days

print(floor(hours_needed))
