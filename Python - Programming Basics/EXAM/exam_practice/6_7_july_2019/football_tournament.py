team_name = input()
matches_played = int(input())
wins_count = 0
draws_count = 0
loses_count = 0

for _ in range(matches_played):
    result = input()

    if result == 'W':
        wins_count += 1
    elif result == 'D':
        draws_count += 1
    elif result == 'L':
        loses_count += 1

points_won = (wins_count * 3) + (draws_count * 1)

if matches_played <= 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    win_percentage = (wins_count / matches_played) * 100
    print(f'{team_name} has won {points_won} points during this season.')
    print(f'Total stats:')
    print(f'## W: {wins_count}')
    print(f'## D: {draws_count}')
    print(f'## L: {loses_count}')
    print(f'Win rate: {win_percentage:.2f}%')

