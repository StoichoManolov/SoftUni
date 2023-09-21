money_saved = 0

while True:
    destination = input()
    if destination == 'End':
        break
    money = float(input())
    while money_saved < float(money):
        saved_money = float(input())
        money_saved += saved_money
        if money_saved >= float(money):
            print(f'Going to {destination}!')
            money_saved = 0
            break
