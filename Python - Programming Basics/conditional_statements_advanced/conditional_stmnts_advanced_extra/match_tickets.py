VIP_TICKET = 499.99  # VIP – 499.99 лева.
NORMAL_TICKET = 249.99  # Normal – 249.99 лева.

budget = float(input())
category = input().lower()
people_in_the_group = int(input())
ticket = 0
transport_cost = 0
if 1 <= people_in_the_group <= 4:
    transport_cost = 0.75
elif 5 <= people_in_the_group <= 9:
    transport_cost = 0.60
elif 10 <= people_in_the_group <= 24:
    transport_cost = 0.50
elif 25 <= people_in_the_group <= 49:
    transport_cost = 0.40
else:
    transport_cost = 0.25

if category == 'vip':
    ticket = 499.99
else:
    ticket = 249.99

transport_price = budget * transport_cost
money_left_after_transport = budget - transport_price

ticket_needed = people_in_the_group * ticket

if ticket_needed < money_left_after_transport:
    money_left = money_left_after_transport  - ticket_needed
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    money_needed = ticket_needed - money_left_after_transport
    print(f'Not enough money! You need {money_needed:.2f} leva.')


