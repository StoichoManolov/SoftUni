from math import floor,ceil

days_away = int(input())
food_left_in_kg = int(input())
food_per_day_for_dog_kg = float(input())
food_per_day_for_cat_kg = float(input())
food_per_day_for_turtle_grams = float(input())

food_for_dog = days_away * food_per_day_for_dog_kg
food_for_cat = days_away * food_per_day_for_cat_kg
food_for_turtle = days_away * food_per_day_for_turtle_grams / 1000

total_food_needed = food_for_turtle + food_for_cat + food_for_dog

if total_food_needed >= food_left_in_kg:
    food_left = total_food_needed - food_left_in_kg
    print(f'{ceil(food_left)} kilos of food left.')

else:
    food_left = food_left_in_kg - total_food_needed
    print(f'{floor(food_left)} more kilos of food are needed.')
