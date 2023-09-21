junior_bikers = int(input())
senior_bikers = int(input())
type_of_route = input().lower()

tax_for_juniors = 0
tax_for_seniors = 0
discount = 0
total_bikers = junior_bikers + senior_bikers

if type_of_route == 'trail':
    tax_for_juniors = 5.50
    tax_for_seniors = 7
elif type_of_route == 'cross-country':
    tax_for_juniors = 8
    tax_for_seniors = 9.50
elif type_of_route == 'downhill':
    tax_for_juniors = 12.25
    tax_for_seniors = 13.75
elif type_of_route == 'road':
    tax_for_juniors = 20
    tax_for_seniors = 21.50

if type_of_route == 'cross-country' and total_bikers >= 50:
    discount = 0.25

total_cost = junior_bikers * tax_for_juniors + tax_for_seniors * senior_bikers
total_cost_with_discount = total_cost * (1 - discount)
money_left_after_tax = total_cost_with_discount * 0.05
money_for_charity = total_cost_with_discount - money_left_after_tax

print(f'{money_for_charity:.2f}')
