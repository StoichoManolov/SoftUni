locations = int(input())


for n in range(locations):
    average = 0
    avg_gold = int(input())
    days = int(input())
    for _ in range(days):
        gold = int(input())
        average += gold
    avg_gained = average / days
    diff = abs(avg_gold - avg_gained)
    if avg_gained >= avg_gold:
        print(f'Good job! Average gold per day: {avg_gained:.2f}.')
    else:
        print(f'You need {diff:.2f} gold.')