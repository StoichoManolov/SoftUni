actor_name = input()
academic_points = float(input())
juries = int(input())

points = 0
points_goal = 1250.5

for _ in range(juries):

    jury_name = input()
    jury_grade = float(input())
    academic_points += (len(jury_name) * jury_grade) / 2

    if academic_points > points_goal:
        break

diff = abs(academic_points - points_goal)

if academic_points >= points_goal:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {academic_points:.1f}!')
else:
    print(f'Sorry, {actor_name} you need {diff:.1f} more!')

