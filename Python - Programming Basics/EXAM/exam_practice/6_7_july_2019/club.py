goal = float(input())
total_income = 0
cocktail = input()
is_reached = False

while cocktail != "Party!":
    current_cost = 0
    cocktail_amount = int(input())
    cost = len(cocktail) * cocktail_amount
    current_cost += cost
    if current_cost % 2 != 0:
        current_cost *= 0.75
    total_income += current_cost

    if total_income >= goal:
        is_reached = True
        break
    cocktail = input()

if is_reached:
    print(f'Target acquired.')
elif goal > total_income:
    diff = abs(goal - total_income)
    print(f'We need {diff:.2f} leva more.')

print(f'Club income - {total_income:.2f} leva.')





