TAXI_START_TAX = 0.70
TAXI_DAILY_TAX_PER_KM = 0.79
TAXI_NIGHT_TAX_PER_KM = 0.90

AUTO_TAX_PER_KM = 0.09
TRAIN_TAX_PER_KM = 0.06

total_cost = 0
kilometers = int(input())
time_of_day = input()

if kilometers < 20:
    if time_of_day != 'day':
        total_cost = TAXI_START_TAX + (kilometers * TAXI_NIGHT_TAX_PER_KM)
        print(f'{total_cost:.2f}')
    else:
        total_cost = TAXI_START_TAX + (kilometers * TAXI_DAILY_TAX_PER_KM)
        print(f'{total_cost:.2f}')
elif 100 > kilometers >= 20:
    if time_of_day == 'day' or 'night':
        total_cost = AUTO_TAX_PER_KM * kilometers
        print(f'{total_cost:.2f}')
else:
    total_cost = TRAIN_TAX_PER_KM * kilometers
    print(f'{total_cost:.2f}')


