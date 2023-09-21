from math import floor
number_of_tourneys = int(input())
starting_rank = int(input())
tourneys_played = 0
wins = 0
diff = starting_rank   # to subtract from total points to get the average

for rank in range(number_of_tourneys):
    win_or_not = input()
    tourneys_played += 1
    if win_or_not == 'W':
        wins += 1
        starting_rank += 2000
    elif win_or_not == 'F':
        starting_rank += 1200
    elif win_or_not == 'SF':
        starting_rank += 720

avg_points_per_tourney = (starting_rank - diff) / tourneys_played # avg points per tournament without starting pts
tourney_won_as_percent = wins / tourneys_played * 100  # % of tourneys won

print(f'Final points: {starting_rank}')
print(f'Average points: {floor(avg_points_per_tourney)}')
print(f'{tourney_won_as_percent:.2f}%')