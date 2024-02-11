def team_lineup(*args):

    teams = {}

    for name,country in args:
        if country not in teams:
            teams[country] = []
        teams[country].append(name)

    team = sorted(teams.items(), key=lambda x: (-len(x[1]),x[0]))

    result = ''

    for current_country, players in team:
        result += f'{current_country}:\n'
        for current_player in players:
            result += f'  -{current_player}\n'

    return result


print(team_lineup(

   ("Lionel Messi", "Argentina"),

   ("Neymar", "Brazil"),

   ("Cristiano Ronaldo", "Portugal"),

   ("Harry Kane", "England"),

   ("Kylian Mbappe", "France"),

   ("Raheem Sterling", "England")))
