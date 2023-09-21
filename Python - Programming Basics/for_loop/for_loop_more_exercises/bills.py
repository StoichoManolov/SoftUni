number_of_months = int(input())
total_expenses = 0
electricity_expense = 0
other_expenses = 0
water_expenses = 0
internet_expenses = 0

for months in range(1, number_of_months + 1):
    electricity = float(input())
    electricity_expense += electricity
    water_expenses += 20
    internet_expenses += 15
    other_expenses += (electricity + 20 + 15) * 1.20

average_expenses = (electricity_expense + water_expenses + other_expenses + internet_expenses) / number_of_months


print(f'Electricity: {electricity_expense:.2f} lv')
print(f'Water: {water_expenses:.2f} lv')
print(f'Internet: {internet_expenses:.2f} lv')
print(f'Other: {other_expenses:.2f} lv')
print(f'Average: {average_expenses:.2f} lv')

