from collections import deque

chocolates = [int(x) for x in input().split(', ')]
cups_of_milk = deque(int(x) for x in input().split(', '))

milkshakes_made = 0
while chocolates and cups_of_milk:

    chocolate = chocolates.pop()
    milk = cups_of_milk.popleft()

    if chocolate <= 0 and milk <= 0:
        continue
    elif chocolate <= 0:
        cups_of_milk.appendleft(milk)
        continue
    elif milk <= 0:
        chocolates.append(chocolate)
        continue
    if milk == chocolate:
        milkshakes_made += 1
    else:
        chocolate -= 5
        chocolates.append(chocolate)
        cups_of_milk.append(milk)

    if milkshakes_made == 5:
        break

if milkshakes_made == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(str(x) for x in cups_of_milk)}")
else:
    print("Milk: empty")