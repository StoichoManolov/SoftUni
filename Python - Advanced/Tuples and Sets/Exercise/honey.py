from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
honey_making = deque(input().split())

total_honey = 0

while bees and nectar:

    bee = bees.popleft()
    honey = nectar.pop()

    if bee <= honey:
        symbol = honey_making.popleft()
        if symbol == '+':
            total_honey += bee + honey
        elif symbol == '/':
            if honey == 0:
                continue
            total_honey += abs(bee / honey)
        elif symbol == '*':
            total_honey += abs(bee * honey)
        elif symbol == '-':
            total_honey += abs(bee - honey)

    elif honey < bee:
        bees.appendleft(bee)
        continue

print(f'Total honey made: {total_honey}')
if bees:
    print(f'Bees left: {", ".join(str(x) for x in bees)}')
if nectar:
    print(f'Nectar left: {", ".join(str(x) for x in nectar)}')