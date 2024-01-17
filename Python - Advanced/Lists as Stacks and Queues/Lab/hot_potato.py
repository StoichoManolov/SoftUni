from collections import deque

kids = deque(input().split())
toss = int(input()) - 1


while len(kids) > 1:
    kids.rotate(-toss)
    kid_in_a_row = kids.popleft()
    print(f'Removed {kid_in_a_row}')

print(f'Last is {kids.popleft()}')





