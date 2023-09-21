lily_age = int(input())
washing_price = float(input())
price_per_toy = int(input())
money_gifts = 0
toy_gifts = 0
brother_stash = 0

for number in range(1, lily_age + 1):
    if number % 2 == 0:
        money_gifts += number * 10/2
        brother_stash += 1
    else:
        toy_gifts += 1


total_money = (money_gifts - brother_stash) + (toy_gifts * price_per_toy)

if total_money >= washing_price:
    print(f'Yes! {total_money - washing_price:.2f}')
else:
    money_need = washing_price - total_money
    print(f'No! {money_need:.2f}')
