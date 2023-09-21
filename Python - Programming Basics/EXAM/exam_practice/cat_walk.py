minutes_walked = int(input())
walk_amount = int(input())
calories_taken = int(input())


calorie_burned = (minutes_walked * walk_amount) * 5
calories_needed = (calories_taken * 0.5)

if calorie_burned >= calories_needed:
    print(f'Yes {calorie_burned}')
else:
    print(f'No{calorie_burned}')