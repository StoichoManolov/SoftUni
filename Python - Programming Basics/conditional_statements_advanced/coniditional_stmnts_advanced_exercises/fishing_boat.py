budget = int(input())
season = input()
fishers = int(input())

rent = 0
discount = 0
extra_discount = 0

if season == 'Spring':
    rent = 3000
elif season == 'Summer' or season == 'Autumn':
    rent = 4200
elif season == 'Winter':
    rent = 2600

if fishers <= 6:
    discount = 0.10
elif 7 <= fishers <= 11:
    discount = 0.15
else:
    discount = 0.25

if fishers % 2 == 0 and season != 'Autumn':
    extra_discount = 0.05

total_cost = rent * (1 - discount)*(1 - extra_discount)

if budget >= total_cost:
    money_left = budget - total_cost
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    money_needed = total_cost - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")








