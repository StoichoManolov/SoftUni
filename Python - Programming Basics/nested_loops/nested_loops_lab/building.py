floors = int(input())
rooms = int(input())

for x in range(floors, 0, -1):
    for y in range(rooms):
        if x == floors:
            print(f'L{x}{y}',end=" ")
        else:
            if not x % 2 == 0:
                print(f'A{x}{y}',end=" ")
            else:
                print(f'O{x}{y}',end=" ")
    print("")


