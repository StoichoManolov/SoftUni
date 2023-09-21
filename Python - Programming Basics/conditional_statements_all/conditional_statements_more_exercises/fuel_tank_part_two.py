GASOLINE = 2.22  # Бензин – 2.22 лева за един литър,
DIESEL = 2.33  # Дизел – 2.33 лева за един литър
GAS = 0.93  # Газ – 0.93 лева за литър

final_price_with_discount = 0
type_of_fuel = input().lower()
amount_of_fuel = float(input())
club_card = input().lower()
discount = 0

if 20 < amount_of_fuel <= 25:
    discount = 0.08
elif amount_of_fuel > 25:
    discount = 0.10
if club_card == 'yes':
    GASOLINE = 2.04
    DIESEL = 2.21
    GAS = 0.85
if type_of_fuel == 'gas':
    final_price = GAS * amount_of_fuel
elif type_of_fuel == 'gasoline':
    final_price = GASOLINE * amount_of_fuel
else:
    final_price = DIESEL * amount_of_fuel

final_price_with_discount = final_price * (1 - discount)
print(f'{final_price_with_discount:.2f} lv.')
