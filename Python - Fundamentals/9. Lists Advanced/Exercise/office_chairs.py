rooms = int(input())

free_chairs = 0
chairs_enough = True

for num in range(1, rooms + 1):
    chairs_visitors = input().split()
    chairs = len(chairs_visitors[0])
    visitors = int(chairs_visitors[1])

    if chairs == visitors:
        continue
    elif chairs > visitors:
        free_chairs += chairs - visitors
    elif visitors > chairs:
        diff = abs(chairs - visitors)
        print(f'{diff} more chairs needed in room {num}')
        chairs_enough = False

if chairs_enough:
    print(f'Game On, {free_chairs} free chairs left')





