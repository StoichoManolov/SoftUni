lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
shield_breaks = 0


for num in range(1, lost_fights + 1):

    if num % 2 == 0 and num % 3 == 0:
        expenses += shield_price + sword_price + helmet_price
        shield_breaks += 1
    elif num % 2 == 0:
        expenses += helmet_price
    elif num % 3 == 0:
        expenses += sword_price

    if shield_breaks != 0 and shield_breaks % 2 == 0:
        expenses += armor_price
        shield_breaks = 0

print(f'Gladiator expenses: {expenses:.2f} aureus')


