command = input().split()

team_a = []
team_b = []
game_suspended = False

for player in command:

    if 'A' in player:
        if player not in team_a:
            team_a.append(player)
        else:
            continue
    elif 'B' in player:
        if player not in team_b:
            team_b.append(player)
        else:
            continue

    if len(team_a) > 4 or len(team_b) > 4:
        game_suspended = True
        break

print(f'Team A - {11 - len(team_a) }; Team B - {11 - len(team_b)}')
if game_suspended:
    print(f'Game was terminated')