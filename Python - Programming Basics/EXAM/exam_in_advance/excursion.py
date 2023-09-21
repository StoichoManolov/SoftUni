group = int(input())
days_spent = int(input())
cards_of_transport = int(input())
tickets_for_museum = int(input())


nights_spent = days_spent * 20
transport_cards = cards_of_transport * 1.60
museum = tickets_for_museum * 6

total_cost_per_person = nights_spent + transport_cards + museum

cost_whole_group = (total_cost_per_person * group) * 1.25

print(f'{cost_whole_group:.2f}')

