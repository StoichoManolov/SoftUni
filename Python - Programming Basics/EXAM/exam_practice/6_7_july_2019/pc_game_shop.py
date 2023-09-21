games_sold = int(input())
other_count = 0
hearthstone_count = 0
fornite_count = 0
overwatch_count = 0
total_games = 0

for _ in range(games_sold):
    game_name = input()
    total_games += 1
    if game_name == 'Hearthstone':
        hearthstone_count += 1
    elif game_name == 'Fornite':
        fornite_count += 1
    elif game_name == 'Overwatch':
        overwatch_count += 1
    else:
        other_count += 1

percent_fortnite = (fornite_count / total_games) * 100
percent_overwatch = (overwatch_count / total_games) * 100
percent_hearthstone = (hearthstone_count / total_games) * 100
percent_others = (other_count / total_games) * 100

print(f'Hearthstone - {percent_hearthstone:.2f}%')
print(f'Fornite - {percent_fortnite:.2f}%')
print(f'Overwatch - {percent_overwatch:.2f}%')
print(f'Others - {percent_others:.2f}%')