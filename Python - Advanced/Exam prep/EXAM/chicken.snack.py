from collections import deque

amount_of_money = [int(x) for x in input().split()]
price_of_food = deque(int(x) for x in input().split())
foods = 0

while amount_of_money and price_of_food:

    current_money = amount_of_money.pop()
    current_price = price_of_food.popleft()

    if current_price == current_money:
        foods += 1
    elif current_money > current_price:
        foods += 1
        result = current_money - current_price
        if amount_of_money:
            amount_of_money[-1] += result

if foods >= 4:
    print(f"Gluttony of the day! Henry ate {foods} foods.")

elif 0 < foods < 4:
    if foods == 1:
        print(f"Henry ate: {foods} food.")
    else:
        print(f"Henry ate: {foods} foods.")
elif foods == 0:
    print(f"Henry remained hungry. He will try next weekend again.")