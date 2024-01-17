from collections import deque

food_for_the_day = int(input())
order_complete = True

orders = deque([int(x) for x in input().split()])
max_order = max(orders)

while food_for_the_day > 0:

    food = orders.popleft()

    if food_for_the_day >= food:
        food_for_the_day -= food
    else:
        orders.appendleft(food)
        order_complete = False
        break
    if not orders:
        break

print(max_order)
if order_complete:
    print(f'Orders complete')
else:
    print(f"Orders left:", *orders)  # " ".join([str(x) for x in orders])


# from collections import deque
#
# food = int(input())
# orders = deque([int(x) for x in input().split()])
#
# print(max(orders))
#
# for order in orders.copy():  # O(n)
#     if food >= order:
#         orders.popleft()
#         food -= order
#     else:
#         print(f"Orders left:", *orders)  # " ".join([str(x) for x in orders])
#         break
# else:
#     print("Orders complete")
