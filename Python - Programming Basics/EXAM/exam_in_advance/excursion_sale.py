sea_excursion = int(input())
mountain_excursion = int(input())

type_of_excursion = input()

total_cost = 0
is_sold = False

while not type_of_excursion == 'Stop':

    if type_of_excursion == 'sea' and sea_excursion > 0:
        total_cost += 680
        sea_excursion -= 1
    elif type_of_excursion == 'mountain' and mountain_excursion > 0:
        total_cost += 499
        mountain_excursion -= 1

    if sea_excursion == 0 and mountain_excursion == 0:
        is_sold = True
        break

    type_of_excursion = input()

if is_sold:
    print(f'Good job! Everything is sold.')

print(f'Profit: {total_cost} leva.')