type_of_flower = input()
amount_of_flowers = int(input())
budget = int(input())
flower_cost = 0
discount = 0
if type_of_flower == 'Roses':
    flower_cost = 5
    if amount_of_flowers > 80:
        discount = 0.10
elif type_of_flower == 'Dahlias':
    flower_cost = 3.80
    if amount_of_flowers > 90:
        discount = 0.15
elif type_of_flower == 'Tulips':
    flower_cost = 2.80
    if amount_of_flowers > 80:
        discount = 0.15
elif type_of_flower == 'Narcissus':
    flower_cost = 3.00
    if amount_of_flowers < 120:
        flower_cost = 3 + (3 * 0.15)
elif type_of_flower == 'Gladiolus':
    flower_cost = 2.50
    if amount_of_flowers < 80:
        flower_cost = 2.50 + (2.50 * 0.20)

total_cost = flower_cost * amount_of_flowers
total_cost_with_discounts = total_cost * (1 - discount)
if budget >= total_cost_with_discounts:
    money_left = budget - total_cost_with_discounts
    print(f'Hey, you have a great garden with {amount_of_flowers} {type_of_flower} and {money_left:.2f} leva left.')
else:
    money_needed = total_cost_with_discounts - budget
    print(f"Not enough money, you need {money_needed:.2f} leva more.")
