from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]

wasted_water = 0

while cups and bottles:

    current_bottle = bottles.pop()
    current_cup = cups.popleft()

    if current_bottle >= current_cup:
        diff = current_bottle - current_cup
        wasted_water += diff
    else:
        diff = abs(current_bottle - current_cup)
        cups.appendleft(diff)

if cups:
    print(f'Cups:', *cups)
elif bottles:
    print(f'Bottles:', *bottles)
print(f'Wasted litters of water: {wasted_water}')