city = input()
type_of_package = input()
vip_discount = input()
days_of_stay = int(input())
discount = 0
price = 0
city1 = "Bansko", 'Borovets'
city2 = 'Varna', 'Burgas'


if city in city1:
    if vip_discount == 'yes':
        if type_of_package == 'withEquipment':
            price = 100
            discount = 0.10
        elif type_of_package == 'noEquipment':
            price = 80
            discount = 0.05
    else:
        if type_of_package == 'withEquipment':
            price = 100
        elif type_of_package == 'noEquipment':
            price = 80

elif city in city2:
    if vip_discount == 'yes':
        if type_of_package == 'withBreakfast':
            price = 130
            discount = 0.12
        elif type_of_package == 'noBreakfast':
            price = 100
            discount = 0.07
    elif vip_discount == 'no':
        if type_of_package == 'withBreakfast':
            price = 130
        elif type_of_package == 'noBreakfast':
            price = 100

price *= (1 - discount)
total = price * days_of_stay
if days_of_stay > 7:
    total -= price
if days_of_stay < 1:
    print(f'Days must be positive number!')
elif price == 0:
    print(f'Invalid input!')
else:
    print(f'The price is {total:.2f}lv! Have a nice time!')

#uslovieto