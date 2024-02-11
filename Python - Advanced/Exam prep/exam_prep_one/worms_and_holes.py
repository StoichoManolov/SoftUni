from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])
matches = 0
worms_count = len(worms)
while worms and holes:

    current_worm = worms.pop()
    current_hole = holes.popleft()

    if current_hole == current_worm:
        matches += 1
        continue
    elif current_hole != current_worm:
        current_worm -= 3
        if current_worm <= 0:
            continue
        worms.append(current_worm)

if matches:
    print(f'Matches: {matches}')
else:
    print('There are no matches.')

if worms:
    print(f'Worms left: {", ".join(str(x) for x in worms)}')
elif not worms and matches == worms_count:
    print('Every worm found a suitable hole!')
else:
    print("Worms left: none")

if holes:
    print(f'Holes left: {", ".join(str(x) for x in holes)}')
else:
    print(f'Holes left: none')