name_of_actor = input()
academy_points = float(input())
amount_of_jury = int(input())

for actors in range(amount_of_jury):

    name_of_jury = input()
    points_given = float(input())
    academy_points += (len(name_of_jury) * points_given / 2)

    if academy_points >= 1250.5:
        break

if academy_points > 1250.5:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {academy_points:.1f}!")
else:
    diff = abs(academy_points - 1250.5)
    print(f'Sorry, {name_of_actor} you need {diff:.1f} more!')
