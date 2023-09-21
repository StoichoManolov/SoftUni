pocket_money_tereza = float(input())
money_per_day_tereza = float(input())
tax_per_day_tereza = float(input())
gift_price = float(input())

TIME_LEFT_TO_BIRTHDAY = 5


saved_money_from_pocket = pocket_money_tereza * TIME_LEFT_TO_BIRTHDAY
money_earned_per_day = money_per_day_tereza * TIME_LEFT_TO_BIRTHDAY
total_saved_money = (saved_money_from_pocket + money_earned_per_day) - tax_per_day_tereza

if total_saved_money >= gift_price:
    print(f'Profit: {total_saved_money:.2f} BGN, the gift has been purchased.')
else:
    diff = abs(total_saved_money - gift_price)
    print(f'Insufficient money: {diff:.2f} BGN.')

