budget = float(input())
budget_left = budget
actor_name = input()
is_enough = True

while actor_name != 'ACTION':

    if len(actor_name) <= 15:
        salary = float(input())
        budget_left -= salary
    else:
        budget_left *= 0.80

    if budget_left < 0:
        is_enough = False
        break

    actor_name = input()

diff = abs(budget_left)

if is_enough:
    print(f'We are left with {diff:.2f} leva.')
else:
    print(f'We need {diff:.2f} leva for our actors.')
