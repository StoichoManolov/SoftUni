from collections import deque

egg_size = deque(int(x) for x in input().split(', '))
paper = [int(x) for x in input().split(', ')]
boxes = 0

while egg_size and paper:

    current_paper = paper.pop()
    current_egg = egg_size.popleft()

    if current_egg <= 0:
        paper.append(current_paper)
        continue

    elif current_egg == 13:
        paper.append(current_paper)
        paper[0],paper[-1] = paper[-1],paper[0]
        continue

    result = current_paper + current_egg

    if result <= 50:
        boxes += 1

if boxes > 0:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if egg_size:
    print(f'Eggs left: {", ".join(str(x) for x in egg_size)}')

if paper:
    print(f'Pieces of paper left: {", ".join(str(x) for x in paper)}')


