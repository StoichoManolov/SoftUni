from collections import deque

bullet_price = int(input())
size_gun_barrel = int(input())

bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])

bullets_count = 0
intelligence = int(input())


while bullets and locks:

    for barrel in range(size_gun_barrel):

        if not locks:
            break

        if not bullets:
            break

        bullet = bullets.pop()
        target = locks.popleft()
        bullets_count += 1

        if bullet <= target:
            print(f'Bang!')
        else:
            print('Ping!')
            locks.appendleft(target)
    else:
        if not bullets:
            break
        print('Reloading!')

if not locks:
    earned = intelligence - (bullets_count * bullet_price)
    print(f"{len(bullets)} bullets left. Earned ${earned}" )
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")