contract_time = input()
type_of_contract = input().lower()
mobile_internet = input()
amount_of_months_to_pay = int(input())
price = 0
if contract_time == 'one':
    if type_of_contract == 'small':
        price = 9.98
    elif type_of_contract == 'middle':
        price = 18.99
    elif type_of_contract == 'large':
        price = 25.98
    elif type_of_contract == 'extralarge':
        price = 35.99
elif contract_time == 'two':
    if type_of_contract == 'small':
        price = 8.58
    elif type_of_contract == 'middle':
        price = 17.09
    elif type_of_contract == 'large':
        price = 23.59
    elif type_of_contract == 'extralarge':
        price = 31.79

if mobile_internet == 'yes':
    if price <= 10:
        price += 5.50
    elif price <= 30:
        price += 4.35
    else:
        price += 3.85

total_cost = price * amount_of_months_to_pay

if contract_time == 'two':
    total_cost *= 0.9625

print(f'{total_cost:.2f}')


