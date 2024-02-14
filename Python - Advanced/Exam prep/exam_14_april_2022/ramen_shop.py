from collections import deque

bowls_of_ramen = [int(x) for x in input().split(', ')]
customers = deque(int(x) for x in input().split(', '))

while bowls_of_ramen and customers:

    current_bowl = bowls_of_ramen.pop()
    current_customer = customers.popleft()

    if current_bowl == current_customer:
        continue
    elif current_bowl > current_customer:
        result = current_bowl - current_customer
        bowls_of_ramen.append(result)
    elif current_customer > current_bowl:
        result = current_customer - current_bowl
        customers.appendleft(result)


if not customers:
    print("Great job! You served all the customers.")

    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls_of_ramen)}")

else:
    print("Out of ramen! You didn't manage to serve all customers.")

    if customers:
        print(f"Customers left: {', '.join(str(x) for x in customers)}")