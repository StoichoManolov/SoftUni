from math import ceil,floor

area_grapes_metric = int(input())
grape_kg_per_km = float(input())
wine_needed_in_litres = int(input())
workers = int(input())

grapes_harvested = area_grapes_metric * grape_kg_per_km
wine_in_litres = (grapes_harvested * 0.40) / 2.5

if wine_needed_in_litres > wine_in_litres:
    not_enough_wine = wine_needed_in_litres - wine_in_litres
    print(f'It will be a tough winter! More {floor(not_enough_wine)} liters wine needed.')

elif wine_in_litres >= wine_needed_in_litres:
    left_wine = wine_in_litres - wine_needed_in_litres
    wine_per_worker = left_wine / workers
    print(f'Good harvest this year! Total wine: {floor(wine_in_litres)} liters.')
    print(f'{ceil(left_wine)} liters left -> {ceil(wine_per_worker)} liters per person.')