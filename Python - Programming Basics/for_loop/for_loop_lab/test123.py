drink_type = input()  # "Espresso", "Cappuccino" or "Tea"
sugar_type = input()  # "Without", "Normal" or "Extra"
number_of_drinks = int(input())

cost = 0
if drink_type == "Espresso":
    if sugar_type == "Without":
        cost = 0.90
    elif sugar_type == "Normal":
        cost = 1.00
    elif sugar_type == "Extra":
        cost = 1.20
elif drink_type == "Cappuccino":
    if sugar_type == "Without":
        cost = 1.00
    elif sugar_type == "Normal":
        cost = 1.20
    elif sugar_type == "Extra":
        cost = 1.60
elif drink_type == "Tea":
    if sugar_type == "Without":
        cost = 0.50
    elif sugar_type == "Normal":
        cost = 0.60
    elif sugar_type == "Extra":
        cost = 0.70

total_sum = number_of_drinks * cost
if sugar_type == "Without":
    discount = 0.35
    total_sum = total_sum - (total_sum * discount)
if drink_type == "Espresso" and number_of_drinks >= 5:
    discount = 0.25
    total_sum = total_sum - (total_sum * discount)
if total_sum > 15:
    discount = 0.20
    total_sum = total_sum - (total_sum * discount)

print(f"You bought {number_of_drinks} cups of {drink_type} for {total_sum:.2f} lv.")