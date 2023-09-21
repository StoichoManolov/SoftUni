budget_of_film = float(input())
number_of_extras = int(input())
clothing_per_extra = float(input())

decor_price = budget_of_film * 0.10
clothing_discount = 0

if number_of_extras > 150:
    clothing_discount = 0.10

clothing_extra_price = clothing_per_extra * number_of_extras
clothing_price_with_discount = clothing_extra_price * ( 1 - clothing_discount)

total_cost =  clothing_price_with_discount + decor_price
if total_cost <= budget_of_film:
    print(f'Action!')
    print(f'Wingard starts filming with {budget_of_film - total_cost:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {total_cost - budget_of_film:.2f} leva more.')

