will_left = float(input())
year_goal = int(input())
age = 18
expenses = 0

for years in range(1800, year_goal + 1):
    if years != 1800:
        age += 1
    if years % 2 == 0:
        expenses += 12000
    else:
        expenses += 12000 + (age * 50)

if expenses <= will_left:
    diff = will_left - expenses
    print(f'Yes! He will live a carefree life and will have {diff:.2f} dollars left.')
else:
    diff = abs(will_left - expenses)
    print(f'He will need {diff:.2f} dollars to survive.')