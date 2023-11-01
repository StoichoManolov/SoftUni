from math import floor

biscuits_per_day_per_worker = int(input())
count_of_workers = int(input())
biscuits_for_a_month = int(input())

biscuits_made = 0

for i in range(1,31):
    biscuits_daily = biscuits_per_day_per_worker * count_of_workers
    if i % 3 == 0:
        biscuits_daily *= 0.75
        biscuits_made += floor(biscuits_daily)
    else:
        biscuits_made += biscuits_daily

print(f'You have produced {biscuits_made} biscuits for the past month.')

if biscuits_made > biscuits_for_a_month:
    diff = (biscuits_made - biscuits_for_a_month)
    diff_percent = diff / biscuits_for_a_month * 100
    print(f'You produce {diff_percent:.2f} percent more biscuits.')
else:
    diff = (biscuits_made - biscuits_for_a_month)
    diff_percent = abs(diff / biscuits_for_a_month * 100)
    print(f'You produce {diff_percent:.2f} percent less biscuits.')

